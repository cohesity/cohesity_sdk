# ObjectSnapshot

Specifies an Object Snapshot.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the id of the snapshot. | [optional] 
**snapshot_target_type** | **str, none_type** | Specifies the target type where the Object&#39;s snapshot resides. | [optional] 
**indexing_status** | **str, none_type** | Specifies the indexing status of objects in this snapshot.&lt;br&gt; &#39;InProgress&#39; indicates the indexing is in progress.&lt;br&gt; &#39;Done&#39; indicates indexing is done.&lt;br&gt; &#39;NoIndex&#39; indicates indexing is not applicable.&lt;br&gt; &#39;Error&#39; indicates indexing failed with error. | [optional] 
**protection_group_id** | **str, none_type** | Specifies id of the Protection Group. | [optional] 
**protection_group_name** | **str, none_type** | Specifies name of the Protection Group. | [optional] 
**protection_group_run_id** | **str, none_type** | Specifies id of the Protection Group Run. | [optional] 
**run_instance_id** | **int, none_type** | Specifies the instance id of the protection run which create the snapshot. | [optional] 
**run_start_time_usecs** | **int, none_type** | Specifies the start time of the run in micro seconds. | [optional] 
**source_group_id** | **str, none_type** | Specifies the source protection group id in case of replication. | [optional] 
**run_type** | **str, none_type** | Specifies the type of protection run created this snapshot. | [optional] 
**environment** | **str, none_type** | Specifies the snapshot environment. | [optional] 
**snapshot_timestamp_usecs** | **int, none_type** | Specifies the timestamp in Unix time epoch in microseconds when the snapshot is taken for the specified Object. | [optional] 
**expiry_time_usecs** | **int, none_type** | Specifies the expiry time of the snapshot in Unix timestamp epoch in microseconds. If the snapshot has no expiry, this property will not be set. | [optional] 
**external_target_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the external target information if this is an archival snapshot. | [optional] 
**storage_domain_id** | **int, none_type** | Specifies the Storage Domain id where the snapshot of object is present. | [optional] 
**has_data_lock** | **bool, none_type** | Specifies if this snapshot has datalock. | [optional] 
**on_legal_hold** | **bool, none_type** | Specifies if this snapshot is on legalhold. | [optional] 
**object_id** | **int, none_type** | Specifies the object id which the snapshot is taken from. | [optional] 
**object_name** | **str, none_type** | Specifies the object name which the snapshot is taken from. | [optional] 
**source_id** | **int, none_type** | Specifies the object source id which the snapshot is taken from. | [optional] 
**region_id** | **str, none_type** | Specifies the region id where this snapshot belongs to. | [optional] 
**cluster_id** | **int, none_type** | Specifies the cluster id where this snapshot belongs to. | [optional] 
**cluster_incarnation_id** | **int, none_type** | Specifies the cluster incarnation id where this snapshot belongs to. | [optional] 
**physical_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters specific to Physical type snapshot. | [optional] 
**hyperv_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters specific to HyperV type snapshot. | [optional] 
**aws_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters specific to AWS type snapshot. | [optional] 
**azure_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters specific to Azure type snapshot. | [optional] 
**netapp_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters specific to NetApp type snapshot. | [optional] 
**isilon_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters specific to Isilon type snapshot. | [optional] 
**gpfs_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters specific to GPFS type snapshot. | [optional] 
**flashblade_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters specific to Flashblade type snapshot. | [optional] 
**generic_nas_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters specific to Generic NAS type snapshot. | [optional] 
**elastifile_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters specific to NetApp type snapshot. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


