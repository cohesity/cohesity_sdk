# ProtectedObjectActionResponse

Specifies the response upon performing an action on protected objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the action type to be performed on object getting protected. Based on selected action, provide the action params. | [optional] 
**objects** | [**[ActionObjectLevelResponse]**](ActionObjectLevelResponse.md) | Specifies the list of objects on which the provided action was performed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


