# TdmSnapshotAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the ID of the snapshot. | 
**created_at** | **int, none_type** | Specifies the time (in usecs from epoch) when the snapshot was created. | [optional] 
**created_by_user** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the details of the user, who created the snapshot. This will be null for snapshots, that are taken by system, such as a scheduler. | [optional] 
**is_automated** | **bool, none_type** | Specifies whether the snapshot was taken automatically by the scheduler. | [optional] 
**updated_at** | **int, none_type** | Specifies the time (in usecs from epoch) when the snapshot was last updated. | [optional] 
**updated_by_user** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the details of the user, who last updated the snapshot. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


