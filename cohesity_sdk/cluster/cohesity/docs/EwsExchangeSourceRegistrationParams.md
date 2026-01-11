# EwsExchangeSourceRegistrationParams

Specifies the parameters to register an EWS Exchange source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ews_endpoint** | **str, none_type** | Specifies the EWS endpoint of the Exchange server. | 
**service_account_credentials_list** | [**[Credentials]**](Credentials.md) | Specifies a list of service account credentials to be used to access the Exchange server. | 
**auth_method** | **str, none_type** | Specifies the authentication method. | [optional]  if omitted the server will use the default value of "kNtlm"
**use_proxy** | **bool, none_type** | Specifies whether to use the cluster proxy settings. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


