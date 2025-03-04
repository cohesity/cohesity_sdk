# MssqlNativeObjectProtection

Specifies the object params to create Native based MSSQL Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object being protected. If this is a non leaf level object, then the object will be auto-protected unless leaf objects are specified for exclusion. | 

## Example

```python
from cohesity_sdk.models.mssql_native_object_protection import MssqlNativeObjectProtection

# TODO update the JSON string below
json = "{}"
# create an instance of MssqlNativeObjectProtection from a JSON string
mssql_native_object_protection_instance = MssqlNativeObjectProtection.from_json(json)
# print the JSON string representation of the object
print(MssqlNativeObjectProtection.to_json())

# convert the object into a dict
mssql_native_object_protection_dict = mssql_native_object_protection_instance.to_dict()
# create an instance of MssqlNativeObjectProtection from a dict
mssql_native_object_protection_from_dict = MssqlNativeObjectProtection.from_dict(mssql_native_object_protection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


