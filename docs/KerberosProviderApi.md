# cohesity_sdk.cluster.KerberosProviderApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_kerberos_provider_by_id**](KerberosProviderApi.md#get_kerberos_provider_by_id) | **GET** /kerberos-providers/{id} | Get the Registered Kerberos Provider by id.
[**get_kerberos_providers**](KerberosProviderApi.md#get_kerberos_providers) | **GET** /kerberos-providers | Get the list of Kerberos Providers.
[**register_kerberos_provider**](KerberosProviderApi.md#register_kerberos_provider) | **POST** /kerberos-providers/register | Register a Kerberos Authentication Provider.
[**unregister_kerberos_provider**](KerberosProviderApi.md#unregister_kerberos_provider) | **POST** /kerberos-providers/{id}/unregister | Unregister a Kerberos Provider.
[**update_kerberos_provider**](KerberosProviderApi.md#update_kerberos_provider) | **PUT** /kerberos-providers/{id} | Update the Kerberos Provider Registration.


# **get_kerberos_provider_by_id**
> KerberosProvider get_kerberos_provider_by_id(id)

Get the Registered Kerberos Provider by id.

Get the Registered Kerberos Provider by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.kerberos_provider import KerberosProvider
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
    api_instance = cohesity_sdk.cluster.KerberosProviderApi(api_client)
    id = 'id_example' # str | Specifies the id which will be of the pattern cluster_id:clusterincarnation_id:resource_id.

    try:
        # Get the Registered Kerberos Provider by id.
        api_response = api_instance.get_kerberos_provider_by_id(id)
        print("The response of KerberosProviderApi->get_kerberos_provider_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KerberosProviderApi->get_kerberos_provider_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id which will be of the pattern cluster_id:clusterincarnation_id:resource_id. | 

### Return type

[**KerberosProvider**](KerberosProvider.md)

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

# **get_kerberos_providers**
> KerberosProviders get_kerberos_providers(realm_names=realm_names, has_ldap=has_ldap, ids=ids, kdc_servers=kdc_servers)

Get the list of Kerberos Providers.

Get the list of Kerberos Authentication Providers.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.kerberos_providers import KerberosProviders
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
    api_instance = cohesity_sdk.cluster.KerberosProviderApi(api_client)
    realm_names = ['realm_names_example'] # List[str] | Filter by a list of realm names. (optional)
    has_ldap = True # bool | Filter by whether LDAP is associated with the provider. (optional)
    ids = [56] # List[int] | Filter by a list of Kerberos Provider Ids. (optional)
    kdc_servers = ['kdc_servers_example'] # List[str] | Filter by a list of KDC servers. (optional)

    try:
        # Get the list of Kerberos Providers.
        api_response = api_instance.get_kerberos_providers(realm_names=realm_names, has_ldap=has_ldap, ids=ids, kdc_servers=kdc_servers)
        print("The response of KerberosProviderApi->get_kerberos_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KerberosProviderApi->get_kerberos_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm_names** | [**List[str]**](str.md)| Filter by a list of realm names. | [optional] 
 **has_ldap** | **bool**| Filter by whether LDAP is associated with the provider. | [optional] 
 **ids** | [**List[int]**](int.md)| Filter by a list of Kerberos Provider Ids. | [optional] 
 **kdc_servers** | [**List[str]**](str.md)| Filter by a list of KDC servers. | [optional] 

### Return type

[**KerberosProviders**](KerberosProviders.md)

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

# **register_kerberos_provider**
> KerberosProvider register_kerberos_provider(body)

Register a Kerberos Authentication Provider.

Register a Kerberos Authentication Provider.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.kerberos_provider import KerberosProvider
from cohesity_sdk.cluster.models.register_or_update_kerberos_provider_request import RegisterOrUpdateKerberosProviderRequest
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
    api_instance = cohesity_sdk.cluster.KerberosProviderApi(api_client)
    body = cohesity_sdk.cluster.RegisterOrUpdateKerberosProviderRequest() # RegisterOrUpdateKerberosProviderRequest | Specifies the parameters to Register a Kerberos Provider.

    try:
        # Register a Kerberos Authentication Provider.
        api_response = api_instance.register_kerberos_provider(body)
        print("The response of KerberosProviderApi->register_kerberos_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KerberosProviderApi->register_kerberos_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterOrUpdateKerberosProviderRequest**](RegisterOrUpdateKerberosProviderRequest.md)| Specifies the parameters to Register a Kerberos Provider. | 

### Return type

[**KerberosProvider**](KerberosProvider.md)

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

# **unregister_kerberos_provider**
> UnregisterKerberosProvider unregister_kerberos_provider(id, body)

Unregister a Kerberos Provider.

Unregister a Kerberos Provider.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.unregister_kerberos_provider import UnregisterKerberosProvider
from cohesity_sdk.cluster.models.unregister_kerberos_request import UnregisterKerberosRequest
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
    api_instance = cohesity_sdk.cluster.KerberosProviderApi(api_client)
    id = 'id_example' # str | Specifies the id.
    body = cohesity_sdk.cluster.UnregisterKerberosRequest() # UnregisterKerberosRequest | Request to unregister a Kerberos Provider.

    try:
        # Unregister a Kerberos Provider.
        api_response = api_instance.unregister_kerberos_provider(id, body)
        print("The response of KerberosProviderApi->unregister_kerberos_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KerberosProviderApi->unregister_kerberos_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id. | 
 **body** | [**UnregisterKerberosRequest**](UnregisterKerberosRequest.md)| Request to unregister a Kerberos Provider. | 

### Return type

[**UnregisterKerberosProvider**](UnregisterKerberosProvider.md)

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

# **update_kerberos_provider**
> KerberosProvider update_kerberos_provider(id, body)

Update the Kerberos Provider Registration.

Update the Kerberos Provider Registration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.kerberos_provider import KerberosProvider
from cohesity_sdk.cluster.models.register_or_update_kerberos_provider_request import RegisterOrUpdateKerberosProviderRequest
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
    api_instance = cohesity_sdk.cluster.KerberosProviderApi(api_client)
    id = 'id_example' # str | Specifies the id which will be of the pattern cluster_id:clusterincarnation_id:resource_id.
    body = cohesity_sdk.cluster.RegisterOrUpdateKerberosProviderRequest() # RegisterOrUpdateKerberosProviderRequest | Request to update a Kerberos Provider.

    try:
        # Update the Kerberos Provider Registration.
        api_response = api_instance.update_kerberos_provider(id, body)
        print("The response of KerberosProviderApi->update_kerberos_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KerberosProviderApi->update_kerberos_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id which will be of the pattern cluster_id:clusterincarnation_id:resource_id. | 
 **body** | [**RegisterOrUpdateKerberosProviderRequest**](RegisterOrUpdateKerberosProviderRequest.md)| Request to update a Kerberos Provider. | 

### Return type

[**KerberosProvider**](KerberosProvider.md)

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

