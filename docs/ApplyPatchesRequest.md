# ApplyPatchesRequest

Specifies the request to apply a patch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **bool** | Specifies all the available patches should be applied. | [optional] 
**service** | **str** | Specifies the name of the service whose patch should be applied. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.apply_patches_request import ApplyPatchesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyPatchesRequest from a JSON string
apply_patches_request_instance = ApplyPatchesRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyPatchesRequest.to_json())

# convert the object into a dict
apply_patches_request_dict = apply_patches_request_instance.to_dict()
# create an instance of ApplyPatchesRequest from a dict
apply_patches_request_from_dict = ApplyPatchesRequest.from_dict(apply_patches_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


