# RevertPatchesRequest

Specifies the request to revert a patch. An optional patch level can be specified. When a patch level is specified, system keeps reverting patches until the given patch level is reverted. If no patch level is specified, just the last applied patch is reverted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** | Specifies the name of the service whose patch should be reverted. | 

## Example

```python
from cohesity_sdk.models.revert_patches_request import RevertPatchesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevertPatchesRequest from a JSON string
revert_patches_request_instance = RevertPatchesRequest.from_json(json)
# print the JSON string representation of the object
print(RevertPatchesRequest.to_json())

# convert the object into a dict
revert_patches_request_dict = revert_patches_request_instance.to_dict()
# create an instance of RevertPatchesRequest from a dict
revert_patches_request_from_dict = RevertPatchesRequest.from_dict(revert_patches_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


