# RecoverRdsMsSQLParams

Specifies the parameters to recover AWS RDS MS SQL.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**[RecoverRdsMsSQLSnapshotParams], none_type**](RecoverRdsMsSQLSnapshotParams.md) | Specifies the details of the AWS RDS MS SQL objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kAWS"
**aws_target_params** | [**AwsTargetParamsForRecoverRdsMsSQL**](AwsTargetParamsForRecoverRdsMsSQL.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


