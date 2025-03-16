# PhysicalNodeConfigParams

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
from cohesity_sdk.cluster.models.physical_node_config_params import PhysicalNodeConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalNodeConfigParams from a JSON string
physical_node_config_params_instance = PhysicalNodeConfigParams.from_json(json)
# print the JSON string representation of the object
print(PhysicalNodeConfigParams.to_json())

# convert the object into a dict
physical_node_config_params_dict = physical_node_config_params_instance.to_dict()
# create an instance of PhysicalNodeConfigParams from a dict
physical_node_config_params_from_dict = PhysicalNodeConfigParams.from_dict(physical_node_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


