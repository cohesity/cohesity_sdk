# Tag

Tag details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Name of the Tag. Name has to be unique under Namespace. | 
**namespace** | **str, none_type** | Namespace of the Tag. This is used to filter tags based on application or usecase. For example all tags related to vcenter can be put under one namespace or different departments could have their own namespaces e.g. finance/tag1 or operations/tag2 etc. | 
**created_time_usecs** | **int, none_type** | Specifies the timestamp in microseconds since the epoch when this Tag was created. | [optional] [readonly] 
**description** | **str, none_type** | Description of the Tag. | [optional] 
**id** | **str, none_type** | Specifies unique id of the Tag. | [optional] [readonly] 
**last_updated_time_usecs** | **int, none_type** | Specifies the timestamp in microseconds since the epoch when this Tag was last updated. | [optional] [readonly] 
**marked_for_deletion** | **bool, none_type** | If true, Tag is marked for deletion. | [optional] [readonly] 
**tenant_id** | **str, none_type** | Tenant Id to whom the Tag belongs. | [optional] [readonly] 
**ui_color** | **str, none_type** | Color of the tag in UI. | [optional] 
**ui_path_elements** | **[str], none_type** | Path of the tag for UI nesting purposes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


