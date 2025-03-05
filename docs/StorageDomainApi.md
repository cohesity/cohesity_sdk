# cohesity_sdk.StorageDomainApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_storage_domain**](StorageDomainApi.md#create_storage_domain) | **POST** /storage-domains | Create a Storage Domain.
[**delete_storage_domain**](StorageDomainApi.md#delete_storage_domain) | **DELETE** /storage-domains/{id} | Delete a Storage Domain.
[**get_storage_domain_by_id**](StorageDomainApi.md#get_storage_domain_by_id) | **GET** /storage-domains/{id} | Get a Storage Domain by id.
[**get_storage_domains**](StorageDomainApi.md#get_storage_domains) | **GET** /storage-domains | Get Storage Domains.
[**update_storage_domain**](StorageDomainApi.md#update_storage_domain) | **PUT** /storage-domains/{id} | Update a Storage Domain.


# **create_storage_domain**
> StorageDomain create_storage_domain(body)

Create a Storage Domain.

Create a Storage Domain.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.storage_domain import StorageDomain
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
    api_instance = cohesity_sdk.StorageDomainApi(api_client)
    body = cohesity_sdk.StorageDomain() # StorageDomain | Specified the request to create a Storage Domain.

    try:
        # Create a Storage Domain.
        api_response = api_instance.create_storage_domain(body)
        print("The response of StorageDomainApi->create_storage_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageDomainApi->create_storage_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **StorageDomain**| Specified the request to create a Storage Domain. | 

### Return type

[**StorageDomain**](StorageDomain.md)

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

# **delete_storage_domain**
> delete_storage_domain(id)

Delete a Storage Domain.

Delete a Storage Domain.

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
    api_instance = cohesity_sdk.StorageDomainApi(api_client)
    id = 56 # int | Specified the Storage Domain id to delete.

    try:
        # Delete a Storage Domain.
        api_instance.delete_storage_domain(id)
    except Exception as e:
        print("Exception when calling StorageDomainApi->delete_storage_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specified the Storage Domain id to delete. | 

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

# **get_storage_domain_by_id**
> StorageDomain get_storage_domain_by_id(id, include_stats=include_stats, include_time_series_schema=include_time_series_schema, include_file_count_by_size=include_file_count_by_size, include_tenants=include_tenants)

Get a Storage Domain by id.

Get a Storage Domain by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.storage_domain import StorageDomain
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
    api_instance = cohesity_sdk.StorageDomainApi(api_client)
    id = 56 # int | Specified the Storage Domain id to fetch.
    include_stats = True # bool | Whether to include Storage Domain stats in response. (optional)
    include_time_series_schema = True # bool | Whether to include Storage Domain time series schema in response. (optional)
    include_file_count_by_size = True # bool | Whether to include Storage Domain file count by size. (optional)
    include_tenants = True # bool | Whether to include Storage Domains that belong to Tenants. This param is only effective when the User has privilege to view Storage Domain details of a tenant. (optional)

    try:
        # Get a Storage Domain by id.
        api_response = api_instance.get_storage_domain_by_id(id, include_stats=include_stats, include_time_series_schema=include_time_series_schema, include_file_count_by_size=include_file_count_by_size, include_tenants=include_tenants)
        print("The response of StorageDomainApi->get_storage_domain_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageDomainApi->get_storage_domain_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specified the Storage Domain id to fetch. | 
 **include_stats** | **bool**| Whether to include Storage Domain stats in response. | [optional] 
 **include_time_series_schema** | **bool**| Whether to include Storage Domain time series schema in response. | [optional] 
 **include_file_count_by_size** | **bool**| Whether to include Storage Domain file count by size. | [optional] 
 **include_tenants** | **bool**| Whether to include Storage Domains that belong to Tenants. This param is only effective when the User has privilege to view Storage Domain details of a tenant. | [optional] 

### Return type

[**StorageDomain**](StorageDomain.md)

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

# **get_storage_domains**
> StorageDomains get_storage_domains(ids=ids, names=names, cluster_partition_ids=cluster_partition_ids, tenant_ids=tenant_ids, include_tenants=include_tenants, include_stats=include_stats, include_time_series_schema=include_time_series_schema, include_file_count_by_size=include_file_count_by_size, match_partial_names=match_partial_names, view_template_id=view_template_id)

Get Storage Domains.

Get Storage Domains.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.storage_domains import StorageDomains
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
    api_instance = cohesity_sdk.StorageDomainApi(api_client)
    ids = [56] # List[int] | Filter by a list of Storage Domain ids. (optional)
    names = ['names_example'] # List[str] | Filter by a list of Storage Domain names. (optional)
    cluster_partition_ids = [56] # List[int] | Filter by a list of cluster partition ids. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which Storage Domains are to be returned. (optional)
    include_tenants = True # bool | IncludeTenants specifies if Storage Domains of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)
    include_stats = True # bool | Whether to include Storage Domain stats in response. (optional)
    include_time_series_schema = True # bool | Whether to include Storage Domain time series schema in response. (optional)
    include_file_count_by_size = True # bool | Whether to include Storage Domain file count by size. (optional)
    match_partial_names = True # bool | If true, the names in viewNames are matched by any partial rather than exactly matched. (optional)
    view_template_id = 56 # int | Specifies a view template id for Storage Domain. Storage Domains with same deduplication and compression settings will be recommended. (optional)

    try:
        # Get Storage Domains.
        api_response = api_instance.get_storage_domains(ids=ids, names=names, cluster_partition_ids=cluster_partition_ids, tenant_ids=tenant_ids, include_tenants=include_tenants, include_stats=include_stats, include_time_series_schema=include_time_series_schema, include_file_count_by_size=include_file_count_by_size, match_partial_names=match_partial_names, view_template_id=view_template_id)
        print("The response of StorageDomainApi->get_storage_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageDomainApi->get_storage_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| Filter by a list of Storage Domain ids. | [optional] 
 **names** | [**List[str]**](str.md)| Filter by a list of Storage Domain names. | [optional] 
 **cluster_partition_ids** | [**List[int]**](int.md)| Filter by a list of cluster partition ids. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which Storage Domains are to be returned. | [optional] 
 **include_tenants** | **bool**| IncludeTenants specifies if Storage Domains of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional] 
 **include_stats** | **bool**| Whether to include Storage Domain stats in response. | [optional] 
 **include_time_series_schema** | **bool**| Whether to include Storage Domain time series schema in response. | [optional] 
 **include_file_count_by_size** | **bool**| Whether to include Storage Domain file count by size. | [optional] 
 **match_partial_names** | **bool**| If true, the names in viewNames are matched by any partial rather than exactly matched. | [optional] 
 **view_template_id** | **int**| Specifies a view template id for Storage Domain. Storage Domains with same deduplication and compression settings will be recommended. | [optional] 

### Return type

[**StorageDomains**](StorageDomains.md)

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

# **update_storage_domain**
> StorageDomain update_storage_domain(id, body)

Update a Storage Domain.

Update a Storage Domain.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.storage_domain import StorageDomain
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
    api_instance = cohesity_sdk.StorageDomainApi(api_client)
    id = 56 # int | Specified the Storage Domain id to update.
    body = cohesity_sdk.StorageDomain() # StorageDomain | Specified the request to update a Storage Domain.

    try:
        # Update a Storage Domain.
        api_response = api_instance.update_storage_domain(id, body)
        print("The response of StorageDomainApi->update_storage_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageDomainApi->update_storage_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specified the Storage Domain id to update. | 
 **body** | **StorageDomain**| Specified the request to update a Storage Domain. | 

### Return type

[**StorageDomain**](StorageDomain.md)

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

