# CommonRecoveryOptions

Configuration options for recovery and conflict resolutions for ServiceNow tables and records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_column_map** | **Dict[str, str]** | Mapping of alternate columns to be used when the target table lacks the required columns. | [optional] 
**default_values_for_extra_columns** | **str** | Default values of extra columns | [optional] 
**extra_target_column_action** | **str** | Action when there is a extra column in target table. Default value is skip. | [optional] 
**include_deleted_objects** | **bool** | Specifies whether to include deleted Objects in the recovery. | [optional] 
**missing_target_column_action** | **str** | Action when column is missing from target table. Default value is create. | [optional] 
**override_row_data** | **bool** | Specifies whether to override row data. Default value is true. | [optional] 
**preserve_sys_id** | **bool** | Specifies whether to preseve sys_id of the restored records | [optional] 
**table_not_found_action** | **str** | Action when target table is not found. Default value is error. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_recovery_options import CommonRecoveryOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CommonRecoveryOptions from a JSON string
common_recovery_options_instance = CommonRecoveryOptions.from_json(json)
# print the JSON string representation of the object
print(CommonRecoveryOptions.to_json())

# convert the object into a dict
common_recovery_options_dict = common_recovery_options_instance.to_dict()
# create an instance of CommonRecoveryOptions from a dict
common_recovery_options_from_dict = CommonRecoveryOptions.from_dict(common_recovery_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


