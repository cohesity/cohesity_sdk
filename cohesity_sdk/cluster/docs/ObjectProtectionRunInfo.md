# ObjectProtectionRunInfo

Specifies the run info for a run protecting an object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_info** | [**ArchivalRun**](ArchivalRun.md) |  | [optional] 
**cloud_spin_info** | [**CloudSpinRun**](CloudSpinRun.md) |  | [optional] 
**data_lock** | **str, none_type** | Specifies WORM retention type for the local backeup. When a WORM retention type is specified, the snapshots of the Protection Groups using this policy will be kept until the maximum of the snapshot retention time. During that time, the snapshots cannot be deleted. &lt;br&gt;&#39;Compliance&#39; implies WORM retention is set for compliance reason. &lt;br&gt;&#39;Administrative&#39; implies WORM retention is set for administrative purposes. | [optional] 
**is_cloud_archival_direct** | **bool, none_type** | Specifies whether the run is a CAD run if cloud archive direct feature is enabled. If this field is true, the primary backup copy will only be available at the given archived location. | [optional] 
**is_local_snapshots_deleted** | **bool, none_type** | Specifies if snapshots for this run has been deleted. | [optional] 
**is_replication_run** | **bool, none_type** | Specifies if this protection run is a replication run. | [optional] 
**is_sla_violated** | **bool, none_type** | Indicated if SLA has been violated for this run. | [optional] 
**local_snapshot_info** | [**BackupRun**](BackupRun.md) |  | [optional] 
**on_legal_hold** | **bool, none_type** | Specifies if object&#39;s snapshot is on legal hold. | [optional] 
**on_prem_deploy_info** | [**OnPremDeployRun**](OnPremDeployRun.md) |  | [optional] 
**origin_cluster_identifier** | [**ClusterIdentifier**](ClusterIdentifier.md) |  | [optional] 
**origin_protection_group_id** | **str, none_type** | ProtectionGroupId to which this run belongs on the primary cluster if this run is a replication run. | [optional] 
**original_backup_info** | [**BackupRun**](BackupRun.md) |  | [optional] 
**permissions** | [**[Tenant], none_type**](TenantInfo.md) | Specifies the list of tenants that have permissions for this protection group run. | [optional] 
**policy_id** | **str, none_type** | Specifies the unique id of the Protection Policy associated with the Protection Run. The Policy provides retry settings Protection Schedules, Priority, SLA, etc. | [optional] 
**policy_name** | **str, none_type** | Specifies Specifies the name of the Protection Policy. | [optional] 
**protection_group_id** | **str, none_type** | ProtectionGroupId to which this run belongs. This will only be populated if the object is protected by a protection group. | [optional] 
**protection_group_name** | **str, none_type** | Name of the Protection Group to which this run belongs. This will only be populated if the object is protected by a protection group. | [optional] 
**replication_info** | [**ReplicationRun**](ReplicationRun.md) |  | [optional] 
**run_id** | **str, none_type** | Specifies the ID of the protection run. | [optional] 
**run_label** | **str, none_type** | Specifies a label with which this run is created. Only applicable for user triggered protect now action. | [optional] 
**run_type** | **str, none_type** | Type of Protection run. &#39;kRegular&#39; indicates an incremental (CBT) backup. Incremental backups utilizing CBT (if supported) are captured of the target protection objects. The first run of a kRegular schedule captures all the blocks. &#39;kFull&#39; indicates a full (no CBT) backup. A complete backup (all blocks) of the target protection objects are always captured and Change Block Tracking (CBT) is not utilized. &#39;kLog&#39; indicates a Database Log backup. Capture the database transaction logs to allow rolling back to a specific point in time. &#39;kSystem&#39; indicates system volume backup. It produces an image for bare metal recovery. | [optional] 
**storage_domain_id** | **int, none_type** | Specifies the Storage Domain (View Box) ID where this Protection Run writes data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


