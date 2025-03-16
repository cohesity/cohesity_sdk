# GenericNasProtectionGroupParams

Specifies the parameters which are specific to NAS related Protection Groups.

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
**direct_cloud_archive** | **bool** | Specifies whether or not to store the snapshots in this run directly in an Archive Target instead of on the Cluster. If this is set to true, the associated policy must have exactly one Archive Target associated with it and the policy must be set up to archive after every run. Also, a Storage Domain cannot be specified. Default behavior is &#39;false&#39;. | [optional] 
**native_format** | **bool** | Specifies whether or not to enable native format for direct archive job. This field is set to true if native format should be used for archiving. | [optional] 
**protocol** | **str** | Specifies the preferred protocol to use if this device supports multiple protocols. | [optional] 
**objects** | [**List[ProtectionObjectInput]**](ProtectionObjectInput.md) | Specifies the objects to be included in the Protection Group. | 

## Example

```python
from cohesity_sdk.helios.models.generic_nas_protection_group_params import GenericNasProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of GenericNasProtectionGroupParams from a JSON string
generic_nas_protection_group_params_instance = GenericNasProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(GenericNasProtectionGroupParams.to_json())

# convert the object into a dict
generic_nas_protection_group_params_dict = generic_nas_protection_group_params_instance.to_dict()
# create an instance of GenericNasProtectionGroupParams from a dict
generic_nas_protection_group_params_from_dict = GenericNasProtectionGroupParams.from_dict(generic_nas_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


