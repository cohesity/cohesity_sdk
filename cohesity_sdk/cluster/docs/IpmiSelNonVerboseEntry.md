# IpmiSelNonVerboseEntry

Specifies each entry in the sel verbose response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_assertion_type** | **str** | Specifies whether the event is asserted or not. This is only returned in case of verbose &#x3D; false. | [optional] 
**record_date** | **str** | Specifies the date on which the record is added to SEL. This is only returned in case of verbose &#x3D; false. | [optional] 
**record_description** | **str** | Specifies a short description corresponding to the sensor event for which record is added to SEL. | [optional] 
**record_event** | **str** | Provides a short description related to sensor action. This is only returned in case of verbose &#x3D; false. | [optional] 
**record_id** | **str** | Specifies the ID corresponding to record in SEL(System Event Log) for given node. | [optional] 
**record_time** | **str** | Specifies the time at which the record is added to SEL. This is only returned in case of verbose &#x3D; false. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ipmi_sel_non_verbose_entry import IpmiSelNonVerboseEntry

# TODO update the JSON string below
json = "{}"
# create an instance of IpmiSelNonVerboseEntry from a JSON string
ipmi_sel_non_verbose_entry_instance = IpmiSelNonVerboseEntry.from_json(json)
# print the JSON string representation of the object
print(IpmiSelNonVerboseEntry.to_json())

# convert the object into a dict
ipmi_sel_non_verbose_entry_dict = ipmi_sel_non_verbose_entry_instance.to_dict()
# create an instance of IpmiSelNonVerboseEntry from a dict
ipmi_sel_non_verbose_entry_from_dict = IpmiSelNonVerboseEntry.from_dict(ipmi_sel_non_verbose_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


