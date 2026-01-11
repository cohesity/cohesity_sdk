# RecoverServiceNowParams

Specifies the recovery params specific to ServiceNow recovery.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other ServiceNow tables if one of tables failed to recover. Default value is false. | [optional] 
**error_count** | **int, none_type** | Specifies the number of errors we faced while trying to restore ServiceNow tables. | [optional] 
**instance** | [**RecoverServiceNowInstanceParams**](RecoverServiceNowInstanceParams.md) |  | [optional] 
**recover_to** | **int, none_type** | Specifies the id of registered source where the tables are to be recovered. If this is not specified, the recovery job will recover to the original location. | [optional] 
**tables** | [**[RecoverServiceNowTableParams], none_type**](RecoverServiceNowTableParams.md) | Specifies the params for table level recovery. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


