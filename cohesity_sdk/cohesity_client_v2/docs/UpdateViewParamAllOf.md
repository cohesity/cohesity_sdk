# UpdateViewParamAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the View. | [optional] 
**category** | **str, none_type** | Specifies the category of the View. | [optional] 
**protocol_access** | [**[ViewProtocol], none_type**](ViewProtocol.md) | Specifies the supported Protocols for the View. | [optional] 
**qos** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the Quality of Service (QoS) Policy for the View. | [optional] 
**override_global_subnet_whitelist** | **bool, none_type** | Specifies whether view level client subnet whitelist overrides cluster and global setting. | [optional] 
**subnet_whitelist** | [**[Subnet], none_type**](Subnet.md) | Array of Subnets. Specifies a list of Subnets with IP addresses that have permissions to access the View. (Overrides or extends the Subnets specified at the global Cohesity Cluster level.) | [optional] 
**override_global_netgroup_whitelist** | **bool, none_type** | Specifies whether view level client netgroup whitelist overrides cluster and global setting. | [optional] 
**netgroup_whitelist** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Array of Netgroups. Specifies a list of netgroups with domains that have permissions to access the View. (Overrides or extends the Netgroup specified at the global Cohesity Cluster level.) | [optional] 
**security_mode** | **str, none_type** | Specifies the security mode used for this view. Currently we support the following modes: Native, Unified and NTFS style. &#39;NativeMode&#39; indicates a native security mode. &#39;UnifiedMode&#39; indicates a unified security mode. &#39;NtfsMode&#39; indicates a NTFS style security mode. | [optional] 
**storage_policy_override** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies if inline deduplication and compression settings inherited from the Storage Domain (View Box) should be disabled for this View. | [optional] 
**logical_quota** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies an optional logical quota limit (in bytes) for the usage allowed on this View. (Logical data is when the data is fully hydrated and expanded.) This limit overrides the limit inherited from the Storage Domain (View Box) (if set). If logicalQuota is nil, the limit is inherited from the Storage Domain (View Box) (if set). A new write is not allowed if the Storage Domain (View Box) will exceed the specified quota. However, it takes time for the Cohesity Cluster to calculate the usage across Nodes, so the limit may be exceeded by a small amount. In addition, if the limit is increased or data is removed, there may be a delay before the Cohesity Cluster allows more data to be written to the View, as the Cluster is calculating the usage across Nodes. | [optional] 
**file_lock_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Optional config that enables file locking for this view. It cannot be disabled during the edit of a view, if it has been enabled during the creation of the view. Also, it cannot be enabled if it was disabled during the creation of the view. | [optional] 
**file_extension_filter** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Optional filtering criteria that should be satisfied by all the files created in this view. It does not affect existing files. | [optional] 
**antivirus_scan_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the antivirus scan config settings for this View. | [optional] 
**description** | **str, none_type** | Specifies an optional text description about the View. | [optional] 
**allow_mount_on_windows** | **bool, none_type** | Specifies if this View can be mounted using the NFS protocol on Windows systems. If true, this View can be NFS mounted on Windows systems. | [optional] 
**enable_minion** | **bool, none_type** | Specifies if this view should allow minion or not. If true, this will allow minion. | [optional] 
**enable_filer_audit_logging** | **bool, none_type** | Specifies if Filer Audit Logging is enabled for this view. | [optional] 
**tenant_id** | **str, none_type** | Optional tenant id who has access to this View. | [optional] 
**enable_live_indexing** | **bool, none_type** | Specifies whether to enable live indexing for the view. | [optional] 
**enable_offline_caching** | **bool, none_type** | Specifies whether to enable offline file caching of the view. | [optional] 
**access_sids** | **[str], none_type** | Array of Security Identifiers (SIDs) Specifies the list of security identifiers (SIDs) for the restricted Principals who have access to this View. | [optional] 
**view_lock_enabled** | **bool, none_type** | Specifies whether view lock is enabled. If enabled the view cannot be modified or deleted until unlock. By default it is disabled. | [optional] 
**is_read_only** | **bool, none_type** | Specifies if the view is a read only view. User will no longer be able to write to this view if this is set to true. | [optional] 
**view_pinning_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the pinning config of this view. | [optional] 
**self_service_snapshot_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies self service config of this view. | [optional] 
**enable_metadata_accelerator** | **bool, none_type** | Specifies if metadata accelerator is enabled for this view. Only supported while creating a view. | [optional] 
**is_externally_triggered_backup_target** | **bool, none_type** | Specifies whether the view is for externally triggered backup target. If so, Magneto will ignore the backup schedule for the view protection job of this view. By default it is disabled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


