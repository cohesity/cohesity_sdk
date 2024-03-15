# RecoverOneDriveParams

Specifies the parameters to recover an Office 365 OneDrive.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[ObjectOneDriveParam], none_type**](ObjectOneDriveParam.md) | Specifies a list of OneDrive params associated with the objects to recover. These parameters allow overriding the request level &#39;recoverUserDefaultDrive&#39; parameter for each object specified here. | 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other OneDrive items if one of items failed to recover. Default value is false. | [optional] 
**recover_preservation_hold_library** | **bool, none_type** | Specifies whether to recover Preservation Hold Library associated with the OneDrives selected for restore. Default value is false. | [optional] 
**recover_user_default_drive** | **bool, none_type** | Specifies whether to recover default drives associated with the OneDrives selected for restore. Default value is true. This setting can be overridden for each object selected for recovery, by specifying &#39;recoverEntireDrive&#39; for the desired drive within &#39;oneDriveParams&#39;. Granular recovery is still allowed even if this value is set to true. | [optional] 
**target_drive** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the target OneDrive to recover to. If not specified, the objects will be recovered to original location. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


