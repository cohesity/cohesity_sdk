# RegisteredRemoteStorageList

Specifies information about registered remote storage servers which are used by cohesity cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_storages** | [**List[RemoteStorageInfo]**](RemoteStorageInfo.md) | Specifies the list of registered remote storage info. | [optional] 

## Example

```python
from cohesity_sdk.models.registered_remote_storage_list import RegisteredRemoteStorageList

# TODO update the JSON string below
json = "{}"
# create an instance of RegisteredRemoteStorageList from a JSON string
registered_remote_storage_list_instance = RegisteredRemoteStorageList.from_json(json)
# print the JSON string representation of the object
print(RegisteredRemoteStorageList.to_json())

# convert the object into a dict
registered_remote_storage_list_dict = registered_remote_storage_list_instance.to_dict()
# create an instance of RegisteredRemoteStorageList from a dict
registered_remote_storage_list_from_dict = RegisteredRemoteStorageList.from_dict(registered_remote_storage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


