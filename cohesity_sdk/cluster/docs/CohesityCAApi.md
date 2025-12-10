# cohesity_sdk.cluster.CohesityCAApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchange_certificates**](CohesityCAApi.md#exchange_certificates) | **POST** /cert-manager/exchange-ca-certs | 


# **exchange_certificates**
> ExchangeCaCertificatesResponse exchange_certificates(body)



**Privileges:** ```CLUSTER_MODIFY``` <br><br>Exchange ca certificate/s between clusters

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.exchange_ca_certificates_request import ExchangeCaCertificatesRequest
from cohesity_sdk.cluster.models.exchange_ca_certificates_response import ExchangeCaCertificatesResponse
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.CohesityCAApi(api_client)
    body = cohesity_sdk.cluster.ExchangeCaCertificatesRequest() # ExchangeCaCertificatesRequest | Specifies the parameters to exchange ca certs

    try:
        api_response = api_instance.exchange_certificates(body)
        print("The response of CohesityCAApi->exchange_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CohesityCAApi->exchange_certificates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExchangeCaCertificatesRequest**](ExchangeCaCertificatesRequest.md)| Specifies the parameters to exchange ca certs | 

### Return type

[**ExchangeCaCertificatesResponse**](ExchangeCaCertificatesResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

