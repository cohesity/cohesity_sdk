# ApplyBaseosPatchRequest

Specifies the name of the baseos patch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch_name** | **str** | Name of the hotfix with security patch | 

## Example

```python
from cohesity_sdk.cluster.models.apply_baseos_patch_request import ApplyBaseosPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyBaseosPatchRequest from a JSON string
apply_baseos_patch_request_instance = ApplyBaseosPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyBaseosPatchRequest.to_json())

# convert the object into a dict
apply_baseos_patch_request_dict = apply_baseos_patch_request_instance.to_dict()
# create an instance of ApplyBaseosPatchRequest from a dict
apply_baseos_patch_request_from_dict = ApplyBaseosPatchRequest.from_dict(apply_baseos_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


