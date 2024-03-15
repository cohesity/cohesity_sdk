# SfdcSourceRegistrationParams

Specifies parameters to register an SFDC Protection Source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_token** | **str, none_type** | Specifies the token that will be used for fetching oAuth tokens from salesforce. | 
**concurrent_api_requests_limit** | **int, none_type** | Specifies the maximum number of concurrent API requests allowed for salesforce. | 
**consumer_key** | **str, none_type** | Specifies Consumer key from the connected app in SFDC. | 
**consumer_secret** | **str, none_type** | Specifies Consumer secret from the connected app in SFDC. | 
**daily_api_limit** | **int, none_type** | Specifies the maximum number of daily API requests allowed for salesforce. | 
**endpoint** | **str, none_type** | Specifies the SFDC endpoint URL. | 
**endpoint_type** | **str, none_type** | SFDC Endpoint type. | 
**callback_url** | **str, none_type** | Specifies the URL added in the connected apps Callback URL field. You can find this URL on the connected apps Manage Connected Apps page or from the connected apps definition. This value must be URL encoded. | [optional] 
**metadata_endpoint_url** | **str, none_type** | Specifies the url to access salesforce metadata requests. | [optional] [readonly] 
**password** | **str, none_type** | Specifies the password to access salesforce. | [optional] 
**soap_endpoint_url** | **str, none_type** | Specifies the url to access salesforce soap requests. | [optional] [readonly] 
**username** | **str, none_type** | Specifies the username to access salesforce. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


