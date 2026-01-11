# ArchivalNasExternalTargetParams

Specifies the parameters which are specific to Nas related External Targets of archival purpose type.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str, none_type** | Specifies the host of the NAS external target. | 
**mount_path** | **str, none_type** | Specifies the mount path of the NAS external target. | 
**is_forever_incremental_archival_enabled** | **bool, none_type** | Specifies if Forever Incremental Archival setting is enabled or not. | [optional] 
**is_incremental_archival_enabled** | **bool, none_type** | Specifies if Incremental Archival setting is enabled or not. | [optional] 
**is_network_optimized_gc** | **bool, none_type** | Specifies whether the garbage collection mode is network optimized or storage optimized. If this field is set to true, it refers to network optimized GC and if set to false, it refers to storage optimized GC. | [optional] 
**kerberos_realm_name** | **str, none_type** | Specifies the Kerberos realm name for a Kerberos-secured target. | [optional] 
**nfs_security_type** | **str, none_type** | Specifies the NFS security type of the target. | [optional] 
**nfs_version_number** | **str, none_type** | Specifies the NFS version number of the target. | [optional] 
**share_type** | **str, none_type** | Specifies the share type of the NAS external target. | [optional] [readonly] 
**source_side_deduplication** | **bool, none_type** | Specifies the Source Side Deduplication setting for the Nas external target | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


