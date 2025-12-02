# ServiceNowOAuth2Credentials

Specifies the credentials to register a ServiceNow source

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Specifies the Client ID for OAuth2 authentication. | 
**client_secret** | **str** | Specifies the Client Secret for OAuth2 authentication. | 

## Example

```python
from cohesity_sdk.cluster.models.service_now_o_auth2_credentials import ServiceNowOAuth2Credentials

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceNowOAuth2Credentials from a JSON string
service_now_o_auth2_credentials_instance = ServiceNowOAuth2Credentials.from_json(json)
# print the JSON string representation of the object
print(ServiceNowOAuth2Credentials.to_json())

# convert the object into a dict
service_now_o_auth2_credentials_dict = service_now_o_auth2_credentials_instance.to_dict()
# create an instance of ServiceNowOAuth2Credentials from a dict
service_now_o_auth2_credentials_from_dict = ServiceNowOAuth2Credentials.from_dict(service_now_o_auth2_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


