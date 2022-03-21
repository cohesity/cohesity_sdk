# cohesity_sdk.StorageDomainApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cad_storage_domains**](StorageDomainApi.md#create_cad_storage_domains) | **POST** /cad-storage-domains | Create CAD Storage Domains.
[**create_storage_domain**](StorageDomainApi.md#create_storage_domain) | **POST** /storage-domains | Create a Storage Domain.
[**delete_storage_domain**](StorageDomainApi.md#delete_storage_domain) | **DELETE** /storage-domains/{id} | Delete a Storage Domain.
[**get_storage_domain_by_id**](StorageDomainApi.md#get_storage_domain_by_id) | **GET** /storage-domains/{id} | Get a Storage Domain by id.
[**get_storage_domains**](StorageDomainApi.md#get_storage_domains) | **GET** /storage-domains | Get Storage Domains.
[**update_storage_domain**](StorageDomainApi.md#update_storage_domain) | **PUT** /storage-domains/{id} | Update a Storage Domain.


# **create_cad_storage_domains**
> StorageDomain create_cad_storage_domains(body)

Create CAD Storage Domains.

Create CAD Storage Domains. Instead of returning error, This API will return the CAD Storage Domain mapped to the external target if there is one.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.storage_domain import StorageDomain
from cohesity_sdk.cluster.model.create_cad_storage_domain_param import CreateCadStorageDomainParam
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateCadStorageDomainParam(
        external_target_id=1,
    ) # CreateCadStorageDomainParam | Specified the request to create a CAD Storage Domain.

# example passing only required values which don't have defaults set
try:
	# Create CAD Storage Domains.
	api_response = client.storage_domain.create_cad_storage_domains(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StorageDomainApi->create_cad_storage_domains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCadStorageDomainParam**](CreateCadStorageDomainParam.md)| Specified the request to create a CAD Storage Domain. |

### Return type

[**StorageDomain**](StorageDomain.md)

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

# **create_storage_domain**
> StorageDomain create_storage_domain(body)

Create a Storage Domain.

Create a Storage Domain.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.storage_domain import StorageDomain
from cohesity_sdk.cluster.model.create_storage_domain_param import CreateStorageDomainParam
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateStorageDomainParam() # CreateStorageDomainParam | Specified the request to create a Storage Domain.

# example passing only required values which don't have defaults set
try:
	# Create a Storage Domain.
	api_response = client.storage_domain.create_storage_domain(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StorageDomainApi->create_storage_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateStorageDomainParam**](CreateStorageDomainParam.md)| Specified the request to create a Storage Domain. |

### Return type

[**StorageDomain**](StorageDomain.md)

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

# **delete_storage_domain**
> delete_storage_domain(id)

Delete a Storage Domain.

Delete a Storage Domain.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specified the Storage Domain id to delete.

# example passing only required values which don't have defaults set
try:
	# Delete a Storage Domain.
	client.storage_domain.delete_storage_domain(id)
except ApiException as e:
	print("Exception when calling StorageDomainApi->delete_storage_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specified the Storage Domain id to delete. |

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

# **get_storage_domain_by_id**
> StorageDomain get_storage_domain_by_id(id)

Get a Storage Domain by id.

Get a Storage Domain by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.storage_domain import StorageDomain
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specified the Storage Domain id to fetch.
include_stats = True # bool | Whether to include Storage Domain stats in response. (optional)
include_time_series_schema = True # bool | Whether to include Storage Domain time series schema in response. (optional)
include_file_count_by_size = True # bool | Whether to include Storage Domain file count by size. (optional)

# example passing only required values which don't have defaults set
try:
	# Get a Storage Domain by id.
	api_response = client.storage_domain.get_storage_domain_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StorageDomainApi->get_storage_domain_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a Storage Domain by id.
	api_response = client.storage_domain.get_storage_domain_by_id(id, include_stats=include_stats, include_time_series_schema=include_time_series_schema, include_file_count_by_size=include_file_count_by_size)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StorageDomainApi->get_storage_domain_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specified the Storage Domain id to fetch. |
 **include_stats** | **bool**| Whether to include Storage Domain stats in response. | [optional]
 **include_time_series_schema** | **bool**| Whether to include Storage Domain time series schema in response. | [optional]
 **include_file_count_by_size** | **bool**| Whether to include Storage Domain file count by size. | [optional]

### Return type

[**StorageDomain**](StorageDomain.md)

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

# **get_storage_domains**
> StorageDomains get_storage_domains()

Get Storage Domains.

Get Storage Domains.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.storage_domains import StorageDomains
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


ids = [
        1,
    ] # [int] | Filter by a list of Storage Domain ids. (optional)
names = [
        "names_example",
    ] # [str] | Filter by a list of Storage Domain names. (optional)
cluster_partition_ids = [
        1,
    ] # [int] | Filter by a list of cluster partition ids. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which Storage Domains are to be returned. (optional)
include_tenants = True # bool | IncludeTenants specifies if Storage Domains of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)
include_stats = True # bool | Whether to include Storage Domain stats in response. (optional)
include_time_series_schema = True # bool | Whether to include Storage Domain time series schema in response. (optional)
include_file_count_by_size = True # bool | Whether to include Storage Domain file count by size. (optional)
match_partial_names = True # bool | If true, the names in viewNames are matched by any partial rather than exactly matched. (optional)
view_template_id = 1 # int | Specifies a view template id for Storage Domain. Storage Domains with same deduplication and compression settings will be recommended. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Storage Domains.
	api_response = client.storage_domain.get_storage_domains(ids=ids, names=names, cluster_partition_ids=cluster_partition_ids, tenant_ids=tenant_ids, include_tenants=include_tenants, include_stats=include_stats, include_time_series_schema=include_time_series_schema, include_file_count_by_size=include_file_count_by_size, match_partial_names=match_partial_names, view_template_id=view_template_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StorageDomainApi->get_storage_domains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**| Filter by a list of Storage Domain ids. | [optional]
 **names** | **[str]**| Filter by a list of Storage Domain names. | [optional]
 **cluster_partition_ids** | **[int]**| Filter by a list of cluster partition ids. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which Storage Domains are to be returned. | [optional]
 **include_tenants** | **bool**| IncludeTenants specifies if Storage Domains of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional]
 **include_stats** | **bool**| Whether to include Storage Domain stats in response. | [optional]
 **include_time_series_schema** | **bool**| Whether to include Storage Domain time series schema in response. | [optional]
 **include_file_count_by_size** | **bool**| Whether to include Storage Domain file count by size. | [optional]
 **match_partial_names** | **bool**| If true, the names in viewNames are matched by any partial rather than exactly matched. | [optional]
 **view_template_id** | **int**| Specifies a view template id for Storage Domain. Storage Domains with same deduplication and compression settings will be recommended. | [optional]

### Return type

[**StorageDomains**](StorageDomains.md)

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

# **update_storage_domain**
> StorageDomain update_storage_domain(id, body)

Update a Storage Domain.

Update a Storage Domain.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.storage_domain import StorageDomain
from cohesity_sdk.cluster.model.update_storage_domain_param import UpdateStorageDomainParam
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specified the Storage Domain id to update.
body = UpdateStorageDomainParam() # UpdateStorageDomainParam | Specified the request to update a Storage Domain.

# example passing only required values which don't have defaults set
try:
	# Update a Storage Domain.
	api_response = client.storage_domain.update_storage_domain(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling StorageDomainApi->update_storage_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specified the Storage Domain id to update. |
 **body** | [**UpdateStorageDomainParam**](UpdateStorageDomainParam.md)| Specified the request to update a Storage Domain. |

### Return type

[**StorageDomain**](StorageDomain.md)

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

