# GraphNodeRelationFilterParams

Determines filter that can be applied to query edge of a graph node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aad_params** | [**AadRelationFilterParams**](AadRelationFilterParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.graph_node_relation_filter_params import GraphNodeRelationFilterParams

# TODO update the JSON string below
json = "{}"
# create an instance of GraphNodeRelationFilterParams from a JSON string
graph_node_relation_filter_params_instance = GraphNodeRelationFilterParams.from_json(json)
# print the JSON string representation of the object
print(GraphNodeRelationFilterParams.to_json())

# convert the object into a dict
graph_node_relation_filter_params_dict = graph_node_relation_filter_params_instance.to_dict()
# create an instance of GraphNodeRelationFilterParams from a dict
graph_node_relation_filter_params_from_dict = GraphNodeRelationFilterParams.from_dict(graph_node_relation_filter_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


