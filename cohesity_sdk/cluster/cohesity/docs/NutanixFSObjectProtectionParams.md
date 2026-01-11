# NutanixFSObjectProtectionParams

Specifies the parameters which are specific to NutanixFS object protection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_existing_snapshot** | **bool, none_type** | Specifies that snapshot label is not set for Data-Protect NutanixFS Volumes backup. If field is set to true, existing oldest snapshot is used for backup and subsequent incremental will be selected in ascending order of snapshot create time on the source. If snapshot label is set, this field is set to false. | [optional] 
**continuous_snapshots** | [**ContinuousSnapshotParams**](ContinuousSnapshotParams.md) |  | [optional] 
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection. | [optional] 
**nfs_version_preference** | **str, none_type** | Specifies the preference of NFS version to be backed up | [optional] 
**protocol** | **str, none_type** | Specifies the protocol of the NAS device being backed up. | [optional] 
**snapshot_label** | [**SnapshotLabel**](SnapshotLabel.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


