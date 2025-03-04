# cohesity_sdk.FailoverApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_failover**](FailoverApi.md#cancel_failover) | **POST** /data-protect/failover/{id}/cancel | Cancel failover workflow.
[**cancel_view_failover**](FailoverApi.md#cancel_view_failover) | **POST** /data-protect/failover/views/{id}/cancel | Cancel View Failover Task.
[**create_planned_run**](FailoverApi.md#create_planned_run) | **POST** /data-protect/failover/{id}/planned-run | Create a planned run for backup and replication.
[**create_view_failover**](FailoverApi.md#create_view_failover) | **POST** /data-protect/failover/views/{id} | Create View Failover Task.
[**get_failover_ops**](FailoverApi.md#get_failover_ops) | **GET** /data-protect/failover/views/{id}/operations | Gets all the failover operations which can be performed on this view.
[**get_tracking_view_id**](FailoverApi.md#get_tracking_view_id) | **GET** /data-protect/failover/views/trackingViewId/{id} | Get tracking View Id
[**get_view_failover**](FailoverApi.md#get_view_failover) | **GET** /data-protect/failover/views/{id} | Get View Failover.
[**init_failover**](FailoverApi.md#init_failover) | **POST** /data-protect/failover/{id} | Initiate a failover request.
[**object_linkage**](FailoverApi.md#object_linkage) | **POST** /data-protect/failover/{id}/object-linkage | Linking between replicated objects and failover objects
[**poll_planned_runs**](FailoverApi.md#poll_planned_runs) | **GET** /data-protect/failover/planned-runs | Get the list of failover planned runs.
[**replication_backup_activation**](FailoverApi.md#replication_backup_activation) | **POST** /data-protect/failover/{id}/backup-activation | Activate failover entity backup on replication clsuter.
[**source_backup_deactivation**](FailoverApi.md#source_backup_deactivation) | **POST** /data-protect/failover/{id}/backup-deactivation | Deactivate failover entity backup on source clsuter.


# **cancel_failover**
> cancel_failover(id)

Cancel failover workflow.

Specifies the request to cancel failover workflow. The cancellation request should not be made if '/backupActivation' or '/backupDeactivaetion' are already called on replication or source cluster respectively.

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
    api_instance = cohesity_sdk.FailoverApi(api_client)
    id = 'id_example' # str | Specifies the id of the failover workflow.

    try:
        # Cancel failover workflow.
        api_instance.cancel_failover(id)
    except Exception as e:
        print("Exception when calling FailoverApi->cancel_failover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the failover workflow. | 

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
**201** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_view_failover**
> cancel_view_failover(id)

Cancel View Failover Task.

Cancel an in progress view failover task.

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
    api_instance = cohesity_sdk.FailoverApi(api_client)
    id = 56 # int | Specifies a view id to cancel it's failover.

    try:
        # Cancel View Failover Task.
        api_instance.cancel_view_failover(id)
    except Exception as e:
        print("Exception when calling FailoverApi->cancel_view_failover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a view id to cancel it&#39;s failover. | 

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

# **create_planned_run**
> FailoverCreateRunResponse create_planned_run(id, body)

Create a planned run for backup and replication.

Specifies the configuration required for executing a special run as a part of failover workflow. This special run is triggered during palnned failover to sync the source cluster to replication cluster with minimum possible delta.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.failover_create_run_response import FailoverCreateRunResponse
from cohesity_sdk.models.failover_run_configuration import FailoverRunConfiguration
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
    api_instance = cohesity_sdk.FailoverApi(api_client)
    id = 'id_example' # str | Specifies the id of the failover workflow.
    body = cohesity_sdk.FailoverRunConfiguration() # FailoverRunConfiguration | Specifies the paramteres to create a planned run while failover workflow.

    try:
        # Create a planned run for backup and replication.
        api_response = api_instance.create_planned_run(id, body)
        print("The response of FailoverApi->create_planned_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverApi->create_planned_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the failover workflow. | 
 **body** | [**FailoverRunConfiguration**](FailoverRunConfiguration.md)| Specifies the paramteres to create a planned run while failover workflow. | 

### Return type

[**FailoverCreateRunResponse**](FailoverCreateRunResponse.md)

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

# **create_view_failover**
> Failover create_view_failover(id, body)

Create View Failover Task.

Create a view failover task.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.create_view_failover_request import CreateViewFailoverRequest
from cohesity_sdk.models.failover import Failover
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
    api_instance = cohesity_sdk.FailoverApi(api_client)
    id = 56 # int | Specifies a view id to create an failover task.
    body = cohesity_sdk.CreateViewFailoverRequest() # CreateViewFailoverRequest | Specifies the request body to create failover task.

    try:
        # Create View Failover Task.
        api_response = api_instance.create_view_failover(id, body)
        print("The response of FailoverApi->create_view_failover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverApi->create_view_failover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a view id to create an failover task. | 
 **body** | [**CreateViewFailoverRequest**](CreateViewFailoverRequest.md)| Specifies the request body to create failover task. | 

### Return type

[**Failover**](Failover.md)

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

# **get_failover_ops**
> GetFailoverOpsResponse get_failover_ops(id)

Gets all the failover operations which can be performed on this view.

Gets all the failover operations which can be performed on this view.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.get_failover_ops_response import GetFailoverOpsResponse
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
    api_instance = cohesity_sdk.FailoverApi(api_client)
    id = 56 # int | Specifies the view id.

    try:
        # Gets all the failover operations which can be performed on this view.
        api_response = api_instance.get_failover_ops(id)
        print("The response of FailoverApi->get_failover_ops:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverApi->get_failover_ops: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the view id. | 

### Return type

[**GetFailoverOpsResponse**](GetFailoverOpsResponse.md)

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

# **get_tracking_view_id**
> GetTrackingViewIdResponse get_tracking_view_id(id, is_forwarded=is_forwarded)

Get tracking View Id

Get tracking View Id

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.get_tracking_view_id_response import GetTrackingViewIdResponse
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
    api_instance = cohesity_sdk.FailoverApi(api_client)
    id = 'id_example' # str | Specifies the view_uid of the source view.
    is_forwarded = True # bool | Indicates whether the request is forwarded (optional)

    try:
        # Get tracking View Id
        api_response = api_instance.get_tracking_view_id(id, is_forwarded=is_forwarded)
        print("The response of FailoverApi->get_tracking_view_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverApi->get_tracking_view_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the view_uid of the source view. | 
 **is_forwarded** | **bool**| Indicates whether the request is forwarded | [optional] 

### Return type

[**GetTrackingViewIdResponse**](GetTrackingViewIdResponse.md)

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

# **get_view_failover**
> GetViewFailoverResponseBody get_view_failover(id)

Get View Failover.

Get failover tasks of a View.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.get_view_failover_response_body import GetViewFailoverResponseBody
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
    api_instance = cohesity_sdk.FailoverApi(api_client)
    id = 56 # int | Specifies a view id to create an failover task.

    try:
        # Get View Failover.
        api_response = api_instance.get_view_failover(id)
        print("The response of FailoverApi->get_view_failover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverApi->get_view_failover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a view id to create an failover task. | 

### Return type

[**GetViewFailoverResponseBody**](GetViewFailoverResponseBody.md)

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

# **init_failover**
> InitFailoverResponse init_failover(id, body)

Initiate a failover request.

Initiate a failover request.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.init_failover_request import InitFailoverRequest
from cohesity_sdk.models.init_failover_response import InitFailoverResponse
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
    api_instance = cohesity_sdk.FailoverApi(api_client)
    id = 'id_example' # str | Specifies the id of the failover workflow.
    body = cohesity_sdk.InitFailoverRequest() # InitFailoverRequest | Specifies the parameters to initiate a failover. This failover request should be intiaited from replication cluster.

    try:
        # Initiate a failover request.
        api_response = api_instance.init_failover(id, body)
        print("The response of FailoverApi->init_failover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverApi->init_failover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the failover workflow. | 
 **body** | [**InitFailoverRequest**](InitFailoverRequest.md)| Specifies the parameters to initiate a failover. This failover request should be intiaited from replication cluster. | 

### Return type

[**InitFailoverResponse**](InitFailoverResponse.md)

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

# **object_linkage**
> object_linkage(id, body)

Linking between replicated objects and failover objects

Specifies the request to link failover objects on replication cluster to the replicated entity from source cluster. This linking need to be done after perforing recoveries for failed entities on replication cluster. This linkage will be useful when merging snapshots of object across replications and failovers.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.object_linking_request import ObjectLinkingRequest
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
    api_instance = cohesity_sdk.FailoverApi(api_client)
    id = 'id_example' # str | Specifies the id of the failover workflow.
    body = cohesity_sdk.ObjectLinkingRequest() # ObjectLinkingRequest | Specifies the paramteres to create links between replicated objects and failover objects.

    try:
        # Linking between replicated objects and failover objects
        api_instance.object_linkage(id, body)
    except Exception as e:
        print("Exception when calling FailoverApi->object_linkage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the failover workflow. | 
 **body** | [**ObjectLinkingRequest**](ObjectLinkingRequest.md)| Specifies the paramteres to create links between replicated objects and failover objects. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_planned_runs**
> FailoverRunsResponse poll_planned_runs(failover_ids, tenant_ids=tenant_ids, include_tenants=include_tenants)

Get the list of failover planned runs.

Poll to see whether planned run has been scheduled or not.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.failover_runs_response import FailoverRunsResponse
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
    api_instance = cohesity_sdk.FailoverApi(api_client)
    failover_ids = ['failover_ids_example'] # List[str] | Get runs for specific failover workflows.
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
    include_tenants = True # bool | If true, the response will include Protection Groups which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. (optional)

    try:
        # Get the list of failover planned runs.
        api_response = api_instance.poll_planned_runs(failover_ids, tenant_ids=tenant_ids, include_tenants=include_tenants)
        print("The response of FailoverApi->poll_planned_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverApi->poll_planned_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **failover_ids** | [**List[str]**](str.md)| Get runs for specific failover workflows. | 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which objects are to be returned. | [optional] 
 **include_tenants** | **bool**| If true, the response will include Protection Groups which were created by all tenants which the current user has permission to see. If false, then only Protection Groups created by the current user will be returned. | [optional] 

### Return type

[**FailoverRunsResponse**](FailoverRunsResponse.md)

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

# **replication_backup_activation**
> ReplicationBackupActivationResult replication_backup_activation(id, body)

Activate failover entity backup on replication clsuter.

Specifies the configuration required for activating backup for failover objects on replication cluster. Here orchastrator can call this API multiple times as long as full set of object are non-overlapping. They can also use the existing job if its compatible to backup failover objects.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.replication_backup_activation import ReplicationBackupActivation
from cohesity_sdk.models.replication_backup_activation_result import ReplicationBackupActivationResult
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
    api_instance = cohesity_sdk.FailoverApi(api_client)
    id = 'id_example' # str | Specifies the id of the failover workflow.
    body = cohesity_sdk.ReplicationBackupActivation() # ReplicationBackupActivation | Specifies the paramteres to activate the backup of failover entities.

    try:
        # Activate failover entity backup on replication clsuter.
        api_response = api_instance.replication_backup_activation(id, body)
        print("The response of FailoverApi->replication_backup_activation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FailoverApi->replication_backup_activation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the failover workflow. | 
 **body** | [**ReplicationBackupActivation**](ReplicationBackupActivation.md)| Specifies the paramteres to activate the backup of failover entities. | 

### Return type

[**ReplicationBackupActivationResult**](ReplicationBackupActivationResult.md)

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

# **source_backup_deactivation**
> source_backup_deactivation(id, body)

Deactivate failover entity backup on source clsuter.

Specifies the configuration required for deactivating backup for failover entities on source cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.source_backup_deactivation import SourceBackupDeactivation
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
    api_instance = cohesity_sdk.FailoverApi(api_client)
    id = 'id_example' # str | Specifies the id of the failover workflow.
    body = cohesity_sdk.SourceBackupDeactivation() # SourceBackupDeactivation | Specifies the paramteres to deactivate the backup of failover entities.

    try:
        # Deactivate failover entity backup on source clsuter.
        api_instance.source_backup_deactivation(id, body)
    except Exception as e:
        print("Exception when calling FailoverApi->source_backup_deactivation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the failover workflow. | 
 **body** | [**SourceBackupDeactivation**](SourceBackupDeactivation.md)| Specifies the paramteres to deactivate the backup of failover entities. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

