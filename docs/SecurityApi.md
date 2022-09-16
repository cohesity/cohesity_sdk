# cohesity_sdk.SecurityApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_clientcsr**](SecurityApi.md#create_clientcsr) | **POST** /clientcsr | Create Certificate Signing Requests on the cluster.
[**create_csr**](SecurityApi.md#create_csr) | **POST** /csr | Create a Certificate Signing Request on the cluster.
[**delete_csr**](SecurityApi.md#delete_csr) | **DELETE** /csr/{id} | Delete a Certificate Signing Request on the cluster.
[**get_ciphers**](SecurityApi.md#get_ciphers) | **GET** /security/ciphers | Gets the list of ciphers enabled on the cluster.
[**get_csr_by_id**](SecurityApi.md#get_csr_by_id) | **GET** /csr/{id} | List the specified Certificate Signing Request.
[**get_csr_list**](SecurityApi.md#get_csr_list) | **GET** /csr | List Certificate Signing Requests on the cluster.
[**get_security_config**](SecurityApi.md#get_security_config) | **GET** /security-config | Get cluster security settings.
[**import_certificate_by_clientcsr**](SecurityApi.md#import_certificate_by_clientcsr) | **POST** /clientcsr/certificate | Import the signed certificates on the cluster after the Certificate Signing Requests are created.
[**list_trusted_ca_by_id**](SecurityApi.md#list_trusted_ca_by_id) | **GET** /trusted-cas/{id} | List the specified Certificate.
[**list_trusted_cas**](SecurityApi.md#list_trusted_cas) | **GET** /trusted-cas | List all Certificates with cluster trust store.
[**modify_ciphers**](SecurityApi.md#modify_ciphers) | **POST** /security/ciphers | Enable/Disable a list of ciphers on the cluster. Iris must be restarted for the change to take effect.
[**register_trusted_cas**](SecurityApi.md#register_trusted_cas) | **POST** /trusted-cas | Register CA Certificate to the cluster trust store.
[**unregister_trusted_ca**](SecurityApi.md#unregister_trusted_ca) | **DELETE** /trusted-cas/{id} | Unregister CA Certificate from the cluster trust store.
[**update_certificate_by_csr**](SecurityApi.md#update_certificate_by_csr) | **POST** /csr/certificate | Update the signed certificate on the cluster after a Certificate Signing Request is created.
[**update_security_config**](SecurityApi.md#update_security_config) | **PUT** /security-config | Update cluster security settings.
[**validate_trusted_ca_by_id**](SecurityApi.md#validate_trusted_ca_by_id) | **POST** /trusted-cas/{id}/validate | Validate CA Certificate.


# **create_clientcsr**
> CreateClientcsrResponseBody create_clientcsr(body)

Create Certificate Signing Requests on the cluster.

Create two Certificate Signing Request on the cluster with the given details one each for client and server. Each service can have at most one outstanding pair of CSR.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.create_clientcsr_response_body import CreateClientcsrResponseBody
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.create_csr_request import CreateCsrRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateCsrRequest() # CreateCsrRequest | Specifies the parameters to create the Certificate Signing Requests.

# example passing only required values which don't have defaults set
try:
	# Create Certificate Signing Requests on the cluster.
	api_response = client.security.create_clientcsr(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->create_clientcsr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCsrRequest**](CreateCsrRequest.md)| Specifies the parameters to create the Certificate Signing Requests. |

### Return type

[**CreateClientcsrResponseBody**](CreateClientcsrResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_csr**
> CreateCsrResponseBody create_csr(body)

Create a Certificate Signing Request on the cluster.

Create a Certificate Signing Request on the cluster with the given details. Each service has at most one outstanding CSR.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.create_csr_response_body import CreateCsrResponseBody
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.create_csr_request import CreateCsrRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateCsrRequest() # CreateCsrRequest | Specifies the parameters to create a Certificate Signing Request.

# example passing only required values which don't have defaults set
try:
	# Create a Certificate Signing Request on the cluster.
	api_response = client.security.create_csr(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->create_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCsrRequest**](CreateCsrRequest.md)| Specifies the parameters to create a Certificate Signing Request. |

### Return type

[**CreateCsrResponseBody**](CreateCsrResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_csr**
> delete_csr(id)

Delete a Certificate Signing Request on the cluster.

Delete a Certificate Signing Request on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "id_example" # str | Specifies the id of the csr to be deleted.

# example passing only required values which don't have defaults set
try:
	# Delete a Certificate Signing Request on the cluster.
	client.security.delete_csr(id)
except ApiException as e:
	print("Exception when calling SecurityApi->delete_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the csr to be deleted. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ciphers**
> CiphersResp get_ciphers()

Gets the list of ciphers enabled on the cluster.

Gets the list of ciphers enabled on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.ciphers_resp import CiphersResp
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Gets the list of ciphers enabled on the cluster.
	api_response = client.security.get_ciphers()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->get_ciphers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CiphersResp**](CiphersResp.md)

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

# **get_csr_by_id**
> CommonCsrResponseParams get_csr_by_id(id)

List the specified Certificate Signing Request.

List the specified Certificate Signing Request.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.common_csr_response_params import CommonCsrResponseParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "id_example" # str | Specifies the id of the csr.

# example passing only required values which don't have defaults set
try:
	# List the specified Certificate Signing Request.
	api_response = client.security.get_csr_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->get_csr_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the csr. |

### Return type

[**CommonCsrResponseParams**](CommonCsrResponseParams.md)

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

# **get_csr_list**
> GetCsrListResponseBody get_csr_list()

List Certificate Signing Requests on the cluster.

List Certificate Signing Requests on the cluster with service name filtering.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.get_csr_list_response_body import GetCsrListResponseBody
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


service_name = "iris" # str | Specifies the Cohesity service name for which the CSR is generated. If this is not specified, all the csrs on the cluster will be returned. (optional) if omitted the server will use the default value of "iris"
ids = [
        "ids_example",
    ] # [str] | Specifies the ids of the csrs. If this is not specified, all the csrs on the cluster will be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List Certificate Signing Requests on the cluster.
	api_response = client.[class Tag {
    name: Security
    description: null
    externalDocs: null
}].get_csr_list(service_name=service_name, ids=ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->get_csr_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| Specifies the Cohesity service name for which the CSR is generated. If this is not specified, all the csrs on the cluster will be returned. | [optional] if omitted the server will use the default value of "iris"
 **ids** | **[str]**| Specifies the ids of the csrs. If this is not specified, all the csrs on the cluster will be returned. | [optional]

### Return type

[**GetCsrListResponseBody**](GetCsrListResponseBody.md)

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

# **get_security_config**
> SecurityConfigResponse get_security_config()

Get cluster security settings.

Get cluster security settings.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.security_config_response import SecurityConfigResponse
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get cluster security settings.
	api_response = client.security.get_security_config()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->get_security_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SecurityConfigResponse**](SecurityConfigResponse.md)

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

# **import_certificate_by_clientcsr**
> ImportCertificateByClientcsrResponseBody import_certificate_by_clientcsr(body)

Import the signed certificates on the cluster after the Certificate Signing Requests are created.

Import the signed certificates on the cluster after the Certificate Signing Requests are created.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.import_certificate_by_clientcsr_response_body import ImportCertificateByClientcsrResponseBody
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.import_certificate_by_clientcsr_request import ImportCertificateByClientcsrRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ImportCertificateByClientcsrRequest(
        certificate_server="certificate_server_example",
        certificate_client="certificate_client_example",
    ) # ImportCertificateByClientcsrRequest | Specifies the parameters to import the certificate.

# example passing only required values which don't have defaults set
try:
	# Import the signed certificates on the cluster after the Certificate Signing Requests are created.
	api_response = client.security.import_certificate_by_clientcsr(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->import_certificate_by_clientcsr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImportCertificateByClientcsrRequest**](ImportCertificateByClientcsrRequest.md)| Specifies the parameters to import the certificate. |

### Return type

[**ImportCertificateByClientcsrResponseBody**](ImportCertificateByClientcsrResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_trusted_ca_by_id**
> TrustedCa list_trusted_ca_by_id(id)

List the specified Certificate.

List the specified Certificate.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.trusted_ca import TrustedCa
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "id_example" # str | Specifies the id of the certificate.

# example passing only required values which don't have defaults set
try:
	# List the specified Certificate.
	api_response = client.security.list_trusted_ca_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->list_trusted_ca_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the certificate. |

### Return type

[**TrustedCa**](TrustedCa.md)

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

# **list_trusted_cas**
> ListTrustedCasResult list_trusted_cas()

List all Certificates with cluster trust store.

List all trusted certificates in cluster trust store.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.list_trusted_cas_result import ListTrustedCasResult
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


ids = [
        "ids_example",
    ] # [str] | Specifies the ids of the certificates to be returned. (optional)
names = [
        "names_example",
    ] # [str] | Specifies the names of the certificates to be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List all Certificates with cluster trust store.
	api_response = client.[class Tag {
    name: Security
    description: null
    externalDocs: null
}].list_trusted_cas(ids=ids, names=names)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->list_trusted_cas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[str]**| Specifies the ids of the certificates to be returned. | [optional]
 **names** | **[str]**| Specifies the names of the certificates to be returned. | [optional]

### Return type

[**ListTrustedCasResult**](ListTrustedCasResult.md)

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

# **modify_ciphers**
> CiphersResp modify_ciphers(body)

Enable/Disable a list of ciphers on the cluster. Iris must be restarted for the change to take effect.

Enable/Disable a list of ciphers on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.ciphers_resp import CiphersResp
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.modify_ciphers_request_body import ModifyCiphersRequestBody
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ModifyCiphersRequestBody(
        enable=True,
        ciphers=[
            "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
        ],
    ) # ModifyCiphersRequestBody | Enable/Disable ciphers.

# example passing only required values which don't have defaults set
try:
	# Enable/Disable a list of ciphers on the cluster. Iris must be restarted for the change to take effect.
	api_response = client.security.modify_ciphers(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->modify_ciphers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyCiphersRequestBody**](ModifyCiphersRequestBody.md)| Enable/Disable ciphers. |

### Return type

[**CiphersResp**](CiphersResp.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_trusted_cas**
> ListTrustedCasResult register_trusted_cas(body)

Register CA Certificate to the cluster trust store.

Register CA Certificate to the cluster trust store.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.register_trusted_cas import RegisterTrustedCas
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.list_trusted_cas_result import ListTrustedCasResult
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = RegisterTrustedCas(
        certificates=[
            TrustedCaRequest(
                certificate="certificate_example",
                name="name_example",
                description="description_example",
            ),
        ],
        only_validate=True,
    ) # RegisterTrustedCas | Specifies the parameters to register a Certificate.

# example passing only required values which don't have defaults set
try:
	# Register CA Certificate to the cluster trust store.
	api_response = client.security.register_trusted_cas(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->register_trusted_cas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterTrustedCas**](RegisterTrustedCas.md)| Specifies the parameters to register a Certificate. |

### Return type

[**ListTrustedCasResult**](ListTrustedCasResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_trusted_ca**
> unregister_trusted_ca(id)

Unregister CA Certificate from the cluster trust store.

Unregister CA Certificate from the cluster trust store.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "id_example" # str | Specifies the id of the certificate to be unregistered.

# example passing only required values which don't have defaults set
try:
	# Unregister CA Certificate from the cluster trust store.
	client.security.unregister_trusted_ca(id)
except ApiException as e:
	print("Exception when calling SecurityApi->unregister_trusted_ca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the certificate to be unregistered. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_certificate_by_csr**
> UpdateCertificateByCsrResponseBody update_certificate_by_csr(body)

Update the signed certificate on the cluster after a Certificate Signing Request is created.

Update the signed certificate on the cluster after a Certificate Signing Request is created.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.update_certificate_by_csr_request import UpdateCertificateByCsrRequest
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.update_certificate_by_csr_response_body import UpdateCertificateByCsrResponseBody
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = UpdateCertificateByCsrRequest(
        certificate="certificate_example",
        csr_id="csr_id_example",
    ) # UpdateCertificateByCsrRequest | Specifies the parameters to update the certificate.

# example passing only required values which don't have defaults set
try:
	# Update the signed certificate on the cluster after a Certificate Signing Request is created.
	api_response = client.security.update_certificate_by_csr(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->update_certificate_by_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCertificateByCsrRequest**](UpdateCertificateByCsrRequest.md)| Specifies the parameters to update the certificate. |

### Return type

[**UpdateCertificateByCsrResponseBody**](UpdateCertificateByCsrResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_security_config**
> SecurityConfigResponse update_security_config(body)

Update cluster security settings.

Update cluster security settings.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.update_security_config_request import UpdateSecurityConfigRequest
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.security_config_response import SecurityConfigResponse
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = UpdateSecurityConfigRequest() # UpdateSecurityConfigRequest | Specifies the parameters to update security config.

# example passing only required values which don't have defaults set
try:
	# Update cluster security settings.
	api_response = client.security.update_security_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->update_security_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSecurityConfigRequest**](UpdateSecurityConfigRequest.md)| Specifies the parameters to update security config. |

### Return type

[**SecurityConfigResponse**](SecurityConfigResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_trusted_ca_by_id**
> TrustedCa validate_trusted_ca_by_id(id)

Validate CA Certificate.

Certificate will be checked for Expiration and Revocation.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.trusted_ca import TrustedCa
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "id_example" # str | Specifies the id of the certificate to be validated.

# example passing only required values which don't have defaults set
try:
	# Validate CA Certificate.
	api_response = client.security.validate_trusted_ca_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SecurityApi->validate_trusted_ca_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the certificate to be validated. |

### Return type

[**TrustedCa**](TrustedCa.md)

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

