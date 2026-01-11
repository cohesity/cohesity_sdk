# DataAccessSnapshotInfo

Specifies the snapshot information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment of the source. | 
**snapshot_id** | **str** | Specifies the id of the object snapshot. | 
**restore_time_usecs** | **int, none_type** | Specifies the time to which the object needs to be restored. If this is not specified the object is restore from the base snapshot identified by the run_start_time_usecs. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


