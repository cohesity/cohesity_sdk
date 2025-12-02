# ConnectivityEndpointList

Specifies a list of connectivity endpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectivity_endpoints** | [**List[ConnectivityEndpoint]**](ConnectivityEndpoint.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.connectivity_endpoint_list import ConnectivityEndpointList

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectivityEndpointList from a JSON string
connectivity_endpoint_list_instance = ConnectivityEndpointList.from_json(json)
# print the JSON string representation of the object
print(ConnectivityEndpointList.to_json())

# convert the object into a dict
connectivity_endpoint_list_dict = connectivity_endpoint_list_instance.to_dict()
# create an instance of ConnectivityEndpointList from a dict
connectivity_endpoint_list_from_dict = ConnectivityEndpointList.from_dict(connectivity_endpoint_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


