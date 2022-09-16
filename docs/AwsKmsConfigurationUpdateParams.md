# AwsKmsConfigurationUpdateParams

AWS KMS configuration updatable parameters.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_certificate** | **str, none_type** | Specify the ca certificate. | [optional] 
**secret_access_key** | **str, none_type** | AWS account secret access key. Required when &#39;iamRoleArn&#39; is not given. | [optional] 
**access_key_id** | **str, none_type** | AWS account access key id. Required when &#39;iamRoleArn&#39; is not given. | [optional] 
**iam_role_arn** | **str, none_type** | The IAM role which will be used to authenticate with AWS KMS. Required when &#39;accessKeyId&#39; and &#39;secretAccessKey&#39; fields are not provided. | [optional] 
**verify_ssl** | **bool, none_type** | Enable SSL verification or not. | [optional]  if omitted the server will use the default value of True

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


