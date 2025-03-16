# CreateUserSessionRequestParams

Specifies user session request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | Specifies the certificate for cert based authentication. | [optional] 
**domain** | **str** | Specifies the domain the user is logging in to. For a local user the domain is LOCAL. For LDAP/AD user, the domain will map to a LDAP connection string. A user is uniquely identified by a combination of username and domain. LOCAL is the default domain. | [optional] 
**otp_code** | **str** | Specifies OTP code for MFA verification. | [optional] 
**otp_type** | **str** | Specifies OTP Type for MFA verification. | [optional] 
**password** | **str** | Specifies the password of the Cohesity user | [optional] 
**private_key** | **str** | Specifies the private key for cert based authentication. | [optional] 
**username** | **str** | Specifies the login name of the Cohesity user | [optional] 

## Example

```python
from cohesity_sdk.helios.models.create_user_session_request_params import CreateUserSessionRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserSessionRequestParams from a JSON string
create_user_session_request_params_instance = CreateUserSessionRequestParams.from_json(json)
# print the JSON string representation of the object
print(CreateUserSessionRequestParams.to_json())

# convert the object into a dict
create_user_session_request_params_dict = create_user_session_request_params_instance.to_dict()
# create an instance of CreateUserSessionRequestParams from a dict
create_user_session_request_params_from_dict = CreateUserSessionRequestParams.from_dict(create_user_session_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


