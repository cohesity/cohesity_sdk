# ChassisInfo

ChassisInfo is the struct for the Chassis.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_id** | **int** | ChassisId is a unique id assigned to the chassis. | [optional] 
**chassis_name** | **str** | ChassisName is the name of the chassis. This could be the chassis serial number by default. | [optional] 
**chassis_serial** | **str** | Chassis serial. | [optional] 
**location** | **str** | Location is the location of the chassis within the rack. | [optional] 
**rack_id** | **int** | Rack is the rack within which this chassis lives. | [optional] 

## Example

```python
from cohesity_sdk.models.chassis_info import ChassisInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ChassisInfo from a JSON string
chassis_info_instance = ChassisInfo.from_json(json)
# print the JSON string representation of the object
print(ChassisInfo.to_json())

# convert the object into a dict
chassis_info_dict = chassis_info_instance.to_dict()
# create an instance of ChassisInfo from a dict
chassis_info_from_dict = ChassisInfo.from_dict(chassis_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


