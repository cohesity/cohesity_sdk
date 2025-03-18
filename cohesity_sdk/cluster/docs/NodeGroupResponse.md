# NodeGroupResponse

Specifies the details of Node Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_groups** | [**List[NodeGroup]**](NodeGroup.md) | Specifies the details of a Node Group. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.node_group_response import NodeGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NodeGroupResponse from a JSON string
node_group_response_instance = NodeGroupResponse.from_json(json)
# print the JSON string representation of the object
print(NodeGroupResponse.to_json())

# convert the object into a dict
node_group_response_dict = node_group_response_instance.to_dict()
# create an instance of NodeGroupResponse from a dict
node_group_response_from_dict = NodeGroupResponse.from_dict(node_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


