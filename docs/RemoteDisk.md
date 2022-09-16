# RemoteDisk

Specifies the configuration of a remote disk.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_path** | **str, none_type** | Specifies the NFS mount path of the remote disk. | 
**tier** | **str, none_type** | Specifies the tier of the disk | 
**id** | **int, none_type** | Specifies the disk id. | [optional] [readonly] 
**node_id** | **int, none_type** | Specifies the node id of the disk. If not specified, the disk will be evenly distributed across all the nodes. | [optional] 
**capacity_bytes** | **int, none_type** | Specifies the logical capacity of the disk in bytes. | [optional] [readonly] 
**used_capacity_bytes** | **int, none_type** | Specifies the logical used capacity of remote disk in bytes. | [optional] [readonly] 
**status** | **str, none_type** | Specifies the status of a remote disk. | [optional] [readonly] 
**file_system_name** | **str, none_type** | Specifies the name of filesystem on remote storage. | [optional] 
**data_vip** | **str, none_type** | Specifies the data vip used to mount the filesystem. | [optional] 
**node_ip** | **str, none_type** | Specifies ip address of the node that this remote disk is mounted on. | [optional] 
**used_capacity_bytes_physical** | **int, none_type** | Specifies the physical used capacity of remote disk in bytes. | [optional] [readonly] 
**capacity_bytes_physical** | **int, none_type** | Specifies the physical capacity of the disk in bytes. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


