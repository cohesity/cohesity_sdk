# HeliosOnPremVMNode

Params for a HeliosOnPremVM Node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **int** | Specifies the ID of the Node. | [optional] 
**node_ip** | **str** | Specifies the IP address of the Node. | 

## Example

```python
from cohesity_sdk.helios.models.helios_on_prem_vm_node import HeliosOnPremVMNode

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosOnPremVMNode from a JSON string
helios_on_prem_vm_node_instance = HeliosOnPremVMNode.from_json(json)
# print the JSON string representation of the object
print(HeliosOnPremVMNode.to_json())

# convert the object into a dict
helios_on_prem_vm_node_dict = helios_on_prem_vm_node_instance.to_dict()
# create an instance of HeliosOnPremVMNode from a dict
helios_on_prem_vm_node_from_dict = HeliosOnPremVMNode.from_dict(helios_on_prem_vm_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


