# ObjectSnapshot

Specifies an Object Snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_params** | [**AwsSnapshotParams**](AwsSnapshotParams.md) |  | [optional] 
**azure_params** | [**AzureSnapshotParams**](AzureSnapshotParams.md) |  | [optional] 
**cluster_id** | **int** | Specifies the cluster id where this snapshot belongs to. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the cluster incarnation id where this snapshot belongs to. | [optional] 
**elastifile_params** | [**CommonNasObjectParams**](CommonNasObjectParams.md) |  | [optional] 
**environment** | **str** | Specifies the snapshot environment. | [optional] 
**expiry_time_usecs** | **int** | Specifies the expiry time of the snapshot in Unix timestamp epoch in microseconds. If the snapshot has no expiry, this property will not be set. | [optional] 
**external_target_info** | [**ArchivalTargetSummaryInfo**](ArchivalTargetSummaryInfo.md) |  | [optional] 
**flashblade_params** | [**FlashbladeObjectParams**](FlashbladeObjectParams.md) |  | [optional] 
**generic_nas_params** | [**CommonNasObjectParams**](CommonNasObjectParams.md) |  | [optional] 
**gpfs_params** | [**CommonNasObjectParams**](CommonNasObjectParams.md) |  | [optional] 
**has_data_lock** | **bool** | Specifies if this snapshot has datalock. | [optional] 
**hyperv_params** | [**HypervSnapshotParams**](HypervSnapshotParams.md) |  | [optional] 
**id** | **str** | Specifies the id of the snapshot. | [optional] 
**indexing_status** | **str** | Specifies the indexing status of objects in this snapshot.&lt;br&gt; &#39;InProgress&#39; indicates the indexing is in progress.&lt;br&gt; &#39;Done&#39; indicates indexing is done.&lt;br&gt; &#39;NoIndex&#39; indicates indexing is not applicable.&lt;br&gt; &#39;Error&#39; indicates indexing failed with error. | [optional] 
**isilon_params** | [**IsilonObjectParams**](IsilonObjectParams.md) |  | [optional] 
**netapp_params** | [**NetappObjectParams**](NetappObjectParams.md) |  | [optional] 
**object_id** | **int** | Specifies the object id which the snapshot is taken from. | [optional] 
**object_name** | **str** | Specifies the object name which the snapshot is taken from. | [optional] 
**on_legal_hold** | **bool** | Specifies if this snapshot is on legalhold. | [optional] 
**ownership_context** | **str** | Specifies the ownership context for the target. | [optional] 
**physical_params** | [**PhysicalSnapshotParams**](PhysicalSnapshotParams.md) |  | [optional] 
**protection_group_id** | **str** | Specifies id of the Protection Group. | [optional] 
**protection_group_name** | **str** | Specifies name of the Protection Group. | [optional] 
**protection_group_run_id** | **str** | Specifies id of the Protection Group Run. | [optional] 
**region_id** | **str** | Specifies the region id where this snapshot belongs to. | [optional] 
**run_instance_id** | **int** | Specifies the instance id of the protection run which create the snapshot. | [optional] 
**run_start_time_usecs** | **int** | Specifies the start time of the run in micro seconds. | [optional] 
**run_type** | **str** | Specifies the type of protection run created this snapshot. | [optional] 
**sfdc_params** | [**SfdcObjectParams**](SfdcObjectParams.md) |  | [optional] 
**snapshot_target_type** | **str** | Specifies the target type where the Object&#39;s snapshot resides. | [optional] 
**snapshot_timestamp_usecs** | **int** | Specifies the timestamp in Unix time epoch in microseconds when the snapshot is taken for the specified Object. | [optional] 
**source_group_id** | **str** | Specifies the source protection group id in case of replication. | [optional] 
**source_id** | **int** | Specifies the object source id which the snapshot is taken from. | [optional] 
**storage_domain_id** | **int** | Specifies the Storage Domain id where the snapshot of object is present. | [optional] 

## Example

```python
from cohesity_sdk.models.object_snapshot import ObjectSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectSnapshot from a JSON string
object_snapshot_instance = ObjectSnapshot.from_json(json)
# print the JSON string representation of the object
print(ObjectSnapshot.to_json())

# convert the object into a dict
object_snapshot_dict = object_snapshot_instance.to_dict()
# create an instance of ObjectSnapshot from a dict
object_snapshot_from_dict = ObjectSnapshot.from_dict(object_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


