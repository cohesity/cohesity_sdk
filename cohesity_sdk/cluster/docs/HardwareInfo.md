# HardwareInfo

Specifies general information about node hardware.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_model** | **str** | Chassis model. | [optional] 
**chassis_serial** | **str** | Chassis serial number programmed by manufacturer. | [optional] 
**chassis_type** | **str** | Chassis serial number programmed by manufacturer. | [optional] 
**cohesity_chassis_serial** | **str** | Chassis serial number programmed by cohesity software. | [optional] 
**cohesity_node_serial** | **str** | Node serial number programmed by cohesity software. | [optional] 
**hba_model** | **str** | Specifies the HBA model type for the given node. | [optional] 
**ipmi_lan_channel** | **str** | Specifies the channel through which the IPMI interface communicates on the network. | [optional] 
**max_slots** | **str** | Maximum number of slots. | [optional] 
**node_model** | **str** | Node model. | [optional] 
**node_serial** | **str** | Node serial number programmed by manufacturer. | [optional] 
**product_model** | **str** | Specifies the product model for the given node. | [optional] 
**product_model_type** | **str** | Specifies the type of the product model for the given node. | [optional] 
**slot_number** | **str** | Slot number of the node in the chassis. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.hardware_info import HardwareInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HardwareInfo from a JSON string
hardware_info_instance = HardwareInfo.from_json(json)
# print the JSON string representation of the object
print(HardwareInfo.to_json())

# convert the object into a dict
hardware_info_dict = hardware_info_instance.to_dict()
# create an instance of HardwareInfo from a dict
hardware_info_from_dict = HardwareInfo.from_dict(hardware_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


