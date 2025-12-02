# IpmiSelVerboseEntry

Specifies each entry in the sel verbose response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_data** | **str** | Specifies additional info about the event. | [optional] 
**event_direction** | **str** | Specifies whether the event occurred is assertion or deassertion. | [optional] 
**event_type** | **str** | Specifies the type of event occurred. | [optional] 
**evm_revision** | **str** | Specifies the version of the Event Message Format for the record added to SEL. | [optional] 
**generator_id** | **str** | Corresponds to source of component that generated the record. | [optional] 
**record_description** | **str** | Specifies a short description corresponding to the sensor event for which record is added to SEL. | [optional] 
**record_id** | **str** | Specifies the ID corresponding to record in SEL(System Event Log) for given node. | [optional] 
**record_timestamp** | **str** | Specifies the time stamp at which the record is added to SEL. | [optional] 
**record_type** | **str** | Specifies the type of SEL record corresponding to the entry. | [optional] 
**sensor_number** | **str** | Specifies the sensor number corresponding to the current SEL record. | [optional] 
**sensor_type** | **str** | Specifies the type of the sensor corresponding to the current SEL record. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ipmi_sel_verbose_entry import IpmiSelVerboseEntry

# TODO update the JSON string below
json = "{}"
# create an instance of IpmiSelVerboseEntry from a JSON string
ipmi_sel_verbose_entry_instance = IpmiSelVerboseEntry.from_json(json)
# print the JSON string representation of the object
print(IpmiSelVerboseEntry.to_json())

# convert the object into a dict
ipmi_sel_verbose_entry_dict = ipmi_sel_verbose_entry_instance.to_dict()
# create an instance of IpmiSelVerboseEntry from a dict
ipmi_sel_verbose_entry_from_dict = IpmiSelVerboseEntry.from_dict(ipmi_sel_verbose_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


