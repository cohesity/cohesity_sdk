# ServiceEndpointsMetadata

Specifies the service endpoints that can be configured based on the environnment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_service_name** | **str** | Specifies the name of the IBM cloud service for which the endpoints need to be configured. Based on the provided name here, API callers must set the appropriate service metadata. | 
**iam_params** | [**IbmIAMCServiceMetadata**](IbmIAMCServiceMetadata.md) |  | [optional] 
**vpc_params** | [**IbmVPCServiceMetadata**](IbmVPCServiceMetadata.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.service_endpoints_metadata import ServiceEndpointsMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceEndpointsMetadata from a JSON string
service_endpoints_metadata_instance = ServiceEndpointsMetadata.from_json(json)
# print the JSON string representation of the object
print(ServiceEndpointsMetadata.to_json())

# convert the object into a dict
service_endpoints_metadata_dict = service_endpoints_metadata_instance.to_dict()
# create an instance of ServiceEndpointsMetadata from a dict
service_endpoints_metadata_from_dict = ServiceEndpointsMetadata.from_dict(service_endpoints_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


