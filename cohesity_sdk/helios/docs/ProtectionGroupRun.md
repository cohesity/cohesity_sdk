# ProtectionGroupRun

Protection run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_info** | [**ArchivalRunSummary**](ArchivalRunSummary.md) |  | [optional] 
**cloud_spin_info** | [**CloudSpinRunSummary**](CloudSpinRunSummary.md) |  | [optional] 
**environment** | **str** | Specifies the environment of the Protection Group. | [optional] 
**externally_triggered_backup_tag** | **str** | The tag of externally triggered backup job. | [optional] 
**has_local_snapshot** | **bool** | Specifies whether the run has a local snapshot. For cloud retrieved runs there may not be local snapshots. | [optional] 
**id** | **str** | Specifies the ID of the Protection Group run. | [optional] 
**is_cloud_archival_direct** | **bool** | Specifies whether the run is a CAD run if cloud archive direct feature is enabled. If this field is true, the primary backup copy will only be available at the given archived location. | [optional] 
**is_local_snapshots_deleted** | **bool** | Specifies if snapshots for this run has been deleted. | [optional] 
**is_metadata_deleted** | **bool** | Specifies if snapshots metadata for this run has been deleted. | [optional] 
**is_replication_run** | **bool** | Specifies if this protection run is a replication run. | [optional] 
**local_backup_info** | [**BackupRunSummary**](BackupRunSummary.md) |  | [optional] 
**objects** | [**List[ObjectRunResult]**](ObjectRunResult.md) | Snapahot, replication, archival results for each object. | [optional] 
**on_legal_hold** | **bool** | Specifies if the Protection Run is on legal hold. | [optional] 
**origin_cluster_identifier** | [**ClusterIdentifier**](ClusterIdentifier.md) |  | [optional] 
**origin_protection_group_id** | **str** | ProtectionGroupId to which this run belongs on the primary cluster if this run is a replication run. | [optional] 
**original_backup_info** | [**BackupRunSummary**](BackupRunSummary.md) |  | [optional] 
**permissions** | [**List[Tenant]**](Tenant.md) | Specifies the list of tenants that have permissions for this protection group run. | [optional] 
**protection_group_id** | **str** | ProtectionGroupId to which this run belongs. | [optional] 
**protection_group_instance_id** | **int** | Protection Group instance Id. This field will be removed later. | [optional] 
**protection_group_name** | **str** | Name of the Protection Group to which this run belongs. | [optional] 
**replication_info** | [**ReplicationRunSummary**](ReplicationRunSummary.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.protection_group_run import ProtectionGroupRun

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionGroupRun from a JSON string
protection_group_run_instance = ProtectionGroupRun.from_json(json)
# print the JSON string representation of the object
print(ProtectionGroupRun.to_json())

# convert the object into a dict
protection_group_run_dict = protection_group_run_instance.to_dict()
# create an instance of ProtectionGroupRun from a dict
protection_group_run_from_dict = ProtectionGroupRun.from_dict(protection_group_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


