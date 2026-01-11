# cohesity_sdk.cluster.CohesityCAApi

All URIs are relative to *http://localhost/v2*

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
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import cohesity_ca
from cohesity_sdk.cluster.cohesity.model.exchange_ca_certificates_request import ExchangeCaCertificatesRequest
from cohesity_sdk.cluster.cohesity.model.exchange_ca_certificates_response import ExchangeCaCertificatesResponse
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_ca.CohesityCAApi(api_client)
    body = ExchangeCaCertificatesRequest(
        ca_certificates=[
            "ca_certificates_example",
        ],
        cluster_id=1,
    ) # ExchangeCaCertificatesRequest | Specifies the parameters to exchange ca certs

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.exchange_certificates(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
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

