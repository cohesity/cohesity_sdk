# CommonObjectSummaryae87bd38C431437aA4584a94414c39e8VmwareObjectEntityParamsWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies object id. | [optional] 
**name** | **str, none_type** | Specifies the name of the object. | [optional] 
**source_id** | **int, none_type** | Specifies registered source id to which object belongs. | [optional] 
**source_name** | **str, none_type** | Specifies registered source name to which object belongs. | [optional] 
**environment** | **str, none_type** | Specifies the environment of the object. | [optional] 
**object_hash** | **str, none_type** | Specifies the hash identifier of the object. | [optional] 
**object_type** | **str, none_type** | Specifies the type of the object. | [optional] 
**logical_size_bytes** | **int, none_type** | Specifies the logical size of object in bytes. | [optional] 
**uuid** | **str, none_type** | Specifies the uuid which is a unique identifier of the object. | [optional] 
**protection_type** | **str, none_type** | Specifies the protection type of the object if any. | [optional] 
**os_type** | **str, none_type** | Specifies the operating system type of the object. | [optional] 
**v_center_summary** | [**ObjectTypeVCenterParams**](ObjectTypeVCenterParams.md) |  | [optional] 
**sharepoint_site_summary** | [**SharepointObjectParams**](SharepointObjectParams.md) |  | [optional] 
**protection_stats** | [**[ObjectProtectionStatsSummary], none_type**](ObjectProtectionStatsSummary.md) | Specifies the count and size of protected and unprotected objects for the size. | [optional] 
**permissions** | [**PermissionInfo**](PermissionInfo.md) |  | [optional] 
**vmware_params** | [**VmwareObjectEntityParams**](VmwareObjectEntityParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


