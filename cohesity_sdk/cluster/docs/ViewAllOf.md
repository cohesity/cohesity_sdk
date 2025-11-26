# ViewAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**[ViewAliasInfo], none_type**](ViewAliasInfo.md) | Aliases created for the view. A view alias allows a directory path inside a view to be mounted using the alias name. | [optional] [readonly] 
**basic_mount_path** | **str, none_type** | Specifies the NFS mount path of the View (without the hostname information). This path is used to support NFS mounting of the paths specified in the nfsExportPathList on Windows systems. | [optional] [readonly] 
**case_insensitive_names_enabled** | **bool, none_type** | Specifies whether to support case insensitive file/folder names. This parameter can only be set during create and cannot be changed. | [optional] [readonly] 
**create_time_msecs** | **int, none_type** | Specifies the time that the View was created in milliseconds. | [optional] [readonly] 
**data_lock_expiry_usecs** | **int, none_type** | DataLock (Write Once Read Many) lock expiry epoch time in microseconds. If a view is marked as a DataLock view, only a Data Security Officer (a user having Data Security Privilege) can delete the view until the lock expiry time. | [optional] 
**file_count_by_size** | [**[FileCount], none_type**](FileCount.md) | Specifies the file count by size for the View. | [optional] 
**intent** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the intent of the View. | [optional] 
**is_category_inferred** | **bool, none_type** | If True, category in response is not set by user but inferred by Iris because none is set. Category can only be none when view was created by v1 API or cloned from a view created by v1 API.  Inference Logic is as follows: 1. Object Services if only S3 or Swift protocol is selected. 2. Backup Target only if one read-write protocol is selected and    QoS is \&quot;Backup Target Commvault\&quot; or \&quot;Backup Target SSD\&quot;. 3. File Services if there are more than 1 read-write protocol or    it doesn&#39;t fit any other category. | [optional] [readonly] 
**is_target_for_migrated_data** | **bool, none_type** | Specifies if a view contains migrated data. | [optional] [readonly] 
**nfs_mount_path** | **str, none_type** | This field is currently deprecated. Please use NFS MountPaths which would be an array of strings. | [optional] [readonly] 
**nfs_mount_paths** | **[str], none_type** | Array of NFS Paths. Specifies the path for mounting this View as an NFS share. If Kerberos Provider has multiple hostaliases, each host alias has  its own path. | [optional] [readonly] 
**object_services_mapping_config** | **str, none_type** | Specifies the Object Services key mapping config of the view. This parameter can only be set during create and cannot be changed. Configuration of Object Services key mapping. Specifies the type of Object Services key mapping config. | [optional] [readonly] 
**owner_sid** | **str, none_type** | Specifies the sid of the view owner. | [optional] 
**s3_folder_support_enabled** | **bool, none_type** | Specifies whether to support s3 folder support feature. This parameter can only be set during create and cannot be changed. | [optional] [readonly] 
**smb_mount_paths** | **[str], none_type** | Array of SMB Paths. Specifies the possible paths that can be used to mount this View as a SMB share. If Active Directory has multiple account names; each machine account has its own path. | [optional] [readonly] 
**stats** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies statistics about the View. | [optional] 
**storage_domain_id** | **int, none_type** | Specifies the id of the Storage Domain (View Box) where the View is stored. | [optional] [readonly] 
**storage_domain_name** | **str, none_type** | Specifies the name of the Storage Domain (View Box) where the View is stored. | [optional] [readonly] 
**view_failover** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the information about the failover of the view. | [optional] 
**view_id** | **int, none_type** | Specifies an id of the View assigned by the Cohesity Cluster. | [optional] [readonly] 
**view_protection** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


