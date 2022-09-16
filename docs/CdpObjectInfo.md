# CdpObjectInfo

Specifies the CDP related information for a given object. This field will only be populated when protection group is configured with policy having CDP retention settings.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdp_enabled** | **bool, none_type** | Specifies whether CDP is currently active or not. CDP might have been active on this object before, but it might not be anymore. | [optional] 
**last_run_info** | [**CdpObjectLastRunInfo**](CdpObjectLastRunInfo.md) |  | [optional] 
**protection_group_id** | **str, none_type** | Specifies the protection group id to which this CDP object belongs. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


