# MssqlObjectProtectionParams

Specifies the parameters specific to MSSQL Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_object_protection_type_params** | [**MssqlFileObjectProtectionParams**](MssqlFileObjectProtectionParams.md) |  | [optional] 
**native_object_protection_type_params** | [**MssqlNativeObjectProtectionParams**](MssqlNativeObjectProtectionParams.md) |  | [optional] 
**object_protection_type** | **str** | Specifies the MSSQL Object Protection type. | 

## Example

```python
from cohesity_sdk.models.mssql_object_protection_params import MssqlObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of MssqlObjectProtectionParams from a JSON string
mssql_object_protection_params_instance = MssqlObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(MssqlObjectProtectionParams.to_json())

# convert the object into a dict
mssql_object_protection_params_dict = mssql_object_protection_params_instance.to_dict()
# create an instance of MssqlObjectProtectionParams from a dict
mssql_object_protection_params_from_dict = MssqlObjectProtectionParams.from_dict(mssql_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


