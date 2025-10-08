# IndexingPolicy

Specifies settings for indexing files found in an Object (such as a VM) so these files can be searched and recovered. This also specifies inclusion and exclusion rules that determine the directories to index.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_indexing** | **bool, none_type** | Specifies if the files found in an Object (such as a VM) should be indexed. If true (the default), files are indexed. | 
**exclude_paths** | **[str], none_type** | Array of Excluded Directories. Specifies a list of directories to exclude from indexing.Regular expression can also be specified to provide the directory paths. Example: /Users/&lt;wildcard&gt;/AppData | [optional] 
**include_paths** | **[str], none_type** | Array of Indexed Directories. Specifies a list of directories to index. Regular expression can also be specified to provide the directory paths. Example: /Users/&lt;wildcard&gt;/AppData | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


