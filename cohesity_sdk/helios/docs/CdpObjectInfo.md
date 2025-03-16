# CdpObjectInfo

Specifies the CDP related information for a given object. This field will only be populated when protection group is configured with policy having CDP retention settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_re_enable_cdp** | **bool** | Specifies if re-enabling CDP is allowed or not through UI without any job or policy update through API. | [optional] 
**cdp_enabled** | **bool** | Specifies whether CDP is currently active or not. CDP might have been active on this object before, but it might not be anymore. | [optional] 
**last_run_info** | [**CdpObjectLastRunInfo**](CdpObjectLastRunInfo.md) |  | [optional] 
**protection_group_id** | **str** | Specifies the protection group id to which this CDP object belongs. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.cdp_object_info import CdpObjectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CdpObjectInfo from a JSON string
cdp_object_info_instance = CdpObjectInfo.from_json(json)
# print the JSON string representation of the object
print(CdpObjectInfo.to_json())

# convert the object into a dict
cdp_object_info_dict = cdp_object_info_instance.to_dict()
# create an instance of CdpObjectInfo from a dict
cdp_object_info_from_dict = CdpObjectInfo.from_dict(cdp_object_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


