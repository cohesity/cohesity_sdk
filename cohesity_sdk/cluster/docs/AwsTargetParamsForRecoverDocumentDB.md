# AwsTargetParamsForRecoverDocumentDB

Specifies the parameters for an AWS DocumentDB recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_target_config** | [**AwsDocumentDBRecoveryTargetConfig**](AwsDocumentDBRecoveryTargetConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_target_params_for_recover_document_db import AwsTargetParamsForRecoverDocumentDB

# TODO update the JSON string below
json = "{}"
# create an instance of AwsTargetParamsForRecoverDocumentDB from a JSON string
aws_target_params_for_recover_document_db_instance = AwsTargetParamsForRecoverDocumentDB.from_json(json)
# print the JSON string representation of the object
print(AwsTargetParamsForRecoverDocumentDB.to_json())

# convert the object into a dict
aws_target_params_for_recover_document_db_dict = aws_target_params_for_recover_document_db_instance.to_dict()
# create an instance of AwsTargetParamsForRecoverDocumentDB from a dict
aws_target_params_for_recover_document_db_from_dict = AwsTargetParamsForRecoverDocumentDB.from_dict(aws_target_params_for_recover_document_db_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


