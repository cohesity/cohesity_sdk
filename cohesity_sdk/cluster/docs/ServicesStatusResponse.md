# ServicesStatusResponse

\"Response containing images details of an on-demand service.\" 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loaded_images** | **List[str]** | Images loaded by the service. | [optional] 
**service_name** | **str** | Name of the service. | [optional] 
**service_status** | **str** | Images and Status of ondemand service. | [optional] 
**supported_images** | **List[str]** | Images supported by the service. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.services_status_response import ServicesStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesStatusResponse from a JSON string
services_status_response_instance = ServicesStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ServicesStatusResponse.to_json())

# convert the object into a dict
services_status_response_dict = services_status_response_instance.to_dict()
# create an instance of ServicesStatusResponse from a dict
services_status_response_from_dict = ServicesStatusResponse.from_dict(services_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


