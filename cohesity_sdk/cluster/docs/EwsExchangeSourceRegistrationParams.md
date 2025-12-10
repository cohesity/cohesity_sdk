# EwsExchangeSourceRegistrationParams

Specifies the parameters to register an EWS Exchange source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_method** | **str** | Specifies the authentication method. | [optional] [default to 'kNtlm']
**ews_endpoint** | **str** | Specifies the EWS endpoint of the Exchange server. | 
**service_account_credentials_list** | [**List[Credentials]**](Credentials.md) | Specifies a list of service account credentials to be used to access the Exchange server. | 
**use_proxy** | **bool** | Specifies whether to use the cluster proxy settings. | [optional] [default to False]

## Example

```python
from cohesity_sdk.cluster.models.ews_exchange_source_registration_params import EwsExchangeSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of EwsExchangeSourceRegistrationParams from a JSON string
ews_exchange_source_registration_params_instance = EwsExchangeSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(EwsExchangeSourceRegistrationParams.to_json())

# convert the object into a dict
ews_exchange_source_registration_params_dict = ews_exchange_source_registration_params_instance.to_dict()
# create an instance of EwsExchangeSourceRegistrationParams from a dict
ews_exchange_source_registration_params_from_dict = EwsExchangeSourceRegistrationParams.from_dict(ews_exchange_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


