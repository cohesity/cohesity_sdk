# AzureRecoverFilesOriginalTargetConfig

Specifies the configuration for recovering files and folders to the original target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_original_path** | **bool, none_type** | Specifies whether to recover files and folders to the original path location. If false, alternatePath must be specified. | 
**target_vm_credentials** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the credentials for the target VM. | [optional] 
**alternate_path** | **str, none_type** | Specifies the alternate path location to recover files to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


