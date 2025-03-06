# ReplicaFailoverObject

Specifies the object paring of replicated object and failover object created after restore.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failover_object_id** | **int** | Specifies the corrosponding object id of the failover object. | [optional] 
**replica_object_id** | **int** | Specifies the object Id existing on the replciation cluster. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.replica_failover_object import ReplicaFailoverObject

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicaFailoverObject from a JSON string
replica_failover_object_instance = ReplicaFailoverObject.from_json(json)
# print the JSON string representation of the object
print(ReplicaFailoverObject.to_json())

# convert the object into a dict
replica_failover_object_dict = replica_failover_object_instance.to_dict()
# create an instance of ReplicaFailoverObject from a dict
replica_failover_object_from_dict = ReplicaFailoverObject.from_dict(replica_failover_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


