# ElastifileObjectProtectionUpdateRequestParams

Specifies the update parameters which are specific to Elastifile object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether or not the backup should continue regardless of whether or not an error was encountered. | [optional] 
**encryption_enabled** | **bool** | Specifies whether the encryption should be used while backup or not. | [optional] 
**file_filters** | [**FileFilteringPolicy**](FileFilteringPolicy.md) |  | [optional] 
**file_lock_config** | [**FileLevelDataLockConfig**](FileLevelDataLockConfig.md) |  | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**pre_post_script** | [**HostBasedBackupScriptParams**](HostBasedBackupScriptParams.md) |  | [optional] 
**throttling_config** | [**NasThrottlingConfig**](NasThrottlingConfig.md) |  | [optional] 
**protocol** | **str** | Specifies the protocol of the NAS device being backed up. | [optional] 

## Example

```python
from cohesity_sdk.models.elastifile_object_protection_update_request_params import ElastifileObjectProtectionUpdateRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of ElastifileObjectProtectionUpdateRequestParams from a JSON string
elastifile_object_protection_update_request_params_instance = ElastifileObjectProtectionUpdateRequestParams.from_json(json)
# print the JSON string representation of the object
print(ElastifileObjectProtectionUpdateRequestParams.to_json())

# convert the object into a dict
elastifile_object_protection_update_request_params_dict = elastifile_object_protection_update_request_params_instance.to_dict()
# create an instance of ElastifileObjectProtectionUpdateRequestParams from a dict
elastifile_object_protection_update_request_params_from_dict = ElastifileObjectProtectionUpdateRequestParams.from_dict(elastifile_object_protection_update_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


