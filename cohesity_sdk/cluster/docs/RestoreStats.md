# RestoreStats

Specifies the restore statistics details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_cloned_objects** | **int** | Specifies the count of cloned objects in the given time frame. | [optional] 
**num_recovered_objects** | **int** | Specifies the count of recovered objects in the given time frame. | [optional] 
**stats_by_environment** | [**List[RestoreEnvStats]**](RestoreEnvStats.md) | Specifies the stats of recovery jobs aggregated by the environment type. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.restore_stats import RestoreStats

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreStats from a JSON string
restore_stats_instance = RestoreStats.from_json(json)
# print the JSON string representation of the object
print(RestoreStats.to_json())

# convert the object into a dict
restore_stats_dict = restore_stats_instance.to_dict()
# create an instance of RestoreStats from a dict
restore_stats_from_dict = RestoreStats.from_dict(restore_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


