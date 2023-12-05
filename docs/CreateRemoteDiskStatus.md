# CreateRemoteDiskStatus

Specifies the status of creating remote disk.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str, none_type** | Specifies the error message when creating remote disk fails. | [optional] 
**mount_path** | **str, none_type** | Specifies the NFS mount path of the remote disk. | [optional] 
**node_id** | **int, none_type** | Specifies the node id of the disk. If not specified, the disk will be evenly distributed across all the nodes. | [optional] 
**status** | **str, none_type** | Specifies the creating status of this disk. | [optional] 
**tier** | **str, none_type** | Specifies the tier of the disk | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


