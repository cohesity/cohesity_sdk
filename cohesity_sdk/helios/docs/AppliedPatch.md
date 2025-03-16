# AppliedPatch

Specifies the description of an applied patch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied_time_msecs** | **int** | Specifies the time when the patch was applied in Unix epoch in milliseconds. | [optional] 
**component** | **str** | Specifies the description of the service. | [optional] 
**count** | **int** | Specifies the number of fixed issues. | [optional] 
**dependencies** | **List[str]** | Specifies the services for which their patches were applied together. They will also be reverted together. | [optional] 
**fixed_issues** | [**List[FixedIssue]**](FixedIssue.md) | Specifies the details of the issues fixed in the patch. | [optional] 
**patch_level** | **int** | Specifies the number of patches applied so far for this service. | [optional] 
**service** | **str** | Specifies the name of the service. | [optional] 
**version** | **str** | Specifies the version of the patch. | [optional] 
**version_replaced** | **str** | Specifies the version it replaced. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.applied_patch import AppliedPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AppliedPatch from a JSON string
applied_patch_instance = AppliedPatch.from_json(json)
# print the JSON string representation of the object
print(AppliedPatch.to_json())

# convert the object into a dict
applied_patch_dict = applied_patch_instance.to_dict()
# create an instance of AppliedPatch from a dict
applied_patch_from_dict = AppliedPatch.from_dict(applied_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


