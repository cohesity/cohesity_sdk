# IpmiSel

Specifies the sel for the ipmi.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sel_non_verbose_entries** | [**List[IpmiSelNonVerboseEntry]**](IpmiSelNonVerboseEntry.md) | Specifies the list of sel entries when verbose&#x3D;false. | [optional] 
**sel_verbose_entries** | [**List[IpmiSelVerboseEntry]**](IpmiSelVerboseEntry.md) | Specifies the list of sel entries when verbose&#x3D;true. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ipmi_sel import IpmiSel

# TODO update the JSON string below
json = "{}"
# create an instance of IpmiSel from a JSON string
ipmi_sel_instance = IpmiSel.from_json(json)
# print the JSON string representation of the object
print(IpmiSel.to_json())

# convert the object into a dict
ipmi_sel_dict = ipmi_sel_instance.to_dict()
# create an instance of IpmiSel from a dict
ipmi_sel_from_dict = IpmiSel.from_dict(ipmi_sel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


