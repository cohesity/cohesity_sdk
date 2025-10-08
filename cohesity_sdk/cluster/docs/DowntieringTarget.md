# DowntieringTarget

Specifies the target data tiering details for downtier job. This is in beta phase. Please use target inside CommonDataTieringTaskParams, present directly under data tiering request body. If target is present inside CommonDataTieringTaskParams, this target will be ignored.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_domain_id** | **int, none_type** | Specifies the Storage Domain ID where the view will be kept. | 
**view_name_prefix** | **str, none_type** | Specifies the view name prefix. | 
**downtiered_data_locations** | [**[DowntieredDataLocation], none_type**](DowntieredDataLocation.md) | Specifies a list of mapping between sources and its corresponding viewNames and mountPaths, where the sources were downtiered. | [optional] [readonly] 
**mount_path_prefix** | **str, none_type** | Specifies the mount path prefix inside the view. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


