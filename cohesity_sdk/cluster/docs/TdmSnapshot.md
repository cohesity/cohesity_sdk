# TdmSnapshot

Specifies the response params for a TDM snapshot.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the ID of the snapshot. | 
**label** | **str, none_type** | Specifies the label for the snapshot. | [optional] 
**is_automated** | **bool, none_type** | Specifies whether the snapshot was taken automatically by the scheduler. | [optional] 
**created_at** | **int, none_type** | Specifies the time (in usecs from epoch) when the snapshot was created. | [optional] 
**updated_at** | **int, none_type** | Specifies the time (in usecs from epoch) when the snapshot was last updated. | [optional] 
**created_by_user** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the details of the user, who created the snapshot. This will be null for snapshots, that are taken by system, such as a scheduler. | [optional] 
**updated_by_user** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the details of the user, who last updated the snapshot. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


