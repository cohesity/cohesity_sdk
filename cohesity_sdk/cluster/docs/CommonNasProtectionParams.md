# CommonNasProtectionParams

Specifies the parameters which are specific to NAS Protection.

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

## Example

```python
from cohesity_sdk.cluster.models.common_nas_protection_params import CommonNasProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonNasProtectionParams from a JSON string
common_nas_protection_params_instance = CommonNasProtectionParams.from_json(json)
# print the JSON string representation of the object
print(CommonNasProtectionParams.to_json())

# convert the object into a dict
common_nas_protection_params_dict = common_nas_protection_params_instance.to_dict()
# create an instance of CommonNasProtectionParams from a dict
common_nas_protection_params_from_dict = CommonNasProtectionParams.from_dict(common_nas_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


