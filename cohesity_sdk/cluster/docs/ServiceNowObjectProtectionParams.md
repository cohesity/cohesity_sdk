# ServiceNowObjectProtectionParams

Specifies the object parameters to create an ServiceNow Object Protection. If a table is in excludedTableVec and/or its prefix matches any of the prefixes in excludeTablePrefixVec then it will not be protected even if its name includeTableVec or its prefix matches any of the prefixes in includeTablePrefixVec.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue protecting other ServiceNow tables if object protection fails for one of tables failed. Default value is false. | [optional] 
**error_count** | **int** | Specifies the number of errors we faced while trying to protect ServiceNow instance. | [optional] 
**exclude_table_prefix_vec** | **List[str]** | Specifies the prefix for the tables to be excluded in the Object Protection. | [optional] 
**exclude_table_vec** | **List[str]** | Specifies the names for the tables to be excluded in the Object Protection. | [optional] 
**id** | **int** | Specifies the id of the ServiceNow instance being protected. | 
**include_table_prefix_vec** | **List[str]** | Specifies the prefix for the tables to be included in the Object Protection. | [optional] 
**include_table_vec** | **List[str]** | Specifies the names for the tables to be included in the Object Protection. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.service_now_object_protection_params import ServiceNowObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceNowObjectProtectionParams from a JSON string
service_now_object_protection_params_instance = ServiceNowObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(ServiceNowObjectProtectionParams.to_json())

# convert the object into a dict
service_now_object_protection_params_dict = service_now_object_protection_params_instance.to_dict()
# create an instance of ServiceNowObjectProtectionParams from a dict
service_now_object_protection_params_from_dict = ServiceNowObjectProtectionParams.from_dict(service_now_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


