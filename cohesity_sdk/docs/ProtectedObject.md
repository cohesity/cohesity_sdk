# ProtectedObject

Specifies the Protected Object with last Run's snapshot information per Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | [**ObjectStringIdentifier**](ObjectStringIdentifier.md) |  | [optional] 
**environment** | **str, none_type** | Specifies the environment of the object. | [optional] 
**id** | **int, none_type** | Specifies object id. | [optional] 
**name** | **str, none_type** | Specifies the name of the object. | [optional] 
**source_id** | **int, none_type** | Specifies registered source id to which object belongs. | [optional] 
**source_name** | **str, none_type** | Specifies registered source name to which object belongs. | [optional] 
**child_objects** | [**[ObjectSummary], none_type**](ObjectSummary.md) | Specifies child object details. | [optional] 
**global_id** | **str, none_type** | Specifies the global id which is a unique identifier of the object. | [optional] 
**logical_size_bytes** | **int, none_type** | Specifies the logical size of object in bytes. | [optional] 
**object_hash** | **str, none_type** | Specifies the hash identifier of the object. | [optional] 
**object_type** | **str, none_type** | Specifies the type of the object. | [optional] 
**os_type** | **str, none_type** | Specifies the operating system type of the object. | [optional] 
**protection_type** | **str, none_type** | Specifies the protection type of the object if any. | [optional] 
**sharepoint_site_summary** | [**SharepointObjectParams**](SharepointObjectParams.md) |  | [optional] 
**uuid** | **str, none_type** | Specifies the uuid which is a unique identifier of the object. | [optional] 
**v_center_summary** | [**ObjectTypeVCenterParams**](ObjectTypeVCenterParams.md) |  | [optional] 
**windows_cluster_summary** | [**ObjectTypeWindowsClusterParams**](ObjectTypeWindowsClusterParams.md) |  | [optional] 
**permissions** | [**PermissionInfo**](PermissionInfo.md) |  | [optional] 
**protection_stats** | [**[ObjectProtectionStatsSummary], none_type**](ObjectProtectionStatsSummary.md) | Specifies the count and size of protected and unprotected objects for the size. | [optional] 
**elastifile_params** | [**CommonNasObjectParams**](CommonNasObjectParams.md) |  | [optional] 
**flashblade_params** | [**FlashbladeObjectParams**](FlashbladeObjectParams.md) |  | [optional] 
**generic_nas_params** | [**CommonNasObjectParams**](CommonNasObjectParams.md) |  | [optional] 
**gpfs_params** | [**CommonNasObjectParams**](CommonNasObjectParams.md) |  | [optional] 
**group_params** | [**GroupObjectEntityParams**](GroupObjectEntityParams.md) |  | [optional] 
**isilon_params** | [**IsilonObjectParams**](IsilonObjectParams.md) |  | [optional] 
**mongo_db_params** | [**MongoDBObjectParams**](MongoDBObjectParams.md) |  | [optional] 
**mssql_params** | [**MssqlObjectEntityParams**](MssqlObjectEntityParams.md) |  | [optional] 
**netapp_params** | [**NetappObjectParams**](NetappObjectParams.md) |  | [optional] 
**oracle_params** | [**OracleObjectEntityParams**](OracleObjectEntityParams.md) |  | [optional] 
**physical_params** | [**PhysicalObjectEntityParams**](PhysicalObjectEntityParams.md) |  | [optional] 
**sharepoint_params** | [**SharepointObjectEntityParams**](SharepointObjectEntityParams.md) |  | [optional] 
**uda_params** | [**UdaObjectParams**](UdaObjectParams.md) |  | [optional] 
**view_params** | [**ViewObjectParams**](ViewObjectParams.md) |  | [optional] 
**vmware_params** | [**VmwareObjectEntityParams**](VmwareObjectEntityParams.md) |  | [optional] 
**latest_snapshots_info** | [**[ObjectSnapshotsInfo], none_type**](ObjectSnapshotsInfo.md) | Specifies the latest snapshot information for every Protection Group for a given object. | [optional] 
**source_info** | [**ObjectSummary**](ObjectSummary.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


