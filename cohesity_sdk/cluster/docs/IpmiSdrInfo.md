# IpmiSdrInfo

Specifies the sdr info for the given node ipmi.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sdr_entries** | [**List[IpmiSdrInfoEntry]**](IpmiSdrInfoEntry.md) | Specifies the list of sdr entries for the given node. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ipmi_sdr_info import IpmiSdrInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IpmiSdrInfo from a JSON string
ipmi_sdr_info_instance = IpmiSdrInfo.from_json(json)
# print the JSON string representation of the object
print(IpmiSdrInfo.to_json())

# convert the object into a dict
ipmi_sdr_info_dict = ipmi_sdr_info_instance.to_dict()
# create an instance of IpmiSdrInfo from a dict
ipmi_sdr_info_from_dict = IpmiSdrInfo.from_dict(ipmi_sdr_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


