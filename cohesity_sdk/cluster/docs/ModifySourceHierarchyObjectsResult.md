# ModifySourceHierarchyObjectsResult

Result of modifying objects in source hierarchy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[SourceHierarchyModificationResult]**](SourceHierarchyModificationResult.md) | Results of individual modification requests. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.modify_source_hierarchy_objects_result import ModifySourceHierarchyObjectsResult

# TODO update the JSON string below
json = "{}"
# create an instance of ModifySourceHierarchyObjectsResult from a JSON string
modify_source_hierarchy_objects_result_instance = ModifySourceHierarchyObjectsResult.from_json(json)
# print the JSON string representation of the object
print(ModifySourceHierarchyObjectsResult.to_json())

# convert the object into a dict
modify_source_hierarchy_objects_result_dict = modify_source_hierarchy_objects_result_instance.to_dict()
# create an instance of ModifySourceHierarchyObjectsResult from a dict
modify_source_hierarchy_objects_result_from_dict = ModifySourceHierarchyObjectsResult.from_dict(modify_source_hierarchy_objects_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


