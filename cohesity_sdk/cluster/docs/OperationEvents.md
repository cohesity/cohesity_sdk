# OperationEvents

List of events that took place during the operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Specifies the message describing the event. | [optional] 
**severity** | **str** | Specifies the severity of an event. | [optional] 
**timestamp** | **int** | Specifies the unix epoch timestamp in microseconds when this event took place. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.operation_events import OperationEvents

# TODO update the JSON string below
json = "{}"
# create an instance of OperationEvents from a JSON string
operation_events_instance = OperationEvents.from_json(json)
# print the JSON string representation of the object
print(OperationEvents.to_json())

# convert the object into a dict
operation_events_dict = operation_events_instance.to_dict()
# create an instance of OperationEvents from a dict
operation_events_from_dict = OperationEvents.from_dict(operation_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


