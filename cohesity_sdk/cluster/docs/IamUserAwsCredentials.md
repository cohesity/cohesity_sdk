# IamUserAwsCredentials

Specifies the credentials to register a commercial AWS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | Specifies Access key of the AWS account. | 
**arn** | **str** | Specifies Amazon Resource Name (owner ID) of the IAM user, acts as an unique identifier of as AWS entity. | 
**secret_access_key** | **str** | Specifies Secret Access key of the AWS account. | 

## Example

```python
from cohesity_sdk.cluster.models.iam_user_aws_credentials import IamUserAwsCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of IamUserAwsCredentials from a JSON string
iam_user_aws_credentials_instance = IamUserAwsCredentials.from_json(json)
# print the JSON string representation of the object
print(IamUserAwsCredentials.to_json())

# convert the object into a dict
iam_user_aws_credentials_dict = iam_user_aws_credentials_instance.to_dict()
# create an instance of IamUserAwsCredentials from a dict
iam_user_aws_credentials_from_dict = IamUserAwsCredentials.from_dict(iam_user_aws_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


