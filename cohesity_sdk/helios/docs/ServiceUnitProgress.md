# ServiceUnitProgress

Specifies the progress of one patch operation for one service at one patch level.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**in_progress** | **bool** | Specifies whether a operation is in progress for the service. | [optional] 
**nodes_progress** | [**List[NodeUnitProgress]**](NodeUnitProgress.md) | Specifies the details of patch operation for each service at each patch level. | [optional] 
**percentage** | **int** | Specifies the percentage of completion of the patch unit operation. | [optional] 
**service** | **str** | Specifies the service which is patched. | [optional] 
**service_message** | **str** | Specifies a message about the patch unit operation. | [optional] 
**time_remaining_seconds** | **int** | Specifies the time remaining to complete the patch operation for the service. | [optional] 
**time_taken_seconds** | **int** | Specifies the time taken so far in this patch unit operation for the service. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.service_unit_progress import ServiceUnitProgress

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUnitProgress from a JSON string
service_unit_progress_instance = ServiceUnitProgress.from_json(json)
# print the JSON string representation of the object
print(ServiceUnitProgress.to_json())

# convert the object into a dict
service_unit_progress_dict = service_unit_progress_instance.to_dict()
# create an instance of ServiceUnitProgress from a dict
service_unit_progress_from_dict = ServiceUnitProgress.from_dict(service_unit_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


