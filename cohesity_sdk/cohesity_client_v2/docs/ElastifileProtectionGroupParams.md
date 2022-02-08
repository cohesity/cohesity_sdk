# ElastifileProtectionGroupParams

Specifies the parameters which are specific to Elastifile related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[ElastifileProtectionGroupObjectParams]**](ElastifileProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | 
**direct_cloud_archive** | **bool, none_type** | Specifies whether or not to store the snapshots in this run directly in an Archive Target instead of on the Cluster. If this is set to true, the associated policy must have exactly one Archive Target associated with it and the policy must be set up to archive after every run. Also, a Storage Domain cannot be specified. Default behavior is &#39;false&#39;. | [optional] 
**native_format** | **bool, none_type** | Specifies whether or not to enable native format for direct archive job. This field is set to true if native format should be used for archiving. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**protocol** | **str, none_type** | Specifies the protocol of the NAS device being backed up. | [optional] 
**continue_on_error** | **bool, none_type** | Specifies whether or not the Protection Group should continue regardless of whether or not an error was encountered. | [optional] 
**encryption_enabled** | **bool, none_type** | Specifies whether the protection group should use encryption while backup or not. | [optional] 
**file_lock_config** | [**FileLevelDataLockConfig**](FileLevelDataLockConfig.md) |  | [optional] 
**file_filters** | [**FileFilteringPolicy**](FileFilteringPolicy.md) |  | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**pre_post_script** | [**HostBasedBackupScriptParams**](HostBasedBackupScriptParams.md) |  | [optional] 
**filter_ip_config** | [**FilterIpConfig**](FilterIpConfig.md) |  | [optional] 
**throttling_config** | [**NasThrottlingConfig**](NasThrottlingConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


