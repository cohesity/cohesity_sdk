# AadNodeInfo

Determines information about an aad node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_attributes** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the list of nodes&#39;s attributes as key/value pair. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aad_node_info import AadNodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AadNodeInfo from a JSON string
aad_node_info_instance = AadNodeInfo.from_json(json)
# print the JSON string representation of the object
print(AadNodeInfo.to_json())

# convert the object into a dict
aad_node_info_dict = aad_node_info_instance.to_dict()
# create an instance of AadNodeInfo from a dict
aad_node_info_from_dict = AadNodeInfo.from_dict(aad_node_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


