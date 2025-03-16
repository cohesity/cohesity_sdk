# cohesity_sdk.helios.CertificateApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_helios_ssl_certificate**](CertificateApi.md#get_helios_ssl_certificate) | **GET** /mcm/ssl-certificate | Get the Helios SSL Certificate.


# **get_helios_ssl_certificate**
> SslCertificateParams get_helios_ssl_certificate(region_id=region_id)

Get the Helios SSL Certificate.

Get the Helios SSL certificate.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.ssl_certificate_params import SslCertificateParams
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.CertificateApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get the Helios SSL Certificate.
        api_response = api_instance.get_helios_ssl_certificate(region_id=region_id)
        print("The response of CertificateApi->get_helios_ssl_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateApi->get_helios_ssl_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**SslCertificateParams**](SslCertificateParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

