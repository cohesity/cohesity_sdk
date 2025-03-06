# MSSQLProtectionGroupParams

Specifies the parameters specific to MSSQL Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_protection_type_params** | [**MSSQLFileProtectionGroupParams**](MSSQLFileProtectionGroupParams.md) |  | [optional] 
**native_protection_type_params** | [**MSSQLNativeProtectionGroupParams**](MSSQLNativeProtectionGroupParams.md) |  | [optional] 
**protection_type** | **str** | Specifies the MSSQL Protection Group type. | 
**volume_protection_type_params** | [**MSSQLVolumeProtectionGroupParams**](MSSQLVolumeProtectionGroupParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.mssql_protection_group_params import MSSQLProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of MSSQLProtectionGroupParams from a JSON string
mssql_protection_group_params_instance = MSSQLProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(MSSQLProtectionGroupParams.to_json())

# convert the object into a dict
mssql_protection_group_params_dict = mssql_protection_group_params_instance.to_dict()
# create an instance of MSSQLProtectionGroupParams from a dict
mssql_protection_group_params_from_dict = MSSQLProtectionGroupParams.from_dict(mssql_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


