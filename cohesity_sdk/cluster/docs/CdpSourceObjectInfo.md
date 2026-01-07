# CdpSourceObjectInfo

Specifies the CDP related information for a given object. This field will only be populated when protection source having protection groups which are configured with policy having CDP retention settings.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdp_enabled** | **bool, none_type** | Specifies whether CDP is currently active or not. CDP might have been active on this object before, but it might not be anymore. | [optional] 
**protection_group_ids** | **[str], none_type** | Specifies the protection group ids which belong to this source object for which CDP is enabled. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


