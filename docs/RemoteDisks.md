# RemoteDisks

Specifies a list of remote disks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_disks** | [**List[RemoteDisk]**](RemoteDisk.md) | Specifies a list of remote disks. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.remote_disks import RemoteDisks

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteDisks from a JSON string
remote_disks_instance = RemoteDisks.from_json(json)
# print the JSON string representation of the object
print(RemoteDisks.to_json())

# convert the object into a dict
remote_disks_dict = remote_disks_instance.to_dict()
# create an instance of RemoteDisks from a dict
remote_disks_from_dict = RemoteDisks.from_dict(remote_disks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


