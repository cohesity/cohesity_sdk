# FilerLifecycleAgingPolicy

Specifies the aging policy. Note: Both the fields days and dateInUsecs are mutually exclusive to each other.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aging_criteria** | **str, none_type** | Specifies the criteria for aging | 
**date_in_usecs** | **int, none_type** | Files that possess timestamps exceeding the specified value will be eligible for selection. | [optional] 
**days** | **int, none_type** | Files that possess timestamps older than the specified value in days will be eligible for selection. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


