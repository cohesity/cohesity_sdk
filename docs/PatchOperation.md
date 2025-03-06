# PatchOperation

Specifies a patch operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** | Specifies the description of the service. | [optional] 
**domain** | **str** | Specifies the domain of the user. | [optional] 
**operation** | **str** | Specifies what patch management operation was performed | [optional] 
**operation_time_msecs** | **int** | Specifies the time when the patch operation was done in Unix epoch in milliseconds. | [optional] 
**service** | **str** | Specifies the name of the service. | [optional] 
**user** | **str** | Specifies the user who performed the operation. | [optional] 
**version** | **str** | Specifies the version of the patch. | [optional] 
**version_replaced** | **str** | Specifies the version it replaced. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.patch_operation import PatchOperation

# TODO update the JSON string below
json = "{}"
# create an instance of PatchOperation from a JSON string
patch_operation_instance = PatchOperation.from_json(json)
# print the JSON string representation of the object
print(PatchOperation.to_json())

# convert the object into a dict
patch_operation_dict = patch_operation_instance.to_dict()
# create an instance of PatchOperation from a dict
patch_operation_from_dict = PatchOperation.from_dict(patch_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


