import time
import random

from cohesity_sdk.helios_mcm.v2.model.create_or_update_protection_group_request import (
    CreateOrUpdateProtectionGroupRequest,
)
from cohesity_sdk.helios_mcm.v2.model.create_protection_group_run_request import (
    CreateProtectionGroupRunRequest,
)
from cohesity_sdk.helios_mcm.v2.model.create_or_update_protection_group_request import (
    CreateOrUpdateProtectionGroupRequest,
)
from cohesity_sdk.helios_mcm.v2.model.vmware_protection_group_object_params import (
    VmwareProtectionGroupObjectParams,
)
from cohesity_sdk.helios_mcm.v2.model.vmware_protection_group_params import (
    VmwareProtectionGroupParams,
)

from config import vcenter_name, vcenter_username, vcenter_password
from library import register_vmware_source
from helios_client import helios_v2_connector_with_cluster_id

# Initialise a client.
client = helios_v2_connector_with_cluster_id()
job_name = "VmwareJob_" + str(random.randint(1, 100))


def get_storage_domain_id():
    domains = client.storage_domain.get_storage_domains().storage_domains or []
    for domain in domains:
        if domain.name == "DefaultStorageDomain":
            return domain.id
    return -1


def get_policy_id():
    policies = client.policy.get_protection_policies().policies or []
    for policy in policies:
        if policy.name == "Bronze":
            return policy.id
    return -1


def create_job(job_name):
    try:
        source_id = None
        jobs = client.protection_group.get_protection_groups(is_deleted=False)[
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

        # Check if the source is already registered.
        sources = client.source.mcm_get_protection_sources(
            environments=["kVMware"]
        ).sources
        for source in sources:
            if source.name == vcenter_name:
                source_id = source.id
        if not source_id:
            register_vmware_source(vcenter_name, vcenter_username, vcenter_password)
        body = CreateOrUpdateProtectionGroupRequest(
            storage_domain_id=domain_id,
            policy_id=get_policy_id(),
            name=job_name,
            environment="kVMware",
            vmware_params=VmwareProtectionGroupParams(
                objects=[
                    VmwareProtectionGroupObjectParams(id=search_objects(source_id))
                ]
            ),
        )
        resp = client.protection_group.create_protection_group(body)
        return resp
    except Exception as err:
        print(err)
        exit()


def search_objects(source_id):
    """
    Function to search for Vms available in the vcenter source.
    : return object Id.
    """
    vm_id = None
    vm_size = 99999999999  # 99 GB
    vms = client.search.search_objects(
        environments=["kVMware"], source_ids=[source_id]
    ).objects
    for vm in vms:
        # Search for a VM of smaller size.
        if vm.logical_size_bytes and (vm.logical_size_bytes <= vm_size):
            vm_id = vm["object_protection_infos"][0]["object_id"]
    return vm_id


def run_job(job_id):
    # Check for job run and trigger one.
    runs = client.protection_group.get_protection_group_runs(job_id)["runs"]
    if len(runs) == 0 or runs[0]["local_backup_info"]["status"] not in [
        "Running",
        "Accepted",
    ]:
        # Trigger a job run.
        body = CreateProtectionGroupRunRequest(run_type="kRegular")
        client.protection_group.create_protection_group_run(job_id, body)

    count = 15
    while count != 0:
        runs = client.protection_group.get_protection_group_runs(job_id)["runs"]
        if not runs:
            time.sleep(10)
            continue
        if runs[0]["local_backup_info"]["status"] in ["Running", "Accepted"]:
            time.sleep(30)
            count -= 1
        else:
            return True


if __name__ == "__main__":
    print("Creating job")
    job = create_job(job_name)
    job_id = job.id
    print("Job Content", job)
    print("Updating job with id %s" % job_id)
    resp = client.protection_group.update_protection_group(job_id, job)
    print("Trigger job run")
    run = run_job(job_id)
    if run:
        objects = client.search.search_protected_objects(protection_group_ids=[job_id])[
            "objects"
        ]
        snapshot_id = (
            objects[0].latest_snapshots_info[0].local_snapshot_info["snapshotId"]
        )

    # Delete the job.
    print("Deleting created job '%s'" % job_name)
    client.protection_group.delete_protection_group(job_id, delete_snapshots=True)
    print("Successfully deleted job '%s'" % job_name)
