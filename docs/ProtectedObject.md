# ProtectedObject

Specifies the Protected Object with last Run's snapshot information per Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str, none_type** | Specifies the environment of the object. | [optional] 
**id** | **int, none_type** | Specifies object id. | [optional] 
**name** | **str, none_type** | Specifies the name of the object. | [optional] 
**source_id** | **int, none_type** | Specifies registered source id to which object belongs. | [optional] 
**source_name** | **str, none_type** | Specifies registered source name to which object belongs. | [optional] 
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
**elastifile_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters for Elastifile object. | [optional] 
**flashblade_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters for Flashblade object. | [optional] 
**generic_nas_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters for GenericNas object. | [optional] 
**gpfs_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters for GPFS object. | [optional] 
**isilon_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters for Isilon object. | [optional] 
**mssql_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters for Msssql object. | [optional] 
**netapp_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters for NetApp object. | [optional] 
**oracle_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters for Oracle object. | [optional] 
**physical_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters for Physical object. | [optional] 
**sharepoint_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters for Sharepoint object. | [optional] 
**uda_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters for UDA object. | [optional] 
**vmware_params** | [**VmwareObjectEntityParams**](VmwareObjectEntityParams.md) |  | [optional] 
**latest_snapshots_info** | [**[ObjectSnapshotsInfo], none_type**](ObjectSnapshotsInfo.md) | Specifies the latest snapshot information for every Protection Group for a given object. | [optional] 
**source_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the Source Object information. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


