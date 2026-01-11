# PolicySummaryResponse

Specifies the details about the Protection Policy Summary.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_protection_run_summary** | [**LastProtectionRunSummary**](LastProtectionRunSummary.md) |  | [optional] 
**pagination_cookie** | **str, none_type** | If there are more results to display, use this value to get the next set of results, by using this value in paginationCookie param for the next request to GetProtectionPolicySummary. | [optional] 
**policy** | [**ProtectionPolicy**](ProtectionPolicy.md) |  | [optional] 
**protection_groups_summary** | [**[ProtectionGroupRun], none_type**](CommonProtectionGroupRunResponseParameters.md) | Specifies the list of Protection Groups associated with the given Protection Policy. This is only populated if the type of the Protection Policy is kRegular. | [optional] 
**protection_runs_summary** | [**ProtectionRunsInPolicySummary**](ProtectionRunsInPolicySummary.md) |  | [optional] 
**protection_sources_summary** | [**[ProtectionSourceSummary], none_type**](ProtectionSourceSummary.md) | Specifies the list of Protection Sources which are protected under the given policy. This is only populated if the policy is of type kRPO. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


