from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.create_protection_group_run_request import (
    CreateProtectionGroupRunRequest,
)
from cohesity_sdk.cluster.model.create_or_update_protection_group_request import (
    CreateOrUpdateProtectionGroupRequest,
)
from cohesity_sdk.cluster.model.common_recovery_request_params import CommonRecoveryRequestParams
from cohesity_sdk.cluster.model.vmware_source_registration_params import (
    VmwareSourceRegistrationParams,
)
from cohesity_sdk.cluster.model.vmware_protection_group_object_params import (
    VmwareProtectionGroupObjectParams,
)
from cohesity_sdk.cluster.model.vcenter_registration_params import (
    VcenterRegistrationParams,
)
from cohesity_sdk.cluster.model.source_registration_request_params import (
    SourceRegistrationRequestParams,
)
from cohesity_sdk.cluster.model.vmware_protection_group_params import (
    VmwareProtectionGroupParams,
)

client = ClusterClient(
    api_key="1625435g-4tr43t5f-g54t5r-5gfr",
    cluster_vip="x.x.x.x",
)


def get_storage_domain_id():
    domains = client.storage_domains.get_storage_domains()["storage_domains"]
    for domain in domains:
        if domain["name"] == "DefaultStorageDomain":
            return domain["id"]
    return -1


def get_policy_id():
    return "1744409997479013:1644498100685:3"
    policies = client.protection_policies.get_protection_policies()["policies"]
    for policy in policies:
        if policy["name"] == "Bronze":
            return policy["id"]
    return -1


def get_source_by_name(source_name, environment):
    sources = client.protection_sources.get_source_registrations()["registrations"]
    for source in sources:
        source_info = source["source_info"]
        if (
            source_info["environment"] == environment
            and source_info["name"] == source_name
        ):
            return source_info["id"]
    return -1


def register_source(source_name, username, password):
    print("Registering Source %s" % source_name)
    body = SourceRegistrationRequestParams(
        environment="kVMware",
        is_internal_encrypted=False,
        vmware_params=VmwareSourceRegistrationParams(
            type="kVCenter",
            v_center_params=VcenterRegistrationParams(
                username=username,
                password=password,
                endpoint=source_name,
            ),
        ),
    )
    code, resp = client.protection_sources.register_protection_source(body=body)


def create_job(job_name):
    try:
        jobs = client.protection_groups.get_protection_groups(is_deleted=False)[
            "protection_groups"
        ]
        # Check the job is already available.
        for job in jobs:
            if job["name"] == job_name:
                print("Job %s is already available, skipping creation" % job_name)
                return job["id"], job
        # Get storage_domain id.
        print("Fetching storage domains")
        domain_id = get_storage_domain_id()
        if domain_id == -1:
            raise Exception("Storage Domain not available.")
            exit()
        vcenter_name = input("Enter Vcenter name ")

        source_id = get_source_by_name(vcenter_name, "kVMware")
        source_id = 1
        if source_id == -1:
            username = input("Enter Vcenter username ")
            password = input("Enter Vcenter password ")
            register_source(vcenter_name, username, password)
        body = CreateOrUpdateProtectionGroupRequest(
            storage_domain_id=domain_id,
            policy_id=get_policy_id(),
            name=job_name,
            environment="kVMware",
            vmware_params=VmwareProtectionGroupParams(
                objects=[
                    VmwareProtectionGroupObjectParams(
                        id=get_objects_by_vmname("chandra-pwsh01")
                    )
                ]
            ),
        )
        code, resp = client.protection_groups.create_protection_group(body)
        if code != 201:
            raise Exception(resp)
        return resp["id"], resp
    except Exception as err:
        print(err)
        exit()


def get_objects_by_vmname(vmname):
    vms = client.search.search_objects(environments=["kVMware"])["objects"]
    for vm in vms:
        if vm["name"] == vmname:
            print(vm["object_protection_infos"][0]["object_id"])
            return vm["object_protection_infos"][0]["object_id"]


def run_job(job_id):
    # Check for job run and trigger one.
    runs = client.protection_groups.get_protection_group_runs(job_id)["runs"]
    if len(runs) == 0 or runs[0]["local_backup_info"]["status"] not in [
        "Running",
        "Accepted",
    ]:
        # Trigger a job run.
        body = CreateProtectionGroupRunRequest(run_type="kRegular")
        client.protection_groups.create_protection_group_run(job_id, body)

    count = 15
    while count != 0:
        runs = client.protection_groups.get_protection_group_runs(job_id)["runs"]
        if not runs:
            time.sleep(10)
            continue
        if runs[0]["local_backup_info"]["status"] in ["Running", "Accepted"]:
            time.sleep(30)
            count -= 1
        else:
            return True

if __name__ =="__main__":
    print("Creating job")
    job_id, job = create_job("new")
    print("Job Content", job)
    print("Updating job with id %s" % job_id)
    code, resp = client.protection_groups.update_protection_group(job_id, job)
    print("Trigger job run")
    run = run_job(job_id)
    if run:
        # Recover the backup.
        objects = client.search.search_protected_objects(protection_group_ids=[job_id])["objects"]
        snapshot_id = objects[0].latest_snapshots_info[0].local_snapshot_info["snapshotId"]
    
    # Delete the job.
    print("Delete created job")
    print(client.protection_groups.delete_protection_group(job_id, delete_snapshots=True))
