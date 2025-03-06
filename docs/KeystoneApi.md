# cohesity_sdk.cluster.KeystoneApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_keystone**](KeystoneApi.md#create_keystone) | **POST** /keystones | Create a Keystone configuration.
[**delete_keystone**](KeystoneApi.md#delete_keystone) | **DELETE** /keystones/{id} | Delete a Keystone configuration.
[**get_keystones**](KeystoneApi.md#get_keystones) | **GET** /keystones | Get Keystones.
[**get_keystones_by_id**](KeystoneApi.md#get_keystones_by_id) | **GET** /keystones/{id} | Get a Keystone by its id.
[**update_keystone**](KeystoneApi.md#update_keystone) | **PUT** /keystones/{id} | Update a Keystone configuration.


# **create_keystone**
> Keystone create_keystone(body)

Create a Keystone configuration.

Create a Keystone configuration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.keystone import Keystone
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
    api_instance = cohesity_sdk.cluster.KeystoneApi(api_client)
    body = cohesity_sdk.cluster.Keystone() # Keystone | Specifies the paremters to create a Keystone configuration.

    try:
        # Create a Keystone configuration.
        api_response = api_instance.create_keystone(body)
        print("The response of KeystoneApi->create_keystone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeystoneApi->create_keystone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Keystone**| Specifies the paremters to create a Keystone configuration. | 

### Return type

[**Keystone**](Keystone.md)

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

# **delete_keystone**
> delete_keystone(id, admin_password)

Delete a Keystone configuration.

Delete a Keystone configuration.

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
    api_instance = cohesity_sdk.cluster.KeystoneApi(api_client)
    id = 56 # int | Specifies the Keystone id.
    admin_password = 'admin_password_example' # str | Specifies the password of Keystone administrator.

    try:
        # Delete a Keystone configuration.
        api_instance.delete_keystone(id, admin_password)
    except Exception as e:
        print("Exception when calling KeystoneApi->delete_keystone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the Keystone id. | 
 **admin_password** | **str**| Specifies the password of Keystone administrator. | 

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

# **get_keystones**
> Keystones get_keystones(names=names, tenant_ids=tenant_ids, include_tenants=include_tenants)

Get Keystones.

Get Keystones.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.keystones import Keystones
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
    api_instance = cohesity_sdk.cluster.KeystoneApi(api_client)
    names = ['names_example'] # List[str] | Specifies a list of Keystone names. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
    include_tenants = True # bool | If true, the response will include Keystones which were created by all tenants which the current user has permission to see. If false, then only Keystones created by the current user will be returned. (optional)

    try:
        # Get Keystones.
        api_response = api_instance.get_keystones(names=names, tenant_ids=tenant_ids, include_tenants=include_tenants)
        print("The response of KeystoneApi->get_keystones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeystoneApi->get_keystones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**List[str]**](str.md)| Specifies a list of Keystone names. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which objects are to be returned. | [optional] 
 **include_tenants** | **bool**| If true, the response will include Keystones which were created by all tenants which the current user has permission to see. If false, then only Keystones created by the current user will be returned. | [optional] 

### Return type

[**Keystones**](Keystones.md)

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

# **get_keystones_by_id**
> Keystone get_keystones_by_id(id)

Get a Keystone by its id.

Get a Keystone by its id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.keystone import Keystone
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
    api_instance = cohesity_sdk.cluster.KeystoneApi(api_client)
    id = 56 # int | Specifies the Keystone id.

    try:
        # Get a Keystone by its id.
        api_response = api_instance.get_keystones_by_id(id)
        print("The response of KeystoneApi->get_keystones_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeystoneApi->get_keystones_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the Keystone id. | 

### Return type

[**Keystone**](Keystone.md)

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

# **update_keystone**
> Keystone update_keystone(id, body)

Update a Keystone configuration.

Update a Keystone configuration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.keystone import Keystone
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
    api_instance = cohesity_sdk.cluster.KeystoneApi(api_client)
    id = 56 # int | Specifies the Keystone id.
    body = cohesity_sdk.cluster.Keystone() # Keystone | Specifies the paremters to update a Keystone configuration.

    try:
        # Update a Keystone configuration.
        api_response = api_instance.update_keystone(id, body)
        print("The response of KeystoneApi->update_keystone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeystoneApi->update_keystone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the Keystone id. | 
 **body** | **Keystone**| Specifies the paremters to update a Keystone configuration. | 

### Return type

[**Keystone**](Keystone.md)

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

