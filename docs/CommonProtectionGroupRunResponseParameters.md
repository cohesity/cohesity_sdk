# CommonProtectionGroupRunResponseParameters

Specifies the parameters which are common between Protection Group runs of all Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the ID of the Protection Group run. | [optional] 
**protection_group_instance_id** | **int, none_type** | Protection Group instance Id. This field will be removed later. | [optional] 
**protection_group_id** | **str, none_type** | ProtectionGroupId to which this run belongs. | [optional] 
**is_replication_run** | **bool, none_type** | Specifies if this protection run is a replication run. | [optional] 
**origin_cluster_identifier** | [**ClusterIdentifier**](ClusterIdentifier.md) |  | [optional] 
**origin_protection_group_id** | **str, none_type** | ProtectionGroupId to which this run belongs on the primary cluster if this run is a replication run. | [optional] 
**protection_group_name** | **str, none_type** | Name of the Protection Group to which this run belongs. | [optional] 
**is_local_snapshots_deleted** | **bool, none_type** | Specifies if snapshots for this run has been deleted. | [optional] 
**objects** | [**[ObjectRunResult]**](ObjectRunResult.md) | Snapahot, replication, archival results for each object. | [optional] 
**local_backup_info** | [**BackupRunSummary**](BackupRunSummary.md) |  | [optional] 
**original_backup_info** | [**BackupRunSummary**](BackupRunSummary.md) |  | [optional] 
**replication_info** | [**ReplicationRunSummary**](ReplicationRunSummary.md) |  | [optional] 
**archival_info** | [**ArchivalRunSummary**](ArchivalRunSummary.md) |  | [optional] 
**cloud_spin_info** | [**CloudSpinRunSummary**](CloudSpinRunSummary.md) |  | [optional] 
**on_legal_hold** | **bool, none_type** | Specifies if the Protection Run is on legal hold. | [optional] 
**permissions** | [**[Tenant], none_type**](Tenant.md) | Specifies the list of tenants that have permissions for this protection group run. | [optional] 
**is_cloud_archival_direct** | **bool, none_type** | Specifies whether the run is a CAD run if cloud archive direct feature is enabled. If this field is true, the primary backup copy will only be available at the given archived location. | [optional] 
**has_local_snapshot** | **bool, none_type** | Specifies whether the run has a local snapshot. For cloud retrieved runs there may not be local snapshots. | [optional] 
**environment** | **str, none_type** | Specifies the environment of the Protection Group. | [optional] 
**externally_triggered_backup_tag** | **str, none_type** | The tag of externally triggered backup job. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


