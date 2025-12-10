# AwsCredentials

Specifies the object to Aws related credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** | Specifies the type of authentication being used in the request. | [optional] 
**directory_dns_address** | **str** | Specifies the DNS address of the AWS managed active directory in which. Currently is set only for kerberos authentication. | [optional] 
**password** | **str** | Specifies the password to access target entity. | [optional] 
**realm_name** | **str** | Specifies the Kerberos realm name for a Kerberos-secured target. | [optional] 
**username** | **str** | Specifies the username to access target entity. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_credentials import AwsCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of AwsCredentials from a JSON string
aws_credentials_instance = AwsCredentials.from_json(json)
# print the JSON string representation of the object
print(AwsCredentials.to_json())

# convert the object into a dict
aws_credentials_dict = aws_credentials_instance.to_dict()
# create an instance of AwsCredentials from a dict
aws_credentials_from_dict = AwsCredentials.from_dict(aws_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


