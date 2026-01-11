# cohesity_sdk.cluster.SecurityApi

All URIs are relative to *http://localhost/v2*

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
[**get_ssl_certificates**](SecurityApi.md#get_ssl_certificates) | **GET** /ssl-certificates | Get list of SSL certificates.
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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Create two Certificate Signing Request on the cluster with the given details one each for client and server. Each service can have at most one outstanding pair of CSR.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import security
from cohesity_sdk.cluster.cohesity.model.create_clientcsr_response_body import CreateClientcsrResponseBody
from cohesity_sdk.cluster.cohesity.model.common_csr_request_params import CommonCsrRequestParams
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
    api_instance = security.SecurityApi(api_client)
    body = CommonCsrRequestParams(
        city="city_example",
        common_name="common_name_example",
        country_code="country_code_example",
        dns_names=[
            "dns_names_example",
        ],
        email_address="email_address_example",
        host_ips=[
            "host_ips_example",
        ],
        key_size_bits=1,
        key_type="rsa",
        organization="organization_example",
        organization_unit="organization_unit_example",
        service_name="iris",
        state="state_example",
    ) # CommonCsrRequestParams | Specifies the parameters to create the Certificate Signing Requests.

    # example passing only required values which don't have defaults set
    try:
        # Create Certificate Signing Requests on the cluster.
        api_response = api_instance.create_clientcsr(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SecurityApi->create_clientcsr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommonCsrRequestParams**](CommonCsrRequestParams.md)| Specifies the parameters to create the Certificate Signing Requests. |

### Return type

[**CreateClientcsrResponseBody**](CreateClientcsrResponseBody.md)

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

# **create_csr**
> CommonCsrResponseParams create_csr(body)

Create a Certificate Signing Request on the cluster.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Create a Certificate Signing Request on the cluster with the given details. Each service has at most one outstanding CSR.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import security
from cohesity_sdk.cluster.cohesity.model.common_csr_request_params import CommonCsrRequestParams
from cohesity_sdk.cluster.cohesity.model.common_csr_response_params import CommonCsrResponseParams
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
    api_instance = security.SecurityApi(api_client)
    body = CommonCsrRequestParams(
        city="city_example",
        common_name="common_name_example",
        country_code="country_code_example",
        dns_names=[
            "dns_names_example",
        ],
        email_address="email_address_example",
        host_ips=[
            "host_ips_example",
        ],
        key_size_bits=1,
        key_type="rsa",
        organization="organization_example",
        organization_unit="organization_unit_example",
        service_name="iris",
        state="state_example",
    ) # CommonCsrRequestParams | Specifies the parameters to create a Certificate Signing Request.

    # example passing only required values which don't have defaults set
    try:
        # Create a Certificate Signing Request on the cluster.
        api_response = api_instance.create_csr(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SecurityApi->create_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommonCsrRequestParams**](CommonCsrRequestParams.md)| Specifies the parameters to create a Certificate Signing Request. |

### Return type

[**CommonCsrResponseParams**](CommonCsrResponseParams.md)

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

# **delete_csr**
> delete_csr(id)

Delete a Certificate Signing Request on the cluster.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Delete a Certificate Signing Request on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import security
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
    api_instance = security.SecurityApi(api_client)
    id = "id_example" # str | Specifies the id of the csr to be deleted.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Certificate Signing Request on the cluster.
        api_instance.delete_csr(id)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SecurityApi->delete_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the csr to be deleted. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Gets the list of ciphers enabled on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import security
from cohesity_sdk.cluster.cohesity.model.ciphers_resp import CiphersResp
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
    api_instance = security.SecurityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Gets the list of ciphers enabled on the cluster.
        api_response = api_instance.get_ciphers()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SecurityApi->get_ciphers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CiphersResp**](CiphersResp.md)

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

# **get_csr_by_id**
> CommonCsrResponseParams get_csr_by_id(id)

List the specified Certificate Signing Request.

**Privileges:** ```CLUSTER_VIEW``` <br><br>List the specified Certificate Signing Request.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import security
from cohesity_sdk.cluster.cohesity.model.common_csr_response_params import CommonCsrResponseParams
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
    api_instance = security.SecurityApi(api_client)
    id = "id_example" # str | Specifies the id of the csr.

    # example passing only required values which don't have defaults set
    try:
        # List the specified Certificate Signing Request.
        api_response = api_instance.get_csr_by_id(id)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SecurityApi->get_csr_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the csr. |

