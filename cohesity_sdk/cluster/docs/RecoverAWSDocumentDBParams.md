# RecoverAWSDocumentDBParams

Specifies the parameters to recover AWS DocumentDB.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_target_params** | [**AwsTargetParamsForRecoverDocumentDB**](AwsTargetParamsForRecoverDocumentDB.md) |  | [optional] 
**snapshots** | [**List[RecoverAwsDocumentDBSnapshotParams]**](RecoverAwsDocumentDBSnapshotParams.md) | Specifies the details of the AWS DocumentDB objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_aws_document_db_params import RecoverAWSDocumentDBParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAWSDocumentDBParams from a JSON string
recover_aws_document_db_params_instance = RecoverAWSDocumentDBParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAWSDocumentDBParams.to_json())

# convert the object into a dict
recover_aws_document_db_params_dict = recover_aws_document_db_params_instance.to_dict()
# create an instance of RecoverAWSDocumentDBParams from a dict
recover_aws_document_db_params_from_dict = RecoverAWSDocumentDBParams.from_dict(recover_aws_document_db_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


