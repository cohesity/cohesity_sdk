# CdpSourceObjectInfo

Specifies the CDP related information for a given object. This field will only be populated when protection source having protection groups which are configured with policy having CDP retention settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdp_enabled** | **bool** | Specifies whether CDP is currently active or not. CDP might have been active on this object before, but it might not be anymore. | [optional] 
**protection_group_ids** | **List[str]** | Specifies the protection group ids which belong to this source object for which CDP is enabled. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.cdp_source_object_info import CdpSourceObjectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CdpSourceObjectInfo from a JSON string
cdp_source_object_info_instance = CdpSourceObjectInfo.from_json(json)
# print the JSON string representation of the object
print(CdpSourceObjectInfo.to_json())

# convert the object into a dict
cdp_source_object_info_dict = cdp_source_object_info_instance.to_dict()
# create an instance of CdpSourceObjectInfo from a dict
cdp_source_object_info_from_dict = CdpSourceObjectInfo.from_dict(cdp_source_object_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


