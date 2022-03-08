# ProtectedObjectInfo

Specifies the details of a protected object.

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
**global_id** | **str, none_type** | Specifies the global id which is a unique identifier of the object. | [optional] 
**protection_type** | **str, none_type** | Specifies the protection type of the object if any. | [optional] 
**os_type** | **str, none_type** | Specifies the operating system type of the object. | [optional] 
**v_center_summary** | [**ObjectTypeVCenterParams**](ObjectTypeVCenterParams.md) |  | [optional] 
**sharepoint_site_summary** | [**SharepointObjectParams**](SharepointObjectParams.md) |  | [optional] 
**permissions** | [**[Tenant], none_type**](Tenant.md) | Specifies the list of tenants that have permissions for this accessing given protected object. | [optional] 
**object_backup_configuration** | [**ProtectedObjectBackupConfig**](ProtectedObjectBackupConfig.md) |  | [optional] 
**protection_group_configurations** | [**[ProtectedObjectGroupBackupConfig], none_type**](ProtectedObjectGroupBackupConfig.md) | Specifies the protection info associated with every object. There can be multiple instances of protection info since the same object can be protected in multiple protection groups. | [optional] 
**last_run** | [**ObjectProtectionRunSummary**](ObjectProtectionRunSummary.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


