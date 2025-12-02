# cohesity_sdk.CertificatesApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_web_server_certificate**](CertificatesApi.md#get_web_server_certificate) | **GET** /webserver-certificate | Get the Server Certificate configured on the Cluster.


# **get_web_server_certificate**
> SslCertificate get_web_server_certificate()

Get the Server Certificate configured on the Cluster.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Returns the Server Certificate configured on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.ssl_certificate import SslCertificate
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get the Server Certificate configured on the Cluster.
	api_response = client.certificates.get_web_server_certificate()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling CertificatesApi->get_web_server_certificate: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SslCertificate**](SslCertificate.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

