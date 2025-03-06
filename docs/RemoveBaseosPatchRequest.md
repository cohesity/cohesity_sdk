# RemoveBaseosPatchRequest

Specifies the name and force option for baseos patch removal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_remove** | **bool** | If patch files should be removed even for inprogress patch | [optional] 
**patch_name** | **str** | Name of the hotfix with security patch | 

## Example

```python
from cohesity_sdk.cluster.models.remove_baseos_patch_request import RemoveBaseosPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveBaseosPatchRequest from a JSON string
remove_baseos_patch_request_instance = RemoveBaseosPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveBaseosPatchRequest.to_json())

# convert the object into a dict
remove_baseos_patch_request_dict = remove_baseos_patch_request_instance.to_dict()
# create an instance of RemoveBaseosPatchRequest from a dict
remove_baseos_patch_request_from_dict = RemoveBaseosPatchRequest.from_dict(remove_baseos_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


