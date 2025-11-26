# SfdcAuroraClusterInfo

Specifies the Aurora cluster information required to protect an Sfdc Org. This parameter is filled internally by cohesity. It should not be filled by end user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aurora_cluster_arn** | **str, none_type** | Arn of the Aurora cluster. | 
**database_access_iam_role_arn** | **str, none_type** | Contains the Arn of the IAM role of the which has access to the db user allocated to the tenant. | 
**database_port** | **str, none_type** | Database port to access the dbs on the Aurora cluster. | 
**database_user** | **str, none_type** | Database user to access the dbs on the Aurora cluster. | 
**region_id** | **str, none_type** | Specifies the region id of the Aurora cluster. | 
**s3_access_iam_role_arn** | **str, none_type** | Contains the Arn of the IAM role which has read and write access to the tenant&#39;s s3 bucket. | 
**s3_bucket_name** | **str, none_type** | Contains the tenant&#39;s S3 bucket. | 
**s3_bucket_prefix** | **str, none_type** | S3Bucket prefix for the intermediate. | 
**tenant_id** | **str, none_type** | Contains the Id of the tenant. | 
**writer_endpoint** | **str, none_type** | Writer endpoint of the Aurora cluster. | 
**database_schema** | **str, none_type** | Database schema to access the dbs on the Aurora cluster. | [optional] 
**reader_endpoint** | **str, none_type** | Reader endpoint of the Aurora cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