### Return type

[**CommonCsrResponseParams**](CommonCsrResponseParams.md)

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

# **get_csr_list**
> GetCsrListResponseBody get_csr_list()

List Certificate Signing Requests on the cluster.

**Privileges:** ```CLUSTER_VIEW``` <br><br>List Certificate Signing Requests on the cluster with service name filtering.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import security
from cohesity_sdk.cluster.cohesity.model.get_csr_list_response_body import GetCsrListResponseBody
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
    api_instance = security.SecurityApi(api_client)
    service_name = "iris" # str | Specifies the Cohesity service name for which the CSR is generated. If this is not specified, all the csrs on the cluster will be returned. (optional)
    ids = [
        "ids_example",
    ] # [str] | Specifies the ids of the csrs. If this is not specified, all the csrs on the cluster will be returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Certificate Signing Requests on the cluster.
        api_response = api_instance.get_csr_list(service_name=service_name, ids=ids)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SecurityApi->get_csr_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| Specifies the Cohesity service name for which the CSR is generated. If this is not specified, all the csrs on the cluster will be returned. | [optional]
 **ids** | **[str]**| Specifies the ids of the csrs. If this is not specified, all the csrs on the cluster will be returned. | [optional]

### Return type

[**GetCsrListResponseBody**](GetCsrListResponseBody.md)

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

# **get_object_store_ciphers**
> ObjectStoreCiphersResp get_object_store_ciphers()

Gets the list of object store ciphers enabled on the cluster.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Gets the list of object store ciphers enabled on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import security
from cohesity_sdk.cluster.cohesity.model.object_store_ciphers_resp import ObjectStoreCiphersResp
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
    api_instance = security.SecurityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Gets the list of object store ciphers enabled on the cluster.
        api_response = api_instance.get_object_store_ciphers()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SecurityApi->get_object_store_ciphers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ObjectStoreCiphersResp**](ObjectStoreCiphersResp.md)

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

# **get_security_config**
> SecurityConfigResponse get_security_config()

Get cluster security settings.

**Privileges:** ```SECURITY_ADVISOR_VIEW, TENANT_VIEW``` <br><br>Get cluster security settings.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import security
from cohesity_sdk.cluster.cohesity.model.security_config_response import SecurityConfigResponse
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
    api_instance = security.SecurityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get cluster security settings.
        api_response = api_instance.get_security_config()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SecurityApi->get_security_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SecurityConfigResponse**](SecurityConfigResponse.md)

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

# **get_ssl_certificates**
> GetSslCertificatesResult get_ssl_certificates()

Get list of SSL certificates.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get list of SSL certificates.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import security
from cohesity_sdk.cluster.cohesity.model.get_ssl_certificates_result import GetSslCertificatesResult
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
    api_instance = security.SecurityApi(api_client)
    service_name = "iris" # str | Specifies the service name for which the certificate details needs to be returned. If this is not specified, all certificates are returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get list of SSL certificates.
        api_response = api_instance.get_ssl_certificates(service_name=service_name)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SecurityApi->get_ssl_certificates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| Specifies the service name for which the certificate details needs to be returned. If this is not specified, all certificates are returned. | [optional]

### Return type

[**GetSslCertificatesResult**](GetSslCertificatesResult.md)

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

# **import_certificate_by_clientcsr**
> ImportCertificateByClientcsrResponseBody import_certificate_by_clientcsr(body)

Import the signed certificates on the cluster after the Certificate Signing Requests are created.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Import the signed certificates on the cluster after the Certificate Signing Requests are created.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import security
from cohesity_sdk.cluster.cohesity.model.import_certificate_by_clientcsr_request import ImportCertificateByClientcsrRequest
from cohesity_sdk.cluster.cohesity.model.import_certificate_by_clientcsr_response_body import ImportCertificateByClientcsrResponseBody
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
    api_instance = security.SecurityApi(api_client)
    body = ImportCertificateByClientcsrRequest(
        certificate_client="certificate_client_example",
        certificate_server="certificate_server_example",
    ) # ImportCertificateByClientcsrRequest | Specifies the parameters to import the certificate.

    # example passing only required values which don't have defaults set
    try:
        # Import the signed certificates on the cluster after the Certificate Signing Requests are created.
        api_response = api_instance.import_certificate_by_clientcsr(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SecurityApi->import_certificate_by_clientcsr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImportCertificateByClientcsrRequest**](ImportCertificateByClientcsrRequest.md)| Specifies the parameters to import the certificate. |

