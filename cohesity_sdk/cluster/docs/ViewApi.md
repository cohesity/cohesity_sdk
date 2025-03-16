# cohesity_sdk.cluster.ViewApi

All URIs are relative to */v2*

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.user_quota_overrides import UserQuotaOverrides
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    view_id = 56 # int | Specifies the id of a view.
    body = cohesity_sdk.cluster.UserQuotaOverrides() # UserQuotaOverrides | Specifies the parameters to override the default user quota on the view.

    try:
        # Add User Quota overrides.
        api_response = api_instance.add_view_user_quota_overrides(view_id, body)
        print("The response of ViewApi->add_view_user_quota_overrides:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->add_view_user_quota_overrides: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **int**| Specifies the id of a view. | 
 **body** | [**UserQuotaOverrides**](UserQuotaOverrides.md)| Specifies the parameters to override the default user quota on the view. | 

### Return type

[**UserQuotaOverrides**](UserQuotaOverrides.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.clear_nlm_lock_request import ClearNlmLockRequest
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    body = cohesity_sdk.cluster.ClearNlmLockRequest() # ClearNlmLockRequest | Request to clear NLM lock.

    try:
        # Clear NLM locks.
        api_instance.clear_nlm_locks(body)
    except Exception as e:
        print("Exception when calling ViewApi->clear_nlm_locks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClearNlmLockRequest**](ClearNlmLockRequest.md)| Request to clear NLM lock. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.clone_view_params import CloneViewParams
from cohesity_sdk.cluster.models.view import View
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    id = 56 # int | Specifies the View id to clone.
    body = cohesity_sdk.cluster.CloneViewParams() # CloneViewParams | Specifies the request to clone the View.

    try:
        # Clone View.
        api_response = api_instance.clone_view(id, body)
        print("The response of ViewApi->clone_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->clone_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the View id to clone. | 
 **body** | [**CloneViewParams**](CloneViewParams.md)| Specifies the request to clone the View. | 

### Return type

[**View**](View.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.clone_view_directory_params import CloneViewDirectoryParams
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    body = cohesity_sdk.cluster.CloneViewDirectoryParams() # CloneViewDirectoryParams | Specifies the request to clone View directory.

    try:
        # Clone View Directory.
        api_instance.clone_view_directory(body)
    except Exception as e:
        print("Exception when calling ViewApi->clone_view_directory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloneViewDirectoryParams**](CloneViewDirectoryParams.md)| Specifies the request to clone View directory. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> close_smb_file_open(body=body)

Close SMB File open.

Close an active SMB file open.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.close_smb_file_open_params import CloseSmbFileOpenParams
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    body = cohesity_sdk.cluster.CloseSmbFileOpenParams() # CloseSmbFileOpenParams | Specifies parameters to close active  SMB file open. (optional)

    try:
        # Close SMB File open.
        api_instance.close_smb_file_open(body=body)
    except Exception as e:
        print("Exception when calling ViewApi->close_smb_file_open: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloseSmbFileOpenParams**](CloseSmbFileOpenParams.md)| Specifies parameters to close active  SMB file open. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.share import Share
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    body = cohesity_sdk.cluster.Share() # Share | Specifies the request to create a Share.

    try:
        # Create a Share.
        api_response = api_instance.create_share(body)
        print("The response of ViewApi->create_share:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->create_share: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Share**](Share.md)| Specifies the request to create a Share. | 

### Return type

[**Share**](Share.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.create_view_request import CreateViewRequest
from cohesity_sdk.cluster.models.view import View
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    body = cohesity_sdk.cluster.CreateViewRequest() # CreateViewRequest | Request to create a View.

    try:
        # Create a View
        api_response = api_instance.create_view(body)
        print("The response of ViewApi->create_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->create_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateViewRequest**](CreateViewRequest.md)| Request to create a View. | 

### Return type

[**View**](View.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.template import Template
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    body = cohesity_sdk.cluster.Template() # Template | Request to create a view template.

    try:
        # Create a View Template
        api_response = api_instance.create_view_template(body)
        print("The response of ViewApi->create_view_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->create_view_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Template**](Template.md)| Request to create a view template. | 

### Return type

[**Template**](Template.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    name = 'name_example' # str | Specifies the Share name to delete.

    try:
        # Delete a Share.
        api_instance.delete_share(name)
    except Exception as e:
        print("Exception when calling ViewApi->delete_share: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the Share name to delete. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    id = 56 # int | Specifies a unique id of the View to delete.

    try:
        # Delete a View
        api_instance.delete_view(id)
    except Exception as e:
        print("Exception when calling ViewApi->delete_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the View to delete. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> delete_view_directory_quota(id, directory_path=directory_path, delete_all_directory_quotas=delete_all_directory_quotas)

Delete directory quota for the View.

Delete directory quota for the View.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    id = 56 # int | Specifies the View id.
    directory_path = 'directory_path_example' # str | Specifies the directory path to delete. Exactly one of 'directoryPath' and 'deleteAllDirectoryQuotas' should be provided. (optional)
    delete_all_directory_quotas = True # bool | Specifies whether to delete all directory quotas for this view. Exactly one of 'directoryPath' and 'deleteAllDirectoryQuotas' should be provided. (optional)

    try:
        # Delete directory quota for the View.
        api_instance.delete_view_directory_quota(id, directory_path=directory_path, delete_all_directory_quotas=delete_all_directory_quotas)
    except Exception as e:
        print("Exception when calling ViewApi->delete_view_directory_quota: %s\n" % e)
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

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    id = 56 # int | Specifies a unique id of the view template to delete.

    try:
        # Delete a View Template
        api_instance.delete_view_template(id)
    except Exception as e:
        print("Exception when calling ViewApi->delete_view_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the view template to delete. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.user_quota_delete_params import UserQuotaDeleteParams
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    view_id = 56 # int | Specifies the id of a view.
    body = cohesity_sdk.cluster.UserQuotaDeleteParams() # UserQuotaDeleteParams | Specifies parameters to delete user quotas.

    try:
        # Delete user quota overrides.
        api_instance.delete_view_user_quota_overrides(view_id, body)
    except Exception as e:
        print("Exception when calling ViewApi->delete_view_user_quota_overrides: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **int**| Specifies the id of a view. | 
 **body** | [**UserQuotaDeleteParams**](UserQuotaDeleteParams.md)| Specifies parameters to delete user quotas. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.file_lock_status import FileLockStatus
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    id = 56 # int | Specifies the id of a view.
    path = 'path_example' # str | Specifies the request file path in a view.

    try:
        # Get file lock status
        api_response = api_instance.get_file_lock_status(id, path)
        print("The response of ViewApi->get_file_lock_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->get_file_lock_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of a view. | 
 **path** | **str**| Specifies the request file path in a view. | 

### Return type

[**FileLockStatus**](FileLockStatus.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> GetNlmLocksResult get_nlm_locks(file_path=file_path, view_name=view_name, max_count=max_count, cookie=cookie)

Get NLM locks.

Get the list of NLM locks in the views.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.get_nlm_locks_result import GetNlmLocksResult
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    file_path = 'file_path_example' # str | Specifies the filepath in the view relative to the root filesystem. If this field is specified, viewName field must also be specified. (optional)
    view_name = 'view_name_example' # str | Specifies the name of the View in which to search. If a view name is not specified, all the views in the Cluster is searched. This field is mandatory if filePath field is specified. (optional)
    max_count = 56 # int | Specifies the maximum number of NLM locks to return in the response. By default, maxCount is set to 1000. At any given instance, maxCount value cannot be set to more than 1000. (optional)
    cookie = 'cookie_example' # str | Specifies the pagination cookie. If this is set, next set of locks just after the previous response are returned. If this is not set, first set of NLM locks are returned.\" (optional)

    try:
        # Get NLM locks.
        api_response = api_instance.get_nlm_locks(file_path=file_path, view_name=view_name, max_count=max_count, cookie=cookie)
        print("The response of ViewApi->get_nlm_locks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->get_nlm_locks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path** | **str**| Specifies the filepath in the view relative to the root filesystem. If this field is specified, viewName field must also be specified. | [optional] 
 **view_name** | **str**| Specifies the name of the View in which to search. If a view name is not specified, all the views in the Cluster is searched. This field is mandatory if filePath field is specified. | [optional] 
 **max_count** | **int**| Specifies the maximum number of NLM locks to return in the response. By default, maxCount is set to 1000. At any given instance, maxCount value cannot be set to more than 1000. | [optional] 
 **cookie** | **str**| Specifies the pagination cookie. If this is set, next set of locks just after the previous response are returned. If this is not set, first set of NLM locks are returned.\&quot; | [optional] 

### Return type

[**GetNlmLocksResult**](GetNlmLocksResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.qos_policies_result import QosPoliciesResult
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)

    try:
        # Get QoS Policies.
        api_response = api_instance.get_qos_policies()
        print("The response of ViewApi->get_qos_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->get_qos_policies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**QosPoliciesResult**](QosPoliciesResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> Shares get_shares(name=name, match_partial_name=match_partial_name, max_count=max_count, cookie=cookie, tenant_ids=tenant_ids, include_tenants=include_tenants)

Get Shares.

If no parameters are specified, all shares on the Cohesity Cluster are returned. Specifying share name/prefix filters the results that are returned. NOTE: If maxCount is set and the number of Shares returned exceeds the maxCount, there are more Share to return. To get the next set of Views, send another request and specify the pagination cookie from the previous response. If maxCount is not specified, the first 2000 Shares.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.shares import Shares
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    name = 'name_example' # str | Specifies the Share name. (optional)
    match_partial_name = True # bool | If true, the share name is matched by any partial rather than exactly matched. (optional)
    max_count = 56 # int | Specifies a limit on the number of Shares returned. If maxCount is not specified, the first 2000 Shares. (optional)
    cookie = 'cookie_example' # str | Specifies the pagination cookie. Expected to be empty in the first call to the API. To get the next set of results, set this value to the pagination cookie value returned in the response of the previous call. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
    include_tenants = True # bool | IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)

    try:
        # Get Shares.
        api_response = api_instance.get_shares(name=name, match_partial_name=match_partial_name, max_count=max_count, cookie=cookie, tenant_ids=tenant_ids, include_tenants=include_tenants)
        print("The response of ViewApi->get_shares:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->get_shares: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the Share name. | [optional] 
 **match_partial_name** | **bool**| If true, the share name is matched by any partial rather than exactly matched. | [optional] 
 **max_count** | **int**| Specifies a limit on the number of Shares returned. If maxCount is not specified, the first 2000 Shares. | [optional] 
 **cookie** | **str**| Specifies the pagination cookie. Expected to be empty in the first call to the API. To get the next set of results, set this value to the pagination cookie value returned in the response of the previous call. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which objects are to be returned. | [optional] 
 **include_tenants** | **bool**| IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional] 

### Return type

[**Shares**](Shares.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.view import View
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    id = 56 # int | Specifies a unique id of the View to fetch.

    try:
        # Get a View by Id
        api_response = api_instance.get_view_by_id(id)
        print("The response of ViewApi->get_view_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->get_view_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the View to fetch. | 

### Return type

[**View**](View.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> ViewClients get_view_clients(protocols=protocols, view_ids=view_ids, node_ip=node_ip, max_count=max_count)

Get View Clients.

Get View Clients.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.view_clients import ViewClients
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    protocols = ['protocols_example'] # List[str] | Specifies a list of protocols to filter the clients. (optional)
    view_ids = [56] # List[int] | Specifies a list of View ids. Only clients connected to these Views will be returned. (optional)
    node_ip = 'node_ip_example' # str | Specifies a node ip. Only clients connected to this node will be returned. (optional)
    max_count = 56 # int | Specifies the maximum number of connections to return for SMB and NFS protocols respectively. (optional)

    try:
        # Get View Clients.
        api_response = api_instance.get_view_clients(protocols=protocols, view_ids=view_ids, node_ip=node_ip, max_count=max_count)
        print("The response of ViewApi->get_view_clients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->get_view_clients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocols** | [**List[str]**](str.md)| Specifies a list of protocols to filter the clients. | [optional] 
 **view_ids** | [**List[int]**](int.md)| Specifies a list of View ids. Only clients connected to these Views will be returned. | [optional] 
 **node_ip** | **str**| Specifies a node ip. Only clients connected to this node will be returned. | [optional] 
 **max_count** | **int**| Specifies the maximum number of connections to return for SMB and NFS protocols respectively. | [optional] 

### Return type

[**ViewClients**](ViewClients.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> ViewClientsSummary get_view_clients_summary(view_ids=view_ids)

Get View Clients Summary.

Get View Clients Summary.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.view_clients_summary import ViewClientsSummary
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    view_ids = [56] # List[int] | Specifies a list of View ids. Only clients connected to these Views will be included in the summary. (optional)

    try:
        # Get View Clients Summary.
        api_response = api_instance.get_view_clients_summary(view_ids=view_ids)
        print("The response of ViewApi->get_view_clients_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->get_view_clients_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_ids** | [**List[int]**](int.md)| Specifies a list of View ids. Only clients connected to these Views will be included in the summary. | [optional] 

### Return type

[**ViewClientsSummary**](ViewClientsSummary.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> ViewDirectoryQuotas get_view_directory_quotas(id, max_count=max_count, cookie=cookie)

Get directory quotas for the View.

Get directory quotas for the View.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.view_directory_quotas import ViewDirectoryQuotas
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    id = 56 # int | Specifies the View id.
    max_count = 56 # int | Specifies a limit on the number of quotas returned. (optional)
    cookie = 56 # int | Specifies the cookie. (optional)

    try:
        # Get directory quotas for the View.
        api_response = api_instance.get_view_directory_quotas(id, max_count=max_count, cookie=cookie)
        print("The response of ViewApi->get_view_directory_quotas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->get_view_directory_quotas: %s\n" % e)
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

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> ViewUserQuotas get_view_user_quotas(view_id, max_count=max_count, cookie=cookie, unix_uid=unix_uid, sid=sid)

Get View user quotas.

Get user quotas for the View.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.view_user_quotas import ViewUserQuotas
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    view_id = 56 # int | Specifies the View id.
    max_count = 56 # int | Specifies a limit on the number of quotas returned. If maxCount is not set, response will have a maximum of 100 results. (optional)
    cookie = 'cookie_example' # str | Specifies the cookie. If there are more results than maxCount, response will include a cookie with has to be set as part of the next GET request. (optional)
    unix_uid = 56 # int | Specifies the user identifier of an Unix user. If a valid unix-id to SID mappings are available (i.e., when mixed mode is enabled) the server will perform the necessary id mapping and return the correct usage irrespective of whether the unix id / SID is provided. (optional)
    sid = 'sid_example' # str | Specifies the user identifier of a SMB user. If a valid unix-id to SID mappings are available (i.e., when mixed mode is enabled) the server will perform the necessary id mapping and return the correct usage irrespective of whether the unix id / SID is provided. (optional)

    try:
        # Get View user quotas.
        api_response = api_instance.get_view_user_quotas(view_id, max_count=max_count, cookie=cookie, unix_uid=unix_uid, sid=sid)
        print("The response of ViewApi->get_view_user_quotas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->get_view_user_quotas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **int**| Specifies the View id. | 
 **max_count** | **int**| Specifies a limit on the number of quotas returned. If maxCount is not set, response will have a maximum of 100 results. | [optional] 
 **cookie** | **str**| Specifies the cookie. If there are more results than maxCount, response will include a cookie with has to be set as part of the next GET request. | [optional] 
 **unix_uid** | **int**| Specifies the user identifier of an Unix user. If a valid unix-id to SID mappings are available (i.e., when mixed mode is enabled) the server will perform the necessary id mapping and return the correct usage irrespective of whether the unix id / SID is provided. | [optional] 
 **sid** | **str**| Specifies the user identifier of a SMB user. If a valid unix-id to SID mappings are available (i.e., when mixed mode is enabled) the server will perform the necessary id mapping and return the correct usage irrespective of whether the unix id / SID is provided. | [optional] 

### Return type

[**ViewUserQuotas**](ViewUserQuotas.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> GetViewsResult get_views(view_names=view_names, view_ids=view_ids, storage_domain_ids=storage_domain_ids, storage_domain_names=storage_domain_names, protocol_accesses=protocol_accesses, match_partial_names=match_partial_names, max_count=max_count, include_internal_views=include_internal_views, include_protection_groups=include_protection_groups, max_view_id=max_view_id, include_inactive=include_inactive, protection_group_ids=protection_group_ids, view_protection_group_ids=view_protection_group_ids, view_count_only=view_count_only, summary_only=summary_only, sort_by_logical_usage=sort_by_logical_usage, internal_access_sids=internal_access_sids, match_alias_names=match_alias_names, tenant_ids=tenant_ids, include_tenants=include_tenants, include_stats=include_stats, include_file_count_by_size=include_file_count_by_size, include_views_with_antivirus_enabled_only=include_views_with_antivirus_enabled_only, include_views_with_data_lock_enabled_only=include_views_with_data_lock_enabled_only, filer_audit_log_enabled=filer_audit_log_enabled, categories=categories, view_protection_types=view_protection_types, last_run_any_statuses=last_run_any_statuses, last_run_local_backup_statuses=last_run_local_backup_statuses, last_run_replication_statuses=last_run_replication_statuses, last_run_archival_statuses=last_run_archival_statuses, is_protected=is_protected, qos_principal_ids=qos_principal_ids, use_cached_data=use_cached_data, include_deleted_protection_groups=include_deleted_protection_groups)

List Views

If no parameters are specified, all Views on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned. NOTE: If maxCount is set and the number of Views returned exceeds the maxCount, there are more Views to return. To get the next set of Views, send another request and specify the id of the last View returned in viewList from the previous response.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.get_views_result import GetViewsResult
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    view_names = ['view_names_example'] # List[str] | Filter by a list of View names. (optional)
    view_ids = [56] # List[int] | Filter by a list of View ids. (optional)
    storage_domain_ids = [56] # List[int] | Filter by a list of Storage Domains (View Boxes) specified by id. (optional)
    storage_domain_names = ['storage_domain_names_example'] # List[str] | Filter by a list of View Box names. (optional)
    protocol_accesses = ['protocol_accesses_example'] # List[str] | Filter by a list of protocol accesses. Only views with protocol accesses in these specified accesses list will be returned. (optional)
    match_partial_names = True # bool | If true, the names in viewNames are matched by any partial rather than exactly matched. (optional)
    max_count = 56 # int | Specifies a limit on the number of Views returned. (optional)
    include_internal_views = True # bool | Specifies if internal Views created by the Cohesity Cluster are also returned. In addition, regular Views are returned. (optional)
    include_protection_groups = True # bool | Specifies if Protection Groups information needs to be returned along with view metadata. By default, if not set or set to true, Group information is returned. (optional)
    max_view_id = 56 # int | If the number of Views to return exceeds the maxCount specified in the original request, specify the id of the last View from the viewList in the previous response to get the next set of Views. (optional)
    include_inactive = True # bool | Specifies if inactive Views on this Remote Cluster (which have Snapshots copied by replication) should also be returned. Inactive Views are not counted towards the maxCount. By default, this field is set to false. (optional)
    protection_group_ids = [56] # List[int] | This field will be deprecated. Filter by Protection Group ids. Return Views that are being protected by listed Groups, which are specified by ids. If both protectionGroupIds and viewProtectionGroupIds are specified, only viewProtectionGroupIds will be used. (optional)
    view_protection_group_ids = ['view_protection_group_ids_example'] # List[str] | Filter by Protection Group ids. Return Views that are being protected by listed Groups, which are specified by ids. (optional)
    view_count_only = True # bool | Whether to get just the total number of views with the given input filters. If the flag is true, we ignore the parameter 'maxViews' for the count. Also, if flag is true, list of views will not be returned. (optional)
    summary_only = True # bool | Whether to get only view summary including 'name', 'viewId', 'storageDomainName', 'storageDomainId' and 'tenantId'. (optional)
    sort_by_logical_usage = True # bool | If set to true, the list is sorted descending by logical usage. (optional)
    internal_access_sids = ['internal_access_sids_example'] # List[str] | Sids of restricted principals who can access the view. This is an internal field and therefore does not have json tag. (optional)
    match_alias_names = True # bool | If true, view aliases are also matched with the names in viewNames. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
    include_tenants = True # bool | IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)
    include_stats = True # bool | If set to true, stats of views will be returned. By default this parameter is set to false. (optional)
    include_file_count_by_size = True # bool | Whether to include View file count by size. (optional)
    include_views_with_antivirus_enabled_only = True # bool | If set to true, the list will contain only the views for which antivirus scan is enabled. (optional)
    include_views_with_data_lock_enabled_only = True # bool | If set to true, the list will contain only the views for which either file level data lock is enabled or view level data lock is enabled. (optional)
    filer_audit_log_enabled = True # bool | If set to true, only views with filer audit log enabled will be returned. If set to false, only views with filer audit log disabled will be returned. (optional)
    categories = ['categories_example'] # List[str] | Filter by a list of View categories. (optional)
    view_protection_types = ['view_protection_types_example'] # List[str] | Filter by a list of View protection types. Supported types: [Local Archival ReplicationOut ReplicationIn UnProtected]. UnProtected is mutually exclusive from remaining types. (optional)
    last_run_any_statuses = ['last_run_any_statuses_example'] # List[str] | Filter by last any run status of the view.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Skipped' indicates that the run was skipped. (optional)
    last_run_local_backup_statuses = ['last_run_local_backup_statuses_example'] # List[str] | Filter by last local backup run status of the view.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Skipped' indicates that the run was skipped. (optional)
    last_run_replication_statuses = ['last_run_replication_statuses_example'] # List[str] | Filter by last remote replication run status of the view.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Skipped' indicates that the run was skipped. (optional)
    last_run_archival_statuses = ['last_run_archival_statuses_example'] # List[str] | Filter by last cloud archival run status of the view.<br> 'Running' indicates that the run is still running.<br> 'Canceled' indicates that the run has been canceled.<br> 'Canceling' indicates that the run is in the process of being canceled.<br> 'Failed' indicates that the run has failed.<br> 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening.<br> 'Succeeded' indicates that the run has finished successfully.<br> 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages.<br> 'Skipped' indicates that the run was skipped. (optional)
    is_protected = True # bool | Specifies the protection status of Views. If set to true, only protected Views will be returned. If set to false, only unprotected Views will be returned. (optional)
    qos_principal_ids = [56] # List[int] | qosPrincipalIds contains ids of the QoS principal for which views are to be returned. (optional)
    use_cached_data = True # bool | Specifies whether we can serve the GET request to the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. (optional)
    include_deleted_protection_groups = True # bool | Specifies if deleted Protection Groups information needs to be returned along with view metadata. By default, deleted Protection Groups are not returned. This is only applied if used along with any view protection related parameter. (optional)

    try:
        # List Views
        api_response = api_instance.get_views(view_names=view_names, view_ids=view_ids, storage_domain_ids=storage_domain_ids, storage_domain_names=storage_domain_names, protocol_accesses=protocol_accesses, match_partial_names=match_partial_names, max_count=max_count, include_internal_views=include_internal_views, include_protection_groups=include_protection_groups, max_view_id=max_view_id, include_inactive=include_inactive, protection_group_ids=protection_group_ids, view_protection_group_ids=view_protection_group_ids, view_count_only=view_count_only, summary_only=summary_only, sort_by_logical_usage=sort_by_logical_usage, internal_access_sids=internal_access_sids, match_alias_names=match_alias_names, tenant_ids=tenant_ids, include_tenants=include_tenants, include_stats=include_stats, include_file_count_by_size=include_file_count_by_size, include_views_with_antivirus_enabled_only=include_views_with_antivirus_enabled_only, include_views_with_data_lock_enabled_only=include_views_with_data_lock_enabled_only, filer_audit_log_enabled=filer_audit_log_enabled, categories=categories, view_protection_types=view_protection_types, last_run_any_statuses=last_run_any_statuses, last_run_local_backup_statuses=last_run_local_backup_statuses, last_run_replication_statuses=last_run_replication_statuses, last_run_archival_statuses=last_run_archival_statuses, is_protected=is_protected, qos_principal_ids=qos_principal_ids, use_cached_data=use_cached_data, include_deleted_protection_groups=include_deleted_protection_groups)
        print("The response of ViewApi->get_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->get_views: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_names** | [**List[str]**](str.md)| Filter by a list of View names. | [optional] 
 **view_ids** | [**List[int]**](int.md)| Filter by a list of View ids. | [optional] 
 **storage_domain_ids** | [**List[int]**](int.md)| Filter by a list of Storage Domains (View Boxes) specified by id. | [optional] 
 **storage_domain_names** | [**List[str]**](str.md)| Filter by a list of View Box names. | [optional] 
 **protocol_accesses** | [**List[str]**](str.md)| Filter by a list of protocol accesses. Only views with protocol accesses in these specified accesses list will be returned. | [optional] 
 **match_partial_names** | **bool**| If true, the names in viewNames are matched by any partial rather than exactly matched. | [optional] 
 **max_count** | **int**| Specifies a limit on the number of Views returned. | [optional] 
 **include_internal_views** | **bool**| Specifies if internal Views created by the Cohesity Cluster are also returned. In addition, regular Views are returned. | [optional] 
 **include_protection_groups** | **bool**| Specifies if Protection Groups information needs to be returned along with view metadata. By default, if not set or set to true, Group information is returned. | [optional] 
 **max_view_id** | **int**| If the number of Views to return exceeds the maxCount specified in the original request, specify the id of the last View from the viewList in the previous response to get the next set of Views. | [optional] 
 **include_inactive** | **bool**| Specifies if inactive Views on this Remote Cluster (which have Snapshots copied by replication) should also be returned. Inactive Views are not counted towards the maxCount. By default, this field is set to false. | [optional] 
 **protection_group_ids** | [**List[int]**](int.md)| This field will be deprecated. Filter by Protection Group ids. Return Views that are being protected by listed Groups, which are specified by ids. If both protectionGroupIds and viewProtectionGroupIds are specified, only viewProtectionGroupIds will be used. | [optional] 
 **view_protection_group_ids** | [**List[str]**](str.md)| Filter by Protection Group ids. Return Views that are being protected by listed Groups, which are specified by ids. | [optional] 
 **view_count_only** | **bool**| Whether to get just the total number of views with the given input filters. If the flag is true, we ignore the parameter &#39;maxViews&#39; for the count. Also, if flag is true, list of views will not be returned. | [optional] 
 **summary_only** | **bool**| Whether to get only view summary including &#39;name&#39;, &#39;viewId&#39;, &#39;storageDomainName&#39;, &#39;storageDomainId&#39; and &#39;tenantId&#39;. | [optional] 
 **sort_by_logical_usage** | **bool**| If set to true, the list is sorted descending by logical usage. | [optional] 
 **internal_access_sids** | [**List[str]**](str.md)| Sids of restricted principals who can access the view. This is an internal field and therefore does not have json tag. | [optional] 
 **match_alias_names** | **bool**| If true, view aliases are also matched with the names in viewNames. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which objects are to be returned. | [optional] 
 **include_tenants** | **bool**| IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional] 
 **include_stats** | **bool**| If set to true, stats of views will be returned. By default this parameter is set to false. | [optional] 
 **include_file_count_by_size** | **bool**| Whether to include View file count by size. | [optional] 
 **include_views_with_antivirus_enabled_only** | **bool**| If set to true, the list will contain only the views for which antivirus scan is enabled. | [optional] 
 **include_views_with_data_lock_enabled_only** | **bool**| If set to true, the list will contain only the views for which either file level data lock is enabled or view level data lock is enabled. | [optional] 
 **filer_audit_log_enabled** | **bool**| If set to true, only views with filer audit log enabled will be returned. If set to false, only views with filer audit log disabled will be returned. | [optional] 
 **categories** | [**List[str]**](str.md)| Filter by a list of View categories. | [optional] 
 **view_protection_types** | [**List[str]**](str.md)| Filter by a list of View protection types. Supported types: [Local Archival ReplicationOut ReplicationIn UnProtected]. UnProtected is mutually exclusive from remaining types. | [optional] 
 **last_run_any_statuses** | [**List[str]**](str.md)| Filter by last any run status of the view.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Skipped&#39; indicates that the run was skipped. | [optional] 
 **last_run_local_backup_statuses** | [**List[str]**](str.md)| Filter by last local backup run status of the view.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Skipped&#39; indicates that the run was skipped. | [optional] 
 **last_run_replication_statuses** | [**List[str]**](str.md)| Filter by last remote replication run status of the view.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Skipped&#39; indicates that the run was skipped. | [optional] 
 **last_run_archival_statuses** | [**List[str]**](str.md)| Filter by last cloud archival run status of the view.&lt;br&gt; &#39;Running&#39; indicates that the run is still running.&lt;br&gt; &#39;Canceled&#39; indicates that the run has been canceled.&lt;br&gt; &#39;Canceling&#39; indicates that the run is in the process of being canceled.&lt;br&gt; &#39;Failed&#39; indicates that the run has failed.&lt;br&gt; &#39;Missed&#39; indicates that the run was unable to take place at the scheduled time because the previous run was still happening.&lt;br&gt; &#39;Succeeded&#39; indicates that the run has finished successfully.&lt;br&gt; &#39;SucceededWithWarning&#39; indicates that the run finished successfully, but there were some warning messages.&lt;br&gt; &#39;Skipped&#39; indicates that the run was skipped. | [optional] 
 **is_protected** | **bool**| Specifies the protection status of Views. If set to true, only protected Views will be returned. If set to false, only unprotected Views will be returned. | [optional] 
 **qos_principal_ids** | [**List[int]**](int.md)| qosPrincipalIds contains ids of the QoS principal for which views are to be returned. | [optional] 
 **use_cached_data** | **bool**| Specifies whether we can serve the GET request to the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. | [optional] 
 **include_deleted_protection_groups** | **bool**| Specifies if deleted Protection Groups information needs to be returned along with view metadata. By default, deleted Protection Groups are not returned. This is only applied if used along with any view protection related parameter. | [optional] 

### Return type

[**GetViewsResult**](GetViewsResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> ViewsSummary get_views_summary(msecs_before_current_time_to_compare=msecs_before_current_time_to_compare, use_cached_data=use_cached_data, include_internal_views=include_internal_views, tenant_ids=tenant_ids, include_tenants=include_tenants, include_deleted_protection_groups=include_deleted_protection_groups)

Get Views summary.

Get Views summary.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.views_summary import ViewsSummary
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    msecs_before_current_time_to_compare = 56 # int | Specifies the time in msecs before current time to compare with. (optional)
    use_cached_data = True # bool | Specifies whether we can serve the GET request to the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. (optional)
    include_internal_views = True # bool | Specifies if internal Views created by the Cohesity Cluster are also returned. In addition, regular Views are returned. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
    include_tenants = True # bool | IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)
    include_deleted_protection_groups = True # bool | Specifies if deleted Protection Groups information needs to be returned along with view metadata. By default, deleted Protection Groups are not returned. This is only applied if used along with any view protection related parameter. (optional)

    try:
        # Get Views summary.
        api_response = api_instance.get_views_summary(msecs_before_current_time_to_compare=msecs_before_current_time_to_compare, use_cached_data=use_cached_data, include_internal_views=include_internal_views, tenant_ids=tenant_ids, include_tenants=include_tenants, include_deleted_protection_groups=include_deleted_protection_groups)
        print("The response of ViewApi->get_views_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->get_views_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msecs_before_current_time_to_compare** | **int**| Specifies the time in msecs before current time to compare with. | [optional] 
 **use_cached_data** | **bool**| Specifies whether we can serve the GET request to the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. | [optional] 
 **include_internal_views** | **bool**| Specifies if internal Views created by the Cohesity Cluster are also returned. In addition, regular Views are returned. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which objects are to be returned. | [optional] 
 **include_tenants** | **bool**| IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional] 
 **include_deleted_protection_groups** | **bool**| Specifies if deleted Protection Groups information needs to be returned along with view metadata. By default, deleted Protection Groups are not returned. This is only applied if used along with any view protection related parameter. | [optional] 

### Return type

[**ViewsSummary**](ViewsSummary.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> SmbFileOpens list_smb_file_opens(file_path=file_path, view_name=view_name, max_count=max_count, cookie=cookie)

Get SMB File opens.

Get SMB active file opens on a Cohesity View.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.smb_file_opens import SmbFileOpens
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    file_path = 'file_path_example' # str | Specifies the filepath in the Cohesity View relative to the root filesystem. If this field is specified, viewName field must also be specified. (optional)
    view_name = 'view_name_example' # str | Specifies the name of the Cohesity View in which to search. If a view name is not specified, all the views in the Cluster are searched. This field is mandatory if filePath field is specified. (optional)
    max_count = 56 # int | Specifies the maximum number of active file opens to return in the response. This field cannot be set above 1000. If this is not set, maximum of 1000 entries are returned. (optional)
    cookie = 'cookie_example' # str | Specifies the Pagination Cookie returned in the previous response. (optional)

    try:
        # Get SMB File opens.
        api_response = api_instance.list_smb_file_opens(file_path=file_path, view_name=view_name, max_count=max_count, cookie=cookie)
        print("The response of ViewApi->list_smb_file_opens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->list_smb_file_opens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path** | **str**| Specifies the filepath in the Cohesity View relative to the root filesystem. If this field is specified, viewName field must also be specified. | [optional] 
 **view_name** | **str**| Specifies the name of the Cohesity View in which to search. If a view name is not specified, all the views in the Cluster are searched. This field is mandatory if filePath field is specified. | [optional] 
 **max_count** | **int**| Specifies the maximum number of active file opens to return in the response. This field cannot be set above 1000. If this is not set, maximum of 1000 entries are returned. | [optional] 
 **cookie** | **str**| Specifies the Pagination Cookie returned in the previous response. | [optional] 

### Return type

[**SmbFileOpens**](SmbFileOpens.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.file_lock_status import FileLockStatus
from cohesity_sdk.cluster.models.lock_file_params import LockFileParams
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    id = 56 # int | Specifies the id of a view.
    body = cohesity_sdk.cluster.LockFileParams() # LockFileParams | Specifies the request params to lock a file

    try:
        # Create a file-lock
        api_response = api_instance.lock_file(id, body)
        print("The response of ViewApi->lock_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->lock_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of a view. | 
 **body** | [**LockFileParams**](LockFileParams.md)| Specifies the request params to lock a file | 

### Return type

[**FileLockStatus**](FileLockStatus.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.overwrite_view_params import OverwriteViewParams
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    id = 56 # int | Specifies the View id to be overwritten.
    body = cohesity_sdk.cluster.OverwriteViewParams() # OverwriteViewParams | Specifies the request to overwrite the View.

    try:
        # Overwrite View.
        api_instance.overwrite_view(id, body)
    except Exception as e:
        print("Exception when calling ViewApi->overwrite_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the View id to be overwritten. | 
 **body** | [**OverwriteViewParams**](OverwriteViewParams.md)| Specifies the request to overwrite the View. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.template import Template
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    id = 56 # int | Specifies a unique id of the view template.

    try:
        # Read a View Template by Id
        api_response = api_instance.read_view_template_by_id(id)
        print("The response of ViewApi->read_view_template_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->read_view_template_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the view template. | 

### Return type

[**Template**](Template.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.get_view_templates_result import GetViewTemplatesResult
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)

    try:
        # List View Templates
        api_response = api_instance.read_view_templates()
        print("The response of ViewApi->read_view_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->read_view_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetViewTemplatesResult**](GetViewTemplatesResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.share import Share
from cohesity_sdk.cluster.models.update_share_param import UpdateShareParam
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    name = 'name_example' # str | Specifies the Share name to update.
    body = cohesity_sdk.cluster.UpdateShareParam() # UpdateShareParam | Specifies the request to update a Share.

    try:
        # Update a Share.
        api_response = api_instance.update_share(name, body)
        print("The response of ViewApi->update_share:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->update_share: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the Share name to update. | 
 **body** | [**UpdateShareParam**](UpdateShareParam.md)| Specifies the request to update a Share. | 

### Return type

[**Share**](Share.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.view import View
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    id = 56 # int | Specifies a unique id of the View to update.
    body = cohesity_sdk.cluster.View() # View | Request to update a view.

    try:
        # Update a View
        api_response = api_instance.update_view(id, body)
        print("The response of ViewApi->update_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->update_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the View to update. | 
 **body** | [**View**](View.md)| Request to update a view. | 

### Return type

[**View**](View.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.view_directory_quota import ViewDirectoryQuota
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    id = 56 # int | Specifies the View id.
    body = cohesity_sdk.cluster.ViewDirectoryQuota() # ViewDirectoryQuota | Specifies the request to update directory quota.

    try:
        # Update directory quota for the View.
        api_response = api_instance.update_view_directory_quota(id, body)
        print("The response of ViewApi->update_view_directory_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->update_view_directory_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the View id. | 
 **body** | [**ViewDirectoryQuota**](ViewDirectoryQuota.md)| Specifies the request to update directory quota. | 

### Return type

[**ViewDirectoryQuota**](ViewDirectoryQuota.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.template import Template
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    id = 56 # int | Specifies a unique id of the view template.
    body = cohesity_sdk.cluster.Template() # Template | Request to update a view template.

    try:
        # Update a View Template
        api_response = api_instance.update_view_template(id, body)
        print("The response of ViewApi->update_view_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->update_view_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the view template. | 
 **body** | [**Template**](Template.md)| Request to update a view template. | 

### Return type

[**Template**](Template.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.quota_policy import QuotaPolicy
from cohesity_sdk.cluster.models.user_quota import UserQuota
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    view_id = 56 # int | Specifies the View id.
    user_id = 'user_id_example' # str | Specifies the unixUid or sid or an user.
    body = cohesity_sdk.cluster.QuotaPolicy() # QuotaPolicy | Specifies the user quota policy of the user.

    try:
        # Update user quota override.
        api_response = api_instance.update_view_user_quota_override(view_id, user_id, body)
        print("The response of ViewApi->update_view_user_quota_override:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->update_view_user_quota_override: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **int**| Specifies the View id. | 
 **user_id** | **str**| Specifies the unixUid or sid or an user. | 
 **body** | [**QuotaPolicy**](QuotaPolicy.md)| Specifies the user quota policy of the user. | 

### Return type

[**UserQuota**](UserQuota.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.view_user_quota_settings import ViewUserQuotaSettings
from cohesity_sdk.cluster.models.view_user_quotas import ViewUserQuotas
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ViewApi(api_client)
    view_id = 56 # int | Specifies the View id.
    body = cohesity_sdk.cluster.ViewUserQuotaSettings() # ViewUserQuotaSettings | Specifies the parameters to enable/disable or update the default quota config on the view.

    try:
        # Update View user quota settings.
        api_response = api_instance.update_view_user_quota_settings(view_id, body)
        print("The response of ViewApi->update_view_user_quota_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->update_view_user_quota_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **int**| Specifies the View id. | 
 **body** | [**ViewUserQuotaSettings**](ViewUserQuotaSettings.md)| Specifies the parameters to enable/disable or update the default quota config on the view. | 

### Return type

[**ViewUserQuotas**](ViewUserQuotas.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

