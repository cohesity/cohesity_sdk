# OAuth2Provider

OAuth 2 provider

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audiences** | [**[OAuthAudience], none_type**](OAuthAudience.md) | Specifies the audiences of the configuration. This is used for validation. We will check this against the &#39;aud&#39; field sent in the JWT at authorization time and if they do not match against at least one of the elements in this list, then authentication will fail. We will also check the &#39;clientIds&#39; under the specified audience to make sure it matches the &#39;appid&#39; in the token. | 
**public_key_url** | **str, none_type** | Specifies the URL to poll for the public key. | 
**polling_frequency_mins** | **int, none_type** | Specifies the number of minutes the cluster should wait before polling for a new public key. Default value is 1440 (24 hours). | [optional]  if omitted the server will use the default value of 1440

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


