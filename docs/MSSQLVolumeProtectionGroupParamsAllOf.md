# MSSQLVolumeProtectionGroupParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[MSSQLVolumeProtectionGroupObjectParams], none_type**](MSSQLVolumeProtectionGroupObjectParams.md) | Specifies the list of object ids to be protected. | 
**incremental_backup_after_restart** | **bool, none_type** | Specifies whether or to perform incremental backups the first time after a server restarts. By default, a full backup will be performed. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**backup_db_volumes_only** | **bool, none_type** | Specifies whether to only backup volumes on which the specified databases reside. If not specified (default), all the volumes of the host will be protected. | [optional] 
**additional_host_params** | [**[MSSQLVolumeProtectionGroupHostParams]**](MSSQLVolumeProtectionGroupHostParams.md) | Specifies settings which are to be applied to specific host containers in this protection group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


