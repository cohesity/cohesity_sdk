# ProtectionGroupRuns

Protection runs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination_cookie** | **str, none_type** | Specifies the information needed in order to support pagination. This will not be included for the last page of results. | [optional] 
**runs** | [**[ProtectionGroupRun], none_type**](CommonProtectionGroupRunResponseParameters.md) | Specifies the list of Protection Group runs. | [optional] 
**total_runs** | **int, none_type** | Specifies the count of total runs exist for the given set of filters. The number of runs in single API call are limited and this count can be used to estimate query filter values to get next set of remaining runs. Please note that this field will only be populated if startTimeUsecs or endTimeUsecs or both are specified in query parameters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


