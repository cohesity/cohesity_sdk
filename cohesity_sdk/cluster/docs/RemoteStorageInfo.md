# RemoteStorageInfo

Specifies the remote storage Registration parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies unique id of the registered remote storage. | [optional] [readonly] 
**product** | **str** | Specifies the product type of the remote storage. | 
**flashblade_params** | [**FlashbladeParams**](FlashbladeParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.remote_storage_info import RemoteStorageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteStorageInfo from a JSON string
remote_storage_info_instance = RemoteStorageInfo.from_json(json)
# print the JSON string representation of the object
print(RemoteStorageInfo.to_json())

# convert the object into a dict
remote_storage_info_dict = remote_storage_info_instance.to_dict()
# create an instance of RemoteStorageInfo from a dict
remote_storage_info_from_dict = RemoteStorageInfo.from_dict(remote_storage_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


