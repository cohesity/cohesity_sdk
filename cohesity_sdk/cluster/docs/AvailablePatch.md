# AvailablePatch

Specifies the description of an available patch.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** | Specifies the description of the service. | [optional] 
**count** | **int** | Specifies the number of fixed issues. | [optional] 
**dependencies** | **[str], none_type** | Specifies the services for which their patches must be applied together. | [optional] 
**fixed_issues** | [**[FixedIssue]**](FixedIssue.md) | Specifies the details of the issues fixed in the patch. | [optional] 
**service** | **str** | Specifies the name of the service. | [optional] 
**version** | **str** | Specifies the version of the patch. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


