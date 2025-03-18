import time



from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.models.create_protection_group_run_request import (
    CreateProtectionGroupRunRequest,
)
from cohesity_sdk.cluster.models.create_or_update_protection_group_request import (
    CreateOrUpdateProtectionGroupRequest,
)
from cohesity_sdk.cluster.models.vmware_source_registration_params import (
    VmwareSourceRegistrationParams,
)
from cohesity_sdk.cluster.models.vmware_protection_group_object_params import (
    VmwareProtectionGroupObjectParams,
)
from cohesity_sdk.cluster.models.vcenter_registration_params import (
    VcenterRegistrationParams,
)
from cohesity_sdk.cluster.models.source_registration_request_params import (
    SourceRegistrationRequestParams,
)
from cohesity_sdk.cluster.models.vmware_protection_group_params import (
    VmwareProtectionGroupParams,
)

client = ClusterClient(
    api_key="xxxxxxx",
    cluster_vip="x.x.x.x",
)

#Fetch Storage Domain Id
def get_storage_domain_id():
    domains = client.storage_domain_api.get_storage_domains().storage_domains
    for domain in domains:
        if domain.name == "DefaultStorageDomain":
            return domain.id
    return -1

#Fetch Policy Id
def get_policy_id():
    policies = client.policy_api.get_protection_policies().policies
    for policy in policies:
        if policy.name == "Bronze":
            return policy.id
    return -1

#Register Protection Source
def register_source():
    body = SourceRegistrationRequestParams(
        environment="kVMware",
        name=input("Enter VcenterName"),
        vmware_params=VmwareSourceRegistrationParams(
            type="kVCenter",
            v_center_params=VcenterRegistrationParams(
                username=input("Enter Username"),
                password=input("Enter Password"),
                endpoint=input("Enter VcenterName")
            )
        )
    )
    response = client.source_api.register_protection_source(body=body)
    return response

# Search for a vCenter object to retrieve the id and object information
def get_objects_by_vmname(parentid, vmname):
        """
        Methos to objects by vm name
        Args:
            vmname:
        Returns: VM Id
        """
        response = client.object_api.get_source_hierarchy_objects(
            source_id=parentid, parent_id=parentid
        )
        objects = response.objects
        for vm in objects:
            if vm.name == vmname:
                return vm.id

#CReate Protection Group
def create_protectiongroup(policyid , objectid) :  # Fixed method name here
    """
    Method to create Protection Job
    Args:
        policyid:
    Returns: Response
    """
    req_body = CreateOrUpdateProtectionGroupRequest(
        policy_id=policyid,
        name=input("Enter JobName"),
        storage_domain_id=2 ,
        environment="kVMware",
        vmware_params=VmwareProtectionGroupParams(
            objects=[VmwareProtectionGroupObjectParams(id=objectid)]
        ) ,
    )
    response = client.protection_group_api.create_protection_group(body=req_body)
    return response

#Run Job
def run_job(job_id) :
    """
    Method to run protection job
    Args:
        job_id:
    Returns: Boolean
    """
    runs = client.protection_group_api.get_protection_group_runs(job_id).runs
    if len(runs) == 0 or runs[0].local_backup_info.status not in [
        "Running" ,
        "Accepted" ,
    ] :
        body = CreateProtectionGroupRunRequest(run_type="kRegular")
        client.protection_group_api.create_protection_group_run(job_id , body)
    count = 15
    while count != 0 :
        runs = client.protection_group_api.get_protection_group_runs(job_id).runs
        if not runs :
            time.sleep(10)
            continue
        if runs[0].local_backup_info.status in ["Running" , "Accepted"] :
            time.sleep(30)
            count -= 1
        else :
            return True

#Delete Protection Group
def delete_protection_group(jobid) :
        """
        Method to delete protection group
        Args:
            jobid:
        Returns: Response
        """
        response = client.protection_group_api.delete_protection_group(id=jobid)
        return response

#Unregister Protection Source
def unregister_source(id) :
        """
        Method to unregister protection source
        Args:
            id:
        Returns: Response
        """
        response = client.source_api.delete_protection_source_registration(
            id=id
        )
        return response

if __name__ =="__main__":
    domain_id = get_storage_domain_id()
    policy_id = get_policy_id()
    registeredsrcresp = register_source()
    parentsrcid = registeredsrcresp.id
    objectid = get_objects_by_vmname(
        parentid=parentsrcid , vmname="XXXXX"
    )
    create_group_resp = create_protectiongroup(policyid=policy_id, objectid=objectid)
    jobid = create_group_resp.id
    run_job(job_id=jobid)
    time.sleep(20)

    delete_protection_group(jobid=jobid)

    unregister_source(id=parentsrcid)