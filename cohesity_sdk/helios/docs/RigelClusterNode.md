# RigelClusterNode

Params for a Rigel Cluster Node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **int** | Specifies the ID of the Node. | [optional] 
**node_ip** | **str** | Specifies the IP address of the Node. | 
**secondary_node_ip** | **str** | Specifies the secondary IP address of the Node. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.rigel_cluster_node import RigelClusterNode

# TODO update the JSON string below
json = "{}"
# create an instance of RigelClusterNode from a JSON string
rigel_cluster_node_instance = RigelClusterNode.from_json(json)
# print the JSON string representation of the object
print(RigelClusterNode.to_json())

# convert the object into a dict
rigel_cluster_node_dict = rigel_cluster_node_instance.to_dict()
# create an instance of RigelClusterNode from a dict
rigel_cluster_node_from_dict = RigelClusterNode.from_dict(rigel_cluster_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


