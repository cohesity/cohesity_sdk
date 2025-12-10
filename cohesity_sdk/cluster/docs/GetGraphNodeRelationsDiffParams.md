# GetGraphNodeRelationsDiffParams

Specify the query params to determine difference of node relation between two snapshots for a given node id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diff_relation** | **bool** | If set to false only the diff of node info will be returned else the diff of relations matching the below edge filters will also be returned. Defaults to false. | [optional] 
**diff_types** | **List[str]** | Specifies an optional mask to filter only certain kinds of diffs. Supported diff types - Added/Modified/Deleted/Unmodified | [optional] 
**relation_filter** | [**GraphNodeRelationFilterParams**](GraphNodeRelationFilterParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.get_graph_node_relations_diff_params import GetGraphNodeRelationsDiffParams

# TODO update the JSON string below
json = "{}"
# create an instance of GetGraphNodeRelationsDiffParams from a JSON string
get_graph_node_relations_diff_params_instance = GetGraphNodeRelationsDiffParams.from_json(json)
# print the JSON string representation of the object
print(GetGraphNodeRelationsDiffParams.to_json())

# convert the object into a dict
get_graph_node_relations_diff_params_dict = get_graph_node_relations_diff_params_instance.to_dict()
# create an instance of GetGraphNodeRelationsDiffParams from a dict
get_graph_node_relations_diff_params_from_dict = GetGraphNodeRelationsDiffParams.from_dict(get_graph_node_relations_diff_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


