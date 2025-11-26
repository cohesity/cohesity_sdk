# AppliedPatch

Specifies the description of an applied patch.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied_time_msecs** | **int** | Specifies the time when the patch was applied in Unix epoch in milliseconds. | [optional] 
**component** | **str** | Specifies the description of the service. | [optional] 
**count** | **int** | Specifies the number of fixed issues. | [optional] 
**dependencies** | **[str], none_type** | Specifies the services for which their patches were applied together. They will also be reverted together. | [optional] 
**fixed_issues** | [**[FixedIssue]**](FixedIssue.md) | Specifies the details of the issues fixed in the patch. | [optional] 
**patch_level** | **int** | Specifies the number of patches applied so far for this service. | [optional] 
**service** | **str** | Specifies the name of the service. | [optional] 
**version** | **str** | Specifies the version of the patch. | [optional] 
**version_replaced** | **str** | Specifies the version it replaced. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


