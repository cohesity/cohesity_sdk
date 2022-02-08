# ContinuousSnapshotParams

Specifies the source snapshots to be taken even if there is a pending run in a protection group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool, none_type** | Specifies whether source snapshots should be taken even if there is a pending run. | 
**max_allowed_snapshots** | **int, none_type** | Specifies the maximum number of source snapshots allowed for a given object in a protection group. This is only applicable if isContinuousSnapshottingEnabled is set to true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


