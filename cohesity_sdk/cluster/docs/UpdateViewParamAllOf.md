# UpdateViewParamAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_sids** | **[str], none_type** | Array of Security Identifiers (SIDs) Specifies the list of security identifiers (SIDs) for the restricted Principals who have access to this View. | [optional] 
**allow_mount_on_windows** | **bool, none_type** | Specifies if this View can be mounted using the NFS protocol on Windows systems. If true, this View can be NFS mounted on Windows systems. | [optional] 
**antivirus_scan_config** | [**AntivirusScanConfig**](AntivirusScanConfig.md) |  | [optional] 
**category** | **str, none_type** | Specifies the category of the View. | [optional] 
**description** | **str, none_type** | Specifies an optional text description about the View. | [optional] 
**enable_filer_audit_logging** | **bool, none_type** | Specifies if Filer Audit Logging is enabled for this view. | [optional] 
**enable_live_indexing** | **bool, none_type** | Specifies whether to enable live indexing for the view. | [optional] 
**enable_metadata_accelerator** | **bool, none_type** | Specifies if metadata accelerator is enabled for this view. Only supported while creating a view. | [optional] 
**enable_minion** | **bool, none_type** | Specifies if this view should allow minion or not. If true, this will allow minion. | [optional] 
**enable_offline_caching** | **bool, none_type** | Specifies whether to enable offline file caching of the view. | [optional] 
**file_extension_filter** | [**FileExtensionFilter**](FileExtensionFilter.md) |  | [optional] 
**file_lock_config** | [**FileLevelDataLockConfig**](FileLevelDataLockConfig.md) |  | [optional] 
**filer_lifecycle_management** | [**FilerLifecycleManagement**](FilerLifecycleManagement.md) |  | [optional] 
**is_externally_triggered_backup_target** | **bool, none_type** | Specifies whether the view is for externally triggered backup target. If so, Magneto will ignore the backup schedule for the view protection job of this view. By default it is disabled. | [optional] 
**is_read_only** | **bool, none_type** | Specifies if the view is a read only view. User will no longer be able to write to this view if this is set to true. | [optional] 
**lexicographic_prefetch** | **bool, none_type** | If small files are accessed sequentially from a client, this specifies whether to detect and prefetch files based on the lexicographic index to improve file read performance. | [optional] 
**logical_quota** | [**QuotaPolicy**](QuotaPolicy.md) |  | [optional] 
**name** | **str, none_type** | Specifies the name of the View. | [optional] 
**netgroup_whitelist** | [**NisNetgroups**](NisNetgroups.md) |  | [optional] 
**override_global_netgroup_whitelist** | **bool, none_type** | Specifies whether view level client netgroup whitelist overrides cluster and global setting. | [optional] 
**override_global_subnet_whitelist** | **bool, none_type** | Specifies whether view level client subnet whitelist overrides cluster and global setting. | [optional] 
**protocol_access** | [**[ViewProtocol], none_type**](ViewProtocol.md) | Specifies the supported Protocols for the View. | [optional] 
**qos** | [**QoS**](QoS.md) |  | [optional] 
**security_mode** | **str, none_type** | Specifies the security mode used for this view. Currently we support the following modes: Native, Unified and NTFS style. &#39;NativeMode&#39; indicates a native security mode. &#39;UnifiedMode&#39; indicates a unified security mode. &#39;NtfsMode&#39; indicates a NTFS style security mode. | [optional] 
**self_service_snapshot_config** | [**SelfServiceSnapshotConfig**](SelfServiceSnapshotConfig.md) |  | [optional] 
**storage_policy_override** | [**StoragePolicyOverride**](StoragePolicyOverride.md) |  | [optional] 
**subnet_whitelist** | [**[Subnet], none_type**](Subnet.md) | Array of Subnets. Specifies a list of Subnets with IP addresses that have permissions to access the View. (Overrides or extends the Subnets specified at the global Cohesity Cluster level.) | [optional] 
**tenant_id** | **str, none_type** | Optional tenant id who has access to this View. | [optional] 
**view_lock_enabled** | **bool, none_type** | Specifies whether view lock is enabled. If enabled the view cannot be modified or deleted until unlock. By default it is disabled. | [optional] 
**view_pinning_config** | [**ViewPinningConfig**](ViewPinningConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


