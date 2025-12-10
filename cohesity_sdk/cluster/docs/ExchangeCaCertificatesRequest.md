# ExchangeCaCertificatesRequest

Specifies the request of exchange ca certificate request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_certificates** | **List[str]** | Specifies ca cert in pem format | [optional] 
**cluster_id** | **int** | Specifies the cluster id. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.exchange_ca_certificates_request import ExchangeCaCertificatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeCaCertificatesRequest from a JSON string
exchange_ca_certificates_request_instance = ExchangeCaCertificatesRequest.from_json(json)
# print the JSON string representation of the object
print(ExchangeCaCertificatesRequest.to_json())

# convert the object into a dict
exchange_ca_certificates_request_dict = exchange_ca_certificates_request_instance.to_dict()
# create an instance of ExchangeCaCertificatesRequest from a dict
exchange_ca_certificates_request_from_dict = ExchangeCaCertificatesRequest.from_dict(exchange_ca_certificates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


