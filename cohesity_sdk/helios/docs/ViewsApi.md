# cohesity_sdk.ViewsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_view**](ViewsApi.md#create_view) | **POST** /file-services/views | Create a View
[**create_view_template**](ViewsApi.md#create_view_template) | **POST** /file-services/view-template | Create a View Template
[**delete_view**](ViewsApi.md#delete_view) | **DELETE** /file-services/views/{id} | Delete a View
[**delete_view_template**](ViewsApi.md#delete_view_template) | **DELETE** /file-services/view-template/{id} | Delete a View Template
[**get_view_by_id**](ViewsApi.md#get_view_by_id) | **GET** /file-services/views/{id} | Get a View by Id
[**get_views**](ViewsApi.md#get_views) | **GET** /file-services/views | List Views
[**read_view_template_by_id**](ViewsApi.md#read_view_template_by_id) | **GET** /file-services/view-template/{id} | Read a View Template by Id
[**read_view_templates**](ViewsApi.md#read_view_templates) | **GET** /file-services/view-template | List View Templates
[**update_view**](ViewsApi.md#update_view) | **PUT** /file-services/views/{id} | Update a View
[**update_view_template**](ViewsApi.md#update_view_template) | **PUT** /file-services/view-template/{id} | Update a View Template


# **create_view**
> View create_view(body)

Create a View

Creates a View.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.view import View
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.create_view_request import CreateViewRequest
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.template import Template
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


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

# **delete_view**
> delete_view(id)

Delete a View

Deletes a View based on given id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


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

# **delete_view_template**
> delete_view_template(id)

Delete a View Template

Deletes a view template based on given template id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


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

# **get_view_by_id**
> View get_view_by_id(id)

Get a View by Id

Get a View based on given Id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.view import View
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies a unique id of the View to delete.

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
 **id** | **int**| Specifies a unique id of the View to delete. |

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

# **get_views**
> GetViewsResult get_views()

List Views

If no parameters are specified, all Views on the Cohesity Cluster are returned.   Specifying parameters filters the results that are returned.   NOTE: If maxCount is set and the number of Views returned exceeds the maxCount,   there are more Views to return.   To get the next set of Views, send another request and specify the id of the   last View returned in viewList from the previous response.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.get_views_result import GetViewsResult
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


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
    ] # [str] | Filter by a list of protocol accesses. Only views with   protocol accesses in these specified accesses list will be returned. (optional)
match_partial_names = True # bool | If true, the names in viewNames are matched by any partial rather than   exactly matched. (optional)
max_count = 1 # int | Specifies a limit on the number of Views returned. (optional)
include_internal_views = True # bool | Specifies if internal Views created by the Cohesity Cluster are   also returned. In addition, regular Views are returned. (optional)
include_protection_groups = True # bool | Specifies if Protection Groups information needs to be returned along with   view metadata. By default, if not set or set to true, Group information is   returned. (optional)
max_view_id = 1 # int | If the number of Views to return exceeds the maxCount specified in the   original request, specify the id of the last View   from the viewList in the previous response   to get the next set of Views. (optional)
include_inactive = True # bool | Specifies if inactive Views on this Remote Cluster (which have   Snapshots copied by replication) should also be returned.   Inactive Views are not counted towards the maxCount.   By default, this field is set to false. (optional)
protection_group_ids = [
        1,
    ] # [int] | This field will be deprecated. Filter by Protection Group ids.   Return Views that are being protected by listed Groups, which are specified by ids.   If both protectionGroupIds and viewProtectionGroupIds are specified, only   viewProtectionGroupIds will be used. (optional)
view_protection_group_ids = [
        "viewProtectionGroupIds_example",
    ] # [str] | Filter by Protection Group ids. Return Views that are being protected by   listed Groups, which are specified by ids. (optional)
view_count_only = True # bool | Whether to get just the total number of views with the given input   filters. If the flag is true, we ignore the parameter 'maxViews' for the   count. Also, if flag is true, list of views will not be returned. (optional)
sort_by_logical_usage = True # bool | If set to true, the list is sorted descending by logical usage. (optional)
internal_access_sids = [
        "internalAccessSids_example",
    ] # [str] | Sids of restricted principals who can access the view. This is an   internal field and therefore does not have json tag. (optional)
match_alias_names = True # bool | If true, view aliases are also matched with the names in viewNames. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which objects are to be   returned. (optional)
include_tenants = True # bool | IncludeTenants specifies if objects of all the tenants under the   hierarchy of the logged in user's organization should be returned. (optional)
include_stats = True # bool | If set to true, stats of views will be returned. By default this parameter   is set to false. (optional)
include_file_count_by_size = True # bool | Whether to include View file count by size. (optional)
include_views_with_antivirus_enabled_only = True # bool | If set to true, the list will contain only the views for which antivirus   scan is enabled. (optional)
include_views_with_data_lock_enabled_only = True # bool | If set to true, the list will contain only the views for which either   file level data lock is enabled or view level data lock is enabled. (optional)
filer_audit_log_enabled = True # bool | If set to true, only views with filer audit log enabled will be returned.   If set to false, only views with filer audit log disabled will be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List Views
	api_response = client.views.get_views(view_names=view_names, view_ids=view_ids, storage_domain_ids=storage_domain_ids, storage_domain_names=storage_domain_names, protocol_accesses=protocol_accesses, match_partial_names=match_partial_names, max_count=max_count, include_internal_views=include_internal_views, include_protection_groups=include_protection_groups, max_view_id=max_view_id, include_inactive=include_inactive, protection_group_ids=protection_group_ids, view_protection_group_ids=view_protection_group_ids, view_count_only=view_count_only, sort_by_logical_usage=sort_by_logical_usage, internal_access_sids=internal_access_sids, match_alias_names=match_alias_names, tenant_ids=tenant_ids, include_tenants=include_tenants, include_stats=include_stats, include_file_count_by_size=include_file_count_by_size, include_views_with_antivirus_enabled_only=include_views_with_antivirus_enabled_only, include_views_with_data_lock_enabled_only=include_views_with_data_lock_enabled_only, filer_audit_log_enabled=filer_audit_log_enabled)
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
 **protocol_accesses** | **[str]**| Filter by a list of protocol accesses. Only views with   protocol accesses in these specified accesses list will be returned. | [optional]
 **match_partial_names** | **bool**| If true, the names in viewNames are matched by any partial rather than   exactly matched. | [optional]
 **max_count** | **int**| Specifies a limit on the number of Views returned. | [optional]
 **include_internal_views** | **bool**| Specifies if internal Views created by the Cohesity Cluster are   also returned. In addition, regular Views are returned. | [optional]
 **include_protection_groups** | **bool**| Specifies if Protection Groups information needs to be returned along with   view metadata. By default, if not set or set to true, Group information is   returned. | [optional]
 **max_view_id** | **int**| If the number of Views to return exceeds the maxCount specified in the   original request, specify the id of the last View   from the viewList in the previous response   to get the next set of Views. | [optional]
 **include_inactive** | **bool**| Specifies if inactive Views on this Remote Cluster (which have   Snapshots copied by replication) should also be returned.   Inactive Views are not counted towards the maxCount.   By default, this field is set to false. | [optional]
 **protection_group_ids** | **[int]**| This field will be deprecated. Filter by Protection Group ids.   Return Views that are being protected by listed Groups, which are specified by ids.   If both protectionGroupIds and viewProtectionGroupIds are specified, only   viewProtectionGroupIds will be used. | [optional]
 **view_protection_group_ids** | **[str]**| Filter by Protection Group ids. Return Views that are being protected by   listed Groups, which are specified by ids. | [optional]
 **view_count_only** | **bool**| Whether to get just the total number of views with the given input   filters. If the flag is true, we ignore the parameter &#39;maxViews&#39; for the   count. Also, if flag is true, list of views will not be returned. | [optional]
 **sort_by_logical_usage** | **bool**| If set to true, the list is sorted descending by logical usage. | [optional]
 **internal_access_sids** | **[str]**| Sids of restricted principals who can access the view. This is an   internal field and therefore does not have json tag. | [optional]
 **match_alias_names** | **bool**| If true, view aliases are also matched with the names in viewNames. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which objects are to be   returned. | [optional]
 **include_tenants** | **bool**| IncludeTenants specifies if objects of all the tenants under the   hierarchy of the logged in user&#39;s organization should be returned. | [optional]
 **include_stats** | **bool**| If set to true, stats of views will be returned. By default this parameter   is set to false. | [optional]
 **include_file_count_by_size** | **bool**| Whether to include View file count by size. | [optional]
 **include_views_with_antivirus_enabled_only** | **bool**| If set to true, the list will contain only the views for which antivirus   scan is enabled. | [optional]
 **include_views_with_data_lock_enabled_only** | **bool**| If set to true, the list will contain only the views for which either   file level data lock is enabled or view level data lock is enabled. | [optional]
 **filer_audit_log_enabled** | **bool**| If set to true, only views with filer audit log enabled will be returned.   If set to false, only views with filer audit log disabled will be returned. | [optional]

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

# **read_view_template_by_id**
> Template read_view_template_by_id(id)

Read a View Template by Id

Reads a view template based on given template id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.template import Template
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


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

All view templates on the Cohesity Cluster are returned.   Specifying parameters filters the results that are returned.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.get_view_templates_result import GetViewTemplatesResult
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)



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

# **update_view**
> View update_view(id, body)

Update a View

Updates a View based on given id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.view import View
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


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

# **update_view_template**
> Template update_view_template(id, body)

Update a View Template

Updates a View Template.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.template import Template
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


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

