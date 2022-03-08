# VmwareProtectionGroupObjectParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies the id of the object being protected. This can be a leaf level or non leaf level object. | 
**name** | **str, none_type** | Specifies the name of the virtual machine. | [optional] [readonly] 
**is_autoprotected** | **bool, none_type** | Specifies whether the vm is part of an Autoprotection. True implies that the vm or its parent directory is autoprotected and will remain part of the autoprotection with additional settings specified here. False implies the object is not part of an Autoprotection and will remain protected and its individual settings here even if a parent directory&#39;s Autoprotection setting is altered. Default is false. | [optional] 
**cdp_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the CDP related information for a given object. This field will only be populated when protection group is configured with policy having CDP retnetion settings. | [optional] 
**standby_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the standby related information for a given object. This field will only be populated when standby is configured in backup job settings. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


