# SelfServiceSnapshotConfig

Specifies the self service snapshot config of a view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_access_sids** | **List[str]** | Specifies a list of sids who has access to the snapshots. | [optional] 
**alternate_snapshot_directory_name** | **str** | Specifies the alternate directory name for the snapshots. If it is not set, this feature for SMB protocol will not work. | [optional] 
**deny_access_sids** | **List[str]** | Specifies a list of sids who does not have access to the snapshots. This field overrides &#39;allowAccessSids&#39;. | [optional] 
**enabled** | **bool** | Specifies if self service snapshot feature is enabled. If this is set to true, the feature will also be enabled for NFS protocol. This field is deprecated. | [optional] 
**nfs_access_enabled** | **bool** | Specifies if self service snapshot feature is enabled for NFS protocol. | [optional] 
**previous_versions_enabled** | **bool** | Specifies if previouse versions feature is enabled with SMB protocol. | [optional] 
**smb_access_enabled** | **bool** | Specifies if self service snapshot feature is enabled for SMB protocol. | [optional] 
**snapshot_directory_name** | **str** | Specifies the directory name for the snapshots. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.self_service_snapshot_config import SelfServiceSnapshotConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SelfServiceSnapshotConfig from a JSON string
self_service_snapshot_config_instance = SelfServiceSnapshotConfig.from_json(json)
# print the JSON string representation of the object
print(SelfServiceSnapshotConfig.to_json())

# convert the object into a dict
self_service_snapshot_config_dict = self_service_snapshot_config_instance.to_dict()
# create an instance of SelfServiceSnapshotConfig from a dict
self_service_snapshot_config_from_dict = SelfServiceSnapshotConfig.from_dict(self_service_snapshot_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


