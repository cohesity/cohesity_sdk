# PolicySummaryResponse

Specifies the details about the Protection Policy Summary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_protection_run_summary** | [**LastProtectionRunSummary**](LastProtectionRunSummary.md) |  | [optional] 
**pagination_cookie** | **str** | If there are more results to display, use this value to get the next set of results, by using this value in paginationCookie param for the next request to GetProtectionPolicySummary. | [optional] 
**policy** | [**ProtectionPolicy**](ProtectionPolicy.md) |  | [optional] 
**protection_groups_summary** | [**List[CommonProtectionGroupRunResponseParameters]**](CommonProtectionGroupRunResponseParameters.md) | Specifies the list of Protection Groups associated with the given Protection Policy. This is only populated if the type of the Protection Policy is kRegular. | [optional] 
**protection_runs_summary** | [**ProtectionRunsInPolicySummary**](ProtectionRunsInPolicySummary.md) |  | [optional] 
**protection_sources_summary** | [**List[ProtectionSourceSummary]**](ProtectionSourceSummary.md) | Specifies the list of Protection Sources which are protected under the given policy. This is only populated if the policy is of type kRPO. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.policy_summary_response import PolicySummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PolicySummaryResponse from a JSON string
policy_summary_response_instance = PolicySummaryResponse.from_json(json)
# print the JSON string representation of the object
print(PolicySummaryResponse.to_json())

# convert the object into a dict
policy_summary_response_dict = policy_summary_response_instance.to_dict()
# create an instance of PolicySummaryResponse from a dict
policy_summary_response_from_dict = PolicySummaryResponse.from_dict(policy_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


