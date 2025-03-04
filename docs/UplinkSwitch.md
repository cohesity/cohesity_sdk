# UplinkSwitch

Uplink switch details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the system. | [optional] 
**name** | **str** | Name of the system. | [optional] 
**port_id** | **str** | Port id. | [optional] 

## Example

```python
from cohesity_sdk.models.uplink_switch import UplinkSwitch

# TODO update the JSON string below
json = "{}"
# create an instance of UplinkSwitch from a JSON string
uplink_switch_instance = UplinkSwitch.from_json(json)
# print the JSON string representation of the object
print(UplinkSwitch.to_json())

# convert the object into a dict
uplink_switch_dict = uplink_switch_instance.to_dict()
# create an instance of UplinkSwitch from a dict
uplink_switch_from_dict = UplinkSwitch.from_dict(uplink_switch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


