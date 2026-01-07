# CreateAccessTokenRequestParams

Specifies the Cohesity credentials required for creating an access token.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str, none_type** | Specifies the certificate for logging in the cert base auth cluster. | [optional] 
**domain** | **str, none_type** | Specifies the domain the user is logging in to. For a local user the domain is LOCAL. For LDAP/AD user, the domain will map to a LDAP connection string. A user is uniquely identified by a combination of username and domain. LOCAL is the default domain. | [optional] 
**mfa_params** | [**MfaParams**](MfaParams.md) |  | [optional] 
**password** | **str, none_type** | Specifies the password of the Cohesity user account. | [optional] 
**private_key** | **str, none_type** | Specifies the matching private key of the above certificate. | [optional] 
**username** | **str, none_type** | Specifies the login name of the Cohesity user. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


