# AwsKmsConfigurationResponse

AWS KMS configuration parameters.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str, none_type** | AWS account access key id. Required when &#39;iamRoleArn&#39; is not given. | [optional] 
**cmk_alias** | **str, none_type** | AWS CMK alias. Only need one of cmkAlias, cmkArn, cmkKeyId to connect to AWS KMS. | [optional] 
**cmk_arn** | **str, none_type** | AWS CMK Amazon resource number. Only need one of cmkAlias, cmkArn, cmkKeyId to connect to AWS KMS. | [optional] 
**cmk_key_id** | **str, none_type** | AWS CMK key id. Only need one of cmkAlias, cmkArn, cmkKeyId to connect to AWS KMS. | [optional] 
**iam_role_arn** | **str, none_type** | The IAM role which will be used to authenticate with AWS KMS. Required when &#39;accessKeyId&#39; and &#39;secretAccessKey&#39; fields are not provided. | [optional] 
**region** | **str, none_type** | AWS region, e.g. us-east-1, us-west-2, for the AWS Glacier service to be used to authenticate resources within this region by the configured AWS account. | [optional] 
**verify_ssl** | **bool, none_type** | Enable SSL verification or not. | [optional]  if omitted the server will use the default value of True

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


