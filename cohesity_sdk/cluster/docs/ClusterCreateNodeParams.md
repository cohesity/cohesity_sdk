# ClusterCreateNodeParams

Node params required for cluster creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **int** | Specifies the node id of the node. | 
**node_ip** | **str** | Specifies the node ip address which is either in ipv4/ipv6 format. | 

## Example

```python
from cohesity_sdk.cluster.models.cluster_create_node_params import ClusterCreateNodeParams

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCreateNodeParams from a JSON string
cluster_create_node_params_instance = ClusterCreateNodeParams.from_json(json)
# print the JSON string representation of the object
print(ClusterCreateNodeParams.to_json())

# convert the object into a dict
cluster_create_node_params_dict = cluster_create_node_params_instance.to_dict()
# create an instance of ClusterCreateNodeParams from a dict
cluster_create_node_params_from_dict = ClusterCreateNodeParams.from_dict(cluster_create_node_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


