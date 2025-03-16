# cohesity_sdk.helios.SourceApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_azure_applications**](SourceApi.md#create_azure_applications) | **POST** /data-protect/sources/microsoft365/azure-applications | Create Microsoft 365 Azure Applications for a given domain.
[**create_or_update_azure_applications**](SourceApi.md#create_or_update_azure_applications) | **PUT** /data-protect/sources/microsoft365/azure-applications | Create/Update Microsoft 365 Azure Applications for a given domain.
[**delete_protection_source_registration**](SourceApi.md#delete_protection_source_registration) | **DELETE** /data-protect/sources/registrations/{id} | Delete Protection Source Registration.
[**generate_m365_device_access_token**](SourceApi.md#generate_m365_device_access_token) | **POST** /data-protect/sources/microsoft365/auth/token | Generate access token for Microsoft365 Device Authorization Grant flow.
[**generate_m365_device_code**](SourceApi.md#generate_m365_device_code) | **POST** /data-protect/sources/microsoft365/auth/device-code | Generate device code for Microsoft365 Device Authorization Grant flow.
[**get_protection_source_registration**](SourceApi.md#get_protection_source_registration) | **GET** /data-protect/sources/registrations/{id} | Get a Protection Source registration.
[**get_protection_sources**](SourceApi.md#get_protection_sources) | **GET** /data-protect/sources | Get a List of Protection Sources.
[**get_source_attribute_filters**](SourceApi.md#get_source_attribute_filters) | **GET** /data-protect/sources/filters | List attribute filters for a source.
[**get_source_registrations**](SourceApi.md#get_source_registrations) | **GET** /data-protect/sources/registrations | Get the list of Protection Source registrations.
[**get_vdc_details**](SourceApi.md#get_vdc_details) | **GET** /data-protect/sources/virtual-datacenter/{id} | Get VDC Details.
[**mcm_delete_protection_source_registration**](SourceApi.md#mcm_delete_protection_source_registration) | **DELETE** /mcm/data-protect/sources/registrations/{id} | Delete Protection Source Registration.
[**mcm_get_protection_source_registration**](SourceApi.md#mcm_get_protection_source_registration) | **GET** /mcm/data-protect/sources/registrations/{id} | Get a Protection Source registration.
[**mcm_get_protection_sources**](SourceApi.md#mcm_get_protection_sources) | **GET** /mcm/data-protect/sources | Get a List of Protection Sources.
[**mcm_register_protection_source**](SourceApi.md#mcm_register_protection_source) | **POST** /mcm/data-protect/sources/registrations | Register a Protection Source.
[**mcm_test_source_connection**](SourceApi.md#mcm_test_source_connection) | **POST** /mcm/data-protect/sources/test-connection | Test connection to a source.
[**patch_protection_source_registration**](SourceApi.md#patch_protection_source_registration) | **PATCH** /data-protect/sources/registrations/{id} | Perform Partial Update on Protection Source registration. Currently this API is supported only for Cassandra
[**protection_source_by_id**](SourceApi.md#protection_source_by_id) | **GET** /data-protect/sources/{id} | Get a Protection Sources.
[**refresh_protection_source_by_id**](SourceApi.md#refresh_protection_source_by_id) | **POST** /data-protect/sources/{id}/refresh | Refresh a Protection Source.
[**register_protection_source**](SourceApi.md#register_protection_source) | **POST** /data-protect/sources/registrations | Register a Protection Source.
[**test_connection_protection_source**](SourceApi.md#test_connection_protection_source) | **POST** /data-protect/sources/test-connection | Test connection to a source.
[**update_protection_source_registration**](SourceApi.md#update_protection_source_registration) | **PUT** /data-protect/sources/registrations/{id} | Update Protection Source registration.
[**update_protection_source_registration_mixin1**](SourceApi.md#update_protection_source_registration_mixin1) | **PUT** /mcm/data-protect/sources/registrations/{id} | Update Protection Source registration.


# **create_azure_applications**
> CreateAzureApplicationResponseParams create_azure_applications(body, access_cluster_id=access_cluster_id, region_id=region_id)

Create Microsoft 365 Azure Applications for a given domain.

Creates Microsoft 365 Azure Applications

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.create_azure_application_request_params import CreateAzureApplicationRequestParams
from cohesity_sdk.helios.models.create_azure_application_response_params import CreateAzureApplicationResponseParams
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    body = cohesity_sdk.helios.CreateAzureApplicationRequestParams() # CreateAzureApplicationRequestParams | Specifies the parameters to create Azure applications within a given Microsoft365 source.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Create Microsoft 365 Azure Applications for a given domain.
        api_response = api_instance.create_azure_applications(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of SourceApi->create_azure_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->create_azure_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAzureApplicationRequestParams**](CreateAzureApplicationRequestParams.md)| Specifies the parameters to create Azure applications within a given Microsoft365 source. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**CreateAzureApplicationResponseParams**](CreateAzureApplicationResponseParams.md)

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

# **create_or_update_azure_applications**
> CreateAzureApplicationResponseParams create_or_update_azure_applications(body, access_cluster_id=access_cluster_id, region_id=region_id)

Create/Update Microsoft 365 Azure Applications for a given domain.

Creates/Updates Microsoft 365 Azure Applications

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.create_azure_application_request_params import CreateAzureApplicationRequestParams
from cohesity_sdk.helios.models.create_azure_application_response_params import CreateAzureApplicationResponseParams
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    body = cohesity_sdk.helios.CreateAzureApplicationRequestParams() # CreateAzureApplicationRequestParams | Specifies the parameters to create/update Azure applications within a given Microsoft365 source.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Create/Update Microsoft 365 Azure Applications for a given domain.
        api_response = api_instance.create_or_update_azure_applications(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of SourceApi->create_or_update_azure_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->create_or_update_azure_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAzureApplicationRequestParams**](CreateAzureApplicationRequestParams.md)| Specifies the parameters to create/update Azure applications within a given Microsoft365 source. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**CreateAzureApplicationResponseParams**](CreateAzureApplicationResponseParams.md)

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

# **delete_protection_source_registration**
> delete_protection_source_registration(id, access_cluster_id=access_cluster_id, region_id=region_id)

Delete Protection Source Registration.

Delete Protection Source Registration.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    id = 56 # int | Specifies the ID of the Protection Source Registration.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Delete Protection Source Registration.
        api_instance.delete_protection_source_registration(id, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
        print("Exception when calling SourceApi->delete_protection_source_registration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the ID of the Protection Source Registration. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

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

# **generate_m365_device_access_token**
> GenerateM365DeviceAccessTokenResponseParams generate_m365_device_access_token(body, access_cluster_id=access_cluster_id, region_id=region_id)

Generate access token for Microsoft365 Device Authorization Grant flow.

Generates the access token if the device code has been granted authorization as part of device login flow.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.generate_m365_device_access_token_request_params import GenerateM365DeviceAccessTokenRequestParams
from cohesity_sdk.helios.models.generate_m365_device_access_token_response_params import GenerateM365DeviceAccessTokenResponseParams
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    body = cohesity_sdk.helios.GenerateM365DeviceAccessTokenRequestParams() # GenerateM365DeviceAccessTokenRequestParams | Specifies the parameters to validate and generate access token for authorizing the client within Microsoft365.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Generate access token for Microsoft365 Device Authorization Grant flow.
        api_response = api_instance.generate_m365_device_access_token(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of SourceApi->generate_m365_device_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->generate_m365_device_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateM365DeviceAccessTokenRequestParams**](GenerateM365DeviceAccessTokenRequestParams.md)| Specifies the parameters to validate and generate access token for authorizing the client within Microsoft365. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**GenerateM365DeviceAccessTokenResponseParams**](GenerateM365DeviceAccessTokenResponseParams.md)

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

# **generate_m365_device_code**
> GenerateM365DeviceCodeResponseParams generate_m365_device_code(body, access_cluster_id=access_cluster_id, region_id=region_id)

Generate device code for Microsoft365 Device Authorization Grant flow.

Generates User and Device code for Microsoft365 Device Authorization Grant for a given domain.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.generate_m365_device_code_request_params import GenerateM365DeviceCodeRequestParams
from cohesity_sdk.helios.models.generate_m365_device_code_response_params import GenerateM365DeviceCodeResponseParams
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    body = cohesity_sdk.helios.GenerateM365DeviceCodeRequestParams() # GenerateM365DeviceCodeRequestParams | Specifies the parameters to generate the user and device code to initiate authentication with Microsoft365.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Generate device code for Microsoft365 Device Authorization Grant flow.
        api_response = api_instance.generate_m365_device_code(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of SourceApi->generate_m365_device_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->generate_m365_device_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateM365DeviceCodeRequestParams**](GenerateM365DeviceCodeRequestParams.md)| Specifies the parameters to generate the user and device code to initiate authentication with Microsoft365. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**GenerateM365DeviceCodeResponseParams**](GenerateM365DeviceCodeResponseParams.md)

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

# **get_protection_source_registration**
> SourceRegistration get_protection_source_registration(id, access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type)

Get a Protection Source registration.

Get a Protection Source registration.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.source_registration import SourceRegistration
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    id = 56 # int | Specifies the id of the Protection Source registration.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    request_initiator_type = 'request_initiator_type_example' # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)

    try:
        # Get a Protection Source registration.
        api_response = api_instance.get_protection_source_registration(id, access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type)
        print("The response of SourceApi->get_protection_source_registration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->get_protection_source_registration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protection Source registration. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional] 

### Return type

[**SourceRegistration**](SourceRegistration.md)

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

# **get_protection_sources**
> Sources get_protection_sources(access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type, tenant_ids=tenant_ids, include_tenants=include_tenants, include_source_credentials=include_source_credentials, encryption_key=encryption_key)

Get a List of Protection Sources.

Get a List of Protection Sources.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.sources import Sources
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    request_initiator_type = 'request_initiator_type_example' # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which Sources are to be returned. (optional)
    include_tenants = True # bool | If true, the response will include Sources which belong belong to all tenants which the current user has permission to see. If false, then only Sources for the current user will be returned. (optional)
    include_source_credentials = True # bool | If true, the encrypted crednetial for the registered sources will be included. Credential is first encrypted with internal key and then reencrypted with user supplied encryption key. (optional)
    encryption_key = 'encryption_key_example' # str | Specifies the key to be used to encrypt the source credential. If includeSourceCredentials is set to true this key must be specified. (optional)

    try:
        # Get a List of Protection Sources.
        api_response = api_instance.get_protection_sources(access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type, tenant_ids=tenant_ids, include_tenants=include_tenants, include_source_credentials=include_source_credentials, encryption_key=encryption_key)
        print("The response of SourceApi->get_protection_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->get_protection_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which Sources are to be returned. | [optional] 
 **include_tenants** | **bool**| If true, the response will include Sources which belong belong to all tenants which the current user has permission to see. If false, then only Sources for the current user will be returned. | [optional] 
 **include_source_credentials** | **bool**| If true, the encrypted crednetial for the registered sources will be included. Credential is first encrypted with internal key and then reencrypted with user supplied encryption key. | [optional] 
 **encryption_key** | **str**| Specifies the key to be used to encrypt the source credential. If includeSourceCredentials is set to true this key must be specified. | [optional] 

### Return type

[**Sources**](Sources.md)

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

# **get_source_attribute_filters**
> SourceAttributeFiltersResponseParams get_source_attribute_filters(source_uuid, access_cluster_id=access_cluster_id, region_id=region_id, environment=environment)

List attribute filters for a source.

Get a List of attribute filters for leaf entities within a a source

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.source_attribute_filters_response_params import SourceAttributeFiltersResponseParams
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    source_uuid = 'source_uuid_example' # str | Specifies the source UUID of the parent entity.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    environment = 'environment_example' # str | Specifies the environment type of the Protection Source. (optional)

    try:
        # List attribute filters for a source.
        api_response = api_instance.get_source_attribute_filters(source_uuid, access_cluster_id=access_cluster_id, region_id=region_id, environment=environment)
        print("The response of SourceApi->get_source_attribute_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->get_source_attribute_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_uuid** | **str**| Specifies the source UUID of the parent entity. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **environment** | **str**| Specifies the environment type of the Protection Source. | [optional] 

### Return type

[**SourceAttributeFiltersResponseParams**](SourceAttributeFiltersResponseParams.md)

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

# **get_source_registrations**
> SourceRegistrations get_source_registrations(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, tenant_ids=tenant_ids, include_tenants=include_tenants, include_source_credentials=include_source_credentials, encryption_key=encryption_key, use_cached_data=use_cached_data, include_external_metadata=include_external_metadata)

Get the list of Protection Source registrations.

Get the list of Protection Source registrations.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.source_registrations import SourceRegistrations
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    ids = [56] # List[int] | Ids specifies the list of source registration ids to return. If left empty, every source registration will be returned by default. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
    include_tenants = True # bool | If true, the response will include Registrations which were created by all tenants which the current user has permission to see. If false, then only Registrations created by the current user will be returned. (optional)
    include_source_credentials = True # bool | If true, the encrypted crednetial for the registered sources will be included. Credential is first encrypted with internal key and then reencrypted with user supplied encryption key. (optional)
    encryption_key = 'encryption_key_example' # str | Specifies the key to be used to encrypt the source credential. If includeSourceCredentials is set to true this key must be specified. (optional)
    use_cached_data = True # bool | Specifies whether we can serve the GET request from the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. (optional)
    include_external_metadata = True # bool | If true, the external entity metadata like maintenance mode config for the registered sources will be included. (optional)

    try:
        # Get the list of Protection Source registrations.
        api_response = api_instance.get_source_registrations(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, tenant_ids=tenant_ids, include_tenants=include_tenants, include_source_credentials=include_source_credentials, encryption_key=encryption_key, use_cached_data=use_cached_data, include_external_metadata=include_external_metadata)
        print("The response of SourceApi->get_source_registrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->get_source_registrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **ids** | [**List[int]**](int.md)| Ids specifies the list of source registration ids to return. If left empty, every source registration will be returned by default. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which objects are to be returned. | [optional] 
 **include_tenants** | **bool**| If true, the response will include Registrations which were created by all tenants which the current user has permission to see. If false, then only Registrations created by the current user will be returned. | [optional] 
 **include_source_credentials** | **bool**| If true, the encrypted crednetial for the registered sources will be included. Credential is first encrypted with internal key and then reencrypted with user supplied encryption key. | [optional] 
 **encryption_key** | **str**| Specifies the key to be used to encrypt the source credential. If includeSourceCredentials is set to true this key must be specified. | [optional] 
 **use_cached_data** | **bool**| Specifies whether we can serve the GET request from the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. | [optional] 
 **include_external_metadata** | **bool**| If true, the external entity metadata like maintenance mode config for the registered sources will be included. | [optional] 

### Return type

[**SourceRegistrations**](SourceRegistrations.md)

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

# **get_vdc_details**
> VdcObject get_vdc_details(id, access_cluster_id=access_cluster_id, region_id=region_id)

Get VDC Details.

Get the details such as catelogs, Org networks associated with a VMware virtual datacenter (VDC).

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.vdc_object import VdcObject
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    id = 56 # int | Specifies the ID of the VMware virtual datacenter.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get VDC Details.
        api_response = api_instance.get_vdc_details(id, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of SourceApi->get_vdc_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->get_vdc_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the ID of the VMware virtual datacenter. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**VdcObject**](VdcObject.md)

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

# **mcm_delete_protection_source_registration**
> mcm_delete_protection_source_registration(id, region_id=region_id)

Delete Protection Source Registration.

Delete Protection Source Registration.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    id = 'id_example' # str | Specifies the ID of the Protection Source Registration.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Delete Protection Source Registration.
        api_instance.mcm_delete_protection_source_registration(id, region_id=region_id)
    except Exception as e:
        print("Exception when calling SourceApi->mcm_delete_protection_source_registration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the ID of the Protection Source Registration. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

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

# **mcm_get_protection_source_registration**
> McmSourceRegistration mcm_get_protection_source_registration(id, region_id=region_id)

Get a Protection Source registration.

Get a Protection Source registration.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.mcm_source_registration import McmSourceRegistration
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    id = 'id_example' # str | Specifies the id of the Protection Source registration.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get a Protection Source registration.
        api_response = api_instance.mcm_get_protection_source_registration(id, region_id=region_id)
        print("The response of SourceApi->mcm_get_protection_source_registration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->mcm_get_protection_source_registration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the Protection Source registration. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**McmSourceRegistration**](McmSourceRegistration.md)

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

# **mcm_get_protection_sources**
> McmSources mcm_get_protection_sources(region_id=region_id, environments=environments, ids=ids, region_ids=region_ids, cluster_ids=cluster_ids, exclude_protection_stats=exclude_protection_stats)

Get a List of Protection Sources.

Get a List of Protection Sources.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.mcm_sources import McmSources
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    environments = ['environments_example'] # List[str] | Specifies the list of environment type of the Protection Source. (optional)
    ids = ['ids_example'] # List[str] | Specifies the list of ids to filter Protection Sources. (optional)
    region_ids = ['region_ids_example'] # List[str] | Filter by a list of region ids. (optional)
    cluster_ids = ['cluster_ids_example'] # List[str] | Filter by a list of cluster ids. (optional)
    exclude_protection_stats = True # bool | Whether to exclude Protection Sources protection stats in response. (optional)

    try:
        # Get a List of Protection Sources.
        api_response = api_instance.mcm_get_protection_sources(region_id=region_id, environments=environments, ids=ids, region_ids=region_ids, cluster_ids=cluster_ids, exclude_protection_stats=exclude_protection_stats)
        print("The response of SourceApi->mcm_get_protection_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->mcm_get_protection_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **environments** | [**List[str]**](str.md)| Specifies the list of environment type of the Protection Source. | [optional] 
 **ids** | [**List[str]**](str.md)| Specifies the list of ids to filter Protection Sources. | [optional] 
 **region_ids** | [**List[str]**](str.md)| Filter by a list of region ids. | [optional] 
 **cluster_ids** | [**List[str]**](str.md)| Filter by a list of cluster ids. | [optional] 
 **exclude_protection_stats** | **bool**| Whether to exclude Protection Sources protection stats in response. | [optional] 

### Return type

[**McmSources**](McmSources.md)

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

# **mcm_register_protection_source**
> McmSourceRegistration mcm_register_protection_source(body, region_id=region_id, access_cluster_id=access_cluster_id)

Register a Protection Source.

Register a Protection Source.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.mcm_source_registration import McmSourceRegistration
from cohesity_sdk.helios.models.mcm_source_registration_request_params import McmSourceRegistrationRequestParams
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    body = cohesity_sdk.helios.McmSourceRegistrationRequestParams() # McmSourceRegistrationRequestParams | Specifies the parameters to register a Protection Source.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    access_cluster_id = 56 # int | Specifies the destination cluster id on which this Source needs to be registered. (optional)

    try:
        # Register a Protection Source.
        api_response = api_instance.mcm_register_protection_source(body, region_id=region_id, access_cluster_id=access_cluster_id)
        print("The response of SourceApi->mcm_register_protection_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->mcm_register_protection_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**McmSourceRegistrationRequestParams**](McmSourceRegistrationRequestParams.md)| Specifies the parameters to register a Protection Source. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **access_cluster_id** | **int**| Specifies the destination cluster id on which this Source needs to be registered. | [optional] 

### Return type

[**McmSourceRegistration**](McmSourceRegistration.md)

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

# **mcm_test_source_connection**
> SourceConnectionResponseParams mcm_test_source_connection(body, region_id=region_id, access_cluster_id=access_cluster_id)

Test connection to a source.

Specifies the endpoint to test the source connectivity.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.source_connection_request_params import SourceConnectionRequestParams
from cohesity_sdk.helios.models.source_connection_response_params import SourceConnectionResponseParams
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    body = cohesity_sdk.helios.SourceConnectionRequestParams() # SourceConnectionRequestParams | Specifies the parameters to test connectivity of a Protection Source.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    access_cluster_id = 56 # int | Specifies the destination cluster id on which this Source needs to be registered. (optional)

    try:
        # Test connection to a source.
        api_response = api_instance.mcm_test_source_connection(body, region_id=region_id, access_cluster_id=access_cluster_id)
        print("The response of SourceApi->mcm_test_source_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->mcm_test_source_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SourceConnectionRequestParams**](SourceConnectionRequestParams.md)| Specifies the parameters to test connectivity of a Protection Source. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **access_cluster_id** | **int**| Specifies the destination cluster id on which this Source needs to be registered. | [optional] 

### Return type

[**SourceConnectionResponseParams**](SourceConnectionResponseParams.md)

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

# **patch_protection_source_registration**
> SourceRegistration patch_protection_source_registration(id, body, access_cluster_id=access_cluster_id, region_id=region_id)

Perform Partial Update on Protection Source registration. Currently this API is supported only for Cassandra

Patches a Protection Source.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.source_registration import SourceRegistration
from cohesity_sdk.helios.models.source_registration_patch_request_params import SourceRegistrationPatchRequestParams
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    id = 56 # int | Specifies the id of the Protection Source registration.
    body = cohesity_sdk.helios.SourceRegistrationPatchRequestParams() # SourceRegistrationPatchRequestParams | Specifies the parameters to partially update the registration.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Perform Partial Update on Protection Source registration. Currently this API is supported only for Cassandra
        api_response = api_instance.patch_protection_source_registration(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of SourceApi->patch_protection_source_registration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->patch_protection_source_registration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protection Source registration. | 
 **body** | [**SourceRegistrationPatchRequestParams**](SourceRegistrationPatchRequestParams.md)| Specifies the parameters to partially update the registration. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**SourceRegistration**](SourceRegistration.md)

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

# **protection_source_by_id**
> Source protection_source_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)

Get a Protection Sources.

Get a Protection Source.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.source import Source
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    id = 56 # int | Specifies the id of the Protection Source.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get a Protection Sources.
        api_response = api_instance.protection_source_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of SourceApi->protection_source_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->protection_source_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protection Source. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**Source**](Source.md)

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

# **refresh_protection_source_by_id**
> refresh_protection_source_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)

Refresh a Protection Source.

Refresh a Protection Source.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    id = 56 # int | Specifies the id of the Protection Source.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Refresh a Protection Source.
        api_instance.refresh_protection_source_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
        print("Exception when calling SourceApi->refresh_protection_source_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protection Source. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

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

# **register_protection_source**
> SourceRegistration register_protection_source(body, access_cluster_id=access_cluster_id, region_id=region_id)

Register a Protection Source.

Register a Protection Source.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.source_registration import SourceRegistration
from cohesity_sdk.helios.models.source_registration_request_params import SourceRegistrationRequestParams
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    body = cohesity_sdk.helios.SourceRegistrationRequestParams() # SourceRegistrationRequestParams | Specifies the parameters to register a Protection Source.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Register a Protection Source.
        api_response = api_instance.register_protection_source(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of SourceApi->register_protection_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->register_protection_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SourceRegistrationRequestParams**](SourceRegistrationRequestParams.md)| Specifies the parameters to register a Protection Source. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**SourceRegistration**](SourceRegistration.md)

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

# **test_connection_protection_source**
> SourceConnectionResponseParams test_connection_protection_source(body, access_cluster_id=access_cluster_id, region_id=region_id)

Test connection to a source.

Test connection to a source.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.source_connection_request_params import SourceConnectionRequestParams
from cohesity_sdk.helios.models.source_connection_response_params import SourceConnectionResponseParams
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    body = cohesity_sdk.helios.SourceConnectionRequestParams() # SourceConnectionRequestParams | Specifies the parameters to test connectivity with a source.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Test connection to a source.
        api_response = api_instance.test_connection_protection_source(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of SourceApi->test_connection_protection_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->test_connection_protection_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SourceConnectionRequestParams**](SourceConnectionRequestParams.md)| Specifies the parameters to test connectivity with a source. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**SourceConnectionResponseParams**](SourceConnectionResponseParams.md)

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

# **update_protection_source_registration**
> SourceRegistration update_protection_source_registration(id, body, access_cluster_id=access_cluster_id, region_id=region_id)

Update Protection Source registration.

Update Protection Source registration.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.source_registration import SourceRegistration
from cohesity_sdk.helios.models.source_registration_update_request_params import SourceRegistrationUpdateRequestParams
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    id = 56 # int | Specifies the id of the Protection Source registration.
    body = cohesity_sdk.helios.SourceRegistrationUpdateRequestParams() # SourceRegistrationUpdateRequestParams | Specifies the parameters to update the registration.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update Protection Source registration.
        api_response = api_instance.update_protection_source_registration(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of SourceApi->update_protection_source_registration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->update_protection_source_registration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protection Source registration. | 
 **body** | [**SourceRegistrationUpdateRequestParams**](SourceRegistrationUpdateRequestParams.md)| Specifies the parameters to update the registration. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**SourceRegistration**](SourceRegistration.md)

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

# **update_protection_source_registration_mixin1**
> McmSourceRegistration update_protection_source_registration_mixin1(id, body, region_id=region_id)

Update Protection Source registration.

Update Protection Source registration.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.mcm_source_registration import McmSourceRegistration
from cohesity_sdk.helios.models.mcm_source_registration_update_request_params import McmSourceRegistrationUpdateRequestParams
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
    api_instance = cohesity_sdk.helios.SourceApi(api_client)
    id = 'id_example' # str | Specifies the id of the Protection Source registration.
    body = cohesity_sdk.helios.McmSourceRegistrationUpdateRequestParams() # McmSourceRegistrationUpdateRequestParams | Specifies the parameters to update the registration.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update Protection Source registration.
        api_response = api_instance.update_protection_source_registration_mixin1(id, body, region_id=region_id)
        print("The response of SourceApi->update_protection_source_registration_mixin1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->update_protection_source_registration_mixin1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the Protection Source registration. | 
 **body** | [**McmSourceRegistrationUpdateRequestParams**](McmSourceRegistrationUpdateRequestParams.md)| Specifies the parameters to update the registration. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**McmSourceRegistration**](McmSourceRegistration.md)

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

