# GcpSqlServerProtectionGroupParams

Specifies the parameters which are specific to Google SQL Server related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_storage_bucket_name** | **str** | The Google Cloud Storage bucket name for Cloud SQL backup. | 
**bucket_auto_create** | **bool, none_type** | This flag controls whether SQL backup auto-creates bucket or uses the provided bucket name. | [optional] 
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**[GcpSqlServerProtectionGroupObjectParams]**](GcpSqlServerProtectionGroupObjectParams.md) | Specifies the SQL Server databases to be included in the Protection Group. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


