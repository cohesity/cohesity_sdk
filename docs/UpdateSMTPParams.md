# UpdateSMTPParams

Specifies the parameters to update cluster SMTP configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Specifies the IP address or the FQDN of the SMTP server. | 
**port** | **int** | Specifies the SMTP port. Usually 465 or 587. For authenticated connection, it is generally 587. | 
**username** | **str, none_type** | Specifies the username which will be used to connect to the SMTP server. If username is not specified, then it would imply that SMTP server is set up for unauthenticated access. | [optional] 
**use_ssl** | **bool, none_type** | This is set to true when the SMTP server uses SSL/TLS without supporting STARTTLS. Typically, this is used for port 465. | [optional]  if omitted the server will use the default value of False
**is_active** | **bool, none_type** | Specifies if the SMTP configuration is active. | [optional]  if omitted the server will use the default value of True
**password** | **str, none_type** | Specifies the password of the SMTP user. This is required if username is specified in the request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


