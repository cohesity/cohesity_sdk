# ModifySourceHierarchyObjectsRequest

Specifies the parameters to add/update objects to/from entity hierarchy. This is a batch API that accepts multiple modification requests. Each request in the batch should specify one object to modify.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modification_requests** | [**List[SourceHierarchyModificationRequest]**](SourceHierarchyModificationRequest.md) | List of modification requests to perform on the source. Each request operates on a single leaf object. | 

## Example

```python
from cohesity_sdk.cluster.models.modify_source_hierarchy_objects_request import ModifySourceHierarchyObjectsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifySourceHierarchyObjectsRequest from a JSON string
modify_source_hierarchy_objects_request_instance = ModifySourceHierarchyObjectsRequest.from_json(json)
# print the JSON string representation of the object
print(ModifySourceHierarchyObjectsRequest.to_json())

# convert the object into a dict
modify_source_hierarchy_objects_request_dict = modify_source_hierarchy_objects_request_instance.to_dict()
# create an instance of ModifySourceHierarchyObjectsRequest from a dict
modify_source_hierarchy_objects_request_from_dict = ModifySourceHierarchyObjectsRequest.from_dict(modify_source_hierarchy_objects_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


