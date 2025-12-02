# ServiceState

Structure to hold service status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of service | [optional] 
**state** | **str** | State of service | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.service_state import ServiceState

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceState from a JSON string
service_state_instance = ServiceState.from_json(json)
# print the JSON string representation of the object
print(ServiceState.to_json())

# convert the object into a dict
service_state_dict = service_state_instance.to_dict()
# create an instance of ServiceState from a dict
service_state_from_dict = ServiceState.from_dict(service_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


