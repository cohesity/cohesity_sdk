# MSSQLNativeProtectionGroupObjectParams

Specifies the object params to create File based MSSQL Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object being protected. If this is a non leaf level object, then the object will be auto-protected unless leaf objects are specified for exclusion. | 
**name** | **str** | Specifies the name of the object being protected. | [optional] [readonly] 
**source_type** | **str** | Specifies the type of source being protected. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.mssql_native_protection_group_object_params import MSSQLNativeProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of MSSQLNativeProtectionGroupObjectParams from a JSON string
mssql_native_protection_group_object_params_instance = MSSQLNativeProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(MSSQLNativeProtectionGroupObjectParams.to_json())

# convert the object into a dict
mssql_native_protection_group_object_params_dict = mssql_native_protection_group_object_params_instance.to_dict()
# create an instance of MSSQLNativeProtectionGroupObjectParams from a dict
mssql_native_protection_group_object_params_from_dict = MSSQLNativeProtectionGroupObjectParams.from_dict(mssql_native_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


