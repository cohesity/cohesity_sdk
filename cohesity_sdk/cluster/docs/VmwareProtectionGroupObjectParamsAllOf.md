# VmwareProtectionGroupObjectParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies the id of the object being protected. This can be a leaf level or non leaf level object. | 
**cdp_info** | [**VmwareCdpObject**](VmwareCdpObject.md) |  | [optional] 
**is_autoprotected** | **bool, none_type** | Specifies whether the vm is part of an Autoprotection and there is at least one object-specific setting applied to this vm. True implies that the vm or its parent directory is autoprotected and will remain part of the autoprotection with additional settings specified here. False implies the object is not part of an Autoprotection and will remain protected and its individual settings here even if a parent directory&#39;s Autoprotection setting is altered. Default is false. | [optional] 
**name** | **str, none_type** | Specifies the name of the virtual machine. | [optional] [readonly] 
**standby_info** | [**VmwareStandbyObject**](VmwareStandbyObject.md) |  | [optional] 
**type** | **str, none_type** | Specifies the type of the VMware object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


