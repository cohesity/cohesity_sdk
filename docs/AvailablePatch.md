# AvailablePatch

Specifies the description of an available patch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** | Specifies the description of the service. | [optional] 
**count** | **int** | Specifies the number of fixed issues. | [optional] 
**dependencies** | **List[str]** | Specifies the services for which their patches must be applied together. | [optional] 
**fixed_issues** | [**List[FixedIssue]**](FixedIssue.md) | Specifies the details of the issues fixed in the patch. | [optional] 
**service** | **str** | Specifies the name of the service. | [optional] 
**version** | **str** | Specifies the version of the patch. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.available_patch import AvailablePatch

# TODO update the JSON string below
json = "{}"
# create an instance of AvailablePatch from a JSON string
available_patch_instance = AvailablePatch.from_json(json)
# print the JSON string representation of the object
print(AvailablePatch.to_json())

# convert the object into a dict
available_patch_dict = available_patch_instance.to_dict()
# create an instance of AvailablePatch from a dict
available_patch_from_dict = AvailablePatch.from_dict(available_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


