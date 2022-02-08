# VmwareRecoverFilesNewTargetConfig

Specifies the configuration for recovering files and folders to a new target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_vm** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the target VM to recover files and folders to. | 
**recover_method** | **str** | Specifies the method to recover files and folders. | 
**absolute_path** | **str, none_type** | Specifies the path location to recover files to. | 
**target_vm_credentials** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the credentials for the target VM. This is mandatory if the recoverMethod is AutoDeploy or UseHypervisorApis. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


