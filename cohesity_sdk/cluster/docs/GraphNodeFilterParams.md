# GraphNodeFilterParams

Determines filter that can be applied to query node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_filter** | **str** | Filter string for node attributes. This filter string is environment-specific and interpretable by respective environment only. | [optional] 
**name** | **str** | Filters the nodes based on provided current node display name. | [optional] 
**node_type** | **str** | Filter the nodes which matches with specified node type. | 
**root_only** | **bool** | If set to true only root nodes would be returned. A root node refers to nodes in the graph with no incoming edges. Defaults to false. | [optional] 
**aad_params** | [**AadGraphNodeFilterParams**](AadGraphNodeFilterParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.graph_node_filter_params import GraphNodeFilterParams

# TODO update the JSON string below
json = "{}"
# create an instance of GraphNodeFilterParams from a JSON string
graph_node_filter_params_instance = GraphNodeFilterParams.from_json(json)
# print the JSON string representation of the object
print(GraphNodeFilterParams.to_json())

# convert the object into a dict
graph_node_filter_params_dict = graph_node_filter_params_instance.to_dict()
# create an instance of GraphNodeFilterParams from a dict
graph_node_filter_params_from_dict = GraphNodeFilterParams.from_dict(graph_node_filter_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


