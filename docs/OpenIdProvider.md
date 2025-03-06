# OpenIdProvider

Open ID provider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience_ids** | **List[str]** | Specifies the audience IDs of the configuration. This is used for validation. We will check this against the &#39;aud&#39; field sent in the JWT at authorization time and if they do not match against at least one of the elements in this list, then authentication will fail. | 
**polling_frequency_mins** | **int** | Specifies the number of minutes the cluster should wait before polling for a new public key. Default value is 1440 (24 hours). | [optional] [default to 1440]
**public_key_url** | **str** | Specifies the URL to poll for the public key. | 

## Example

```python
from cohesity_sdk.cluster.models.open_id_provider import OpenIdProvider

# TODO update the JSON string below
json = "{}"
# create an instance of OpenIdProvider from a JSON string
open_id_provider_instance = OpenIdProvider.from_json(json)
# print the JSON string representation of the object
print(OpenIdProvider.to_json())

# convert the object into a dict
open_id_provider_dict = open_id_provider_instance.to_dict()
# create an instance of OpenIdProvider from a dict
open_id_provider_from_dict = OpenIdProvider.from_dict(open_id_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


