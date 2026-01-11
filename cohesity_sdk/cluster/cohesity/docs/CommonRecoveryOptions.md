# CommonRecoveryOptions

Configuration options for recovery and conflict resolutions for ServiceNow tables and records.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_column_map** | **{str: (str,)}, none_type** | Mapping of alternate columns to be used when the target table lacks the required columns. | [optional] 
**default_values_for_extra_columns** | **str, none_type** | Default values of extra columns | [optional] 
**extra_target_column_action** | **str, none_type** | Action when there is a extra column in target table. Default value is skip. | [optional] 
**include_deleted_objects** | **bool, none_type** | Specifies whether to include deleted Objects in the recovery. | [optional] 
**missing_target_column_action** | **str, none_type** | Action when column is missing from target table. Default value is create. | [optional] 
**override_row_data** | **bool, none_type** | Specifies whether to override row data. Default value is true. | [optional] 
**preserve_sys_id** | **bool, none_type** | Specifies whether to preseve sys_id of the restored records | [optional] 
**table_not_found_action** | **str, none_type** | Action when target table is not found. Default value is error. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


