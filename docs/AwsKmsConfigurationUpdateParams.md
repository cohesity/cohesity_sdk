# AwsKmsConfigurationUpdateParams

AWS KMS configuration updatable parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | AWS account access key id. Required when &#39;iamRoleArn&#39; is not given. | [optional] 
**ca_certificate** | **str** | Specify the ca certificate. | [optional] 
**iam_role_arn** | **str** | The IAM role which will be used to authenticate with AWS KMS. Required when &#39;accessKeyId&#39; and &#39;secretAccessKey&#39; fields are not provided. | [optional] 
**secret_access_key** | **str** | AWS account secret access key. Required when &#39;iamRoleArn&#39; is not given. | [optional] 
**verify_ssl** | **bool** | Enable SSL verification or not. | [optional] [default to True]

## Example

```python
from cohesity_sdk.cluster.models.aws_kms_configuration_update_params import AwsKmsConfigurationUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsKmsConfigurationUpdateParams from a JSON string
aws_kms_configuration_update_params_instance = AwsKmsConfigurationUpdateParams.from_json(json)
# print the JSON string representation of the object
print(AwsKmsConfigurationUpdateParams.to_json())

# convert the object into a dict
aws_kms_configuration_update_params_dict = aws_kms_configuration_update_params_instance.to_dict()
# create an instance of AwsKmsConfigurationUpdateParams from a dict
aws_kms_configuration_update_params_from_dict = AwsKmsConfigurationUpdateParams.from_dict(aws_kms_configuration_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


