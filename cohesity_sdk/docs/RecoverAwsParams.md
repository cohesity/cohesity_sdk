# RecoverAwsParams

Specifies the recovery options specific to AWS environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) |  | [optional] 
**objects** | [**[CommonRecoverObjectSnapshotParams], none_type**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. This property is mandatory for all recovery action types except recover vms. While recovering VMs, a user can specify snapshots of VM&#39;s or a Protection Group Run details to recover all the VM&#39;s that are backed up by that Run. For recovering files, specifies the object contains the file to recover. | [optional] 
**recover_aurora_params** | [**RecoverAwsAuroraParams**](RecoverAwsAuroraParams.md) |  | [optional] 
**recover_file_and_folder_params** | [**RecoverAwsFileAndFolderParams**](RecoverAwsFileAndFolderParams.md) |  | [optional] 
**recover_rds_ingest_params** | [**RecoverRDSPostgresParams**](RecoverRDSPostgresParams.md) |  | [optional] 
**recover_rds_params** | [**RecoverAwsRdsParams**](RecoverAwsRdsParams.md) |  | [optional] 
**recover_s3_bucket_params** | [**RecoverAwsS3BucketParams**](RecoverAwsS3BucketParams.md) |  | [optional] 
**recover_vm_params** | [**RecoverAwsVmParams**](RecoverAwsVmParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


