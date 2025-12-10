# OracleObjectParams

Specifies the common parameters for Oracle database objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rman_backup_type** | **str** | Specifies the type of Oracle RMAN backup type. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.oracle_object_params import OracleObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of OracleObjectParams from a JSON string
oracle_object_params_instance = OracleObjectParams.from_json(json)
# print the JSON string representation of the object
print(OracleObjectParams.to_json())

# convert the object into a dict
oracle_object_params_dict = oracle_object_params_instance.to_dict()
# create an instance of OracleObjectParams from a dict
oracle_object_params_from_dict = OracleObjectParams.from_dict(oracle_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


