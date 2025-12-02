# AwsDocumentDBRecoveryTargetConfig

Specifies the target object parameters to recover AWS DocumentDB.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverAwsDocumentDBNewSourceConfig**](RecoverAwsDocumentDBNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 

## Example

```python
from cohesity_sdk.cluster.models.aws_document_db_recovery_target_config import AwsDocumentDBRecoveryTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AwsDocumentDBRecoveryTargetConfig from a JSON string
aws_document_db_recovery_target_config_instance = AwsDocumentDBRecoveryTargetConfig.from_json(json)
# print the JSON string representation of the object
print(AwsDocumentDBRecoveryTargetConfig.to_json())

# convert the object into a dict
aws_document_db_recovery_target_config_dict = aws_document_db_recovery_target_config_instance.to_dict()
# create an instance of AwsDocumentDBRecoveryTargetConfig from a dict
aws_document_db_recovery_target_config_from_dict = AwsDocumentDBRecoveryTargetConfig.from_dict(aws_document_db_recovery_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


