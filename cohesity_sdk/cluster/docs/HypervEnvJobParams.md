# HypervEnvJobParams

Specifies job parameters applicable for all 'kHyperV' Environment type Protection Sources in a Protection Job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_disks** | [**List[HyperVDiskInfo]**](HyperVDiskInfo.md) | Specifies a list of disks to exclude from being protected for the object/vm. | [optional] 
**fallback_to_crash_consistent** | **bool** | If true, takes a crash-consistent snapshot when app-consistent snapshot fails. Otherwise, the snapshot attempt is marked failed. | [optional] 
**include_disks** | [**List[HyperVDiskInfo]**](HyperVDiskInfo.md) | Specifies a list of disks to included in the protection for the object/vm. | [optional] 
**protection_type** | **str** | Specifies the Protection Group type. If not specified, then backup method is auto determined. Specifying RCT will forcibly use RCT backup for all VMs in this Protection Group. Available only for VMs with hardware version 8.0 and above, but is more efficient. Specifying VSS will forcibly use VSS backup for all VMs in this Protection Group. Available for VMs with hardware version 5.0 and above, but is slower than RCT backup. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.hyperv_env_job_params import HypervEnvJobParams

# TODO update the JSON string below
json = "{}"
# create an instance of HypervEnvJobParams from a JSON string
hyperv_env_job_params_instance = HypervEnvJobParams.from_json(json)
# print the JSON string representation of the object
print(HypervEnvJobParams.to_json())

# convert the object into a dict
hyperv_env_job_params_dict = hyperv_env_job_params_instance.to_dict()
# create an instance of HypervEnvJobParams from a dict
hyperv_env_job_params_from_dict = HypervEnvJobParams.from_dict(hyperv_env_job_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


