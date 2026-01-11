# NodeRemovalParams

Specifies parameters to initiate/cancel node removal.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel** | **bool, none_type** | If true, cancels node removal that is already in progress. | 
**is_clear_pre_check_result_only** | **bool, none_type** | Specifies whether request is for clearing pre-check result only | [optional]  if omitted the server will use the default value of False
**is_offline** | **bool, none_type** | Specifies whether node being removed is offline. | [optional]  if omitted the server will use the default value of False
**is_validate_only** | **bool, none_type** | Specifies whether request is for pre-check validations only | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


