# MssqlObjectProtectionRequestParams

Specifies the request parameters specific to MSSQL object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_object_protection_type_params** | [**MssqlFileObjectProtectionParams**](MssqlFileObjectProtectionParams.md) |  | [optional] 
**native_object_protection_type_params** | [**MssqlNativeObjectProtectionParams**](MssqlNativeObjectProtectionParams.md) |  | [optional] 
**object_protection_type** | **str** | Specifies the MSSQL Object Protection type. | 

## Example

```python
from cohesity_sdk.helios.models.mssql_object_protection_request_params import MssqlObjectProtectionRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of MssqlObjectProtectionRequestParams from a JSON string
mssql_object_protection_request_params_instance = MssqlObjectProtectionRequestParams.from_json(json)
# print the JSON string representation of the object
print(MssqlObjectProtectionRequestParams.to_json())

# convert the object into a dict
mssql_object_protection_request_params_dict = mssql_object_protection_request_params_instance.to_dict()
# create an instance of MssqlObjectProtectionRequestParams from a dict
mssql_object_protection_request_params_from_dict = MssqlObjectProtectionRequestParams.from_dict(mssql_object_protection_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


