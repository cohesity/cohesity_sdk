# cohesity_sdk.cluster.TagApi

All URIs are relative to *http://localhost/v2*

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

**Privileges:** ```TAGS_MODIFY``` <br><br>Creates a Tag.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tag
from cohesity_sdk.cluster.cohesity.model.tag import Tag
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
    api_instance = tag.TagApi(api_client)
    body = Tag(
        description="description_example",
        name="name_example",
        namespace="namespace_example",
        ui_color="ui_color_example",
        ui_path_elements=[
            "ui_path_elements_example",
        ],
    ) # Tag | Request to create a Tag.

    # example passing only required values which don't have defaults set
    try:
        # Create a Tag
        api_response = api_instance.create_tag(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling TagApi->create_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Tag**](Tag.md)| Request to create a Tag. |

### Return type

[**Tag**](Tag.md)

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

# **delete_tag**
> delete_tag(id)

Delete a Tag

**Privileges:** ```TAGS_MODIFY``` <br><br>Deletes a Tag by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tag
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
    api_instance = tag.TagApi(api_client)
    id = "4:072888001528021798096225500850762068629:3OW2EG7P6QW9QKLP6L4Y010FOG5UGCAJVNH6NZN2YP6D" # str | Specifies the Id of the tag.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Tag
        api_instance.delete_tag(id)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling TagApi->delete_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the Id of the tag. |

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

# **get_tag_by_id**
> Tag get_tag_by_id(id)

Get Tag by id.

**Privileges:** ```TAGS_VIEW``` <br><br>Get Tag by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tag
from cohesity_sdk.cluster.cohesity.model.tag import Tag
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
    api_instance = tag.TagApi(api_client)
    id = "4:072888001528021798096225500850762068629:3OW2EG7P6QW9QKLP6L4Y010FOG5UGCAJVNH6NZN2YP6D" # str | Specifies the Id of the tag.

    # example passing only required values which don't have defaults set
    try:
        # Get Tag by id.
        api_response = api_instance.get_tag_by_id(id)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling TagApi->get_tag_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the Id of the tag. |

### Return type

[**Tag**](Tag.md)

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

# **get_tags**
> GetTagsResult get_tags()

Get tags based on filters.

**Privileges:** ```TAGS_VIEW``` <br><br>If no parameters are specified, all tags are returned. Specifying parameters filters the results that are returned.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tag
from cohesity_sdk.cluster.cohesity.model.get_tags_result import GetTagsResult
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
    api_instance = tag.TagApi(api_client)
    ids = [
        "4:072888001528021798096225500850762068629:3OW2EG7P6QW9QKLP6L4Y010FOG5UGCAJVNH6NZN2YP6D",
    ] # [str] | Filter by a list of Tag Ids. If Ids are mentioned all other fields will be ignored. (optional)
    names = [
        "names_example",
    ] # [str] | Filter by a list of Tag names. (optional)
    namespaces = [
        "namespaces_example",
    ] # [str] | Filter by a list of Namespaces. (optional)
    tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which tags are to be returned. (optional)
    include_tenants = True # bool | IncludeTenants specifies if tags of all the tenants under the hierarchy of the logged in user's organization should be returned. False, by default. (optional)
    include_marked_for_deletion = True # bool | Specifies if tags marked for deletion should be shown. These are tags which are undergoing deletion. False, by default. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get tags based on filters.
        api_response = api_instance.get_tags(ids=ids, names=names, namespaces=namespaces, tenant_ids=tenant_ids, include_tenants=include_tenants, include_marked_for_deletion=include_marked_for_deletion)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling TagApi->get_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[str]**| Filter by a list of Tag Ids. If Ids are mentioned all other fields will be ignored. | [optional]
 **names** | **[str]**| Filter by a list of Tag names. | [optional]
 **namespaces** | **[str]**| Filter by a list of Namespaces. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which tags are to be returned. | [optional]
 **include_tenants** | **bool**| IncludeTenants specifies if tags of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. False, by default. | [optional]
 **include_marked_for_deletion** | **bool**| Specifies if tags marked for deletion should be shown. These are tags which are undergoing deletion. False, by default. | [optional]

### Return type

[**GetTagsResult**](GetTagsResult.md)

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

# **update_tag**
> Tag update_tag(id, body)

Update a Tag

**Privileges:** ```TAGS_MODIFY``` <br><br>Updates a Tag by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tag
from cohesity_sdk.cluster.cohesity.model.tag import Tag
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
    api_instance = tag.TagApi(api_client)
    id = "4:072888001528021798096225500850762068629:3OW2EG7P6QW9QKLP6L4Y010FOG5UGCAJVNH6NZN2YP6D" # str | Specifies the Id of the tag.
    body = Tag(
        description="description_example",
        name="name_example",
        namespace="namespace_example",
        ui_color="ui_color_example",
        ui_path_elements=[
            "ui_path_elements_example",
        ],
    ) # Tag | Request to update a tag.

    # example passing only required values which don't have defaults set
    try:
        # Update a Tag
        api_response = api_instance.update_tag(id, body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
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

