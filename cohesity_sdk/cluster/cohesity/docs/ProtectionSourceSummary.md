# ProtectionSourceSummary

ProtectedSourceSummary is the summary of all the Protection Runs for the Protection groups using the Specified Protection Policy. This is only populated for a policy of type kRPO.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_protection_group_paused** | **bool, none_type** | Specifies the status of the protection group | [optional] 
**last_protection_run** | [**CommonProtectionGroupRunResponseParameters**](CommonProtectionGroupRunResponseParameters.md) |  | [optional] 
**next_protection_run_time_usecs** | **int, none_type** | Specifies the time at which the next Protection Run is scheduled for the given Protection Source in Unix epoch Time | [optional] 
**object** | [**Object**](Object.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


