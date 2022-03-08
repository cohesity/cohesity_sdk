# RecoverO365Params

Specifies the recovery options specific to Office 365 environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_action** | **str** | Specifies the type of recovery action to be performed. | 
**objects** | [**[CommonRecoverObjectSnapshotParams], none_type**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. | [optional] 
**recover_one_drive_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters to recover Office 365 One Drive. | [optional] 
**recover_mailbox_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters to recover Office 365 Mailbox. | [optional] 
**recover_public_folders_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters to recover Office 365 Public Folders. | [optional] 
**recover_ms_group_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters to recover Microsoft 365 Group. | [optional] 
**recover_ms_team_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters to recover Microsoft 365 Teams. | [optional] 
**recover_site_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters to recover Microsoft Office 365 Sharepoint Site. | [optional] 
**download_file_and_folder_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the recovery information to download files and folders. For instance, downloading mailbox items as PST. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


