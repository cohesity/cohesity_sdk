# cohesity_sdk.ViewsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_share**](ViewsApi.md#create_share) | **POST** /file-services/shares | Create a Share.
[**create_view**](ViewsApi.md#create_view) | **POST** /file-services/views | Create a View
[**create_view_template**](ViewsApi.md#create_view_template) | **POST** /file-services/view-template | Create a View Template
[**delete_share**](ViewsApi.md#delete_share) | **DELETE** /file-services/shares/{name} | Delete a Share.
[**delete_view**](ViewsApi.md#delete_view) | **DELETE** /file-services/views/{id} | Delete a View
[**delete_view_directory_quota**](ViewsApi.md#delete_view_directory_quota) | **DELETE** /file-services/views/{id}/directory-quotas | Delete directory quota for the View.
[**delete_view_template**](ViewsApi.md#delete_view_template) | **DELETE** /file-services/view-template/{id} | Delete a View Template
[**get_share_by_name**](ViewsApi.md#get_share_by_name) | **GET** /file-services/shares/{name} | Get a Share by name.
[**get_shares**](ViewsApi.md#get_shares) | **GET** /file-services/shares | Get Shares.
[**get_view_by_id**](ViewsApi.md#get_view_by_id) | **GET** /file-services/views/{id} | Get a View by Id
[**get_view_clients**](ViewsApi.md#get_view_clients) | **GET** /file-services/view-clients | Get View Clients.
[**get_view_clients_summary**](ViewsApi.md#get_view_clients_summary) | **GET** /file-services/view-clients/summary | Get View Clients Summary.
[**get_view_directory_quotas**](ViewsApi.md#get_view_directory_quotas) | **GET** /file-services/views/{id}/directory-quotas | Get directory quotas for the View.
[**get_view_user_quotas**](ViewsApi.md#get_view_user_quotas) | **GET** /file-services/views/{id}/user-quotas | Get user quotas for the View.
[**get_view_user_quotas_config**](ViewsApi.md#get_view_user_quotas_config) | **GET** /file-services/views/{id}/user-quotas-config | Get View user quotas config.
[**get_views**](ViewsApi.md#get_views) | **GET** /file-services/views | List Views
[**get_views_summary**](ViewsApi.md#get_views_summary) | **GET** /file-services/views-summary | Get Views summary.
[**read_view_template_by_id**](ViewsApi.md#read_view_template_by_id) | **GET** /file-services/view-template/{id} | Read a View Template by Id
[**read_view_templates**](ViewsApi.md#read_view_templates) | **GET** /file-services/view-template | List View Templates
[**update_share**](ViewsApi.md#update_share) | **PUT** /file-services/shares/{name} | Update a Share.
[**update_view**](ViewsApi.md#update_view) | **PUT** /file-services/views/{id} | Update a View
[**update_view_directory_quota**](ViewsApi.md#update_view_directory_quota) | **PUT** /file-services/views/{id}/directory-quotas | Upadte directory quota for the View.
[**update_view_template**](ViewsApi.md#update_view_template) | **PUT** /file-services/view-template/{id} | Update a View Template


# **create_share**
> Share create_share(body)

Create a Share.

Create a Share.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.share import Share
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = Share() # Share | Specifies the request to create a Share.

# example passing only required values which don't have defaults set
try:
	# Create a Share.
	api_response = client.views.create_share(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->create_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Share**](Share.md)| Specifies the request to create a Share. |

### Return type

[**Share**](Share.md)

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

# **create_view**
> View create_view(body)

Create a View

Creates a View.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.create_view_request import CreateViewRequest
from cohesity_sdk.cohesity_client_v2.model.view import View
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateViewRequest() # CreateViewRequest | Request to create a View.

# example passing only required values which don't have defaults set
try:
	# Create a View
	api_response = client.views.create_view(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->create_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateViewRequest**](CreateViewRequest.md)| Request to create a View. |

### Return type

[**View**](View.md)

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

# **create_view_template**
> Template create_view_template(body)

Create a View Template

Creates a View Template.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.template import Template
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = Template(
        name="name_example",
        dedup=True,
        compress=True,
        view_params={},
    ) # Template | Request to create a view template.

# example passing only required values which don't have defaults set
try:
	# Create a View Template
	api_response = client.views.create_view_template(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->create_view_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Template**](Template.md)| Request to create a view template. |

### Return type

[**Template**](Template.md)

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

# **delete_share**
> delete_share(name)

Delete a Share.

Delete a Share.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


name = "name_example" # str | Specifies the Share name to delete.

# example passing only required values which don't have defaults set
try:
	# Delete a Share.
	client.views.delete_share(name)
except ApiException as e:
	print("Exception when calling ViewsApi->delete_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the Share name to delete. |

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

# **delete_view**
> delete_view(id)

Delete a View

Deletes a View based on given id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies a unique id of the View to delete.

# example passing only required values which don't have defaults set
try:
	# Delete a View
	client.views.delete_view(id)
except ApiException as e:
	print("Exception when calling ViewsApi->delete_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the View to delete. |

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

# **delete_view_directory_quota**
> delete_view_directory_quota(id)

Delete directory quota for the View.

Delete directory quota for the View.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the View id.
directory_path = "directoryPath_example" # str | Specifies the directory path to delete. Exactly one of 'directoryPath' and 'deleteAllDirectoryQuotas' should be provided. (optional)
delete_all_directory_quotas = True # bool | Specifies whether to delete all directory quotas for this view. Exactly one of 'directoryPath' and 'deleteAllDirectoryQuotas' should be provided. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete directory quota for the View.
	client.views.delete_view_directory_quota(id)
except ApiException as e:
	print("Exception when calling ViewsApi->delete_view_directory_quota: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete directory quota for the View.
	client.views.delete_view_directory_quota(id, directory_path=directory_path, delete_all_directory_quotas=delete_all_directory_quotas)
except ApiException as e:
	print("Exception when calling ViewsApi->delete_view_directory_quota: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the View id. |
 **directory_path** | **str**| Specifies the directory path to delete. Exactly one of &#39;directoryPath&#39; and &#39;deleteAllDirectoryQuotas&#39; should be provided. | [optional]
 **delete_all_directory_quotas** | **bool**| Specifies whether to delete all directory quotas for this view. Exactly one of &#39;directoryPath&#39; and &#39;deleteAllDirectoryQuotas&#39; should be provided. | [optional]

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

# **delete_view_template**
> delete_view_template(id)

Delete a View Template

Deletes a view template based on given template id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies a unique id of the view template to delete.

# example passing only required values which don't have defaults set
try:
	# Delete a View Template
	client.views.delete_view_template(id)
except ApiException as e:
	print("Exception when calling ViewsApi->delete_view_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the view template to delete. |

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

# **get_share_by_name**
> Share get_share_by_name(name)

Get a Share by name.

Get a Share by name.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.share import Share
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


name = "name_example" # str | Specifies the Share name.

# example passing only required values which don't have defaults set
try:
	# Get a Share by name.
	api_response = client.views.get_share_by_name(name)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->get_share_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the Share name. |

### Return type

[**Share**](Share.md)

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

# **get_shares**
> Shares get_shares()

Get Shares.

Get Shares.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.shares import Shares
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


name = "name_example" # str | Specifies the Share name. (optional)
match_partial_name = True # bool | If true, the share nane is matched by any partial rather than exactly matched. (optional)
max_count = 1 # int | Specifies a limit on the number of Views returned. (optional)
cookie = "cookie_example" # str | Specifies the cookie. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
include_tenants = True # bool | IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Shares.
	api_response = client.views.get_shares(name=name, match_partial_name=match_partial_name, max_count=max_count, cookie=cookie, tenant_ids=tenant_ids, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->get_shares: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the Share name. | [optional]
 **match_partial_name** | **bool**| If true, the share nane is matched by any partial rather than exactly matched. | [optional]
 **max_count** | **int**| Specifies a limit on the number of Views returned. | [optional]
 **cookie** | **str**| Specifies the cookie. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which objects are to be returned. | [optional]
 **include_tenants** | **bool**| IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional]

### Return type

[**Shares**](Shares.md)

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

# **get_view_by_id**
> View get_view_by_id(id)

Get a View by Id

Get a View based on given Id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.view import View
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies a unique id of the View to fetch.

# example passing only required values which don't have defaults set
try:
	# Get a View by Id
	api_response = client.views.get_view_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->get_view_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the View to fetch. |

### Return type

[**View**](View.md)

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

# **get_view_clients**
> ViewClients get_view_clients()

Get View Clients.

Get View Clients.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.view_clients import ViewClients
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


protocols = [
        "NFS",
    ] # [str] | Specifies a list of protocols to filter the clients. (optional)
view_ids = [
        1,
    ] # [int] | Specifies a list of View ids. Only clients connected to these Views will be returned. (optional)
node_ip = "nodeIp_example" # str | Specifies a node ip. Only clients connected to this node will be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get View Clients.
	api_response = client.views.get_view_clients(protocols=protocols, view_ids=view_ids, node_ip=node_ip)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->get_view_clients: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocols** | **[str]**| Specifies a list of protocols to filter the clients. | [optional]
 **view_ids** | **[int]**| Specifies a list of View ids. Only clients connected to these Views will be returned. | [optional]
 **node_ip** | **str**| Specifies a node ip. Only clients connected to this node will be returned. | [optional]

### Return type

[**ViewClients**](ViewClients.md)

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

# **get_view_clients_summary**
> ViewClientsSummary get_view_clients_summary()

Get View Clients Summary.

Get View Clients Summary.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.view_clients_summary import ViewClientsSummary
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


view_ids = [
        1,
    ] # [int] | Specifies a list of View ids. Only clients connected to these Views will be included in the summary. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get View Clients Summary.
	api_response = client.views.get_view_clients_summary(view_ids=view_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->get_view_clients_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_ids** | **[int]**| Specifies a list of View ids. Only clients connected to these Views will be included in the summary. | [optional]

### Return type

[**ViewClientsSummary**](ViewClientsSummary.md)

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

# **get_view_directory_quotas**
> ViewDirectoryQuotas get_view_directory_quotas(id)

Get directory quotas for the View.

Get directory quotas for the View.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.view_directory_quotas import ViewDirectoryQuotas
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the View id.
max_count = 1 # int | Specifies a limit on the number of quotas returned. (optional)
cookie = 1 # int | Specifies the cookie. (optional)

# example passing only required values which don't have defaults set
try:
	# Get directory quotas for the View.
	api_response = client.views.get_view_directory_quotas(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->get_view_directory_quotas: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get directory quotas for the View.
	api_response = client.views.get_view_directory_quotas(id, max_count=max_count, cookie=cookie)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->get_view_directory_quotas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the View id. |
 **max_count** | **int**| Specifies a limit on the number of quotas returned. | [optional]
 **cookie** | **int**| Specifies the cookie. | [optional]

### Return type

[**ViewDirectoryQuotas**](ViewDirectoryQuotas.md)

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

# **get_view_user_quotas**
> ViewUserQuotas get_view_user_quotas(id)

Get user quotas for the View.

Get user quotas for the View.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.view_user_quotas import ViewUserQuotas
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the View id.
max_count = 1 # int | Specifies a limit on the number of quotas returned. (optional)
cookie = "cookie_example" # str | Specifies the cookie. (optional)

# example passing only required values which don't have defaults set
try:
	# Get user quotas for the View.
	api_response = client.views.get_view_user_quotas(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->get_view_user_quotas: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get user quotas for the View.
	api_response = client.views.get_view_user_quotas(id, max_count=max_count, cookie=cookie)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->get_view_user_quotas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the View id. |
 **max_count** | **int**| Specifies a limit on the number of quotas returned. | [optional]
 **cookie** | **str**| Specifies the cookie. | [optional]

### Return type

[**ViewUserQuotas**](ViewUserQuotas.md)

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

# **get_view_user_quotas_config**
> ViewUserQuotasConfig get_view_user_quotas_config(id)

Get View user quotas config.

Get View user quotas config.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.view_user_quotas_config import ViewUserQuotasConfig
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the View id.

# example passing only required values which don't have defaults set
try:
	# Get View user quotas config.
	api_response = client.views.get_view_user_quotas_config(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->get_view_user_quotas_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the View id. |

### Return type

[**ViewUserQuotasConfig**](ViewUserQuotasConfig.md)

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

# **get_views**
> GetViewsResult get_views()

List Views

If no parameters are specified, all Views on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned. NOTE: If maxCount is set and the number of Views returned exceeds the maxCount, there are more Views to return. To get the next set of Views, send another request and specify the id of the last View returned in viewList from the previous response.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.get_views_result import GetViewsResult
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


view_names = [
        "viewNames_example",
    ] # [str] | Filter by a list of View names. (optional)
view_ids = [
        1,
    ] # [int] | Filter by a list of View ids. (optional)
storage_domain_ids = [
        1,
    ] # [int] | Filter by a list of Storage Domains (View Boxes) specified by id. (optional)
storage_domain_names = [
        "storageDomainNames_example",
    ] # [str] | Filter by a list of View Box names. (optional)
protocol_accesses = [
        "NFS",
    ] # [str] | Filter by a list of protocol accesses. Only views with protocol accesses in these specified accesses list will be returned. (optional)
match_partial_names = True # bool | If true, the names in viewNames are matched by any partial rather than exactly matched. (optional)
max_count = 1 # int | Specifies a limit on the number of Views returned. (optional)
include_internal_views = True # bool | Specifies if internal Views created by the Cohesity Cluster are also returned. In addition, regular Views are returned. (optional)
include_protection_groups = True # bool | Specifies if Protection Groups information needs to be returned along with view metadata. By default, if not set or set to true, Group information is returned. (optional)
max_view_id = 1 # int | If the number of Views to return exceeds the maxCount specified in the original request, specify the id of the last View from the viewList in the previous response to get the next set of Views. (optional)
include_inactive = True # bool | Specifies if inactive Views on this Remote Cluster (which have Snapshots copied by replication) should also be returned. Inactive Views are not counted towards the maxCount. By default, this field is set to false. (optional)
protection_group_ids = [
        1,
    ] # [int] | This field will be deprecated. Filter by Protection Group ids. Return Views that are being protected by listed Groups, which are specified by ids. If both protectionGroupIds and viewProtectionGroupIds are specified, only viewProtectionGroupIds will be used. (optional)
view_protection_group_ids = [
        "viewProtectionGroupIds_example",
    ] # [str] | Filter by Protection Group ids. Return Views that are being protected by listed Groups, which are specified by ids. (optional)
view_count_only = True # bool | Whether to get just the total number of views with the given input filters. If the flag is true, we ignore the parameter 'maxViews' for the count. Also, if flag is true, list of views will not be returned. (optional)
summary_only = True # bool | Whether to get only view summary including 'name', 'viewId', 'storageDomainName', 'storageDomainId' and 'tenantId'. (optional)
sort_by_logical_usage = True # bool | If set to true, the list is sorted descending by logical usage. (optional)
internal_access_sids = [
        "internalAccessSids_example",
    ] # [str] | Sids of restricted principals who can access the view. This is an internal field and therefore does not have json tag. (optional)
match_alias_names = True # bool | If true, view aliases are also matched with the names in viewNames. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
include_tenants = True # bool | IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)
include_stats = True # bool | If set to true, stats of views will be returned. By default this parameter is set to false. (optional)
include_file_count_by_size = True # bool | Whether to include View file count by size. (optional)
include_views_with_antivirus_enabled_only = True # bool | If set to true, the list will contain only the views for which antivirus scan is enabled. (optional)
include_views_with_data_lock_enabled_only = True # bool | If set to true, the list will contain only the views for which either file level data lock is enabled or view level data lock is enabled. (optional)
filer_audit_log_enabled = True # bool | If set to true, only views with filer audit log enabled will be returned. If set to false, only views with filer audit log disabled will be returned. (optional)
categories = [
        "BackupTarget",
    ] # [str] | Filter by a list of View categories. (optional)
view_protection_types = [
        "Local",
    ] # [str] | Filter by a list of View protection types. (optional)
last_run_any_statuses = [
        "Accepted",
    ] # [str] | Filter by last any run status of the view.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages. (optional)
last_run_local_backup_statuses = [
        "Accepted",
    ] # [str] | Filter by last local backup run status of the view.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages. (optional)
last_run_replication_statuses = [
        "Accepted",
    ] # [str] | Filter by last remote replication run status of the view.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages. (optional)
last_run_archival_statuses = [
        "Accepted",
    ] # [str] | Filter by last cloud archival run status of the view.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List Views
	api_response = client.views.get_views(view_names=view_names, view_ids=view_ids, storage_domain_ids=storage_domain_ids, storage_domain_names=storage_domain_names, protocol_accesses=protocol_accesses, match_partial_names=match_partial_names, max_count=max_count, include_internal_views=include_internal_views, include_protection_groups=include_protection_groups, max_view_id=max_view_id, include_inactive=include_inactive, protection_group_ids=protection_group_ids, view_protection_group_ids=view_protection_group_ids, view_count_only=view_count_only, summary_only=summary_only, sort_by_logical_usage=sort_by_logical_usage, internal_access_sids=internal_access_sids, match_alias_names=match_alias_names, tenant_ids=tenant_ids, include_tenants=include_tenants, include_stats=include_stats, include_file_count_by_size=include_file_count_by_size, include_views_with_antivirus_enabled_only=include_views_with_antivirus_enabled_only, include_views_with_data_lock_enabled_only=include_views_with_data_lock_enabled_only, filer_audit_log_enabled=filer_audit_log_enabled, categories=categories, view_protection_types=view_protection_types, last_run_any_statuses=last_run_any_statuses, last_run_local_backup_statuses=last_run_local_backup_statuses, last_run_replication_statuses=last_run_replication_statuses, last_run_archival_statuses=last_run_archival_statuses)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->get_views: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_names** | **[str]**| Filter by a list of View names. | [optional]
 **view_ids** | **[int]**| Filter by a list of View ids. | [optional]
 **storage_domain_ids** | **[int]**| Filter by a list of Storage Domains (View Boxes) specified by id. | [optional]
 **storage_domain_names** | **[str]**| Filter by a list of View Box names. | [optional]
 **protocol_accesses** | **[str]**| Filter by a list of protocol accesses. Only views with protocol accesses in these specified accesses list will be returned. | [optional]
 **match_partial_names** | **bool**| If true, the names in viewNames are matched by any partial rather than exactly matched. | [optional]
 **max_count** | **int**| Specifies a limit on the number of Views returned. | [optional]
 **include_internal_views** | **bool**| Specifies if internal Views created by the Cohesity Cluster are also returned. In addition, regular Views are returned. | [optional]
 **include_protection_groups** | **bool**| Specifies if Protection Groups information needs to be returned along with view metadata. By default, if not set or set to true, Group information is returned. | [optional]
 **max_view_id** | **int**| If the number of Views to return exceeds the maxCount specified in the original request, specify the id of the last View from the viewList in the previous response to get the next set of Views. | [optional]
 **include_inactive** | **bool**| Specifies if inactive Views on this Remote Cluster (which have Snapshots copied by replication) should also be returned. Inactive Views are not counted towards the maxCount. By default, this field is set to false. | [optional]
 **protection_group_ids** | **[int]**| This field will be deprecated. Filter by Protection Group ids. Return Views that are being protected by listed Groups, which are specified by ids. If both protectionGroupIds and viewProtectionGroupIds are specified, only viewProtectionGroupIds will be used. | [optional]
 **view_protection_group_ids** | **[str]**| Filter by Protection Group ids. Return Views that are being protected by listed Groups, which are specified by ids. | [optional]
 **view_count_only** | **bool**| Whether to get just the total number of views with the given input filters. If the flag is true, we ignore the parameter &#39;maxViews&#39; for the count. Also, if flag is true, list of views will not be returned. | [optional]
 **summary_only** | **bool**| Whether to get only view summary including &#39;name&#39;, &#39;viewId&#39;, &#39;storageDomainName&#39;, &#39;storageDomainId&#39; and &#39;tenantId&#39;. | [optional]
 **sort_by_logical_usage** | **bool**| If set to true, the list is sorted descending by logical usage. | [optional]
 **internal_access_sids** | **[str]**| Sids of restricted principals who can access the view. This is an internal field and therefore does not have json tag. | [optional]
 **match_alias_names** | **bool**| If true, view aliases are also matched with the names in viewNames. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which objects are to be returned. | [optional]
 **include_tenants** | **bool**| IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional]
 **include_stats** | **bool**| If set to true, stats of views will be returned. By default this parameter is set to false. | [optional]
 **include_file_count_by_size** | **bool**| Whether to include View file count by size. | [optional]
 **include_views_with_antivirus_enabled_only** | **bool**| If set to true, the list will contain only the views for which antivirus scan is enabled. | [optional]
 **include_views_with_data_lock_enabled_only** | **bool**| If set to true, the list will contain only the views for which either file level data lock is enabled or view level data lock is enabled. | [optional]
 **filer_audit_log_enabled** | **bool**| If set to true, only views with filer audit log enabled will be returned. If set to false, only views with filer audit log disabled will be returned. | [optional]
 **categories** | **[str]**| Filter by a list of View categories. | [optional]
 **view_protection_types** | **[str]**| Filter by a list of View protection types. | [optional]
 **last_run_any_statuses** | **[str]**| Filter by last any run status of the view.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. | [optional]
 **last_run_local_backup_statuses** | **[str]**| Filter by last local backup run status of the view.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. | [optional]
 **last_run_replication_statuses** | **[str]**| Filter by last remote replication run status of the view.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. | [optional]
 **last_run_archival_statuses** | **[str]**| Filter by last cloud archival run status of the view.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages. | [optional]

### Return type

[**GetViewsResult**](GetViewsResult.md)

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

# **get_views_summary**
> ViewsSummary get_views_summary()

Get Views summary.

Get Views summary.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.views_summary import ViewsSummary
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get Views summary.
	api_response = client.views.get_views_summary()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->get_views_summary: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ViewsSummary**](ViewsSummary.md)

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

# **read_view_template_by_id**
> Template read_view_template_by_id(id)

Read a View Template by Id

Reads a view template based on given template id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.template import Template
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies a unique id of the view template.

# example passing only required values which don't have defaults set
try:
	# Read a View Template by Id
	api_response = client.views.read_view_template_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->read_view_template_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the view template. |

### Return type

[**Template**](Template.md)

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

# **read_view_templates**
> GetViewTemplatesResult read_view_templates()

List View Templates

All view templates on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.get_view_templates_result import GetViewTemplatesResult
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# List View Templates
	api_response = client.views.read_view_templates()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->read_view_templates: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetViewTemplatesResult**](GetViewTemplatesResult.md)

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

# **update_share**
> Share update_share(name, body)

Update a Share.

Update a Share.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.update_share_param import UpdateShareParam
from cohesity_sdk.cohesity_client_v2.model.share import Share
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


name = "name_example" # str | Specifies the Share name to update.
body = UpdateShareParam(
        enable_filer_audit_logging=True,
        smb_config={},
        client_subnet_whitelist=[
            Subnet(
                component="component_example",
                description="description_example",
                gateway="gateway_example",
                id=1,
                ip="ip_example",
                netmask_bits=1,
                netmask_ip4="netmask_ip4_example",
                nfs_access="kDisabled",
                nfs_squash="kNone",
                smb_access="kDisabled",
                s3_access="kDisabled",
            ),
        ],
    ) # UpdateShareParam | Specifies the request to update a Share.

# example passing only required values which don't have defaults set
try:
	# Update a Share.
	api_response = client.views.update_share(name, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->update_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the Share name to update. |
 **body** | [**UpdateShareParam**](UpdateShareParam.md)| Specifies the request to update a Share. |

### Return type

[**Share**](Share.md)

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

# **update_view**
> View update_view(id, body)

Update a View

Updates a View based on given id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.view import View
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies a unique id of the View to update.
body = View() # View | Request to update a view.

# example passing only required values which don't have defaults set
try:
	# Update a View
	api_response = client.views.update_view(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->update_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the View to update. |
 **body** | [**View**](View.md)| Request to update a view. |

### Return type

[**View**](View.md)

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

# **update_view_directory_quota**
> ViewDirectoryQuota update_view_directory_quota(id, body)

Upadte directory quota for the View.

Update directory quota for the View.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.view_directory_quota import ViewDirectoryQuota
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the View id.
body = ViewDirectoryQuota(
        directory_path="directory_path_example",
        quota_policy={},
    ) # ViewDirectoryQuota | Specifies the request to update directory quota.

# example passing only required values which don't have defaults set
try:
	# Upadte directory quota for the View.
	api_response = client.views.update_view_directory_quota(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->update_view_directory_quota: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the View id. |
 **body** | [**ViewDirectoryQuota**](ViewDirectoryQuota.md)| Specifies the request to update directory quota. |

### Return type

[**ViewDirectoryQuota**](ViewDirectoryQuota.md)

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

# **update_view_template**
> Template update_view_template(id, body)

Update a View Template

Updates a View Template.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.template import Template
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies a unique id of the view template.
body = Template(
        name="name_example",
        dedup=True,
        compress=True,
        view_params={},
    ) # Template | Request to update a view template.

# example passing only required values which don't have defaults set
try:
	# Update a View Template
	api_response = client.views.update_view_template(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewsApi->update_view_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the view template. |
 **body** | [**Template**](Template.md)| Request to update a view template. |

### Return type

[**Template**](Template.md)

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

