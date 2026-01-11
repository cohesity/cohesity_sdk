# RecoverAwsParams

Specifies the recovery options specific to AWS environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) |  | [optional] 
**objects** | [**[CommonRecoverObjectSnapshotParams], none_type**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. This property is mandatory for all recovery action types except recover vms. While recovering VMs, a user can specify snapshots of VM&#39;s or a Protection Group Run details to recover all the VM&#39;s that are backed up by that Run. For recovering files, specifies the object contains the file to recover. | [optional] 
**recover_aws_document_db_params** | [**RecoverAWSDocumentDBParams**](RecoverAWSDocumentDBParams.md) |  | [optional] 
**recover_aurora_params** | [**RecoverAwsAuroraParams**](RecoverAwsAuroraParams.md) |  | [optional] 
**recover_dynamo_db_params** | [**RecoverDynamoDBParams**](RecoverDynamoDBParams.md) |  | [optional] 
**recover_file_and_folder_params** | [**RecoverAwsFileAndFolderParams**](RecoverAwsFileAndFolderParams.md) |  | [optional] 
**recover_rds_aurora_my_sql_params** | [**RecoverAwsRdsAuroraMySqlParams**](RecoverAwsRdsAuroraMySqlParams.md) |  | [optional] 
**recover_rds_aurora_postgres_db_params** | [**RecoverAwsRdsAuroraPostgresDbParams**](RecoverAwsRdsAuroraPostgresDbParams.md) |  | [optional] 
**recover_rds_ingest_params** | [**RecoverRDSPostgresParams**](RecoverRDSPostgresParams.md) |  | [optional] 
**recover_rds_ms_sql_params** | [**RecoverRdsMsSQLParams**](RecoverRdsMsSQLParams.md) |  | [optional] 
**recover_rds_my_sql_params** | [**RecoverAwsRdsMySqlParams**](RecoverAwsRdsMySqlParams.md) |  | [optional] 
**recover_rds_oracle_params** | [**RecoverAwsRDSOracleParams**](RecoverAwsRDSOracleParams.md) |  | [optional] 
**recover_rds_params** | [**RecoverAwsRdsParams**](RecoverAwsRdsParams.md) |  | [optional] 
**recover_rds_postgres_db_params** | [**RecoverAwsRdsPostgresDbParams**](RecoverAwsRdsPostgresDbParams.md) |  | [optional] 
**recover_redshift_params** | [**RecoverAwsRedshiftParams**](RecoverAwsRedshiftParams.md) |  | [optional] 
**recover_s3_bucket_params** | [**RecoverAwsS3BucketParams**](RecoverAwsS3BucketParams.md) |  | [optional] 
**recover_vm_params** | [**RecoverAwsVmParams**](RecoverAwsVmParams.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


