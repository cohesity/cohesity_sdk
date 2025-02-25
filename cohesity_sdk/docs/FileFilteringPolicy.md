# FileFilteringPolicy

Specifies a set of filters for a file based Protection Group. These values are strings which can represent a prefix or suffix. Example: '/tmp' or '*.mp4'. For file based Protection Groups, all files under prefixes specified by the 'includeFilters' list will be protected unless they are explicitly excluded by the 'excludeFilters' list.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_list** | **[str]** | Specifies the list of excluded files for this protection Protection Group. Exclude filters have a higher priority than include filters. | [optional] 
**include_list** | **[str]** | Specifies the list of included files for this Protection Group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


