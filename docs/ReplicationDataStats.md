# ReplicationDataStats

Specifies statistics about replication data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logical_bytes_transferred** | **int** | Specifies the total logical bytes transferred. | [optional] 
**logical_size_bytes** | **int** | Specifies the total logical size in bytes. | [optional] 
**physical_bytes_transferred** | **int** | Specifies the total physical bytes transferred. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.replication_data_stats import ReplicationDataStats

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationDataStats from a JSON string
replication_data_stats_instance = ReplicationDataStats.from_json(json)
# print the JSON string representation of the object
print(ReplicationDataStats.to_json())

# convert the object into a dict
replication_data_stats_dict = replication_data_stats_instance.to_dict()
# create an instance of ReplicationDataStats from a dict
replication_data_stats_from_dict = ReplicationDataStats.from_dict(replication_data_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


