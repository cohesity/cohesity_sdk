# NutanixFSObjectProtectionParams

Specifies the parameters which are specific to NutanixFS object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_existing_snapshot** | **bool** | Specifies that snapshot label is not set for Data-Protect NutanixFS Volumes backup. If field is set to true, existing oldest snapshot is used for backup and subsequent incremental will be selected in ascending order of snapshot create time on the source. If snapshot label is set, this field is set to false. | [optional] 
**continuous_snapshots** | [**ContinuousSnapshotParams**](ContinuousSnapshotParams.md) |  | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection. | [optional] 
**nfs_version_preference** | **str** | Specifies the preference of NFS version to be backed up | [optional] 
**protocol** | **str** | Specifies the protocol of the NAS device being backed up. | [optional] 
**snapshot_label** | [**SnapshotLabel**](SnapshotLabel.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.nutanix_fs_object_protection_params import NutanixFSObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of NutanixFSObjectProtectionParams from a JSON string
nutanix_fs_object_protection_params_instance = NutanixFSObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(NutanixFSObjectProtectionParams.to_json())

# convert the object into a dict
nutanix_fs_object_protection_params_dict = nutanix_fs_object_protection_params_instance.to_dict()
# create an instance of NutanixFSObjectProtectionParams from a dict
nutanix_fs_object_protection_params_from_dict = NutanixFSObjectProtectionParams.from_dict(nutanix_fs_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


