# RecoverGoogleWorkspaceParams

Specifies the recovery options specific to Google Workspace environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_action** | **str** | Specifies the type of recovery action to be performed. | 
**objects** | [**[CommonRecoverObjectSnapshotParams], none_type**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. | [optional] 
**recover_gmail_params** | [**RecoverGmailParams**](RecoverGmailParams.md) |  | [optional] 
**recover_google_drive_params** | [**RecoverGoogleDriveParams**](RecoverGoogleDriveParams.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


