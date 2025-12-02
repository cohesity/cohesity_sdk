# ServicesHealthGetResponse

\"Response containing the overall health status and health status for\" \" each service.\" 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_status** | **str** | \&quot;The overall health status of the services (e.g., Healthy, Degraded,\&quot; \&quot; Unhealthy).\&quot;  | [optional] 
**services** | [**List[ServiceHealth]**](ServiceHealth.md) | List of services with their respective health statuses. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.services_health_get_response import ServicesHealthGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesHealthGetResponse from a JSON string
services_health_get_response_instance = ServicesHealthGetResponse.from_json(json)
# print the JSON string representation of the object
print(ServicesHealthGetResponse.to_json())

# convert the object into a dict
services_health_get_response_dict = services_health_get_response_instance.to_dict()
# create an instance of ServicesHealthGetResponse from a dict
services_health_get_response_from_dict = ServicesHealthGetResponse.from_dict(services_health_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


