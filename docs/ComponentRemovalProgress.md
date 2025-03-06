# ComponentRemovalProgress

Specifies the removal progress details for services that are not acked yet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_removal_stuck** | **bool** | Specifies if the removal is stuck. | [optional] 
**progress_percentage** | **int** | Specifies the overall progress percentage for the service. | [optional] 
**removal_progress** | **str** | Specifies removal progress details. | [optional] 
**service_name** | **str** | Specifies service name. | [optional] 
**time_remaining** | **int** | Specifies the total duration in seconds left to Ack the service. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.component_removal_progress import ComponentRemovalProgress

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentRemovalProgress from a JSON string
component_removal_progress_instance = ComponentRemovalProgress.from_json(json)
# print the JSON string representation of the object
print(ComponentRemovalProgress.to_json())

# convert the object into a dict
component_removal_progress_dict = component_removal_progress_instance.to_dict()
# create an instance of ComponentRemovalProgress from a dict
component_removal_progress_from_dict = ComponentRemovalProgress.from_dict(component_removal_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


