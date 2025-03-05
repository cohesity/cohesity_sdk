# cohesity_sdk.TagApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag**](TagApi.md#create_tag) | **POST** /tags | Create a Tag
[**delete_tag**](TagApi.md#delete_tag) | **DELETE** /tags/{id} | Delete a Tag
[**get_tag_by_id**](TagApi.md#get_tag_by_id) | **GET** /tags/{id} | Get Tag by id.
[**get_tags**](TagApi.md#get_tags) | **GET** /tags | Get tags based on filters.
[**update_tag**](TagApi.md#update_tag) | **PUT** /tags/{id} | Update a Tag


# **create_tag**
> Tag create_tag(body)

Create a Tag

Creates a Tag.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.tag import Tag
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.TagApi(api_client)
    body = cohesity_sdk.Tag() # Tag | Request to create a Tag.

    try:
        # Create a Tag
        api_response = api_instance.create_tag(body)
        print("The response of TagApi->create_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->create_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Tag**](Tag.md)| Request to create a Tag. | 

### Return type

[**Tag**](Tag.md)

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

# **delete_tag**
> delete_tag(id)

Delete a Tag

Deletes a Tag by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.TagApi(api_client)
    id = 'id_example' # str | Specifies the Id of the tag.

    try:
        # Delete a Tag
        api_instance.delete_tag(id)
    except Exception as e:
        print("Exception when calling TagApi->delete_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the Id of the tag. | 

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

# **get_tag_by_id**
> Tag get_tag_by_id(id)

Get Tag by id.

Get Tag by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.tag import Tag
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.TagApi(api_client)
    id = 'id_example' # str | Specifies the Id of the tag.

    try:
        # Get Tag by id.
        api_response = api_instance.get_tag_by_id(id)
        print("The response of TagApi->get_tag_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->get_tag_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the Id of the tag. | 

### Return type

[**Tag**](Tag.md)

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

# **get_tags**
> List[Tag] get_tags(ids=ids, names=names, namespaces=namespaces, tenant_ids=tenant_ids, include_tenants=include_tenants, include_marked_for_deletion=include_marked_for_deletion)

Get tags based on filters.

If no parameters are specified, all tags are returned.
Specifying parameters filters the results that are returned.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.tag import Tag
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.TagApi(api_client)
    ids = ['ids_example'] # List[str] | Filter by a list of Tag Ids. If Ids are mentioned all other fields will be ignored. (optional)
    names = ['names_example'] # List[str] | Filter by a list of Tag names. (optional)
    namespaces = ['namespaces_example'] # List[str] | Filter by a list of Namespaces. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which tags are to be returned. (optional)
    include_tenants = True # bool | IncludeTenants specifies if tags of all the tenants under the hierarchy of the logged in user's organization should be returned. False, by default. (optional)
    include_marked_for_deletion = True # bool | Specifies if tags marked for deletion should be shown. These are tags which are undergoing deletion. False, by default. (optional)

    try:
        # Get tags based on filters.
        api_response = api_instance.get_tags(ids=ids, names=names, namespaces=namespaces, tenant_ids=tenant_ids, include_tenants=include_tenants, include_marked_for_deletion=include_marked_for_deletion)
        print("The response of TagApi->get_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->get_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[str]**](str.md)| Filter by a list of Tag Ids. If Ids are mentioned all other fields will be ignored. | [optional] 
 **names** | [**List[str]**](str.md)| Filter by a list of Tag names. | [optional] 
 **namespaces** | [**List[str]**](str.md)| Filter by a list of Namespaces. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which tags are to be returned. | [optional] 
 **include_tenants** | **bool**| IncludeTenants specifies if tags of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. False, by default. | [optional] 
 **include_marked_for_deletion** | **bool**| Specifies if tags marked for deletion should be shown. These are tags which are undergoing deletion. False, by default. | [optional] 

### Return type

[**List[Tag]**](Tag.md)

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

# **update_tag**
> Tag update_tag(id, body)

Update a Tag

Updates a Tag by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.tag import Tag
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.TagApi(api_client)
    id = 'id_example' # str | Specifies the Id of the tag.
    body = cohesity_sdk.Tag() # Tag | Request to update a tag.

    try:
        # Update a Tag
        api_response = api_instance.update_tag(id, body)
        print("The response of TagApi->update_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->update_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the Id of the tag. | 
 **body** | [**Tag**](Tag.md)| Request to update a tag. | 

### Return type

[**Tag**](Tag.md)

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

