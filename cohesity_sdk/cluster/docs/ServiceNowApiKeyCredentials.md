# ServiceNowApiKeyCredentials

Specifies the credentials to register a ServiceNow source

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | Specifies the Access Key for API key authentication. | 

## Example

```python
from cohesity_sdk.cluster.models.service_now_api_key_credentials import ServiceNowApiKeyCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceNowApiKeyCredentials from a JSON string
service_now_api_key_credentials_instance = ServiceNowApiKeyCredentials.from_json(json)
# print the JSON string representation of the object
print(ServiceNowApiKeyCredentials.to_json())

# convert the object into a dict
service_now_api_key_credentials_dict = service_now_api_key_credentials_instance.to_dict()
# create an instance of ServiceNowApiKeyCredentials from a dict
service_now_api_key_credentials_from_dict = ServiceNowApiKeyCredentials.from_dict(service_now_api_key_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


