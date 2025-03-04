# NoSqlProtectionGroupObjectParams

Specifies an object protected by a Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.no_sql_protection_group_object_params import NoSqlProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of NoSqlProtectionGroupObjectParams from a JSON string
no_sql_protection_group_object_params_instance = NoSqlProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(NoSqlProtectionGroupObjectParams.to_json())

# convert the object into a dict
no_sql_protection_group_object_params_dict = no_sql_protection_group_object_params_instance.to_dict()
# create an instance of NoSqlProtectionGroupObjectParams from a dict
no_sql_protection_group_object_params_from_dict = NoSqlProtectionGroupObjectParams.from_dict(no_sql_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


