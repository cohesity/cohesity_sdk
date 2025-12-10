# ConnectivityEndpointTag

Specifies a connectivity endpoint tag.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the tag. | [optional] 
**value** | **str** | Specifies the value of the tag. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.connectivity_endpoint_tag import ConnectivityEndpointTag

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectivityEndpointTag from a JSON string
connectivity_endpoint_tag_instance = ConnectivityEndpointTag.from_json(json)
# print the JSON string representation of the object
print(ConnectivityEndpointTag.to_json())

# convert the object into a dict
connectivity_endpoint_tag_dict = connectivity_endpoint_tag_instance.to_dict()
# create an instance of ConnectivityEndpointTag from a dict
connectivity_endpoint_tag_from_dict = ConnectivityEndpointTag.from_dict(connectivity_endpoint_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


