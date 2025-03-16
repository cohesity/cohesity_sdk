# McmLastRunEnvSpecificStatusStats

Specifies the enviournment specific last run status stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregated_stats** | [**List[McmLastRunStatusStats]**](McmLastRunStatusStats.md) | Specifies the aggregated status across all adapters for respective last run. | [optional] 
**environment** | **str** | Specifies the environment type of object. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_last_run_env_specific_status_stats import McmLastRunEnvSpecificStatusStats

# TODO update the JSON string below
json = "{}"
# create an instance of McmLastRunEnvSpecificStatusStats from a JSON string
mcm_last_run_env_specific_status_stats_instance = McmLastRunEnvSpecificStatusStats.from_json(json)
# print the JSON string representation of the object
print(McmLastRunEnvSpecificStatusStats.to_json())

# convert the object into a dict
mcm_last_run_env_specific_status_stats_dict = mcm_last_run_env_specific_status_stats_instance.to_dict()
# create an instance of McmLastRunEnvSpecificStatusStats from a dict
mcm_last_run_env_specific_status_stats_from_dict = McmLastRunEnvSpecificStatusStats.from_dict(mcm_last_run_env_specific_status_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


