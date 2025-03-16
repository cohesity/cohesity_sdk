# OracleProtectionGroupObjectParams

Specifies the object identifier to create Oracle Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_params** | [**List[OracleProtectionGroupDbParams]**](OracleProtectionGroupDbParams.md) | Specifies the properties of the Oracle databases. | [optional] 
**source_id** | **int** | Specifies the id of the host on which databases are hosted. | 
**source_name** | **str** | Specifies the name of the host on which databases are hosted. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.oracle_protection_group_object_params import OracleProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of OracleProtectionGroupObjectParams from a JSON string
oracle_protection_group_object_params_instance = OracleProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(OracleProtectionGroupObjectParams.to_json())

# convert the object into a dict
oracle_protection_group_object_params_dict = oracle_protection_group_object_params_instance.to_dict()
# create an instance of OracleProtectionGroupObjectParams from a dict
oracle_protection_group_object_params_from_dict = OracleProtectionGroupObjectParams.from_dict(oracle_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


