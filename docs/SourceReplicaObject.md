# SourceReplicaObject

Specifies the response after succesfully initiating the failover request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replica_object_id** | **int** | Specifies the object Id existing on the replciation cluster. | [optional] 
**source_object_id** | **int** | Specifies the corrosponding object id existing on the source cluster. | [optional] 

## Example

```python
from cohesity_sdk.models.source_replica_object import SourceReplicaObject

# TODO update the JSON string below
json = "{}"
# create an instance of SourceReplicaObject from a JSON string
source_replica_object_instance = SourceReplicaObject.from_json(json)
# print the JSON string representation of the object
print(SourceReplicaObject.to_json())

# convert the object into a dict
source_replica_object_dict = source_replica_object_instance.to_dict()
# create an instance of SourceReplicaObject from a dict
source_replica_object_from_dict = SourceReplicaObject.from_dict(source_replica_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


