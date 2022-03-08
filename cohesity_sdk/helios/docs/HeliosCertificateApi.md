# cohesity_sdk.HeliosCertificateApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_helios_ssl_certificate**](HeliosCertificateApi.md#get_helios_ssl_certificate) | **GET** /mcm/sslCertificate | Get the Helios SSL Certificate.


# **get_helios_ssl_certificate**
> SslCertificateParams get_helios_ssl_certificate()

Get the Helios SSL Certificate.

Get the Helios SSL certificate.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.ssl_certificate_params import SslCertificateParams
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the Helios SSL Certificate.
	api_response = client.helios_certificate.get_helios_ssl_certificate(region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosCertificateApi->get_helios_ssl_certificate: %s\n" % e)
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

