# IamRoleAwsCredentials

Specifies the credentials to register a commercial AWS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cp_iam_role_arn** | **str** | This is only applicable in case of DMaaS. Control plane IAM role ARN, this is first assumed by the dataplane(cluster). Then we assume the iam_role_arn which is tenant&#39;s IAM role with all required permissions. | [optional] 
**iam_role_arn** | **str** | Specifies the IAM role which will be used to access the security credentials required for API calls. This should have all the permissions required for the tenant&#39;s use case. In case of DMaaS this will be the Tenant&#39;s IAM role ARN. This is assumed only after the cp_iam_role_arn(control plane role) is assumed | 

## Example

```python
from cohesity_sdk.models.iam_role_aws_credentials import IamRoleAwsCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of IamRoleAwsCredentials from a JSON string
iam_role_aws_credentials_instance = IamRoleAwsCredentials.from_json(json)
# print the JSON string representation of the object
print(IamRoleAwsCredentials.to_json())

# convert the object into a dict
iam_role_aws_credentials_dict = iam_role_aws_credentials_instance.to_dict()
# create an instance of IamRoleAwsCredentials from a dict
iam_role_aws_credentials_from_dict = IamRoleAwsCredentials.from_dict(iam_role_aws_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


