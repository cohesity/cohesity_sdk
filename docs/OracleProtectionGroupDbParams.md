# OracleProtectionGroupDbParams

Specifies the parameters of individual databases to create Oracle Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_id** | **int** | Specifies the id of the Oracle database. | [optional] 
**database_name** | **str** | Specifies the name of the Oracle database. | [optional] [readonly] 
**db_channels** | [**List[OracleDbChannel]**](OracleDbChannel.md) | Specifies the Oracle database node channels info. If not specified, the default values assigned by the server are applied to all the databases. | [optional] 

## Example

```python
from cohesity_sdk.models.oracle_protection_group_db_params import OracleProtectionGroupDbParams

# TODO update the JSON string below
json = "{}"
# create an instance of OracleProtectionGroupDbParams from a JSON string
oracle_protection_group_db_params_instance = OracleProtectionGroupDbParams.from_json(json)
# print the JSON string representation of the object
print(OracleProtectionGroupDbParams.to_json())

# convert the object into a dict
oracle_protection_group_db_params_dict = oracle_protection_group_db_params_instance.to_dict()
# create an instance of OracleProtectionGroupDbParams from a dict
oracle_protection_group_db_params_from_dict = OracleProtectionGroupDbParams.from_dict(oracle_protection_group_db_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


