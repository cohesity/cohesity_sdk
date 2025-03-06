# MssqlObjectEntityParams

Object details for Mssql.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aag_info** | [**AAGInfo**](AAGInfo.md) |  | [optional] 
**host_info** | [**HostInformation**](HostInformation.md) |  | [optional] 
**is_encrypted** | **bool** | Specifies whether the database is TDE enabled. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.mssql_object_entity_params import MssqlObjectEntityParams

# TODO update the JSON string below
json = "{}"
# create an instance of MssqlObjectEntityParams from a JSON string
mssql_object_entity_params_instance = MssqlObjectEntityParams.from_json(json)
# print the JSON string representation of the object
print(MssqlObjectEntityParams.to_json())

# convert the object into a dict
mssql_object_entity_params_dict = mssql_object_entity_params_instance.to_dict()
# create an instance of MssqlObjectEntityParams from a dict
mssql_object_entity_params_from_dict = MssqlObjectEntityParams.from_dict(mssql_object_entity_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


