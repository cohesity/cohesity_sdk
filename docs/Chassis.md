# Chassis

Specifies information about hardware chassis.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hardware_model** | **str** | Specifies the hardware model of the chassis. | [optional] 
**id** | **int** | Specifies the id of the chassis used to uniquely identify a chassis. | [optional] 
**name** | **str** | Specifies the name of the chassis. | [optional] 
**node_ids** | **List[int]** | Specifies list of ids of all the nodes in chassis. | [optional] 
**rack_id** | **int** | Rack Id that this chassis belong to | [optional] 
**serial_number** | **str** | Specifies the serial number of the chassis. | [optional] 

## Example

```python
from cohesity_sdk.models.chassis import Chassis

# TODO update the JSON string below
json = "{}"
# create an instance of Chassis from a JSON string
chassis_instance = Chassis.from_json(json)
# print the JSON string representation of the object
print(Chassis.to_json())

# convert the object into a dict
chassis_dict = chassis_instance.to_dict()
# create an instance of Chassis from a dict
chassis_from_dict = Chassis.from_dict(chassis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


