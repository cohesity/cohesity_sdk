# UdaProtectionGroupParams

Specifies parameters related to the Universal Data Adapter Protection job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_job_arguments** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the map of custom arguments to be supplied to the various backup scripts. | [optional] 
**concurrency** | **int** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. If not specified, the default value is taken as 1. | [optional] [default to 1]
**et_log_backup** | **bool** | Specifies whether this Protection Group is created from a source having externally triggered log backup support. | [optional] [readonly] 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**full_backup_args** | **str** | Specifies the custom arguments to be supplied to the full backup script when a full backup is enabled in the policy. This field is deprecated. Use backupJobArguments instead. | [optional] 
**has_entity_support** | **bool** | Specifies whether this Protection Group is created from a source having entity support. | [optional] [readonly] 
**incr_backup_args** | **str** | Specifies the custom arguments to be supplied to the incremental backup script when an incremental backup is enabled in the policy. This field is deprecated. Use backupJobArguments instead. | [optional] 
**log_backup_args** | **str** | Specifies the custom arguments to be supplied to the log backup script when a log backup is enabled in the policy. This field is deprecated. Use backupJobArguments instead. | [optional] 
**mounts** | **int** | Specifies the maximum number of view mounts per host. If not specified, the default value is taken as 1. | [optional] [default to 1]
**objects** | [**List[UdaProtectionGroupObjectParams]**](UdaProtectionGroupObjectParams.md) | Specifies a list of fully qualified names of the objects to be protected. | 
**source_id** | **int** | Specifies the source Id of the objects to be protected. | 

## Example

```python
from cohesity_sdk.cluster.models.uda_protection_group_params import UdaProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of UdaProtectionGroupParams from a JSON string
uda_protection_group_params_instance = UdaProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(UdaProtectionGroupParams.to_json())

# convert the object into a dict
uda_protection_group_params_dict = uda_protection_group_params_instance.to_dict()
# create an instance of UdaProtectionGroupParams from a dict
uda_protection_group_params_from_dict = UdaProtectionGroupParams.from_dict(uda_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


