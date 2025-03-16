# ReplicationCopy

Specifies the information about replication snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_time_usecs** | **int** | Specifies the creation time of replication snapshot. | [optional] 
**replication_cluster** | [**ReplicationCluster**](ReplicationCluster.md) |  | [optional] 
**status** | **str** | Specifies the status of the replication snapshot. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.replication_copy import ReplicationCopy

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationCopy from a JSON string
replication_copy_instance = ReplicationCopy.from_json(json)
# print the JSON string representation of the object
print(ReplicationCopy.to_json())

# convert the object into a dict
replication_copy_dict = replication_copy_instance.to_dict()
# create an instance of ReplicationCopy from a dict
replication_copy_from_dict = ReplicationCopy.from_dict(replication_copy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


