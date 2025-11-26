# PhysicalFileBackupPathParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**included_path** | **str** | Specifies a path to be included on the source. All paths under this path will be included unless they are specifically mentioned in excluded paths. | 
**excluded_paths** | **[str], none_type** | Specifies a set of paths nested under the include path which should be excluded from the Protection Group. | [optional] 
**skip_nested_volumes** | **bool, none_type** | Specifies whether to skip any nested volumes (both local and network) that are mounted under include path. Applicable only for windows sources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


