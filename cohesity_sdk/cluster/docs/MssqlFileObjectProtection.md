# MssqlFileObjectProtection

Specifies the object params to create File based MSSQL Object Protection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object being protected. If this is a non leaf level object, then the object will be auto-protected unless leaf objects are specified for exclusion. | 

## Example

```python
from cohesity_sdk.cluster.models.mssql_file_object_protection import MssqlFileObjectProtection

# TODO update the JSON string below
json = "{}"
# create an instance of MssqlFileObjectProtection from a JSON string
mssql_file_object_protection_instance = MssqlFileObjectProtection.from_json(json)
# print the JSON string representation of the object
print(MssqlFileObjectProtection.to_json())

# convert the object into a dict
mssql_file_object_protection_dict = mssql_file_object_protection_instance.to_dict()
# create an instance of MssqlFileObjectProtection from a dict
mssql_file_object_protection_from_dict = MssqlFileObjectProtection.from_dict(mssql_file_object_protection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


