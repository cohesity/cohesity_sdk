# ResourceEndpoint

Specifies the details about the resource endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | Specifies the fqdn of this endpoint. | [optional] 
**ipv4addr** | **str** | Specifies the ipv4 address of this endpoint. | [optional] 
**ipv6addr** | **str** | Specifies the ipv6 address of this endpoint. | [optional] 
**is_preferred_endpoint** | **bool** | Whether to use this endpoint to connect. | [optional] 
**preferred_address** | **str** | Specifies the preferred address to use for connecting. | [optional] 
**subnet_ip4addr** | **str** | Specifies the subnet Ip4 address of this endpoint. | [optional] 

## Example

```python
from cohesity_sdk.models.resource_endpoint import ResourceEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceEndpoint from a JSON string
resource_endpoint_instance = ResourceEndpoint.from_json(json)
# print the JSON string representation of the object
print(ResourceEndpoint.to_json())

# convert the object into a dict
resource_endpoint_dict = resource_endpoint_instance.to_dict()
# create an instance of ResourceEndpoint from a dict
resource_endpoint_from_dict = ResourceEndpoint.from_dict(resource_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


