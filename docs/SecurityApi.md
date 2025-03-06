# cohesity_sdk.cluster.SecurityApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_clientcsr**](SecurityApi.md#create_clientcsr) | **POST** /client-csr | Create Certificate Signing Requests on the cluster.
[**create_csr**](SecurityApi.md#create_csr) | **POST** /csr | Create a Certificate Signing Request on the cluster.
[**delete_csr**](SecurityApi.md#delete_csr) | **DELETE** /csr/{id} | Delete a Certificate Signing Request on the cluster.
[**get_ciphers**](SecurityApi.md#get_ciphers) | **GET** /security/ciphers | Gets the list of ciphers enabled on the cluster.
[**get_csr_by_id**](SecurityApi.md#get_csr_by_id) | **GET** /csr/{id} | List the specified Certificate Signing Request.
[**get_csr_list**](SecurityApi.md#get_csr_list) | **GET** /csr | List Certificate Signing Requests on the cluster.
[**get_object_store_ciphers**](SecurityApi.md#get_object_store_ciphers) | **GET** /security/object-store-ciphers | Gets the list of object store ciphers enabled on the cluster.
[**get_security_config**](SecurityApi.md#get_security_config) | **GET** /security-config | Get cluster security settings.
[**import_certificate_by_clientcsr**](SecurityApi.md#import_certificate_by_clientcsr) | **POST** /client-csr/certificate | Import the signed certificates on the cluster after the Certificate Signing Requests are created.
[**list_trusted_ca_by_id**](SecurityApi.md#list_trusted_ca_by_id) | **GET** /trusted-cas/{id} | List the specified Certificate.
[**list_trusted_cas**](SecurityApi.md#list_trusted_cas) | **GET** /trusted-cas | List all Certificates with cluster trust store.
[**modify_ciphers**](SecurityApi.md#modify_ciphers) | **POST** /security/ciphers | Enable/Disable a list of ciphers on the cluster. Iris must be restarted for the change to take effect.
[**modify_object_store_ciphers**](SecurityApi.md#modify_object_store_ciphers) | **POST** /security/object-store-ciphers | Enable/Disable a list of object store ciphers on the cluster. Bridge must be restarted for the change to take effect.
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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.common_csr_request_params import CommonCsrRequestParams
from cohesity_sdk.cluster.models.create_clientcsr_response_body import CreateClientcsrResponseBody
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.SecurityApi(api_client)
    body = cohesity_sdk.cluster.CommonCsrRequestParams() # CommonCsrRequestParams | Specifies the parameters to create the Certificate Signing Requests.

    try:
        # Create Certificate Signing Requests on the cluster.
        api_response = api_instance.create_clientcsr(body)
        print("The response of SecurityApi->create_clientcsr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->create_clientcsr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **CommonCsrRequestParams**| Specifies the parameters to create the Certificate Signing Requests. | 

### Return type

[**CreateClientcsrResponseBody**](CreateClientcsrResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
> CommonCsrResponseParams create_csr(body)

Create a Certificate Signing Request on the cluster.

Create a Certificate Signing Request on the cluster with the given details. Each service has at most one outstanding CSR.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.common_csr_request_params import CommonCsrRequestParams
from cohesity_sdk.cluster.models.common_csr_response_params import CommonCsrResponseParams
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.SecurityApi(api_client)
    body = cohesity_sdk.cluster.CommonCsrRequestParams() # CommonCsrRequestParams | Specifies the parameters to create a Certificate Signing Request.

    try:
        # Create a Certificate Signing Request on the cluster.
        api_response = api_instance.create_csr(body)
        print("The response of SecurityApi->create_csr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->create_csr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **CommonCsrRequestParams**| Specifies the parameters to create a Certificate Signing Request. | 

### Return type

[**CommonCsrResponseParams**](CommonCsrResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.SecurityApi(api_client)
    id = 'id_example' # str | Specifies the id of the csr to be deleted.

    try:
        # Delete a Certificate Signing Request on the cluster.
        api_instance.delete_csr(id)
    except Exception as e:
        print("Exception when calling SecurityApi->delete_csr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the csr to be deleted. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.ciphers_resp import CiphersResp
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.SecurityApi(api_client)

    try:
        # Gets the list of ciphers enabled on the cluster.
        api_response = api_instance.get_ciphers()
        print("The response of SecurityApi->get_ciphers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->get_ciphers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CiphersResp**](CiphersResp.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.common_csr_response_params import CommonCsrResponseParams
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.SecurityApi(api_client)
    id = 'id_example' # str | Specifies the id of the csr.

    try:
        # List the specified Certificate Signing Request.
        api_response = api_instance.get_csr_by_id(id)
        print("The response of SecurityApi->get_csr_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->get_csr_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the csr. | 

### Return type

[**CommonCsrResponseParams**](CommonCsrResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
> List[CommonCsrResponseParams] get_csr_list(service_name=service_name, ids=ids)

List Certificate Signing Requests on the cluster.

List Certificate Signing Requests on the cluster with service name filtering.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.common_csr_response_params import CommonCsrResponseParams
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.SecurityApi(api_client)
    service_name = 'service_name_example' # str | Specifies the Cohesity service name for which the CSR is generated. If this is not specified, all the csrs on the cluster will be returned. (optional)
    ids = ['ids_example'] # List[str] | Specifies the ids of the csrs. If this is not specified, all the csrs on the cluster will be returned. (optional)

    try:
        # List Certificate Signing Requests on the cluster.
        api_response = api_instance.get_csr_list(service_name=service_name, ids=ids)
        print("The response of SecurityApi->get_csr_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->get_csr_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| Specifies the Cohesity service name for which the CSR is generated. If this is not specified, all the csrs on the cluster will be returned. | [optional] 
 **ids** | [**List[str]**](str.md)| Specifies the ids of the csrs. If this is not specified, all the csrs on the cluster will be returned. | [optional] 

### Return type

[**List[CommonCsrResponseParams]**](CommonCsrResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_store_ciphers**
> ObjectStoreCiphersResp get_object_store_ciphers()

Gets the list of object store ciphers enabled on the cluster.

Gets the list of object store ciphers enabled on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.object_store_ciphers_resp import ObjectStoreCiphersResp
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.SecurityApi(api_client)

    try:
        # Gets the list of object store ciphers enabled on the cluster.
        api_response = api_instance.get_object_store_ciphers()
        print("The response of SecurityApi->get_object_store_ciphers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->get_object_store_ciphers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ObjectStoreCiphersResp**](ObjectStoreCiphersResp.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
> SecurityConfig get_security_config()

Get cluster security settings.

Get cluster security settings.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.security_config import SecurityConfig
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.SecurityApi(api_client)

    try:
        # Get cluster security settings.
        api_response = api_instance.get_security_config()
        print("The response of SecurityApi->get_security_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->get_security_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SecurityConfig**](SecurityConfig.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.import_certificate_by_clientcsr_request import ImportCertificateByClientcsrRequest
from cohesity_sdk.cluster.models.import_certificate_by_clientcsr_response_body import ImportCertificateByClientcsrResponseBody
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.SecurityApi(api_client)
    body = cohesity_sdk.cluster.ImportCertificateByClientcsrRequest() # ImportCertificateByClientcsrRequest | Specifies the parameters to import the certificate.

    try:
        # Import the signed certificates on the cluster after the Certificate Signing Requests are created.
        api_response = api_instance.import_certificate_by_clientcsr(body)
        print("The response of SecurityApi->import_certificate_by_clientcsr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->import_certificate_by_clientcsr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImportCertificateByClientcsrRequest**](ImportCertificateByClientcsrRequest.md)| Specifies the parameters to import the certificate. | 

### Return type

[**ImportCertificateByClientcsrResponseBody**](ImportCertificateByClientcsrResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.trusted_ca import TrustedCa
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.SecurityApi(api_client)
    id = 'id_example' # str | Specifies the id of the certificate.

    try:
        # List the specified Certificate.
        api_response = api_instance.list_trusted_ca_by_id(id)
        print("The response of SecurityApi->list_trusted_ca_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->list_trusted_ca_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the certificate. | 

### Return type

[**TrustedCa**](TrustedCa.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
> ListTrustedCasResult list_trusted_cas(ids=ids, names=names)

List all Certificates with cluster trust store.

List all trusted certificates in cluster trust store.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.list_trusted_cas_result import ListTrustedCasResult
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.SecurityApi(api_client)
    ids = ['ids_example'] # List[str] | Specifies the ids of the certificates to be returned. (optional)
    names = ['names_example'] # List[str] | Specifies the names of the certificates to be returned. (optional)

    try:
        # List all Certificates with cluster trust store.
        api_response = api_instance.list_trusted_cas(ids=ids, names=names)
        print("The response of SecurityApi->list_trusted_cas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->list_trusted_cas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[str]**](str.md)| Specifies the ids of the certificates to be returned. | [optional] 
 **names** | [**List[str]**](str.md)| Specifies the names of the certificates to be returned. | [optional] 

### Return type

[**ListTrustedCasResult**](ListTrustedCasResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.ciphers_resp import CiphersResp
from cohesity_sdk.cluster.models.modify_ciphers_request_body import ModifyCiphersRequestBody
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.SecurityApi(api_client)
    body = cohesity_sdk.cluster.ModifyCiphersRequestBody() # ModifyCiphersRequestBody | Enable/Disable ciphers.

    try:
        # Enable/Disable a list of ciphers on the cluster. Iris must be restarted for the change to take effect.
        api_response = api_instance.modify_ciphers(body)
        print("The response of SecurityApi->modify_ciphers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->modify_ciphers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyCiphersRequestBody**](ModifyCiphersRequestBody.md)| Enable/Disable ciphers. | 

### Return type

[**CiphersResp**](CiphersResp.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_object_store_ciphers**
> ObjectStoreCiphersResp modify_object_store_ciphers(body)

Enable/Disable a list of object store ciphers on the cluster. Bridge must be restarted for the change to take effect.

Enable/Disable a list of object store ciphers on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.modify_object_store_ciphers_request_body import ModifyObjectStoreCiphersRequestBody
from cohesity_sdk.cluster.models.object_store_ciphers_resp import ObjectStoreCiphersResp
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.SecurityApi(api_client)
    body = cohesity_sdk.cluster.ModifyObjectStoreCiphersRequestBody() # ModifyObjectStoreCiphersRequestBody | Enable/Disable object store ciphers.

    try:
        # Enable/Disable a list of object store ciphers on the cluster. Bridge must be restarted for the change to take effect.
        api_response = api_instance.modify_object_store_ciphers(body)
        print("The response of SecurityApi->modify_object_store_ciphers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->modify_object_store_ciphers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyObjectStoreCiphersRequestBody**](ModifyObjectStoreCiphersRequestBody.md)| Enable/Disable object store ciphers. | 

### Return type

[**ObjectStoreCiphersResp**](ObjectStoreCiphersResp.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.list_trusted_cas_result import ListTrustedCasResult
from cohesity_sdk.cluster.models.register_trusted_cas import RegisterTrustedCas
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.SecurityApi(api_client)
    body = cohesity_sdk.cluster.RegisterTrustedCas() # RegisterTrustedCas | Specifies the parameters to register a Certificate.

    try:
        # Register CA Certificate to the cluster trust store.
        api_response = api_instance.register_trusted_cas(body)
        print("The response of SecurityApi->register_trusted_cas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->register_trusted_cas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterTrustedCas**](RegisterTrustedCas.md)| Specifies the parameters to register a Certificate. | 

### Return type

[**ListTrustedCasResult**](ListTrustedCasResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.SecurityApi(api_client)
    id = 'id_example' # str | Specifies the id of the certificate to be unregistered.

    try:
        # Unregister CA Certificate from the cluster trust store.
        api_instance.unregister_trusted_ca(id)
    except Exception as e:
        print("Exception when calling SecurityApi->unregister_trusted_ca: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the certificate to be unregistered. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.update_certificate_by_csr_request import UpdateCertificateByCsrRequest
from cohesity_sdk.cluster.models.update_certificate_by_csr_response_body import UpdateCertificateByCsrResponseBody
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.SecurityApi(api_client)
    body = cohesity_sdk.cluster.UpdateCertificateByCsrRequest() # UpdateCertificateByCsrRequest | Specifies the parameters to update the certificate.

    try:
        # Update the signed certificate on the cluster after a Certificate Signing Request is created.
        api_response = api_instance.update_certificate_by_csr(body)
        print("The response of SecurityApi->update_certificate_by_csr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->update_certificate_by_csr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCertificateByCsrRequest**](UpdateCertificateByCsrRequest.md)| Specifies the parameters to update the certificate. | 

### Return type

[**UpdateCertificateByCsrResponseBody**](UpdateCertificateByCsrResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
> SecurityConfig update_security_config(body)

Update cluster security settings.

Update cluster security settings.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.security_config import SecurityConfig
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.SecurityApi(api_client)
    body = cohesity_sdk.cluster.SecurityConfig() # SecurityConfig | Specifies the parameters to update security config.

    try:
        # Update cluster security settings.
        api_response = api_instance.update_security_config(body)
        print("The response of SecurityApi->update_security_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->update_security_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **SecurityConfig**| Specifies the parameters to update security config. | 

### Return type

[**SecurityConfig**](SecurityConfig.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.trusted_ca import TrustedCa
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.SecurityApi(api_client)
    id = 'id_example' # str | Specifies the id of the certificate to be validated.

    try:
        # Validate CA Certificate.
        api_response = api_instance.validate_trusted_ca_by_id(id)
        print("The response of SecurityApi->validate_trusted_ca_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->validate_trusted_ca_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the certificate to be validated. | 

### Return type

[**TrustedCa**](TrustedCa.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

