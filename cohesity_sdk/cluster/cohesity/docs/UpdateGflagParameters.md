# UpdateGflagParameters

Specifies the parameters for updating service gflags.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_now** | **bool, none_type** | Specifies whether to apply the change immediately. If set to true, the gflag change will work without restarting the service. | [optional] 
**reason** | **str, none_type** | Specifies the reason for clearing gflags. | [optional] 
**service_flags** | [**ServiceGflags**](ServiceGflags.md) |  | [optional] 
**skip_existence_check** | **bool, none_type** | Skips the KUndefinedFlagPrefix validation check and allows the user to set undefined gflags, effective after service restart/upgrade | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


