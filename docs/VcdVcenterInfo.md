# VcdVcenterInfo

Specifies information about a vCetner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | Specifies the endpoint of the vCenter. | [optional] 
**name** | **str** | Specifies the name of the vCenter. | [optional] 

## Example

```python
from cohesity_sdk.models.vcd_vcenter_info import VcdVcenterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VcdVcenterInfo from a JSON string
vcd_vcenter_info_instance = VcdVcenterInfo.from_json(json)
# print the JSON string representation of the object
print(VcdVcenterInfo.to_json())

# convert the object into a dict
vcd_vcenter_info_dict = vcd_vcenter_info_instance.to_dict()
# create an instance of VcdVcenterInfo from a dict
vcd_vcenter_info_from_dict = VcdVcenterInfo.from_dict(vcd_vcenter_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


