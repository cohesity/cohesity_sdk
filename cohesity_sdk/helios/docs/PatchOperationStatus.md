# PatchOperationStatus

Specifies the status of the current or the last patch operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**in_progress** | **bool** | Specifies whether a operation is in progress now. | [optional] 
**operation** | **str** | Specifies the patch operation. It is either apply or revert patch operation. | [optional] 
**operation_message** | **str** | Specifies a message about the patch operation. | [optional] 
**percentage** | **int** | Specifies the percentage of completion of the current patch operation in progress or the last patch operation completed. | [optional] 
**services_progress** | [**List[ServiceUnitProgress]**](ServiceUnitProgress.md) | Specifies the details of patch operation services at each patch level. | [optional] 
**time_remaining_seconds** | **int** | Specifies the time remaining to complete the patch operation. | [optional] 
**time_taken_seconds** | **int** | Specifies the time taken so far to complete the patch operation. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.patch_operation_status import PatchOperationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PatchOperationStatus from a JSON string
patch_operation_status_instance = PatchOperationStatus.from_json(json)
# print the JSON string representation of the object
print(PatchOperationStatus.to_json())

# convert the object into a dict
patch_operation_status_dict = patch_operation_status_instance.to_dict()
# create an instance of PatchOperationStatus from a dict
patch_operation_status_from_dict = PatchOperationStatus.from_dict(patch_operation_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


