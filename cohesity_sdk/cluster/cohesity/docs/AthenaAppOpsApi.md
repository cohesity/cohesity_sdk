# cohesity_sdk.cluster.AthenaAppOpsApi

All URIs are relative to *http://localhost/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**relaunch_app_instance**](AthenaAppOpsApi.md#relaunch_app_instance) | **PUT** /apps/instances/{id}/relaunch | Relaunch app instance
[**relaunch_system_app**](AthenaAppOpsApi.md#relaunch_system_app) | **PUT** /apps/{id}/relaunch | Relaunch System App


# **relaunch_app_instance**
> relaunch_app_instance(id, body)

Relaunch app instance

**Privileges:** ```APP_LAUNCH``` <br><br>Relaunch (Pause & Resume) an app instance

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import athena_app_ops
from cohesity_sdk.cluster.cohesity.model.relaunch_app_instance_request import RelaunchAppInstanceRequest
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
    api_instance = athena_app_ops.AthenaAppOpsApi(api_client)
    id = 1 # int | ID of the app instance to be relaunched
    body = RelaunchAppInstanceRequest(
        if_failed=True,
    ) # RelaunchAppInstanceRequest | Specifies various conditions to check

    # example passing only required values which don't have defaults set
    try:
        # Relaunch app instance
        api_instance.relaunch_app_instance(id, body)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling AthenaAppOpsApi->relaunch_app_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the app instance to be relaunched |
 **body** | [**RelaunchAppInstanceRequest**](RelaunchAppInstanceRequest.md)| Specifies various conditions to check |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request Accepted |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relaunch_system_app**
> relaunch_system_app(id, body)

Relaunch System App

**Privileges:** ```APP_LAUNCH``` <br><br>Relaunch (Pause & Resume) a system app

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import athena_app_ops
from cohesity_sdk.cluster.cohesity.model.relaunch_system_app_request import RelaunchSystemAppRequest
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
    api_instance = athena_app_ops.AthenaAppOpsApi(api_client)
    id = 1 # int | UID of the system app to be relaunched
    body = RelaunchSystemAppRequest(
        cleanup=True,
        if_failed=True,
    ) # RelaunchSystemAppRequest | Specifies various conditions to check

    # example passing only required values which don't have defaults set
    try:
        # Relaunch System App
        api_instance.relaunch_system_app(id, body)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling AthenaAppOpsApi->relaunch_system_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| UID of the system app to be relaunched |
 **body** | [**RelaunchSystemAppRequest**](RelaunchSystemAppRequest.md)| Specifies various conditions to check |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request Accepted |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

