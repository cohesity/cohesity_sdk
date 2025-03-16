# MssqlObjectProtectionResponseParams

Specifies the response parameters specific to MSSQL object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_file_object_protection_type_params** | [**CommonMssqlFileObjectProtectionParams**](CommonMssqlFileObjectProtectionParams.md) |  | [optional] 
**common_native_object_protection_type_params** | [**CommonMssqlNativeObjectProtectionParams**](CommonMssqlNativeObjectProtectionParams.md) |  | [optional] 
**object_protection_type** | **str** | Specifies the MSSQL Object Protection type. | 

## Example

```python
from cohesity_sdk.helios.models.mssql_object_protection_response_params import MssqlObjectProtectionResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of MssqlObjectProtectionResponseParams from a JSON string
mssql_object_protection_response_params_instance = MssqlObjectProtectionResponseParams.from_json(json)
# print the JSON string representation of the object
print(MssqlObjectProtectionResponseParams.to_json())

# convert the object into a dict
mssql_object_protection_response_params_dict = mssql_object_protection_response_params_instance.to_dict()
# create an instance of MssqlObjectProtectionResponseParams from a dict
mssql_object_protection_response_params_from_dict = MssqlObjectProtectionResponseParams.from_dict(mssql_object_protection_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


