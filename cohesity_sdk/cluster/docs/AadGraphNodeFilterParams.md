# AadGraphNodeFilterParams

Determines filter params that can be applied to query aad node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_type** | **str** | Filter the nodes which matches with specified aad node type provided. Supported AAD node types - Users/Groups/Applications/ AdministrativeUnits/ServicePrincipals/DirectoryRoles/Contacts/ Devices | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aad_graph_node_filter_params import AadGraphNodeFilterParams

# TODO update the JSON string below
json = "{}"
# create an instance of AadGraphNodeFilterParams from a JSON string
aad_graph_node_filter_params_instance = AadGraphNodeFilterParams.from_json(json)
# print the JSON string representation of the object
print(AadGraphNodeFilterParams.to_json())

# convert the object into a dict
aad_graph_node_filter_params_dict = aad_graph_node_filter_params_instance.to_dict()
# create an instance of AadGraphNodeFilterParams from a dict
aad_graph_node_filter_params_from_dict = AadGraphNodeFilterParams.from_dict(aad_graph_node_filter_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


