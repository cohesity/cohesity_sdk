# CassandraParams

Specifies the recovery options specific to Cassandra environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other objects if one of Object failed to recover. Default value is false. | [optional] 
**is_multi_stage_restore** | **bool** | Specifies whether the current recovery operation is a multi-stage restore operation. | [optional] 
**recover_cassandra_params** | [**RecoverCassandraParams**](RecoverCassandraParams.md) |  | 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.cluster.models.cassandra_params import CassandraParams

# TODO update the JSON string below
json = "{}"
# create an instance of CassandraParams from a JSON string
cassandra_params_instance = CassandraParams.from_json(json)
# print the JSON string representation of the object
print(CassandraParams.to_json())

# convert the object into a dict
cassandra_params_dict = cassandra_params_instance.to_dict()
# create an instance of CassandraParams from a dict
cassandra_params_from_dict = CassandraParams.from_dict(cassandra_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


