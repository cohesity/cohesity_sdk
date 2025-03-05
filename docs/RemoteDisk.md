# RemoteDisk

Specifies the configuration of a remote disk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_bytes** | **int** | Specifies the logical capacity of the disk in bytes. | [optional] [readonly] 
**capacity_bytes_physical** | **int** | Specifies the physical capacity of the disk in bytes. | [optional] [readonly] 
**data_vip** | **str** | Specifies the data vip used to mount the filesystem. | [optional] 
**file_system_name** | **str** | Specifies the name of filesystem on remote storage. | [optional] 
**id** | **int** | Specifies the disk id. | [optional] [readonly] 
**mount_path** | **str** | Specifies the NFS mount path of the remote disk. | 
**node_id** | **int** | Specifies the node id of the disk. If not specified, the disk will be evenly distributed across all the nodes. | [optional] 
**node_ip** | **str** | Specifies ip address of the node that this remote disk is mounted on. | [optional] 
**status** | **str** | Specifies the status of a remote disk. | [optional] [readonly] 
**tier** | **str** | Specifies the tier of the disk | 
**used_capacity_bytes** | **int** | Specifies the logical used capacity of remote disk in bytes. | [optional] [readonly] 
**used_capacity_bytes_physical** | **int** | Specifies the physical used capacity of remote disk in bytes. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.remote_disk import RemoteDisk

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteDisk from a JSON string
remote_disk_instance = RemoteDisk.from_json(json)
# print the JSON string representation of the object
print(RemoteDisk.to_json())

# convert the object into a dict
remote_disk_dict = remote_disk_instance.to_dict()
# create an instance of RemoteDisk from a dict
remote_disk_from_dict = RemoteDisk.from_dict(remote_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


