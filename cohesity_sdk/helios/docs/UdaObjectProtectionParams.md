# UdaObjectProtectionParams

Specifies the parameters that are specific to Universal Data Adapter Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_job_arguments** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the map of custom arguments to be supplied to the various backup scripts. | [optional] 
**concurrency** | **int** | Specifies the maximum number of concurrent IO Streams thatwill be created to exchange data with the cluster. If not specified, the default value is taken as 1. | [optional] [default to 1]
**full_backup_args** | **str** | Specifies the custom arguments to be supplied to the full backup script when a full backup is enabled in the policy. This field is deprecated. Use backupJobArguments instead. | [optional] 
**has_entity_support** | **bool** | Specifies whether this Protection Group is created from a source having entity support. | [optional] [readonly] 
**incr_backup_args** | **str** | Specifies the custom arguments to be supplied to the incremental backup script when an incremental backup is enabled in the policy. This field is deprecated. Use backupJobArguments instead. | [optional] 
**log_backup_args** | **str** | Specifies the custom arguments to be supplied to the log backup script when a log backup is enabled in the policy. This field is deprecated. Use backupJobArguments instead. | [optional] 
**mounts** | **int** | Specifies the maximum number of view mounts per host. If not specified, the default value is taken as 1. | [optional] [default to 1]
**objects** | [**List[UdaObjectProtectionObjectParams]**](UdaObjectProtectionObjectParams.md) | Specifies the objects to be included in the Object Protection. | 

## Example

```python
from cohesity_sdk.helios.models.uda_object_protection_params import UdaObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of UdaObjectProtectionParams from a JSON string
uda_object_protection_params_instance = UdaObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(UdaObjectProtectionParams.to_json())

# convert the object into a dict
uda_object_protection_params_dict = uda_object_protection_params_instance.to_dict()
# create an instance of UdaObjectProtectionParams from a dict
uda_object_protection_params_from_dict = UdaObjectProtectionParams.from_dict(uda_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


