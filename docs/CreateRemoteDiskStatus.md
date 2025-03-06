# CreateRemoteDiskStatus

Specifies the status of creating remote disk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Specifies the error message when creating remote disk fails. | [optional] 
**mount_path** | **str** | Specifies the NFS mount path of the remote disk. | [optional] 
**node_id** | **int** | Specifies the node id of the disk. If not specified, the disk will be evenly distributed across all the nodes. | [optional] 
**status** | **str** | Specifies the creating status of this disk. | [optional] 
**tier** | **str** | Specifies the tier of the disk | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.create_remote_disk_status import CreateRemoteDiskStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRemoteDiskStatus from a JSON string
create_remote_disk_status_instance = CreateRemoteDiskStatus.from_json(json)
# print the JSON string representation of the object
print(CreateRemoteDiskStatus.to_json())

# convert the object into a dict
create_remote_disk_status_dict = create_remote_disk_status_instance.to_dict()
# create an instance of CreateRemoteDiskStatus from a dict
create_remote_disk_status_from_dict = CreateRemoteDiskStatus.from_dict(create_remote_disk_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


