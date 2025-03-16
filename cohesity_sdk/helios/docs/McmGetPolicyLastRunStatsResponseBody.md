# McmGetPolicyLastRunStatsResponseBody

Specifies the last Protection Run stats across all Protection Policies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stats_by_policy** | [**List[McmPolicyLastProtectionRunStats]**](McmPolicyLastProtectionRunStats.md) | Specifies the last Protection Run stats by policy. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_get_policy_last_run_stats_response_body import McmGetPolicyLastRunStatsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of McmGetPolicyLastRunStatsResponseBody from a JSON string
mcm_get_policy_last_run_stats_response_body_instance = McmGetPolicyLastRunStatsResponseBody.from_json(json)
# print the JSON string representation of the object
print(McmGetPolicyLastRunStatsResponseBody.to_json())

# convert the object into a dict
mcm_get_policy_last_run_stats_response_body_dict = mcm_get_policy_last_run_stats_response_body_instance.to_dict()
# create an instance of McmGetPolicyLastRunStatsResponseBody from a dict
mcm_get_policy_last_run_stats_response_body_from_dict = McmGetPolicyLastRunStatsResponseBody.from_dict(mcm_get_policy_last_run_stats_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


