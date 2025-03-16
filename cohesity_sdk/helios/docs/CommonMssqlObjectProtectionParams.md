# CommonMssqlObjectProtectionParams

Specifies the common parameters for MSSQL Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_file_object_protection_type_params** | [**CommonMssqlFileObjectProtectionParams**](CommonMssqlFileObjectProtectionParams.md) |  | [optional] 
**common_native_object_protection_type_params** | [**CommonMssqlNativeObjectProtectionParams**](CommonMssqlNativeObjectProtectionParams.md) |  | [optional] 
**object_protection_type** | **str** | Specifies the MSSQL Object Protection type. | 

## Example

```python
from cohesity_sdk.helios.models.common_mssql_object_protection_params import CommonMssqlObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonMssqlObjectProtectionParams from a JSON string
common_mssql_object_protection_params_instance = CommonMssqlObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(CommonMssqlObjectProtectionParams.to_json())

# convert the object into a dict
common_mssql_object_protection_params_dict = common_mssql_object_protection_params_instance.to_dict()
# create an instance of CommonMssqlObjectProtectionParams from a dict
common_mssql_object_protection_params_from_dict = CommonMssqlObjectProtectionParams.from_dict(common_mssql_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


