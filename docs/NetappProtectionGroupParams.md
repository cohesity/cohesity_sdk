# NetappProtectionGroupParams

Specifies the parameters which are specific to Netapp related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_existing_snapshot** | **bool** | Specifies that snapshot label is not set for Data-Protect Netapp Volumes backup. If field is set to true, existing oldest snapshot is used for backup and subsequent incremental will be selected in ascending order of snapshot create time on the source. If snapshot label is set, this field is set to false. | [optional] 
**continue_on_error** | **bool** | Specifies whether or not the Protection Group should continue regardless of whether or not an error was encountered during protection group run. | [optional] 
**continuous_snapshots** | [**ContinuousSnapshotParams**](ContinuousSnapshotParams.md) |  | [optional] 
**direct_cloud_archive** | **bool** | Specifies whether or not to store the snapshots in this run directly in an Archive Target instead of on the Cluster. If this is set to true, the associated policy must have exactly one Archive Target associated with it and the policy must be set up to archive after every run. Also, a Storage Domain cannot be specified. Default behavior is &#39;false&#39;. | [optional] 
**encryption_enabled** | **bool** | Specifies whether the protection group should use encryption while backup or not. | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**file_filters** | [**FileFilteringPolicy**](FileFilteringPolicy.md) |  | [optional] 
**file_lock_config** | [**FileLevelDataLockConfig**](FileLevelDataLockConfig.md) |  | [optional] 
**filter_ip_config** | [**FilterIpConfig**](FilterIpConfig.md) |  | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**modify_source_permissions** | **bool** | Specifies if the Netapp source permissions should be modified internally to allow backups. | [optional] 
**native_format** | **bool** | Specifies whether or not to enable native format for direct archive job. This field is set to true if native format should be used for archiving. | [optional] 
**nfs_version_preference** | **str** | Specifies the preference of NFS version to be backed up if a volume supports multiple versions of NFS. | [optional] 
**objects** | [**List[NetappProtectionGroupObjectParams]**](NetappProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | 
**pre_post_script** | [**HostBasedBackupScriptParams**](HostBasedBackupScriptParams.md) |  | [optional] 
**protocol** | **str** | Specifies the preferred protocol to use if this device supports multiple protocols. | [optional] 
**snap_mirror_config** | [**SnapMirrorConfig**](SnapMirrorConfig.md) |  | [optional] 
**snapshot_label** | [**SnapshotLabel**](SnapshotLabel.md) |  | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**throttling_config** | [**NasThrottlingConfig**](NasThrottlingConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.netapp_protection_group_params import NetappProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of NetappProtectionGroupParams from a JSON string
netapp_protection_group_params_instance = NetappProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(NetappProtectionGroupParams.to_json())

# convert the object into a dict
netapp_protection_group_params_dict = netapp_protection_group_params_instance.to_dict()
# create an instance of NetappProtectionGroupParams from a dict
netapp_protection_group_params_from_dict = NetappProtectionGroupParams.from_dict(netapp_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


