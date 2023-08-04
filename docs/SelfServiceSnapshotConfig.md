# SelfServiceSnapshotConfig

Specifies the self service snapshot config of a view.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool, none_type** | Specifies if self service snapshot feature is enabled. If this is set to true, the feature will also be enabled for NFS protocol. This field is deprecated. | [optional] 
**previous_versions_enabled** | **bool, none_type** | Specifies if previouse versions feature is enabled with SMB protocol. | [optional] 
**nfs_access_enabled** | **bool, none_type** | Specifies if self service snapshot feature is enabled for NFS protocol. | [optional] 
**smb_access_enabled** | **bool, none_type** | Specifies if self service snapshot feature is enabled for SMB protocol. | [optional] 
**snapshot_directory_name** | **str, none_type** | Specifies the directory name for the snapshots. | [optional] 
**alternate_snapshot_directory_name** | **str, none_type** | Specifies the alternate directory name for the snapshots. If it is not set, this feature for SMB protocol will not work. | [optional] 
**allow_access_sids** | **[str]** | Specifies a list of sids who has access to the snapshots. | [optional] 
**deny_access_sids** | **[str]** | Specifies a list of sids who does not have access to the snapshots. This field overrides &#39;allowAccessSids&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


