# ExchangeCaCertificatesResponse

Specifies the response of exchange ca certificate request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_certificates** | **List[str]** | Specifies ca cert in pem format | [optional] 
**cluster_id** | **int** | Specifies the cluster id. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.exchange_ca_certificates_response import ExchangeCaCertificatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeCaCertificatesResponse from a JSON string
exchange_ca_certificates_response_instance = ExchangeCaCertificatesResponse.from_json(json)
# print the JSON string representation of the object
print(ExchangeCaCertificatesResponse.to_json())

# convert the object into a dict
exchange_ca_certificates_response_dict = exchange_ca_certificates_response_instance.to_dict()
# create an instance of ExchangeCaCertificatesResponse from a dict
exchange_ca_certificates_response_from_dict = ExchangeCaCertificatesResponse.from_dict(exchange_ca_certificates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


