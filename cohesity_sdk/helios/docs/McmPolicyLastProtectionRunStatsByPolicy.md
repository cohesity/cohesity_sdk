# McmPolicyLastProtectionRunStatsByPolicy

Specifies the last Protection Run stats for a policy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_objects_met_sla** | **int** | Specifies the number of objects Met SLA. | [optional] 
**num_objects_missed_sla** | **int** | Specifies the number of objects missed SLA. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_policy_last_protection_run_stats_by_policy import McmPolicyLastProtectionRunStatsByPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of McmPolicyLastProtectionRunStatsByPolicy from a JSON string
mcm_policy_last_protection_run_stats_by_policy_instance = McmPolicyLastProtectionRunStatsByPolicy.from_json(json)
# print the JSON string representation of the object
print(McmPolicyLastProtectionRunStatsByPolicy.to_json())

# convert the object into a dict
mcm_policy_last_protection_run_stats_by_policy_dict = mcm_policy_last_protection_run_stats_by_policy_instance.to_dict()
# create an instance of McmPolicyLastProtectionRunStatsByPolicy from a dict
mcm_policy_last_protection_run_stats_by_policy_from_dict = McmPolicyLastProtectionRunStatsByPolicy.from_dict(mcm_policy_last_protection_run_stats_by_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


