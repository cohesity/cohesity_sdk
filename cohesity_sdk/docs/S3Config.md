# S3Config

Specifies the S3 config settings for this View.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl_config** | [**AclConfig**](AclConfig.md) |  | [optional] 
**bucket_policy** | [**BucketPolicy**](BucketPolicy.md) |  | [optional] 
**enable_abac** | **bool, none_type** | Specifies if this View has S3 ABAC enabled. This can only be set while creating a view. The ABAC server corresponding the tenant will be used for authentication and authorization checks.  | [optional] 
**lifecycle_management** | [**S3LifecycleManagement**](S3LifecycleManagement.md) |  | [optional] 
**owner_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the owner info of the View as an S3 bucket. | [optional] 
**s3_access_path** | **str, none_type** | Specifies the path to access this View as an S3 share. | [optional] [readonly] 
**versioning** | **str, none_type** | Specifies the versioning state of S3 bucket. Buckets can be in one of three states: UnVersioned (default), VersioningEnabled, or VersioningSuspended. Once versioning is enabled for a bucket, it can never return to an UnVersioned state. However, versioning on the bucket can be suspended. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


