# GetGraphNodesDetailsResult

Defintion of node relations search query result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph_nodes** | [**List[GraphNodeRelation]**](GraphNodeRelation.md) | Specifies fetched graph node and their edges information. | [optional] 
**pagination_cookie** | **str** | Specifies the pagination cookie with which subsequent parts of the response can be fetched. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.get_graph_nodes_details_result import GetGraphNodesDetailsResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetGraphNodesDetailsResult from a JSON string
get_graph_nodes_details_result_instance = GetGraphNodesDetailsResult.from_json(json)
# print the JSON string representation of the object
print(GetGraphNodesDetailsResult.to_json())

# convert the object into a dict
get_graph_nodes_details_result_dict = get_graph_nodes_details_result_instance.to_dict()
# create an instance of GetGraphNodesDetailsResult from a dict
get_graph_nodes_details_result_from_dict = GetGraphNodesDetailsResult.from_dict(get_graph_nodes_details_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


