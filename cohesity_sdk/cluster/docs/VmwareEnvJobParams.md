# VmwareEnvJobParams

Specifies job parameters applicable for all 'kVMware' Environment type Protection Sources in a Protection Job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_disks** | [**List[DiskInfo]**](DiskInfo.md) | Specifies the list of Disks to be excluded from backing up. These disks are excluded from all Protection Sources in the Protection Job. | [optional] 
**fallback_to_crash_consistent** | **bool** | If true, takes a crash-consistent snapshot when app-consistent snapshot fails. Otherwise, the snapshot attempt is marked failed. | [optional] 
**skip_physical_rdm_disks** | **bool** | If true, skip physical RDM disks when backing up VMs. Otherwise, backup of VMs having physical RDM will fail. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.vmware_env_job_params import VmwareEnvJobParams

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareEnvJobParams from a JSON string
vmware_env_job_params_instance = VmwareEnvJobParams.from_json(json)
# print the JSON string representation of the object
print(VmwareEnvJobParams.to_json())

# convert the object into a dict
vmware_env_job_params_dict = vmware_env_job_params_instance.to_dict()
# create an instance of VmwareEnvJobParams from a dict
vmware_env_job_params_from_dict = VmwareEnvJobParams.from_dict(vmware_env_job_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


