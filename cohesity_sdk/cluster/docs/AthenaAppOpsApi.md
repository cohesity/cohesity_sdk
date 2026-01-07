# cohesity_sdk.AthenaAppOpsApi


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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.relaunch_app_instance_request import RelaunchAppInstanceRequest
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | ID of the app instance to be relaunched
body = RelaunchAppInstanceRequest(
        if_failed=True,
    ) # RelaunchAppInstanceRequest | Specifies various conditions to check

# example passing only required values which don't have defaults set
try:
	# Relaunch app instance
	client.athena_app_ops.relaunch_app_instance(id, body)
except ApiException as e:
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.relaunch_system_app_request import RelaunchSystemAppRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | UID of the system app to be relaunched
body = RelaunchSystemAppRequest(
        cleanup=True,
        if_failed=True,
    ) # RelaunchSystemAppRequest | Specifies various conditions to check

# example passing only required values which don't have defaults set
try:
	# Relaunch System App
	client.athena_app_ops.relaunch_system_app(id, body)
except ApiException as e:
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

