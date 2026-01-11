# RecoverAWSDocumentDBParams

Specifies the parameters to recover AWS DocumentDB.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**[RecoverAwsDocumentDBSnapshotParams], none_type**](RecoverAwsDocumentDBSnapshotParams.md) | Specifies the details of the AWS DocumentDB objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kAWS"
**aws_target_params** | [**AwsTargetParamsForRecoverDocumentDB**](AwsTargetParamsForRecoverDocumentDB.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


