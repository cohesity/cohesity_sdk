# RecoverVMwareFileAndFolderParams

Specifies the parameters to recover files and folders.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files_and_folders** | [**[CommonRecoverFileAndFolderInfo], none_type**](CommonRecoverFileAndFolderInfo.md) | Specifies the info about the files and folders to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kVMware"
**glacier_retrieval_type** | **str, none_type** | Specifies the glacier retrieval type when restoring or downloding files or folders from a Glacier-based cloud snapshot. | [optional] 
**parent_recovery_id** | **str, none_type** | If current recovery is child task triggered through another parent recovery operation, then this field will specify the id of the parent recovery. | [optional] 
**vmware_target_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the parameters to recover to a VMware target. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


