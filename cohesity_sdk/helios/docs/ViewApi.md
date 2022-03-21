# cohesity_sdk.ViewApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**add_view_user_quota_overrides**](ViewApi.md#add_view_user_quota_overrides) | **POST** /file-services/views/{viewId}/user-quotas | Add User Quota overrides.
[**clear_nlm_locks**](ViewApi.md#clear_nlm_locks) | **DELETE** /file-services/nlm-locks | Clear NLM locks.
[**clone_view**](ViewApi.md#clone_view) | **POST** /file-services/views/{id}/clone | Clone View.
[**clone_view_directory**](ViewApi.md#clone_view_directory) | **POST** /file-services/views/clone-directory | Clone View Directory.
[**close_smb_file_open**](ViewApi.md#close_smb_file_open) | **DELETE** /file-services/smb-file-opens | Close SMB File open.
[**create_share**](ViewApi.md#create_share) | **POST** /file-services/shares | Create a Share.
[**create_view**](ViewApi.md#create_view) | **POST** /file-services/views | Create a View
[**create_view_template**](ViewApi.md#create_view_template) | **POST** /file-services/view-template | Create a View Template
[**delete_share**](ViewApi.md#delete_share) | **DELETE** /file-services/shares/{name} | Delete a Share.
[**delete_view**](ViewApi.md#delete_view) | **DELETE** /file-services/views/{id} | Delete a View
[**delete_view_directory_quota**](ViewApi.md#delete_view_directory_quota) | **DELETE** /file-services/views/{id}/directory-quotas | Delete directory quota for the View.
[**delete_view_template**](ViewApi.md#delete_view_template) | **DELETE** /file-services/view-template/{id} | Delete a View Template
[**delete_view_user_quota_overrides**](ViewApi.md#delete_view_user_quota_overrides) | **DELETE** /file-services/views/{viewId}/user-quotas | Delete user quota overrides.
[**get_file_lock_status**](ViewApi.md#get_file_lock_status) | **GET** /file-services/views/{id}/file-lock | Get file lock status
[**get_nlm_locks**](ViewApi.md#get_nlm_locks) | **GET** /file-services/nlm-locks | Get NLM locks.
[**get_qos_policies**](ViewApi.md#get_qos_policies) | **GET** /file-services/qos-policies | Get QoS Policies.
[**get_shares**](ViewApi.md#get_shares) | **GET** /file-services/shares | Get Shares.
[**get_view_by_id**](ViewApi.md#get_view_by_id) | **GET** /file-services/views/{id} | Get a View by Id
[**get_view_clients**](ViewApi.md#get_view_clients) | **GET** /file-services/view-clients | Get View Clients.
[**get_view_clients_summary**](ViewApi.md#get_view_clients_summary) | **GET** /file-services/view-clients/summary | Get View Clients Summary.
[**get_view_directory_quotas**](ViewApi.md#get_view_directory_quotas) | **GET** /file-services/views/{id}/directory-quotas | Get directory quotas for the View.
[**get_view_user_quotas**](ViewApi.md#get_view_user_quotas) | **GET** /file-services/views/{viewId}/user-quotas | Get View user quotas.
[**get_views**](ViewApi.md#get_views) | **GET** /file-services/views | List Views
[**get_views_summary**](ViewApi.md#get_views_summary) | **GET** /file-services/views-summary | Get Views summary.
[**list_smb_file_opens**](ViewApi.md#list_smb_file_opens) | **GET** /file-services/smb-file-opens | Get SMB File opens.
[**lock_file**](ViewApi.md#lock_file) | **POST** /file-services/views/{id}/file-lock | Create a file-lock
[**overwrite_view**](ViewApi.md#overwrite_view) | **POST** /file-services/views/{id}/overwrite | Overwrite View.
[**read_view_template_by_id**](ViewApi.md#read_view_template_by_id) | **GET** /file-services/view-template/{id} | Read a View Template by Id
[**read_view_templates**](ViewApi.md#read_view_templates) | **GET** /file-services/view-template | List View Templates
[**update_share**](ViewApi.md#update_share) | **PUT** /file-services/shares/{name} | Update a Share.
[**update_view**](ViewApi.md#update_view) | **PUT** /file-services/views/{id} | Update a View
[**update_view_directory_quota**](ViewApi.md#update_view_directory_quota) | **PUT** /file-services/views/{id}/directory-quotas | Update directory quota for the View.
[**update_view_template**](ViewApi.md#update_view_template) | **PUT** /file-services/view-template/{id} | Update a View Template
[**update_view_user_quota_override**](ViewApi.md#update_view_user_quota_override) | **PUT** /file-services/views/{viewId}/user-quotas/{userId} | Update user quota override.
[**update_view_user_quota_settings**](ViewApi.md#update_view_user_quota_settings) | **PUT** /file-services/views/{viewId}/user-quotas | Update View user quota settings.


# **add_view_user_quota_overrides**
> UserQuotaOverrides add_view_user_quota_overrides(view_id, body)

Add User Quota overrides.

Specifies the parameters to override the user quota on the view. User quota on the view should be enabled before setting a user override.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.user_quota_overrides import UserQuotaOverrides
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


view_id = 1 # int | Specifies the id of a view.
body = UserQuotaOverrides(
        user_quotas=[
            UserQuota(),
        ],
        cookie="cookie_example",
        override_existing_per_user_quotas=True,
    ) # UserQuotaOverrides | Specifies the parameters to override the default user quota on the view.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Add User Quota overrides.
	api_response = client.view.add_view_user_quota_overrides(view_id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->add_view_user_quota_overrides: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Add User Quota overrides.
	api_response = client.view.add_view_user_quota_overrides(view_id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->add_view_user_quota_overrides: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **int**| Specifies the id of a view. |
 **body** | [**UserQuotaOverrides**](UserQuotaOverrides.md)| Specifies the parameters to override the default user quota on the view. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**UserQuotaOverrides**](UserQuotaOverrides.md)

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

# **clear_nlm_locks**
> clear_nlm_locks(body)

Clear NLM locks.

Clear NLM locks that match the filter criteria specified using parameters

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.clear_nlm_lock_request import ClearNlmLockRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = ClearNlmLockRequest(
        file_path="file_path_example",
        view_name="view_name_example",
        client_id="client_id_example",
    ) # ClearNlmLockRequest | Request to clear NLM lock.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Clear NLM locks.
	client.view.clear_nlm_locks(body)
except ApiException as e:
	print("Exception when calling ViewApi->clear_nlm_locks: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Clear NLM locks.
	client.view.clear_nlm_locks(body, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling ViewApi->clear_nlm_locks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClearNlmLockRequest**](ClearNlmLockRequest.md)| Request to clear NLM lock. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_view**
> View clone_view(id, body)

Clone View.

Clone View.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.clone_view_params import CloneViewParams
from cohesity_sdk.helios.model.view import View
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the View id to clone.
body = CloneViewParams(
        name="name_example",
        description="description_example",
        data_lock_expiry_usecs=1,
        storage_policy_override={},
        qos={},
        subnet_whitelist=[
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
        protocol_access=[
            ViewProtocol(
                type="NFS",
                mode="ReadOnly",
            ),
        ],
        netgroup_whitelist={},
        is_read_only=True,
    ) # CloneViewParams | Specifies the request to clone the View.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Clone View.
	api_response = client.view.clone_view(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->clone_view: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Clone View.
	api_response = client.view.clone_view(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->clone_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the View id to clone. |
 **body** | [**CloneViewParams**](CloneViewParams.md)| Specifies the request to clone the View. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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

# **clone_view_directory**
> clone_view_directory(body)

Clone View Directory.

Clone View Directory.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.clone_view_directory_params import CloneViewDirectoryParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = CloneViewDirectoryParams(
        source_directory_path="source_directory_path_example",
        target_parent_directory_path="target_parent_directory_path_example",
        target_directory_name="target_directory_name_example",
    ) # CloneViewDirectoryParams | Specifies the request to clone View directory.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Clone View Directory.
	client.view.clone_view_directory(body)
except ApiException as e:
	print("Exception when calling ViewApi->clone_view_directory: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Clone View Directory.
	client.view.clone_view_directory(body, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling ViewApi->clone_view_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloneViewDirectoryParams**](CloneViewDirectoryParams.md)| Specifies the request to clone View directory. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_smb_file_open**
> close_smb_file_open()

Close SMB File open.

Close an active SMB file open.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.close_smb_file_open_params import CloseSmbFileOpenParams
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
body = CloseSmbFileOpenParams(
        file_path="file_path_example",
        view_name="view_name_example",
        open_id=1,
    ) # CloseSmbFileOpenParams | Specifies parameters to close active  SMB file open. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Close SMB File open.
	client.view.close_smb_file_open(access_cluster_id=access_cluster_id, region_id=region_id, body=body)
except ApiException as e:
	print("Exception when calling ViewApi->close_smb_file_open: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **body** | [**CloseSmbFileOpenParams**](CloseSmbFileOpenParams.md)| Specifies parameters to close active  SMB file open. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_share**
> Share create_share(body)

Create a Share.

Create a Share.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.share import Share
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = Share() # Share | Specifies the request to create a Share.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a Share.
	api_response = client.view.create_share(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->create_share: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a Share.
	api_response = client.view.create_share(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->create_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Share**](Share.md)| Specifies the request to create a Share. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.view import View
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.create_view_request import CreateViewRequest
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = CreateViewRequest() # CreateViewRequest | Request to create a View.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a View
	api_response = client.view.create_view(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->create_view: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a View
	api_response = client.view.create_view(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->create_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateViewRequest**](CreateViewRequest.md)| Request to create a View. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a View Template
	api_response = client.view.create_view_template(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->create_view_template: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a View Template
	api_response = client.view.create_view_template(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->create_view_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Template**](Template.md)| Request to create a view template. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


name = "name_example" # str | Specifies the Share name to delete.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete a Share.
	client.view.delete_share(name)
except ApiException as e:
	print("Exception when calling ViewApi->delete_share: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete a Share.
	client.view.delete_share(name, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling ViewApi->delete_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the Share name to delete. |
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
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete a View
	client.view.delete_view(id)
except ApiException as e:
	print("Exception when calling ViewApi->delete_view: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete a View
	client.view.delete_view(id, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling ViewApi->delete_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the View to delete. |
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

# **delete_view_directory_quota**
> delete_view_directory_quota(id)

Delete directory quota for the View.

Delete directory quota for the View.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the View id.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
directory_path = "directoryPath_example" # str | Specifies the directory path to delete. Exactly one of 'directoryPath' and 'deleteAllDirectoryQuotas' should be provided. (optional)
delete_all_directory_quotas = True # bool | Specifies whether to delete all directory quotas for this view. Exactly one of 'directoryPath' and 'deleteAllDirectoryQuotas' should be provided. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete directory quota for the View.
	client.view.delete_view_directory_quota(id)
except ApiException as e:
	print("Exception when calling ViewApi->delete_view_directory_quota: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete directory quota for the View.
	client.view.delete_view_directory_quota(id, access_cluster_id=access_cluster_id, region_id=region_id, directory_path=directory_path, delete_all_directory_quotas=delete_all_directory_quotas)
except ApiException as e:
	print("Exception when calling ViewApi->delete_view_directory_quota: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the View id. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies a unique id of the view template to delete.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete a View Template
	client.view.delete_view_template(id)
except ApiException as e:
	print("Exception when calling ViewApi->delete_view_template: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete a View Template
	client.view.delete_view_template(id, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling ViewApi->delete_view_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the view template to delete. |
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

# **delete_view_user_quota_overrides**
> delete_view_user_quota_overrides(view_id, body)

Delete user quota overrides.

Specifies the parameters to delete user quotas on the view.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.user_quota_delete_params import UserQuotaDeleteParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


view_id = 1 # int | Specifies the id of a view.
body = UserQuotaDeleteParams(
        user_ids=[
            UserId(
                sid="sid_example",
                unix_uid=1,
            ),
        ],
    ) # UserQuotaDeleteParams | Specifies parameters to delete user quotas.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete user quota overrides.
	client.view.delete_view_user_quota_overrides(view_id, body)
except ApiException as e:
	print("Exception when calling ViewApi->delete_view_user_quota_overrides: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete user quota overrides.
	client.view.delete_view_user_quota_overrides(view_id, body, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling ViewApi->delete_view_user_quota_overrides: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **int**| Specifies the id of a view. |
 **body** | [**UserQuotaDeleteParams**](UserQuotaDeleteParams.md)| Specifies parameters to delete user quotas. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_lock_status**
> FileLockStatus get_file_lock_status(id, path)

Get file lock status

Get the lock status of a file in a view.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.file_lock_status import FileLockStatus
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of a view.
path = "path_example" # str | Specifies the request file path in a view.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get file lock status
	api_response = client.view.get_file_lock_status(id, path)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->get_file_lock_status: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get file lock status
	api_response = client.view.get_file_lock_status(id, path, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->get_file_lock_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of a view. |
 **path** | **str**| Specifies the request file path in a view. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**FileLockStatus**](FileLockStatus.md)

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

# **get_nlm_locks**
> GetNlmLocksResult get_nlm_locks()

Get NLM locks.

Get the list of NLM locks in the views.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.get_nlm_locks_result import GetNlmLocksResult
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
file_path = "filePath_example" # str | Specifies the filepath in the view relative to the root filesystem. If this field is specified, viewName field must also be specified. (optional)
view_name = "viewName_example" # str | Specifies the name of the View in which to search. If a view name is not specified, all the views in the Cluster is searched. This field is mandatory if filePath field is specified. (optional)
max_count = 1 # int | Specifies the maximum number of NLM locks to return in the response. By default, maxCount is set to 1000. At any given instance, maxCount value cannot be set to more than 1000. (optional)
cookie = "cookie_example" # str | Specifies the pagination cookie. If this is set, next set of locks just after the previous response are returned. If this is not set, first set of NLM locks are returned.\" (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get NLM locks.
	api_response = client.view.get_nlm_locks(access_cluster_id=access_cluster_id, region_id=region_id, file_path=file_path, view_name=view_name, max_count=max_count, cookie=cookie)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->get_nlm_locks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **file_path** | **str**| Specifies the filepath in the view relative to the root filesystem. If this field is specified, viewName field must also be specified. | [optional]
 **view_name** | **str**| Specifies the name of the View in which to search. If a view name is not specified, all the views in the Cluster is searched. This field is mandatory if filePath field is specified. | [optional]
 **max_count** | **int**| Specifies the maximum number of NLM locks to return in the response. By default, maxCount is set to 1000. At any given instance, maxCount value cannot be set to more than 1000. | [optional]
 **cookie** | **str**| Specifies the pagination cookie. If this is set, next set of locks just after the previous response are returned. If this is not set, first set of NLM locks are returned.\&quot; | [optional]

### Return type

[**GetNlmLocksResult**](GetNlmLocksResult.md)

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

# **get_qos_policies**
> QosPoliciesResult get_qos_policies()

Get QoS Policies.

Get the list of QoS policies on the Cohesity cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.qos_policies_result import QosPoliciesResult
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get QoS Policies.
	api_response = client.view.get_qos_policies(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->get_qos_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**QosPoliciesResult**](QosPoliciesResult.md)

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

If no parameters are specified, all shares on the Cohesity Cluster are returned. Specifying share name/prefix filters the results that are returned. NOTE: If maxCount is set and the number of Shares returned exceeds the maxCount, there are more Share to return. To get the next set of Views, send another request and specify the pagination cookie from the previous response. If maxCount is not specified, the first 2000 Shares.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.shares import Shares
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
name = "name_example" # str | Specifies the Share name. (optional)
match_partial_name = True # bool | If true, the share name is matched by any partial rather than exactly matched. (optional)
max_count = 1 # int | Specifies a limit on the number of Shares returned. If maxCount is not specified, the first 2000 Shares. (optional)
cookie = "cookie_example" # str | Specifies the pagination cookie. Expected to be empty in the first call to the API. To get the next set of results, set this value to the pagination cookie value returned in the response of the previous call. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
include_tenants = True # bool | IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Shares.
	api_response = client.view.get_shares(access_cluster_id=access_cluster_id, region_id=region_id, name=name, match_partial_name=match_partial_name, max_count=max_count, cookie=cookie, tenant_ids=tenant_ids, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->get_shares: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **name** | **str**| Specifies the Share name. | [optional]
 **match_partial_name** | **bool**| If true, the share name is matched by any partial rather than exactly matched. | [optional]
 **max_count** | **int**| Specifies a limit on the number of Shares returned. If maxCount is not specified, the first 2000 Shares. | [optional]
 **cookie** | **str**| Specifies the pagination cookie. Expected to be empty in the first call to the API. To get the next set of results, set this value to the pagination cookie value returned in the response of the previous call. | [optional]
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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.view import View
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies a unique id of the View to fetch.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get a View by Id
	api_response = client.view.get_view_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->get_view_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a View by Id
	api_response = client.view.get_view_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->get_view_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the View to fetch. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.view_clients import ViewClients
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
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
	api_response = client.view.get_view_clients(access_cluster_id=access_cluster_id, region_id=region_id, protocols=protocols, view_ids=view_ids, node_ip=node_ip)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->get_view_clients: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.view_clients_summary import ViewClientsSummary
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
view_ids = [
        1,
    ] # [int] | Specifies a list of View ids. Only clients connected to these Views will be included in the summary. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get View Clients Summary.
	api_response = client.view.get_view_clients_summary(access_cluster_id=access_cluster_id, region_id=region_id, view_ids=view_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->get_view_clients_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.view_directory_quotas import ViewDirectoryQuotas
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the View id.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
max_count = 1 # int | Specifies a limit on the number of quotas returned. (optional)
cookie = 1 # int | Specifies the cookie. (optional)

# example passing only required values which don't have defaults set
try:
	# Get directory quotas for the View.
	api_response = client.view.get_view_directory_quotas(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->get_view_directory_quotas: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get directory quotas for the View.
	api_response = client.view.get_view_directory_quotas(id, access_cluster_id=access_cluster_id, region_id=region_id, max_count=max_count, cookie=cookie)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->get_view_directory_quotas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the View id. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
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
> ViewUserQuotas get_view_user_quotas(view_id)

Get View user quotas.

Get user quotas for the View.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.view_user_quotas import ViewUserQuotas
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


view_id = 1 # int | Specifies the View id.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
max_count = 1 # int | Specifies a limit on the number of quotas returned. If maxCount is not set, response will have a maximum of 100 results. (optional)
cookie = "cookie_example" # str | Specifies the cookie. If there are more results than maxCount, response will include a cookie with has to be set as part of the next GET request. (optional)
unix_uid = 1 # int | Specifies the user identifier of an Unix user. If a valid unix-id to SID mappings are available (i.e., when mixed mode is enabled) the server will perform the necessary id mapping and return the correct usage irrespective of whether the unix id / SID is provided. (optional)
sid = "sid_example" # str | Specifies the user identifier of a SMB user. If a valid unix-id to SID mappings are available (i.e., when mixed mode is enabled) the server will perform the necessary id mapping and return the correct usage irrespective of whether the unix id / SID is provided. (optional)

# example passing only required values which don't have defaults set
try:
	# Get View user quotas.
	api_response = client.view.get_view_user_quotas(view_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->get_view_user_quotas: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get View user quotas.
	api_response = client.view.get_view_user_quotas(view_id, access_cluster_id=access_cluster_id, region_id=region_id, max_count=max_count, cookie=cookie, unix_uid=unix_uid, sid=sid)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->get_view_user_quotas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **int**| Specifies the View id. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **max_count** | **int**| Specifies a limit on the number of quotas returned. If maxCount is not set, response will have a maximum of 100 results. | [optional]
 **cookie** | **str**| Specifies the cookie. If there are more results than maxCount, response will include a cookie with has to be set as part of the next GET request. | [optional]
 **unix_uid** | **int**| Specifies the user identifier of an Unix user. If a valid unix-id to SID mappings are available (i.e., when mixed mode is enabled) the server will perform the necessary id mapping and return the correct usage irrespective of whether the unix id / SID is provided. | [optional]
 **sid** | **str**| Specifies the user identifier of a SMB user. If a valid unix-id to SID mappings are available (i.e., when mixed mode is enabled) the server will perform the necessary id mapping and return the correct usage irrespective of whether the unix id / SID is provided. | [optional]

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

# **get_views**
> GetViewsResult get_views()

List Views

If no parameters are specified, all Views on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned. NOTE: If maxCount is set and the number of Views returned exceeds the maxCount, there are more Views to return. To get the next set of Views, send another request and specify the id of the last View returned in viewList from the previous response.

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


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
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
is_protected = True # bool | Specifies the protection status of Views. If set to true, only protected Views will be returned. If set to false, only unprotected Views will be returned. (optional)
qos_principal_ids = [
        1,
    ] # [int] | qosPrincipalIds contains ids of the QoS principal for which views are to be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List Views
	api_response = client.view.get_views(access_cluster_id=access_cluster_id, region_id=region_id, view_names=view_names, view_ids=view_ids, storage_domain_ids=storage_domain_ids, storage_domain_names=storage_domain_names, protocol_accesses=protocol_accesses, match_partial_names=match_partial_names, max_count=max_count, include_internal_views=include_internal_views, include_protection_groups=include_protection_groups, max_view_id=max_view_id, include_inactive=include_inactive, protection_group_ids=protection_group_ids, view_protection_group_ids=view_protection_group_ids, view_count_only=view_count_only, summary_only=summary_only, sort_by_logical_usage=sort_by_logical_usage, internal_access_sids=internal_access_sids, match_alias_names=match_alias_names, tenant_ids=tenant_ids, include_tenants=include_tenants, include_stats=include_stats, include_file_count_by_size=include_file_count_by_size, include_views_with_antivirus_enabled_only=include_views_with_antivirus_enabled_only, include_views_with_data_lock_enabled_only=include_views_with_data_lock_enabled_only, filer_audit_log_enabled=filer_audit_log_enabled, categories=categories, view_protection_types=view_protection_types, last_run_any_statuses=last_run_any_statuses, last_run_local_backup_statuses=last_run_local_backup_statuses, last_run_replication_statuses=last_run_replication_statuses, last_run_archival_statuses=last_run_archival_statuses, is_protected=is_protected, qos_principal_ids=qos_principal_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->get_views: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
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
 **is_protected** | **bool**| Specifies the protection status of Views. If set to true, only protected Views will be returned. If set to false, only unprotected Views will be returned. | [optional]
 **qos_principal_ids** | **[int]**| qosPrincipalIds contains ids of the QoS principal for which views are to be returned. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.views_summary import ViewsSummary
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
msecs_before_current_time_to_compare = 1 # int | Specifies the time in msecs before current time to compare with. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Views summary.
	api_response = client.view.get_views_summary(access_cluster_id=access_cluster_id, region_id=region_id, msecs_before_current_time_to_compare=msecs_before_current_time_to_compare)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->get_views_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **msecs_before_current_time_to_compare** | **int**| Specifies the time in msecs before current time to compare with. | [optional]

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

# **list_smb_file_opens**
> SmbFileOpens list_smb_file_opens()

Get SMB File opens.

Get SMB active file opens on a Cohesity View.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.smb_file_opens import SmbFileOpens
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
file_path = "filePath_example" # str, none_type | Specifies the filepath in the Cohesity View relative to the root filesystem. If this field is specified, viewName field must also be specified. (optional)
view_name = "viewName_example" # str, none_type | Specifies the name of the Cohesity View in which to search. If a view name is not specified, all the views in the Cluster are searched. This field is mandatory if filePath field is specified. (optional)
max_count = 1 # int, none_type | Specifies the maximum number of active file opens to return in the response. This field cannot be set above 1000. If this is not set, maximum of 1000 entries are returned. (optional)
cookie = "cookie_example" # str, none_type | Specifies the Pagination Cookie returned in the previous response. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get SMB File opens.
	api_response = client.view.list_smb_file_opens(access_cluster_id=access_cluster_id, region_id=region_id, file_path=file_path, view_name=view_name, max_count=max_count, cookie=cookie)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->list_smb_file_opens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **file_path** | **str, none_type**| Specifies the filepath in the Cohesity View relative to the root filesystem. If this field is specified, viewName field must also be specified. | [optional]
 **view_name** | **str, none_type**| Specifies the name of the Cohesity View in which to search. If a view name is not specified, all the views in the Cluster are searched. This field is mandatory if filePath field is specified. | [optional]
 **max_count** | **int, none_type**| Specifies the maximum number of active file opens to return in the response. This field cannot be set above 1000. If this is not set, maximum of 1000 entries are returned. | [optional]
 **cookie** | **str, none_type**| Specifies the Pagination Cookie returned in the previous response. | [optional]

### Return type

[**SmbFileOpens**](SmbFileOpens.md)

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

# **lock_file**
> FileLockStatus lock_file(id, body)

Create a file-lock

Locks a file in a view and returns the lock status of the file.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.lock_file_params import LockFileParams
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.file_lock_status import FileLockStatus
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of a view.
body = LockFileParams(
        file_path="file_path_example",
        expiry_timestamp_msecs=1,
    ) # LockFileParams | Specifies the request params to lock a file
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a file-lock
	api_response = client.view.lock_file(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->lock_file: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a file-lock
	api_response = client.view.lock_file(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->lock_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of a view. |
 **body** | [**LockFileParams**](LockFileParams.md)| Specifies the request params to lock a file |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**FileLockStatus**](FileLockStatus.md)

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

# **overwrite_view**
> overwrite_view(id, body)

Overwrite View.

Overwrite View.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.overwrite_view_params import OverwriteViewParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the View id to be overwritten.
body = OverwriteViewParams(
        source_view_id=1,
    ) # OverwriteViewParams | Specifies the request to overwrite the View.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Overwrite View.
	client.view.overwrite_view(id, body)
except ApiException as e:
	print("Exception when calling ViewApi->overwrite_view: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Overwrite View.
	client.view.overwrite_view(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling ViewApi->overwrite_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the View id to be overwritten. |
 **body** | [**OverwriteViewParams**](OverwriteViewParams.md)| Specifies the request to overwrite the View. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
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
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Read a View Template by Id
	api_response = client.view.read_view_template_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->read_view_template_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Read a View Template by Id
	api_response = client.view.read_view_template_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->read_view_template_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the view template. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.get_view_templates_result import GetViewTemplatesResult
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List View Templates
	api_response = client.view.read_view_templates(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->read_view_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.share import Share
from cohesity_sdk.helios.model.update_share_param import UpdateShareParam
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


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
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update a Share.
	api_response = client.view.update_share(name, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->update_share: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update a Share.
	api_response = client.view.update_share(name, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->update_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the Share name to update. |
 **body** | [**UpdateShareParam**](UpdateShareParam.md)| Specifies the request to update a Share. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.view import View
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies a unique id of the View to update.
body = View() # View | Request to update a view.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update a View
	api_response = client.view.update_view(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->update_view: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update a View
	api_response = client.view.update_view(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->update_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the View to update. |
 **body** | [**View**](View.md)| Request to update a view. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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

Update directory quota for the View.

Update directory quota for the View.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.view_directory_quota import ViewDirectoryQuota
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the View id.
body = ViewDirectoryQuota(
        directory_path="directory_path_example",
        quota_policy={},
    ) # ViewDirectoryQuota | Specifies the request to update directory quota.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update directory quota for the View.
	api_response = client.view.update_view_directory_quota(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->update_view_directory_quota: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update directory quota for the View.
	api_response = client.view.update_view_directory_quota(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->update_view_directory_quota: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the View id. |
 **body** | [**ViewDirectoryQuota**](ViewDirectoryQuota.md)| Specifies the request to update directory quota. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update a View Template
	api_response = client.view.update_view_template(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->update_view_template: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update a View Template
	api_response = client.view.update_view_template(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->update_view_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the view template. |
 **body** | [**Template**](Template.md)| Request to update a view template. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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

# **update_view_user_quota_override**
> UserQuota update_view_user_quota_override(view_id, user_id, body)

Update user quota override.

Update user quota. To use this API, User quota settings should be enabled on the View and there should be a user quota override added for this user.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.user_quota import UserQuota
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.quota_policy import QuotaPolicy
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


view_id = 1 # int | Specifies the View id.
user_id = "userId_example" # str | Specifies the unixUid or sid or an user.
body = QuotaPolicy(
        alert_limit_bytes=1,
        alert_threshold_percentage=1,
        hard_limit_bytes=1,
    ) # QuotaPolicy | Specifies the user quota policy of the user.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update user quota override.
	api_response = client.view.update_view_user_quota_override(view_id, user_id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->update_view_user_quota_override: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update user quota override.
	api_response = client.view.update_view_user_quota_override(view_id, user_id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->update_view_user_quota_override: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **int**| Specifies the View id. |
 **user_id** | **str**| Specifies the unixUid or sid or an user. |
 **body** | [**QuotaPolicy**](QuotaPolicy.md)| Specifies the user quota policy of the user. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**UserQuota**](UserQuota.md)

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

# **update_view_user_quota_settings**
> ViewUserQuotas update_view_user_quota_settings(view_id, body)

Update View user quota settings.

Specifies parameters to update View user quota settings.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.view_user_quotas import ViewUserQuotas
from cohesity_sdk.helios.model.view_user_quota_settings import ViewUserQuotaSettings
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


view_id = 1 # int | Specifies the View id.
body = ViewUserQuotaSettings(
        enabled=True,
        default_quota_policy={},
    ) # ViewUserQuotaSettings | Specifies the parameters to enable/disable or update the default quota config on the view.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update View user quota settings.
	api_response = client.view.update_view_user_quota_settings(view_id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->update_view_user_quota_settings: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update View user quota settings.
	api_response = client.view.update_view_user_quota_settings(view_id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ViewApi->update_view_user_quota_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **int**| Specifies the View id. |
 **body** | [**ViewUserQuotaSettings**](ViewUserQuotaSettings.md)| Specifies the parameters to enable/disable or update the default quota config on the view. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ViewUserQuotas**](ViewUserQuotas.md)

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

