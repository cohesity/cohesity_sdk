# ServiceNowObjectProtectionParams

Specifies the object parameters to create an ServiceNow Object Protection. If a table is in excludedTableVec and/or its prefix matches any of the prefixes in excludeTablePrefixVec then it will not be protected even if its name includeTableVec or its prefix matches any of the prefixes in includeTablePrefixVec.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the ServiceNow instance being protected. | 
**continue_on_error** | **bool, none_type** | Specifies whether to continue protecting other ServiceNow tables if object protection fails for one of tables failed. Default value is false. | [optional] 
**error_count** | **int, none_type** | Specifies the number of errors we faced while trying to protect ServiceNow instance. | [optional] 
**exclude_table_prefix_vec** | **[str], none_type** | Specifies the prefix for the tables to be excluded in the Object Protection. | [optional] 
**exclude_table_vec** | **[str], none_type** | Specifies the names for the tables to be excluded in the Object Protection. | [optional] 
**include_table_prefix_vec** | **[str], none_type** | Specifies the prefix for the tables to be included in the Object Protection. | [optional] 
**include_table_vec** | **[str], none_type** | Specifies the names for the tables to be included in the Object Protection. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


