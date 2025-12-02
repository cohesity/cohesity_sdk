# LogicalStats

Specifies the total logical data size of all the local and Cloud Tier data stored by the Cohesity Cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_logical_usage_bytes** | **int** | Specifies the size of data before reduction by deduplication and compression. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.logical_stats import LogicalStats

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalStats from a JSON string
logical_stats_instance = LogicalStats.from_json(json)
# print the JSON string representation of the object
print(LogicalStats.to_json())

# convert the object into a dict
logical_stats_dict = logical_stats_instance.to_dict()
# create an instance of LogicalStats from a dict
logical_stats_from_dict = LogicalStats.from_dict(logical_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


