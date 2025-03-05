# AwsAuthenticationMethodsParams

Specifies the Authentication Methods parameters which are specific to AWS related External Targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_type** | **str** | Specifies the AWS External Target Authentication type. | 
**i_am_role_params** | [**AwsIAmRoleParams**](AwsIAmRoleParams.md) |  | [optional] 
**i_am_user_params** | [**AwsIAmUserParams**](AwsIAmUserParams.md) |  | [optional] 
**use_sts_params** | [**AwsUseSTSParams**](AwsUseSTSParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.aws_authentication_methods_params import AwsAuthenticationMethodsParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsAuthenticationMethodsParams from a JSON string
aws_authentication_methods_params_instance = AwsAuthenticationMethodsParams.from_json(json)
# print the JSON string representation of the object
print(AwsAuthenticationMethodsParams.to_json())

# convert the object into a dict
aws_authentication_methods_params_dict = aws_authentication_methods_params_instance.to_dict()
# create an instance of AwsAuthenticationMethodsParams from a dict
aws_authentication_methods_params_from_dict = AwsAuthenticationMethodsParams.from_dict(aws_authentication_methods_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


