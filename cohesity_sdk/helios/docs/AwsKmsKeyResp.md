# AwsKmsKeyResp

Response about one KMS key provisioned in AWS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_role_json** | **str** | Fortknox AWS role associated with the KMS key. | [optional] 
**kms_key_arn** | **str** | ARN of the KMS key. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.aws_kms_key_resp import AwsKmsKeyResp

# TODO update the JSON string below
json = "{}"
# create an instance of AwsKmsKeyResp from a JSON string
aws_kms_key_resp_instance = AwsKmsKeyResp.from_json(json)
# print the JSON string representation of the object
print(AwsKmsKeyResp.to_json())

# convert the object into a dict
aws_kms_key_resp_dict = aws_kms_key_resp_instance.to_dict()
# create an instance of AwsKmsKeyResp from a dict
aws_kms_key_resp_from_dict = AwsKmsKeyResp.from_dict(aws_kms_key_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


