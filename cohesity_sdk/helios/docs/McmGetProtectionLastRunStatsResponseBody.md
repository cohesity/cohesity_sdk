# McmGetProtectionLastRunStatsResponseBody

Specifies the last Protection Run stats across objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregated_stats** | [**List[McmLastRunStatusStats]**](McmLastRunStatusStats.md) | Specifies the aggregated status across all adapters for respective last run. | [optional] 
**env_stats** | [**List[McmLastRunEnvSpecificStatusStats]**](McmLastRunEnvSpecificStatusStats.md) | Specifies the enviournment specific last run status stats. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_get_protection_last_run_stats_response_body import McmGetProtectionLastRunStatsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of McmGetProtectionLastRunStatsResponseBody from a JSON string
mcm_get_protection_last_run_stats_response_body_instance = McmGetProtectionLastRunStatsResponseBody.from_json(json)
# print the JSON string representation of the object
print(McmGetProtectionLastRunStatsResponseBody.to_json())

# convert the object into a dict
mcm_get_protection_last_run_stats_response_body_dict = mcm_get_protection_last_run_stats_response_body_instance.to_dict()
# create an instance of McmGetProtectionLastRunStatsResponseBody from a dict
mcm_get_protection_last_run_stats_response_body_from_dict = McmGetProtectionLastRunStatsResponseBody.from_dict(mcm_get_protection_last_run_stats_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


