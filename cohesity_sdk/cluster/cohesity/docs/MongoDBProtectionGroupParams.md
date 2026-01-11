# MongoDBProtectionGroupParams

Specifies the parameters for MongoDB Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_scale_concurrency** | **bool, none_type** | Specifies the flag to automatically scale number of concurrent IO Streams that will be created to exchange data with the cluster. | [optional] 
**bandwidth_mbps** | **int, none_type** | Specifies the maximum network bandwidth that each concurrent IO Stream can use for exchanging data with the cluster. | [optional] 
**concurrency** | **int, none_type** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. | [optional] 
**custom_source_name** | **str, none_type** | The user specified name for the Source on which this protection was run. | [optional] [readonly] 
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**exclude_objectlist** | **[str], none_type** | Specifies the list of fully qualified name of the entities to exclude for protection. | [optional] 
**include_objectlist** | **[str], none_type** | Specifies the list of fully qualified name of the entities to include for protection. | [optional] 
**objects** | [**[NoSqlProtectionGroupObjectParams]**](NoSqlProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**overwrite_exclude_objectlist** | **bool, none_type** | If disabled - The excludeObjectlist is merged with the existing exclude_sources_vec, preserving any existing elements while incorporating new ones. | [optional]  if omitted the server will use the default value of True
**overwrite_include_objectlist** | **bool, none_type** | If disabled - The includeObjectlist is merged with the existing sources_vec, preserving any existing elements while incorporating new ones. | [optional]  if omitted the server will use the default value of True
**source_id** | **int, none_type** | Object ID of the Source on which this protection was run . | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the Source on which this protection was run. | [optional] [readonly] 
**cdp_info** | [**MongoDBCdpJobInfo**](MongoDBCdpJobInfo.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


