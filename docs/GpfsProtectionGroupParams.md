# GpfsProtectionGroupParams

Specifies the parameters which are specific to GPFS related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether or not the Protection Group should continue regardless of whether or not an error was encountered during protection group run. | [optional] 
**direct_cloud_archive** | **bool** | Specifies whether or not to store the snapshots in this run directly in an Archive Target instead of on the Cluster. If this is set to true, the associated policy must have exactly one Archive Target associated with it and the policy must be set up to archive after every run. Also, a Storage Domain cannot be specified. Default behavior is &#39;false&#39;. | [optional] 
**encryption_enabled** | **bool** | Specifies whether the protection group should use encryption while backup or not. | [optional] 
**file_filters** | [**FileFilteringPolicy**](FileFilteringPolicy.md) |  | [optional] 
**file_lock_config** | [**FileLevelDataLockConfig**](FileLevelDataLockConfig.md) |  | [optional] 
**filter_ip_config** | [**FilterIpConfig**](FilterIpConfig.md) |  | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**native_format** | **bool** | Specifies whether or not to enable native format for direct archive job. This field is set to true if native format should be used for archiving. | [optional] 
**objects** | [**List[GpfsProtectionGroupObjectParams]**](GpfsProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | 
**pre_post_script** | [**HostBasedBackupScriptParams**](HostBasedBackupScriptParams.md) |  | [optional] 
**protocol** | **str** | Specifies the preferred protocol to use if this device supports multiple protocols. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**throttling_config** | [**NasThrottlingConfig**](NasThrottlingConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.gpfs_protection_group_params import GpfsProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of GpfsProtectionGroupParams from a JSON string
gpfs_protection_group_params_instance = GpfsProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(GpfsProtectionGroupParams.to_json())

# convert the object into a dict
gpfs_protection_group_params_dict = gpfs_protection_group_params_instance.to_dict()
# create an instance of GpfsProtectionGroupParams from a dict
gpfs_protection_group_params_from_dict = GpfsProtectionGroupParams.from_dict(gpfs_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


