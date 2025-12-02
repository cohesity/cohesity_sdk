# CommonGraphNodeFilterParams

Determines filter that can be applied to query node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_filter** | **str** | Filter string for node attributes. This filter string is environment-specific and interpretable by respective environment only. | [optional] 
**name** | **str** | Filters the nodes based on provided current node display name. | [optional] 
**node_type** | **str** | Filter the nodes which matches with specified node type. | 
**root_only** | **bool** | If set to true only root nodes would be returned. A root node refers to nodes in the graph with no incoming edges. Defaults to false. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_graph_node_filter_params import CommonGraphNodeFilterParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonGraphNodeFilterParams from a JSON string
common_graph_node_filter_params_instance = CommonGraphNodeFilterParams.from_json(json)
# print the JSON string representation of the object
print(CommonGraphNodeFilterParams.to_json())

# convert the object into a dict
common_graph_node_filter_params_dict = common_graph_node_filter_params_instance.to_dict()
# create an instance of CommonGraphNodeFilterParams from a dict
common_graph_node_filter_params_from_dict = CommonGraphNodeFilterParams.from_dict(common_graph_node_filter_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


