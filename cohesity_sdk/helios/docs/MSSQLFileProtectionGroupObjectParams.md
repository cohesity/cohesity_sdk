# MSSQLFileProtectionGroupObjectParams

Specifies the object params to create File based MSSQL Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object being protected. If this is a non leaf level object, then the object will be auto-protected unless leaf objects are specified for exclusion. | 
**name** | **str** | Specifies the name of the object being protected. | [optional] [readonly] 
**source_type** | **str** | Specifies the type of source being protected. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.mssql_file_protection_group_object_params import MSSQLFileProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of MSSQLFileProtectionGroupObjectParams from a JSON string
mssql_file_protection_group_object_params_instance = MSSQLFileProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(MSSQLFileProtectionGroupObjectParams.to_json())

# convert the object into a dict
mssql_file_protection_group_object_params_dict = mssql_file_protection_group_object_params_instance.to_dict()
# create an instance of MSSQLFileProtectionGroupObjectParams from a dict
mssql_file_protection_group_object_params_from_dict = MSSQLFileProtectionGroupObjectParams.from_dict(mssql_file_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


