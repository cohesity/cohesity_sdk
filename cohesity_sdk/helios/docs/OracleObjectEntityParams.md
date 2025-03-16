# OracleObjectEntityParams

Object details for Oracle.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_entity_info** | [**DatabaseEntityInfo**](DatabaseEntityInfo.md) |  | [optional] 
**host_info** | [**HostInformation**](HostInformation.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.oracle_object_entity_params import OracleObjectEntityParams

# TODO update the JSON string below
json = "{}"
# create an instance of OracleObjectEntityParams from a JSON string
oracle_object_entity_params_instance = OracleObjectEntityParams.from_json(json)
# print the JSON string representation of the object
print(OracleObjectEntityParams.to_json())

# convert the object into a dict
oracle_object_entity_params_dict = oracle_object_entity_params_instance.to_dict()
# create an instance of OracleObjectEntityParams from a dict
oracle_object_entity_params_from_dict = OracleObjectEntityParams.from_dict(oracle_object_entity_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


