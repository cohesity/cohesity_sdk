# RestoreEnvStats

Specifies the aggregated statistics for restores of a specific environment type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment. | [optional] 
**object_count** | **int** |  | [optional] 
**total_bytes** | **int** |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.restore_env_stats import RestoreEnvStats

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreEnvStats from a JSON string
restore_env_stats_instance = RestoreEnvStats.from_json(json)
# print the JSON string representation of the object
print(RestoreEnvStats.to_json())

# convert the object into a dict
restore_env_stats_dict = restore_env_stats_instance.to_dict()
# create an instance of RestoreEnvStats from a dict
restore_env_stats_from_dict = RestoreEnvStats.from_dict(restore_env_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


