# RecoverPhysicalParams

Specifies the recovery options specific to Physical environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[CommonRecoverObjectSnapshotParams], none_type**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of Recover Object parameters. For recovering files, specifies the object contains the file to recover. | 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 
**recover_volume_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the parameters to recover Physical Volumes. | [optional] 
**mount_volume_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the parameters to mount Physical Volumes. | [optional] 
**recover_file_and_folder_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the parameters to perform a file and folder recovery. | [optional] 
**download_file_and_folder_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the parameters to download files and folders. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


