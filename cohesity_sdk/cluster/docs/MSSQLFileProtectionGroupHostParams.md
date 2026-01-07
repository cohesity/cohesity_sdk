# MSSQLFileProtectionGroupHostParams

Specifies the host specific parameters for a host container in this protection group. Objects specified here should only be MSSQL root containers and will not be protected unless they are also specified in the 'objects' list. This list is just for specifying source level settings.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_id** | **int, none_type** | Specifies the id of the host container on which databases are hosted. | 
**disable_source_side_deduplication** | **bool, none_type** | Specifies whether or not to disable source side deduplication on this source. The default behavior is false unless the user has set &#39;performSourceSideDeduplication&#39; to true. | [optional] 
**host_name** | **str, none_type** | Specifies the name of the host container on which databases are hosted. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


