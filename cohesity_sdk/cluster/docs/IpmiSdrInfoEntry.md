# IpmiSdrInfoEntry

Specifies a single entry in the sdr info for the ipmi.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_description** | **str** | Specifies the description of the event corresponding to the sensor entry. | [optional] 
**id** | **str** | Specifies the id of the sensor. | [optional] 
**reading** | **str** | Specifies the reading of the sensor. | [optional] 
**sensor_type** | **str** | Specifies the type of sensor corresponding to the entry. | [optional] 
**status** | **str** | Specifies the status of the sensor. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ipmi_sdr_info_entry import IpmiSdrInfoEntry

# TODO update the JSON string below
json = "{}"
# create an instance of IpmiSdrInfoEntry from a JSON string
ipmi_sdr_info_entry_instance = IpmiSdrInfoEntry.from_json(json)
# print the JSON string representation of the object
print(IpmiSdrInfoEntry.to_json())

# convert the object into a dict
ipmi_sdr_info_entry_dict = ipmi_sdr_info_entry_instance.to_dict()
# create an instance of IpmiSdrInfoEntry from a dict
ipmi_sdr_info_entry_from_dict = IpmiSdrInfoEntry.from_dict(ipmi_sdr_info_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


