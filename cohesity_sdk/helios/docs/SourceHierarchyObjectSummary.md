# SourceHierarchyObjectSummary

Specifies the list of Object Summaries for Objects under a given Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | [**ObjectStringIdentifier**](ObjectStringIdentifier.md) |  | [optional] 
**environment** | **str** | Specifies the environment of the object. | [optional] 
**id** | **int** | Specifies object id. | [optional] 
**name** | **str** | Specifies the name of the object. | [optional] 
**source_id** | **int** | Specifies registered source id to which object belongs. | [optional] 
**source_name** | **str** | Specifies registered source name to which object belongs. | [optional] 
**child_objects** | [**List[ObjectSummary]**](ObjectSummary.md) | Specifies child object details. | [optional] 
**global_id** | **str** | Specifies the global id which is a unique identifier of the object. | [optional] 
**logical_size_bytes** | **int** | Specifies the logical size of object in bytes. | [optional] 
**object_hash** | **str** | Specifies the hash identifier of the object. | [optional] 
**object_type** | **str** | Specifies the type of the object. | [optional] 
**os_type** | **str** | Specifies the operating system type of the object. | [optional] 
**protection_type** | **str** | Specifies the protection type of the object if any. | [optional] 
**sharepoint_site_summary** | [**SharepointObjectParams**](SharepointObjectParams.md) |  | [optional] 
**uuid** | **str** | Specifies the uuid which is a unique identifier of the object. | [optional] 
**v_center_summary** | [**ObjectTypeVCenterParams**](ObjectTypeVCenterParams.md) |  | [optional] 
**windows_cluster_summary** | [**ObjectTypeWindowsClusterParams**](ObjectTypeWindowsClusterParams.md) |  | [optional] 
**parent_id** | **int** | Specifies the ID of the direct parent of this object in the source hierarchy. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.source_hierarchy_object_summary import SourceHierarchyObjectSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SourceHierarchyObjectSummary from a JSON string
source_hierarchy_object_summary_instance = SourceHierarchyObjectSummary.from_json(json)
# print the JSON string representation of the object
print(SourceHierarchyObjectSummary.to_json())

# convert the object into a dict
source_hierarchy_object_summary_dict = source_hierarchy_object_summary_instance.to_dict()
# create an instance of SourceHierarchyObjectSummary from a dict
source_hierarchy_object_summary_from_dict = SourceHierarchyObjectSummary.from_dict(source_hierarchy_object_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


