# AwsKmsConfigurationResponse

AWS KMS configuration parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | AWS account access key id. Required when &#39;iamRoleArn&#39; is not given. | [optional] 
**cmk_alias** | **str** | AWS CMK alias. Only need one of cmkAlias, cmkArn, cmkKeyId to connect to AWS KMS. | [optional] 
**cmk_arn** | **str** | AWS CMK Amazon resource number. Only need one of cmkAlias, cmkArn, cmkKeyId to connect to AWS KMS. | [optional] 
**cmk_key_id** | **str** | AWS CMK key id. Only need one of cmkAlias, cmkArn, cmkKeyId to connect to AWS KMS. | [optional] 
**iam_role_arn** | **str** | The IAM role which will be used to authenticate with AWS KMS. Required when &#39;accessKeyId&#39; and &#39;secretAccessKey&#39; fields are not provided. | [optional] 
**region** | **str** | AWS region, e.g. us-east-1, us-west-2, for the AWS Glacier service to be used to authenticate resources within this region by the configured AWS account. | [optional] 
**verify_ssl** | **bool** | Enable SSL verification or not. | [optional] [default to True]

## Example

```python
from cohesity_sdk.helios.models.aws_kms_configuration_response import AwsKmsConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AwsKmsConfigurationResponse from a JSON string
aws_kms_configuration_response_instance = AwsKmsConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(AwsKmsConfigurationResponse.to_json())

# convert the object into a dict
aws_kms_configuration_response_dict = aws_kms_configuration_response_instance.to_dict()
# create an instance of AwsKmsConfigurationResponse from a dict
aws_kms_configuration_response_from_dict = AwsKmsConfigurationResponse.from_dict(aws_kms_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


