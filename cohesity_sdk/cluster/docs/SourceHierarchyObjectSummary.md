# SourceHierarchyObjectSummary

Specifies the list of Object Summaries for Objects under a given Source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | [**ObjectStringIdentifier**](ObjectStringIdentifier.md) |  | [optional] 
**environment** | **str, none_type** | Specifies the environment of the object. | [optional] 
**id** | **int, none_type** | Specifies object id. | [optional] 
**name** | **str, none_type** | Specifies the name of the object. | [optional] 
**source_id** | **int, none_type** | Specifies registered source id to which object belongs. | [optional] 
**source_name** | **str, none_type** | Specifies registered source name to which object belongs. | [optional] 
**child_objects** | [**[ObjectSummary], none_type**](ObjectSummary.md) | Specifies child object details. | [optional] 
**global_id** | **str, none_type** | Specifies the global id which is a unique identifier of the object. | [optional] 
**logical_size_bytes** | **int, none_type** | Specifies the logical size of object in bytes. | [optional] 
**object_hash** | **str, none_type** | Specifies the hash identifier of the object. | [optional] 
**object_type** | **str, none_type** | Specifies the type of the object. | [optional] 
**os_type** | **str, none_type** | Specifies the operating system type of the object. | [optional] 
**protection_type** | **str, none_type** | Specifies the protection type of the object if any. | [optional] 
**sharepoint_site_summary** | [**SharepointObjectParams**](SharepointObjectParams.md) |  | [optional] 
**uuid** | **str, none_type** | Specifies the uuid which is a unique identifier of the object. | [optional] 
**v_center_summary** | [**ObjectTypeVCenterParams**](ObjectTypeVCenterParams.md) |  | [optional] 
**windows_cluster_summary** | [**ObjectTypeWindowsClusterParams**](ObjectTypeWindowsClusterParams.md) |  | [optional] 
**parent_id** | **int, none_type** | Specifies the ID of the direct parent of this object in the source hierarchy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


