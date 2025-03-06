# CommonRemoteStorageInfo

Specifies the details of common remote storage info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies unique id of the registered remote storage. | [optional] [readonly] 
**product** | **str** | Specifies the product type of the remote storage. | 

## Example

```python
from cohesity_sdk.cluster.models.common_remote_storage_info import CommonRemoteStorageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CommonRemoteStorageInfo from a JSON string
common_remote_storage_info_instance = CommonRemoteStorageInfo.from_json(json)
# print the JSON string representation of the object
print(CommonRemoteStorageInfo.to_json())

# convert the object into a dict
common_remote_storage_info_dict = common_remote_storage_info_instance.to_dict()
# create an instance of CommonRemoteStorageInfo from a dict
common_remote_storage_info_from_dict = CommonRemoteStorageInfo.from_dict(common_remote_storage_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


