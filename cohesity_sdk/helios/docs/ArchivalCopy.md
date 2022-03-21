# ArchivalCopy

Specifies the information about archival snapshot.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_time_usecs** | **int, none_type** | Specifies the creation time of archival snapshot. | [optional] 
**status** | **str, none_type** | Specifies the status of the archival snapshot. | [optional] 
**is_r_paas** | **bool, none_type** | Specifies whether this archival location is RPaas. | [optional] 
**rpaas_region** | **str, none_type** | If the location is RPaas then this specifies the region. | [optional] 
**archival_target** | [**ArchivalTarget**](ArchivalTarget.md) |  | [optional] 
**snapshot_id** | **str** | Snapshot id of the snapshot corresponding to the archival copy of this backup run. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


