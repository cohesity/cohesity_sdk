# CreateEmailOtpRequestBody

Specifies user session request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Specifies the domain the user is logging in to. For a local user the domain is LOCAL. For LDAP/AD user, the domain will map to a LDAP connection string. A user is uniquely identified by a combination of username and domain. LOCAL is the default domain.  | [optional] 
**password** | **str** | Specifies the password of the Cohesity user | [optional] 
**username** | **str** | Specifies the login name of the Cohesity user | [optional] 

## Example

```python
from cohesity_sdk.models.create_email_otp_request_body import CreateEmailOtpRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEmailOtpRequestBody from a JSON string
create_email_otp_request_body_instance = CreateEmailOtpRequestBody.from_json(json)
# print the JSON string representation of the object
print(CreateEmailOtpRequestBody.to_json())

# convert the object into a dict
create_email_otp_request_body_dict = create_email_otp_request_body_instance.to_dict()
# create an instance of CreateEmailOtpRequestBody from a dict
create_email_otp_request_body_from_dict = CreateEmailOtpRequestBody.from_dict(create_email_otp_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


