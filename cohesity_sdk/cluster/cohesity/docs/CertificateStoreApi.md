# cohesity_sdk.cluster.CertificateStoreApi

All URIs are relative to *http://localhost/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_store_certificate**](CertificateStoreApi.md#add_store_certificate) | **POST** /secret-manager/certificates | 
[**delete_store_certificate**](CertificateStoreApi.md#delete_store_certificate) | **DELETE** /secret-manager/certificates/{thumbprint} | 
[**generate_new_store_certificate**](CertificateStoreApi.md#generate_new_store_certificate) | **POST** /secret-manager/cert/{environment} | 
[**get_env_store_certificate**](CertificateStoreApi.md#get_env_store_certificate) | **GET** /secret-manager/cert/{environment}/{thumbprint} | 
[**get_env_store_certificates**](CertificateStoreApi.md#get_env_store_certificates) | **GET** /secret-manager/cert/{environment} | 
[**get_store_certificate**](CertificateStoreApi.md#get_store_certificate) | **GET** /secret-manager/certificates/{thumbprint} | 
[**get_store_certificates**](CertificateStoreApi.md#get_store_certificates) | **GET** /secret-manager/certificates | 
[**update_store_certificate_metadata**](CertificateStoreApi.md#update_store_certificate_metadata) | **PATCH** /secret-manager/certificates/{thumbprint} | 


# **add_store_certificate**
> CertificateObjectWithMetadata add_store_certificate(body)



**Privileges:** ```SECRET_MANAGER_CERT_MODIFY``` <br><br>Adds a certificate to certificate store based on the given action type query-params.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import certificate_store
from cohesity_sdk.cluster.cohesity.model.certificate_object_with_metadata import CertificateObjectWithMetadata
from cohesity_sdk.cluster.cohesity.model.add_certificate_request import AddCertificateRequest
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
    api_instance = certificate_store.CertificateStoreApi(api_client)
    body = AddCertificateRequest(
        action="Import",
        certificate_generate_params=GenerateNewStoreCertificateRequest(),
        certificate_import_params=ImportCertBundleRequest(),
        environment="microsoft365",
    ) # AddCertificateRequest | Specifies the parameters to import/generate certificate and add it to certificate store.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_store_certificate(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling CertificateStoreApi->add_store_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddCertificateRequest**](AddCertificateRequest.md)| Specifies the parameters to import/generate certificate and add it to certificate store. |

### Return type

[**CertificateObjectWithMetadata**](CertificateObjectWithMetadata.md)

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

# **delete_store_certificate**
> delete_store_certificate(thumbprint)



**Privileges:** ```SECRET_MANAGER_CERT_MODIFY``` <br><br>Deletes the certificate corresponding to the thumbprint.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import certificate_store
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
    api_instance = certificate_store.CertificateStoreApi(api_client)
    thumbprint = "thumbprint_example" # str | Specifies the thumbprint of the certificate to be deleted.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_store_certificate(thumbprint)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling CertificateStoreApi->delete_store_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thumbprint** | **str**| Specifies the thumbprint of the certificate to be deleted. |

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

# **generate_new_store_certificate**
> CertificateObjectWithMetadata generate_new_store_certificate(body)



**Privileges:** ```SECRET_MANAGER_CERT_MODIFY``` <br><br>Generate and store a certificate signed by Cohesity CA to be used for any evironment's workflow. The metadata of the certificate generated will be returned.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import certificate_store
from cohesity_sdk.cluster.cohesity.model.certificate_object_with_metadata import CertificateObjectWithMetadata
from cohesity_sdk.cluster.cohesity.model.generate_new_store_certificate_request import GenerateNewStoreCertificateRequest
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
    api_instance = certificate_store.CertificateStoreApi(api_client)
    body = GenerateNewStoreCertificateRequest() # GenerateNewStoreCertificateRequest | Specifies the parameters to generate a certificate.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_new_store_certificate(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling CertificateStoreApi->generate_new_store_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateNewStoreCertificateRequest**](GenerateNewStoreCertificateRequest.md)| Specifies the parameters to generate a certificate. |
 **environment** | **str**| Specifies the environment for which certificates are to be generated. | defaults to "microsoft365"

### Return type

[**CertificateObjectWithMetadata**](CertificateObjectWithMetadata.md)

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

# **get_env_store_certificate**
> CertificateObjectWithMetadata get_env_store_certificate(thumbprint)



**Privileges:** ```SECRET_MANAGER_CERT_VIEW``` <br><br>Returns certificate corresponding to the thumbprint.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import certificate_store
from cohesity_sdk.cluster.cohesity.model.certificate_object_with_metadata import CertificateObjectWithMetadata
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
    api_instance = certificate_store.CertificateStoreApi(api_client)
    thumbprint = "thumbprint_example" # str | Specifies the thumbprint of the certificate to be fetched.
    certificate_view = "metadataOnly" # str | Specifies which components of the certificate are to be returned. (optional) if omitted the server will use the default value of "metadataOnly"
    format = "PFX" # str | Specifies the format in which certificate data should be returned (e.g., PEM, PFX). Currently PFX format will be used. (optional) if omitted the server will use the default value of "PFX"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_env_store_certificate(thumbprint)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling CertificateStoreApi->get_env_store_certificate: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_env_store_certificate(thumbprint, certificate_view=certificate_view, format=format)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling CertificateStoreApi->get_env_store_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thumbprint** | **str**| Specifies the thumbprint of the certificate to be fetched. |
 **environment** | **str**| Specifies the environment for which certificate is to be fetched. | defaults to "microsoft365"
 **certificate_view** | **str**| Specifies which components of the certificate are to be returned. | [optional] if omitted the server will use the default value of "metadataOnly"
 **format** | **str**| Specifies the format in which certificate data should be returned (e.g., PEM, PFX). Currently PFX format will be used. | [optional] if omitted the server will use the default value of "PFX"

### Return type

[**CertificateObjectWithMetadata**](CertificateObjectWithMetadata.md)

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

# **get_env_store_certificates**
> CertificateStoreListResponse get_env_store_certificates()



**Privileges:** ```SECRET_MANAGER_CERT_VIEW``` <br><br>Returns all the certificates associated with an environment such as Office365 for a particular tenant. For each certificate, only the metadata such as certificate thumbprint, display name etc. will be returned.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import certificate_store
from cohesity_sdk.cluster.cohesity.model.certificate_store_list_response import CertificateStoreListResponse
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
    api_instance = certificate_store.CertificateStoreApi(api_client)
    generated_by = "External" # str | Specifies whether certificates generated by a specific entity are to be returned. Currently certificates can only be cohesity generated or customer generated. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_env_store_certificates()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling CertificateStoreApi->get_env_store_certificates: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_env_store_certificates(generated_by=generated_by)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling CertificateStoreApi->get_env_store_certificates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Specifies the environment for which certificates are to be fetched. | defaults to "microsoft365"
 **generated_by** | **str**| Specifies whether certificates generated by a specific entity are to be returned. Currently certificates can only be cohesity generated or customer generated. | [optional]

### Return type

[**CertificateStoreListResponse**](CertificateStoreListResponse.md)

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

# **get_store_certificate**
> CertificateObjectWithMetadata get_store_certificate(thumbprint)



**Privileges:** ```SECRET_MANAGER_CERT_VIEW``` <br><br>Returns certificate corresponding to the thumbprint.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import certificate_store
from cohesity_sdk.cluster.cohesity.model.certificate_object_with_metadata import CertificateObjectWithMetadata
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
    api_instance = certificate_store.CertificateStoreApi(api_client)
    thumbprint = "thumbprint_example" # str | Specifies the thumbprint of the certificate to be fetched.
    environment = "microsoft365" # str, none_type | Specifies the certificate store environment type. Based on this environment type, corresponding certificate store will be used. (optional) if omitted the server will use the default value of "microsoft365"
    certificate_view = "metadataOnly" # str | Specifies which components of the certificate are to be returned. (optional) if omitted the server will use the default value of "metadataOnly"
    format = "PFX" # str | Specifies the format in which certificate data should be returned (e.g., PEM, PFX). Currently PFX format will be used. (optional) if omitted the server will use the default value of "PFX"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_store_certificate(thumbprint)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling CertificateStoreApi->get_store_certificate: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_store_certificate(thumbprint, environment=environment, certificate_view=certificate_view, format=format)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling CertificateStoreApi->get_store_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thumbprint** | **str**| Specifies the thumbprint of the certificate to be fetched. |
 **environment** | **str, none_type**| Specifies the certificate store environment type. Based on this environment type, corresponding certificate store will be used. | [optional] if omitted the server will use the default value of "microsoft365"
 **certificate_view** | **str**| Specifies which components of the certificate are to be returned. | [optional] if omitted the server will use the default value of "metadataOnly"
 **format** | **str**| Specifies the format in which certificate data should be returned (e.g., PEM, PFX). Currently PFX format will be used. | [optional] if omitted the server will use the default value of "PFX"

### Return type

[**CertificateObjectWithMetadata**](CertificateObjectWithMetadata.md)

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

# **get_store_certificates**
> CertificateStoreListResponse get_store_certificates()



**Privileges:** ```SECRET_MANAGER_CERT_VIEW``` <br><br>Returns all the certificates associated with a particular tenant. For each certificate, only the metadata such as certificate thumbprint, display name etc. will be returned.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import certificate_store
from cohesity_sdk.cluster.cohesity.model.certificate_store_list_response import CertificateStoreListResponse
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
    api_instance = certificate_store.CertificateStoreApi(api_client)
    environment = "microsoft365" # str, none_type | Specifies the certificate store environment type. Based on this environment type, corresponding certificate store will be used. (optional) if omitted the server will use the default value of "microsoft365"
    generated_by = "External" # str, none_type | Specifies whether certificates generated by a specific entity are to be returned. Currently certificates can only be Cohesity generated or customer generated. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_store_certificates(environment=environment, generated_by=generated_by)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling CertificateStoreApi->get_store_certificates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str, none_type**| Specifies the certificate store environment type. Based on this environment type, corresponding certificate store will be used. | [optional] if omitted the server will use the default value of "microsoft365"
 **generated_by** | **str, none_type**| Specifies whether certificates generated by a specific entity are to be returned. Currently certificates can only be Cohesity generated or customer generated. | [optional]

### Return type

[**CertificateStoreListResponse**](CertificateStoreListResponse.md)

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

# **update_store_certificate_metadata**
> CertificateObjectWithMetadata update_store_certificate_metadata(thumbprint, body)



**Privileges:** ```SECRET_MANAGER_CERT_MODIFY``` <br><br>Update an exisiting certificate associated with a tenant. Metadata of the certificate updated will be returned.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import certificate_store
from cohesity_sdk.cluster.cohesity.model.certificate_object_with_metadata import CertificateObjectWithMetadata
from cohesity_sdk.cluster.cohesity.model.mutable_certificate_metadata import MutableCertificateMetadata
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
    api_instance = certificate_store.CertificateStoreApi(api_client)
    thumbprint = "thumbprint_example" # str | Specifies the thumbprint of the certificate to be fetched.
    body = MutableCertificateMetadata(
        display_name="display_name_example",
    ) # MutableCertificateMetadata | Specifies the parameters to update a certificate.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_store_certificate_metadata(thumbprint, body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling CertificateStoreApi->update_store_certificate_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thumbprint** | **str**| Specifies the thumbprint of the certificate to be fetched. |
 **body** | [**MutableCertificateMetadata**](MutableCertificateMetadata.md)| Specifies the parameters to update a certificate. |

### Return type

[**CertificateObjectWithMetadata**](CertificateObjectWithMetadata.md)

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

