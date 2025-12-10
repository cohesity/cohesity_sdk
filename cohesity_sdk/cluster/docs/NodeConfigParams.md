# NodeConfigParams

Specifies the configuration of the nodes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the node ID for this node. | 
**ip** | **str** | Specifies the IP address for the node. | 
**ipmi_ip** | **str** | Specifies IPMI IP for the node. | [optional] 
**is_compute_node** | **bool** | Specifies whether to use the node for compute only. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.node_config_params import NodeConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of NodeConfigParams from a JSON string
node_config_params_instance = NodeConfigParams.from_json(json)
# print the JSON string representation of the object
print(NodeConfigParams.to_json())

# convert the object into a dict
node_config_params_dict = node_config_params_instance.to_dict()
# create an instance of NodeConfigParams from a dict
node_config_params_from_dict = NodeConfigParams.from_dict(node_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


