# CreateUserSessionRequestParams

Specifies user session request parameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str, none_type** | Specifies the certificate for cert based authentication. | [optional] 
**domain** | **str, none_type** | Specifies the domain the user is logging in to. For a local user the domain is LOCAL. For LDAP/AD user, the domain will map to a LDAP connection string. A user is uniquely identified by a combination of username and domain. LOCAL is the default domain. | [optional] 
**otp_code** | **str, none_type** | Specifies OTP code for MFA verification. | [optional] 
**otp_type** | **str, none_type** | Specifies OTP Type for MFA verification. | [optional] 
**password** | **str, none_type** | Specifies the password of the Cohesity user | [optional] 
**private_key** | **str, none_type** | Specifies the private key for cert based authentication. | [optional] 
**username** | **str, none_type** | Specifies the login name of the Cohesity user | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


