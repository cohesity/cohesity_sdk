# IamRoleAwsCredentials

Specifies the credentials to register a commercial AWS

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iam_role_arn** | **str, none_type** | Specifies the IAM role which will be used to access the security credentials required for API calls. This should have all the permissions required for the tenant&#39;s use case. In case of DMaaS this will be the Tenant&#39;s IAM role ARN. This is assumed only after the cp_iam_role_arn(control plane role) is assumed | 
**cp_iam_role_arn** | **str, none_type** | This is only applicable in case of DMaaS. Control plane IAM role ARN, this is first assumed by the dataplane(cluster). Then we assume the iam_role_arn which is tenant&#39;s IAM role with all required permissions. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