### Return type

[**ImportCertificateByClientcsrResponseBody**](ImportCertificateByClientcsrResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>List the specified Certificate.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import security
from cohesity_sdk.cluster.cohesity.model.trusted_ca import TrustedCa
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
    api_instance = security.SecurityApi(api_client)
    id = "id_example" # str | Specifies the id of the certificate.

    # example passing only required values which don't have defaults set
    try:
        # List the specified Certificate.
        api_response = api_instance.list_trusted_ca_by_id(id)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SecurityApi->list_trusted_ca_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the certificate. |

### Return type

[**TrustedCa**](TrustedCa.md)

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

# **list_trusted_cas**
> ListTrustedCasResult list_trusted_cas()

List all Certificates with cluster trust store.

**Privileges:** ```CLUSTER_VIEW``` <br><br>List all trusted certificates in cluster trust store.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import security
from cohesity_sdk.cluster.cohesity.model.list_trusted_cas_result import ListTrustedCasResult
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
    api_instance = security.SecurityApi(api_client)
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
        api_response = api_instance.list_trusted_cas(ids=ids, names=names)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
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

# **modify_ciphers**
> CiphersResp modify_ciphers(body)

Enable/Disable a list of ciphers on the cluster. Iris must be restarted for the change to take effect.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Enable/Disable a list of ciphers on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import security
from cohesity_sdk.cluster.cohesity.model.modify_ciphers_request_body import ModifyCiphersRequestBody
from cohesity_sdk.cluster.cohesity.model.ciphers_resp import CiphersResp
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
    api_instance = security.SecurityApi(api_client)
    body = ModifyCiphersRequestBody(
        ciphers=[
            "TLS_AES_256_GCM_SHA384",
        ],
        enable=True,
    ) # ModifyCiphersRequestBody | Enable/Disable ciphers.

    # example passing only required values which don't have defaults set
    try:
        # Enable/Disable a list of ciphers on the cluster. Iris must be restarted for the change to take effect.
        api_response = api_instance.modify_ciphers(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SecurityApi->modify_ciphers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyCiphersRequestBody**](ModifyCiphersRequestBody.md)| Enable/Disable ciphers. |

### Return type

[**CiphersResp**](CiphersResp.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Enable/Disable a list of object store ciphers on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import security
from cohesity_sdk.cluster.cohesity.model.object_store_ciphers_resp import ObjectStoreCiphersResp
from cohesity_sdk.cluster.cohesity.model.modify_object_store_ciphers_request_body import ModifyObjectStoreCiphersRequestBody
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
    api_instance = security.SecurityApi(api_client)
    body = ModifyObjectStoreCiphersRequestBody(
        ciphers=[
            "TLS_AES_256_GCM_SHA384",
        ],
        enable=True,
    ) # ModifyObjectStoreCiphersRequestBody | Enable/Disable object store ciphers.

    # example passing only required values which don't have defaults set
    try:
        # Enable/Disable a list of object store ciphers on the cluster. Bridge must be restarted for the change to take effect.
        api_response = api_instance.modify_object_store_ciphers(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SecurityApi->modify_object_store_ciphers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyObjectStoreCiphersRequestBody**](ModifyObjectStoreCiphersRequestBody.md)| Enable/Disable object store ciphers. |

### Return type

[**ObjectStoreCiphersResp**](ObjectStoreCiphersResp.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Register CA Certificate to the cluster trust store.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import security
from cohesity_sdk.cluster.cohesity.model.list_trusted_cas_result import ListTrustedCasResult
from cohesity_sdk.cluster.cohesity.model.register_trusted_cas import RegisterTrustedCas
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
    api_instance = security.SecurityApi(api_client)
    body = RegisterTrustedCas(
        certificates=[
            TrustedCaRequest(
                certificate="certificate_example",
                description="description_example",
                name="name_example",
            ),
        ],
        only_validate=True,
    ) # RegisterTrustedCas | Specifies the parameters to register a Certificate.

    # example passing only required values which don't have defaults set
    try:
        # Register CA Certificate to the cluster trust store.
        api_response = api_instance.register_trusted_cas(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SecurityApi->register_trusted_cas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterTrustedCas**](RegisterTrustedCas.md)| Specifies the parameters to register a Certificate. |

### Return type

[**ListTrustedCasResult**](ListTrustedCasResult.md)

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

# **unregister_trusted_ca**
> unregister_trusted_ca(id)

Unregister CA Certificate from the cluster trust store.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Unregister CA Certificate from the cluster trust store.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import security
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
    api_instance = security.SecurityApi(api_client)
    id = "id_example" # str | Specifies the id of the certificate to be unregistered.

    # example passing only required values which don't have defaults set
    try:
        # Unregister CA Certificate from the cluster trust store.
        api_instance.unregister_trusted_ca(id)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SecurityApi->unregister_trusted_ca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the certificate to be unregistered. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update the signed certificate on the cluster after a Certificate Signing Request is created.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import security
from cohesity_sdk.cluster.cohesity.model.update_certificate_by_csr_response_body import UpdateCertificateByCsrResponseBody
from cohesity_sdk.cluster.cohesity.model.update_certificate_by_csr_request import UpdateCertificateByCsrRequest
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
    api_instance = security.SecurityApi(api_client)
    body = UpdateCertificateByCsrRequest(
        certificate="certificate_example",
        csr_id="csr_id_example",
    ) # UpdateCertificateByCsrRequest | Specifies the parameters to update the certificate.

    # example passing only required values which don't have defaults set
    try:
        # Update the signed certificate on the cluster after a Certificate Signing Request is created.
        api_response = api_instance.update_certificate_by_csr(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SecurityApi->update_certificate_by_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCertificateByCsrRequest**](UpdateCertificateByCsrRequest.md)| Specifies the parameters to update the certificate. |

### Return type

[**UpdateCertificateByCsrResponseBody**](UpdateCertificateByCsrResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```SECURITY_ADVISOR_MODIFY``` <br><br>Update cluster security settings.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import security
from cohesity_sdk.cluster.cohesity.model.security_config import SecurityConfig
from cohesity_sdk.cluster.cohesity.model.security_config_response import SecurityConfigResponse
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
    api_instance = security.SecurityApi(api_client)
    body = SecurityConfig(
        account_lockout=SecurityConfigAccountLockout(
            failed_login_lock_time_duration_mins=1,
            inactivity_time_days=1,
            max_failed_login_attempts=1,
        ),
        auth_token_timeout_minutes=1,
        certificate_based_auth=SecurityConfigCertificateBasedAuth(
            ad_mapping="SamAccountName",
            certificate_mapping="CommonName",
            enable_mapping_based_authentication=True,
        ),
        data_classification=SecurityConfigDataClassification(
            classified_data_message="classified_data_message_example",
            is_data_classified=True,
            unclassified_data_message="unclassified_data_message_example",
        ),
        inactivity_timeout_m_secs=1,
        password_lifetime=SecurityConfigPasswordLifetime(
            max_lifetime_days=1,
            min_lifetime_days=0,
        ),
        password_reuse=SecurityConfigPasswordReuse(
            num_different_chars=0,
            num_disallowed_old_passwords=0,
        ),
        password_strength=SecurityConfigPasswordStrength(
            include_lower_letter=True,
            include_number=True,
            include_special_char=True,
            include_upper_letter=True,
            min_length=0,
        ),
        session_configuration=SecurityConfigSessionConfiguration(
            absolute_timeout=1,
            inactivity_timeout=1,
            limit_sessions=True,
            session_limit_per_user=1,
            session_limit_system_wide=1,
        ),
        ssh_configuration=SecurityConfigSshConfiguration(
            ssh_timeout_in_mins=1,
        ),
    ) # SecurityConfig | Specifies the parameters to update security config.

    # example passing only required values which don't have defaults set
    try:
        # Update cluster security settings.
        api_response = api_instance.update_security_config(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SecurityApi->update_security_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecurityConfig**](SecurityConfig.md)| Specifies the parameters to update security config. |

### Return type

[**SecurityConfigResponse**](SecurityConfigResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Certificate will be checked for Expiration and Revocation.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import security
from cohesity_sdk.cluster.cohesity.model.trusted_ca import TrustedCa
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
    api_instance = security.SecurityApi(api_client)
    id = "id_example" # str | Specifies the id of the certificate to be validated.

    # example passing only required values which don't have defaults set
    try:
        # Validate CA Certificate.
        api_response = api_instance.validate_trusted_ca_by_id(id)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SecurityApi->validate_trusted_ca_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the certificate to be validated. |

### Return type

[**TrustedCa**](TrustedCa.md)

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

