# cohesity_sdk.CohesityCAApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**exchange_certificates**](CohesityCAApi.md#exchange_certificates) | **POST** /cert-manager/exchange-ca-certs | 


# **exchange_certificates**
> ExchangeCaCertificatesResponse exchange_certificates(body)



**Privileges:** ```CLUSTER_MODIFY``` <br><br>Exchange ca certificate/s between clusters

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.exchange_ca_certificates_response import ExchangeCaCertificatesResponse
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.exchange_ca_certificates_request import ExchangeCaCertificatesRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ExchangeCaCertificatesRequest(
        ca_certificates=[
            "ca_certificates_example",
        ],
        cluster_id=1,
    ) # ExchangeCaCertificatesRequest | Specifies the parameters to exchange ca certs

# example passing only required values which don't have defaults set
try:
	api_response = client.cohesity_ca.exchange_certificates(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling CohesityCAApi->exchange_certificates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExchangeCaCertificatesRequest**](ExchangeCaCertificatesRequest.md)| Specifies the parameters to exchange ca certs |

### Return type

[**ExchangeCaCertificatesResponse**](ExchangeCaCertificatesResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

