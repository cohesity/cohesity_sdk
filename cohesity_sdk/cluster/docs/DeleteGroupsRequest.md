# DeleteGroupsRequest

Specifies list of groups to delete.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sids** | **List[str]** | Specifies a list of group sids to delete. | 

## Example

```python
from cohesity_sdk.cluster.models.delete_groups_request import DeleteGroupsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteGroupsRequest from a JSON string
delete_groups_request_instance = DeleteGroupsRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteGroupsRequest.to_json())

# convert the object into a dict
delete_groups_request_dict = delete_groups_request_instance.to_dict()
# create an instance of DeleteGroupsRequest from a dict
delete_groups_request_from_dict = DeleteGroupsRequest.from_dict(delete_groups_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


