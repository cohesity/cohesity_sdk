# SfdcSourceRegistrationParams

Specifies parameters to register an SFDC Protection Source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str, none_type** | Specifies the SFDC endpoint URL. | 
**endpoint_type** | **str, none_type** | SFDC Endpoint type. | 
**consumer_key** | **str, none_type** | Specifies Consumer key from the connected app in SFDC. | 
**consumer_secret** | **str, none_type** | Specifies Consumer secret from the connected app in SFDC. | 
**daily_api_limit** | **int, none_type** | Specifies the maximum number of daily API requests allowed for salesforce. | 
**concurrent_api_requests_limit** | **int, none_type** | Specifies the maximum number of concurrent API requests allowed for salesforce. | 
**auth_token** | **str, none_type** | Specifies the token that will be used for fetching oAuth tokens from salesforce. | 
**username** | **str, none_type** | Specifies the username to access salesforce. | [optional] 
**password** | **str, none_type** | Specifies the password to access salesforce. | [optional] 
**soap_endpoint_url** | **str, none_type** | Specifies the url to access salesforce soap requests. | [optional] [readonly] 
**metadata_endpoint_url** | **str, none_type** | Specifies the url to access salesforce metadata requests. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


