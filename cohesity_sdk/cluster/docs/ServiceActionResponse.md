# ServiceActionResponse

Service action response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_name** | **str** | Name of the service. | [optional] 
**service_status** | **str** | Images and Status of ondemand service. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.service_action_response import ServiceActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceActionResponse from a JSON string
service_action_response_instance = ServiceActionResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceActionResponse.to_json())

# convert the object into a dict
service_action_response_dict = service_action_response_instance.to_dict()
# create an instance of ServiceActionResponse from a dict
service_action_response_from_dict = ServiceActionResponse.from_dict(service_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


