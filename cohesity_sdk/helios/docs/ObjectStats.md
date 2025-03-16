# ObjectStats

Specifies the object stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots_summary** | [**List[SnapshotsSummary]**](SnapshotsSummary.md) | Specifies a summary of the object snapshots. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.object_stats import ObjectStats

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectStats from a JSON string
object_stats_instance = ObjectStats.from_json(json)
# print the JSON string representation of the object
print(ObjectStats.to_json())

# convert the object into a dict
object_stats_dict = object_stats_instance.to_dict()
# create an instance of ObjectStats from a dict
object_stats_from_dict = ObjectStats.from_dict(object_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


