# IpmiSelInfo

Specifies the sel info for the ipmi.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_unit_size** | **str** | Specifies the size of each allocation unit in bytes. | [optional] 
**allocation_units** | **str** | Specifies the number of allocation units available in SEL. | [optional] 
**entries** | **str** | Specifies the number of log entries stores in SEL. | [optional] 
**free_space** | **str** | Specifies the number of free bytes in SEL. | [optional] 
**free_units** | **str** | Specifies the number of free allocation units present in SEL. | [optional] 
**largest_free_blk** | **str** | Specifies the size of the largest contiguous block of free space available in the SEL. | [optional] 
**largest_record_size** | **str** | Specifies the maximum size of a single log record that can be stored in the SEL measured in bytes. | [optional] 
**last_addition_time** | **str** | Specifies the latest time stamp at which a log entry was added to SEL. | [optional] 
**last_deletion_time** | **str** | Specifies the latest time stamp at which a log entry was deleted from SEL. | [optional] 
**overflow** | **str** | Specifies whether an overflow has occured in SEL. | [optional] 
**percent_used** | **str** | Specifies the percentage of SEL used by log entries. | [optional] 
**supported_commands** | **str** | Specifies a space seperated list of commands that are supported for managing the SEL. | [optional] 
**version** | **str** | Specifies the SEL(System Event Log) version for given node. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ipmi_sel_info import IpmiSelInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IpmiSelInfo from a JSON string
ipmi_sel_info_instance = IpmiSelInfo.from_json(json)
# print the JSON string representation of the object
print(IpmiSelInfo.to_json())

# convert the object into a dict
ipmi_sel_info_dict = ipmi_sel_info_instance.to_dict()
# create an instance of IpmiSelInfo from a dict
ipmi_sel_info_from_dict = IpmiSelInfo.from_dict(ipmi_sel_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


