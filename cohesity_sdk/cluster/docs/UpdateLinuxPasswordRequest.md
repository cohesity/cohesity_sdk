# UpdateLinuxPasswordRequest

Specifies the linux user params.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str, none_type** | Specifies the linux username for which the password will be updated. | 
**current_password** | **str, none_type** | Specifies the current password of the user. This is required when trying to update the current user&#39;s password. | [optional] 
**new_password** | **str, none_type** | Specifies the new linux password. | [optional] 
**verify_password** | **bool, none_type** | True if request is only to verify if current password matches with set password. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


