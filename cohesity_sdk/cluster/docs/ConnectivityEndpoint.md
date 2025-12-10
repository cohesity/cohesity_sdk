# ConnectivityEndpoint

Specifies a connectivity endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Specifies the host of the endpoint. | [optional] 
**port** | **int** | Specifies the port of the endpoint. | [optional] 
**tags** | [**List[ConnectivityEndpointTag]**](ConnectivityEndpointTag.md) | Specifies the tags corresponding to the endpoint. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.connectivity_endpoint import ConnectivityEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectivityEndpoint from a JSON string
connectivity_endpoint_instance = ConnectivityEndpoint.from_json(json)
# print the JSON string representation of the object
print(ConnectivityEndpoint.to_json())

# convert the object into a dict
connectivity_endpoint_dict = connectivity_endpoint_instance.to_dict()
# create an instance of ConnectivityEndpoint from a dict
connectivity_endpoint_from_dict = ConnectivityEndpoint.from_dict(connectivity_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


