# GcpPostgreSQLProtectionGroupParams

Specifies the parameters which are specific to Google PostgreSQL related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**exclude_postgresql_tag_ids** | **[[int]], none_type** | Array of arrays of PostgreSQL Tag Ids that specify db instances to Exclude. | [optional] 
**objects** | [**[GcpDatabaseProtectionGroupObjectParams]**](GcpDatabaseProtectionGroupObjectParams.md) | Specifies the PostgreSQL databases to be included in the Protection Group. | [optional] 
**postgresql_tag_ids** | **[[int]], none_type** | Array of arrays of PostgreSQL Tag Ids that specify db instances to Protect. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


