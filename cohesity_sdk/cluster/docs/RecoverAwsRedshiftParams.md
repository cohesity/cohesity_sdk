# RecoverAwsRedshiftParams

Specifies the parameters to recover Redshift.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_target_params** | [**AwsTargetParamsForRecoverRedshift**](AwsTargetParamsForRecoverRedshift.md) |  | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kAWS"
**snapshots** | [**[RecoverAwsRedshiftSnapshotParams], none_type**](RecoverAwsRedshiftSnapshotParams.md) | Specifies the details of the aws redshift objects to be recovered. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


