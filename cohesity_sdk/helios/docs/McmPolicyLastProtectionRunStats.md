# McmPolicyLastProtectionRunStats

Specifies the last Protection Run stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the cluster Id. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the cluster Incarnation Id. | [optional] 
**last_run_stats** | [**McmPolicyLastProtectionRunStatsByPolicy**](McmPolicyLastProtectionRunStatsByPolicy.md) |  | [optional] 
**policy_id** | **str** | Specifies the policy Id. | [optional] 
**policy_name** | **str** | Specifies the policy name. | [optional] 
**region_id** | **str** | Specifies the region Id. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_policy_last_protection_run_stats import McmPolicyLastProtectionRunStats

# TODO update the JSON string below
json = "{}"
# create an instance of McmPolicyLastProtectionRunStats from a JSON string
mcm_policy_last_protection_run_stats_instance = McmPolicyLastProtectionRunStats.from_json(json)
# print the JSON string representation of the object
print(McmPolicyLastProtectionRunStats.to_json())

# convert the object into a dict
mcm_policy_last_protection_run_stats_dict = mcm_policy_last_protection_run_stats_instance.to_dict()
# create an instance of McmPolicyLastProtectionRunStats from a dict
mcm_policy_last_protection_run_stats_from_dict = McmPolicyLastProtectionRunStats.from_dict(mcm_policy_last_protection_run_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


