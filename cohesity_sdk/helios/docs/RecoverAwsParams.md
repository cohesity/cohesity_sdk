# RecoverAwsParams

Specifies the recovery options specific to AWS environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_file_and_folder_params** | [**CommonDownloadFileAndFolderParams**](CommonDownloadFileAndFolderParams.md) | Specifies the parameters to download files and folders. | [optional] 
**objects** | [**List[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. This property is mandatory for all recovery action types except recover vms. While recovering VMs, a user can specify snapshots of VM&#39;s or a Protection Group Run details to recover all the VM&#39;s that are backed up by that Run. For recovering files, specifies the object contains the file to recover. | [optional] 
**recover_aurora_params** | [**RecoverAwsAuroraParams**](RecoverAwsAuroraParams.md) | Specifies the parameters to recover AWS Aurora. | [optional] 
**recover_file_and_folder_params** | [**RecoverAwsFileAndFolderParams**](RecoverAwsFileAndFolderParams.md) | Specifies the parameters to recover files and folders. | [optional] 
**recover_rds_ingest_params** | [**RecoverRDSPostgresParams**](RecoverRDSPostgresParams.md) | Specifies the parameters to recover AWS RDS Ingest. | [optional] 
**recover_rds_params** | [**RecoverAwsRdsParams**](RecoverAwsRdsParams.md) | Specifies the parameters to recover AWS RDS. | [optional] 
**recover_s3_bucket_params** | [**RecoverAwsS3BucketParams**](RecoverAwsS3BucketParams.md) | Specifies the parameters to recover AWS S3 Buckets. | [optional] 
**recover_vm_params** | [**RecoverAwsVmParams**](RecoverAwsVmParams.md) | Specifies the parameters to recover AWS VM. | [optional] 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.helios.models.recover_aws_params import RecoverAwsParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsParams from a JSON string
recover_aws_params_instance = RecoverAwsParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsParams.to_json())

# convert the object into a dict
recover_aws_params_dict = recover_aws_params_instance.to_dict()
# create an instance of RecoverAwsParams from a dict
recover_aws_params_from_dict = RecoverAwsParams.from_dict(recover_aws_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


