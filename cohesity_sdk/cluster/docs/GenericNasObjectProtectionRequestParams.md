# GenericNasObjectProtectionRequestParams

Specifies the parameters which are specific to Generic NAS object protection.

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
**objects** | [**List[ProtectionObjectInput]**](ProtectionObjectInput.md) | Specifies the objects to be protected. | 

## Example

```python
from cohesity_sdk.cluster.models.generic_nas_object_protection_request_params import GenericNasObjectProtectionRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of GenericNasObjectProtectionRequestParams from a JSON string
generic_nas_object_protection_request_params_instance = GenericNasObjectProtectionRequestParams.from_json(json)
# print the JSON string representation of the object
print(GenericNasObjectProtectionRequestParams.to_json())

# convert the object into a dict
generic_nas_object_protection_request_params_dict = generic_nas_object_protection_request_params_instance.to_dict()
# create an instance of GenericNasObjectProtectionRequestParams from a dict
generic_nas_object_protection_request_params_from_dict = GenericNasObjectProtectionRequestParams.from_dict(generic_nas_object_protection_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


