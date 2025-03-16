# View

Specifies settings for defining a storage location (called a View) with NFS and SMB mount paths in a Storage Domain (View Box) on the Cohesity Cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_sids** | **List[str]** | Array of Security Identifiers (SIDs) Specifies the list of security identifiers (SIDs) for the restricted Principals who have access to this View. | [optional] 
**allow_mount_on_windows** | **bool** | Specifies if this View can be mounted using the NFS protocol on Windows systems. If true, this View can be NFS mounted on Windows systems. | [optional] 
**antivirus_scan_config** | **object** | Specifies the antivirus scan config settings for this View. | [optional] 
**category** | **str** | Specifies the category of the View. | [optional] 
**description** | **str** | Specifies an optional text description about the View. | [optional] 
**enable_filer_audit_logging** | **bool** | Specifies if Filer Audit Logging is enabled for this view. | [optional] 
**enable_live_indexing** | **bool** | Specifies whether to enable live indexing for the view. | [optional] 
**enable_metadata_accelerator** | **bool** | Specifies if metadata accelerator is enabled for this view. Only supported while creating a view. | [optional] 
**enable_minion** | **bool** | Specifies if this view should allow minion or not. If true, this will allow minion. | [optional] 
**enable_offline_caching** | **bool** | Specifies whether to enable offline file caching of the view. | [optional] 
**file_extension_filter** | **object** | Optional filtering criteria that should be satisfied by all the files created in this view. It does not affect existing files. | [optional] 
**file_lock_config** | **object** | Optional config that enables file locking for this view. It cannot be disabled during the edit of a view, if it has been enabled during the creation of the view. Also, it cannot be enabled if it was disabled during the creation of the view. | [optional] 
**filer_lifecycle_management** | **object** | Specifies the Lifecycle policy of this filer (NFS/SMB) view. | [optional] 
**is_externally_triggered_backup_target** | **bool** | Specifies whether the view is for externally triggered backup target. If so, Magneto will ignore the backup schedule for the view protection job of this view. By default it is disabled. | [optional] 
**is_read_only** | **bool** | Specifies if the view is a read only view. User will no longer be able to write to this view if this is set to true. | [optional] 
**lexicographic_prefetch** | **bool** | If small files are accessed sequentially from a client, this specifies whether to detect and prefetch files based on the lexicographic index to improve file read performance. | [optional] 
**logical_quota** | **object** | Specifies an optional logical quota limit (in bytes) for the usage allowed on this View. (Logical data is when the data is fully hydrated and expanded.) This limit overrides the limit inherited from the Storage Domain (View Box) (if set). If logicalQuota is nil, the limit is inherited from the Storage Domain (View Box) (if set). A new write is not allowed if the Storage Domain (View Box) will exceed the specified quota. However, it takes time for the Cohesity Cluster to calculate the usage across Nodes, so the limit may be exceeded by a small amount. In addition, if the limit is increased or data is removed, there may be a delay before the Cohesity Cluster allows more data to be written to the View, as the Cluster is calculating the usage across Nodes. | [optional] 
**name** | **str** | Specifies the name of the View. | [optional] 
**netgroup_whitelist** | **object** | Array of Netgroups. Specifies a list of netgroups with domains that have permissions to access the View. (Overrides or extends the Netgroup specified at the global Cohesity Cluster level.) | [optional] 
**override_global_netgroup_whitelist** | **bool** | Specifies whether view level client netgroup whitelist overrides cluster and global setting. | [optional] 
**override_global_subnet_whitelist** | **bool** | Specifies whether view level client subnet whitelist overrides cluster and global setting. | [optional] 
**protocol_access** | [**List[ViewProtocol]**](ViewProtocol.md) | Specifies the supported Protocols for the View. | [optional] 
**qos** | **object** | Specifies the Quality of Service (QoS) Policy for the View. | [optional] 
**security_mode** | **str** | Specifies the security mode used for this view. Currently we support the following modes: Native, Unified and NTFS style. &#39;NativeMode&#39; indicates a native security mode. &#39;UnifiedMode&#39; indicates a unified security mode. &#39;NtfsMode&#39; indicates a NTFS style security mode. | [optional] 
**self_service_snapshot_config** | **object** | Specifies self service config of this view. | [optional] 
**storage_policy_override** | **object** | Specifies if inline deduplication and compression settings inherited from the Storage Domain (View Box) should be disabled for this View. | [optional] 
**subnet_whitelist** | [**List[Subnet]**](Subnet.md) | Array of Subnets. Specifies a list of Subnets with IP addresses that have permissions to access the View. (Overrides or extends the Subnets specified at the global Cohesity Cluster level.) | [optional] 
**tenant_id** | **str** | Optional tenant id who has access to this View. | [optional] 
**view_lock_enabled** | **bool** | Specifies whether view lock is enabled. If enabled the view cannot be modified or deleted until unlock. By default it is disabled. | [optional] 
**view_pinning_config** | **object** | Specifies the pinning config of this view. | [optional] 
**enable_nfs_kerberos_authentication** | **bool** | If set, it enables NFS Kerberos Authentication | [optional] 
**enable_nfs_kerberos_integrity** | **bool** | If set, it enables NFS Kerberos Integrity | [optional] 
**enable_nfs_kerberos_privacy** | **bool** | If set, it enables NFS Kerberos Privacy | [optional] 
**enable_nfs_unix_authentication** | **bool** | If set, it enables NFS UNIX Authentication | [optional] 
**enable_nfs_view_discovery** | **bool** | If set, it enables discovery of view for NFS. | [optional] 
**enable_nfs_wcc** | **bool** | If set, it enables NFS weak cache consistency. | [optional] 
**nfs_all_squash** | [**NfsSquash**](NfsSquash.md) | Specifies the NFS all squash config. | [optional] 
**nfs_root_permissions** | [**NfsRootPermissions**](NfsRootPermissions.md) | Specifies the NFS root permission config of the view file system. | [optional] 
**nfs_root_squash** | [**NfsSquash**](NfsSquash.md) | Specifies the NFS root squash config. | [optional] 
**enable_fast_durable_handle** | **bool** | Specifies whether fast durable handle is enabled. If enabled, view open handle will be kept in memory, which results in a higher performance. But the handles cannot be recovered if node or service crashes. | [optional] 
**enable_smb_access_based_enumeration** | **bool** | Specifies if access-based enumeration should be enabled. If &#39;true&#39;, only files and folders that the user has permissions to access are visible on the SMB share for that user. | [optional] 
**enable_smb_encryption** | **bool** | Specifies the SMB encryption for the View. If set, it enables the SMB encryption for the View. Encryption is supported only by SMB 3.x dialects. Dialects that do not support would still access data in unencrypted format. | [optional] 
**enable_smb_oplock** | **bool** | Specifies whether SMB opportunistic lock is enabled. | [optional] 
**enable_smb_view_discovery** | **bool** | If set, it enables discovery of view for SMB. | [optional] 
**enforce_smb_encryption** | **bool** | Specifies the SMB encryption for all the sessions for the View. If set, encryption is enforced for all the sessions for the View. When enabled all future and existing unencrypted sessions are disallowed. | [optional] 
**share_permissions** | [**ViewSharePermissions**](ViewSharePermissions.md) | Specifies share level permissions of the view. | [optional] 
**smb_permissions_info** | [**SmbPermissionsInfo**](SmbPermissionsInfo.md) | Specifies the SMB permissions for the View. | [optional] 
**acl_config** | [**AclConfig**](AclConfig.md) | Specifies the ACL config of the View as an S3 bucket. | [optional] 
**bucket_policy** | [**BucketPolicy**](BucketPolicy.md) | Specifies the policy in effect for this bucket. | [optional] 
**enable_abac** | **bool** | Specifies if this View has S3 ABAC enabled. This can only be set while creating a view. The ABAC server corresponding the tenant will be used for authentication and authorization checks.  | [optional] 
**lifecycle_management** | [**S3LifecycleManagement**](S3LifecycleManagement.md) | Specifies the S3 Lifecycle policy of the bucket | [optional] 
**owner_info** | [**S3ConfigOwnerInfo**](S3ConfigOwnerInfo.md) |  | [optional] 
**s3_access_path** | **str** | Specifies the path to access this View as an S3 share. | [optional] [readonly] 
**versioning** | **str** | Specifies the versioning state of S3 bucket. Buckets can be in one of three states: UnVersioned (default), VersioningEnabled, or VersioningSuspended. Once versioning is enabled for a bucket, it can never return to an UnVersioned state. However, versioning on the bucket can be suspended. | [optional] 
**swift_project_domain** | **str** | Specifies the Keystone project domain. | [optional] 
**swift_project_name** | **str** | Specifies the Keystone project name. | [optional] 
**swift_user_domain** | **str** | Specifies the Keystone user domain. | [optional] 
**swift_username** | **str** | Specifies the Keystone username. | [optional] 
**aliases** | [**List[ViewAliasInfo]**](ViewAliasInfo.md) | Aliases created for the view. A view alias allows a directory path inside a view to be mounted using the alias name. | [optional] [readonly] 
**basic_mount_path** | **str** | Specifies the NFS mount path of the View (without the hostname information). This path is used to support NFS mounting of the paths specified in the nfsExportPathList on Windows systems. | [optional] [readonly] 
**case_insensitive_names_enabled** | **bool** | Specifies whether to support case insensitive file/folder names. This parameter can only be set during create and cannot be changed. | [optional] [readonly] 
**create_time_msecs** | **int** | Specifies the time that the View was created in milliseconds. | [optional] [readonly] 
**data_lock_expiry_usecs** | **int** | DataLock (Write Once Read Many) lock expiry epoch time in microseconds. If a view is marked as a DataLock view, only a Data Security Officer (a user having Data Security Privilege) can delete the view until the lock expiry time. | [optional] 
**file_count_by_size** | [**List[FileCount]**](FileCount.md) | Specifies the file count by size for the View. | [optional] 
**intent** | **object** | Specifies the intent of the View. | [optional] 
**is_category_inferred** | **bool** | If True, category in response is not set by user but inferred by Iris because none is set. Category can only be none when view was created by v1 API or cloned from a view created by v1 API.  Inference Logic is as follows: 1. Object Services if only S3 or Swift protocol is selected. 2. Backup Target only if one read-write protocol is selected and    QoS is \&quot;Backup Target Commvault\&quot; or \&quot;Backup Target SSD\&quot;. 3. File Services if there are more than 1 read-write protocol or    it doesn&#39;t fit any other category. | [optional] [readonly] 
**is_target_for_migrated_data** | **bool** | Specifies if a view contains migrated data. | [optional] [readonly] 
**nfs_mount_path** | **str** | This field is currently deprecated. Please use NFS MountPaths which would be an array of strings. | [optional] [readonly] 
**nfs_mount_paths** | **List[str]** | Array of NFS Paths. Specifies the path for mounting this View as an NFS share. If Kerberos Provider has multiple hostaliases, each host alias has  its own path. | [optional] [readonly] 
**object_services_mapping_config** | **str** | Specifies the Object Services key mapping config of the view. This parameter can only be set during create and cannot be changed. Configuration of Object Services key mapping. Specifies the type of Object Services key mapping config. | [optional] [readonly] 
**owner_sid** | **str** | Specifies the sid of the view owner. | [optional] 
**s3_folder_support_enabled** | **bool** | Specifies whether to support s3 folder support feature. This parameter can only be set during create and cannot be changed. | [optional] [readonly] 
**smb_mount_paths** | **List[str]** | Array of SMB Paths. Specifies the possible paths that can be used to mount this View as a SMB share. If Active Directory has multiple account names; each machine account has its own path. | [optional] [readonly] 
**stats** | **object** | Specifies statistics about the View. | [optional] 
**storage_domain_id** | **int** | Specifies the id of the Storage Domain (View Box) where the View is stored. | [optional] [readonly] 
**storage_domain_name** | **str** | Specifies the name of the Storage Domain (View Box) where the View is stored. | [optional] [readonly] 
**view_failover** | **object** | Specifies the information about the failover of the view. | [optional] 
**view_id** | **int** | Specifies an id of the View assigned by the Cohesity Cluster. | [optional] [readonly] 
**view_protection** | **object** |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.view import View

# TODO update the JSON string below
json = "{}"
# create an instance of View from a JSON string
view_instance = View.from_json(json)
# print the JSON string representation of the object
print(View.to_json())

# convert the object into a dict
view_dict = view_instance.to_dict()
# create an instance of View from a dict
view_from_dict = View.from_dict(view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


