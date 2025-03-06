# OAuth2Provider

OAuth 2 provider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audiences** | [**List[OAuthAudience]**](OAuthAudience.md) | Specifies the audiences of the configuration. This is used for validation. We will check this against the &#39;aud&#39; field sent in the JWT at authorization time and if they do not match against at least one of the elements in this list, then authentication will fail. We will also check the &#39;clientIds&#39; under the specified audience to make sure it matches the &#39;appid&#39; in the token. | 
**polling_frequency_mins** | **int** | Specifies the number of minutes the cluster should wait before polling for a new public key. Default value is 1440 (24 hours). | [optional] [default to 1440]
**public_key_url** | **str** | Specifies the URL to poll for the public key. | 

## Example

```python
from cohesity_sdk.cluster.models.o_auth2_provider import OAuth2Provider

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2Provider from a JSON string
o_auth2_provider_instance = OAuth2Provider.from_json(json)
# print the JSON string representation of the object
print(OAuth2Provider.to_json())

# convert the object into a dict
o_auth2_provider_dict = o_auth2_provider_instance.to_dict()
# create an instance of OAuth2Provider from a dict
o_auth2_provider_from_dict = OAuth2Provider.from_dict(o_auth2_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


