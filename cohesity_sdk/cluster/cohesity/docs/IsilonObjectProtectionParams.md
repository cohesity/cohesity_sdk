# IsilonObjectProtectionParams

Specifies the parameters which are specific to Isilon object protection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuous_snapshots** | [**ContinuousSnapshotParams**](ContinuousSnapshotParams.md) |  | [optional] 
**nfs_version_preference** | **str, none_type** | Specifies the preference of NFS version to be used for backing up Isilon. | [optional] 
**protocol** | **str, none_type** | Specifies the protocol of the NAS device being backed up. | [optional] 
**use_changelist** | **bool, none_type** | Specify whether to use the Isilon Changelist API to directly discover changed files/directories for faster incremental backup. Cohesity will keep an extra snapshot which will be deleted by the next successful backup. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


