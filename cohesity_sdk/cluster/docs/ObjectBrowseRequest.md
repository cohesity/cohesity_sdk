# ObjectBrowseRequest

Specifies the request to fetch children of an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment type of the Object. | 
**hdfs_params** | [**HdfsBrowseRequestParams**](HdfsBrowseRequestParams.md) |  | [optional] 
**pagination_info** | [**PaginationInfo**](PaginationInfo.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.object_browse_request import ObjectBrowseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectBrowseRequest from a JSON string
object_browse_request_instance = ObjectBrowseRequest.from_json(json)
# print the JSON string representation of the object
print(ObjectBrowseRequest.to_json())

# convert the object into a dict
object_browse_request_dict = object_browse_request_instance.to_dict()
# create an instance of ObjectBrowseRequest from a dict
object_browse_request_from_dict = ObjectBrowseRequest.from_dict(object_browse_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


