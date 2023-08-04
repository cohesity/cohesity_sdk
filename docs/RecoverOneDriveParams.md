# RecoverOneDriveParams

Specifies the parameters to recover an Office 365 OneDrive.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[ObjectOneDriveParam], none_type**](ObjectOneDriveParam.md) | Specifies a list of OneDrive params associated with the objects to recover. | 
**target_drive** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the target OneDrive to recover to. If not specified, the objects will be recovered to original location. | [optional] 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other OneDrive items if one of items failed to recover. Default value is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


