# cohesity_sdk.OneHeliosApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_services_status**](OneHeliosApi.md#get_services_status) | **GET** /helios/services/ondemand/{serviceName}/status | Get status of an ondemand service
[**install_logs**](OneHeliosApi.md#install_logs) | **GET** /helios/services/install/logs | Get Helios install logs.
[**perform_service_action**](OneHeliosApi.md#perform_service_action) | **PUT** /helios/services/ondemand/{serviceName}/action | Perform action to enable/disable an on demand service.
[**services_health**](OneHeliosApi.md#services_health) | **GET** /helios/health/services | Get Health Status for Services
[**upgrade_logs**](OneHeliosApi.md#upgrade_logs) | **GET** /helios/services/upgrade/logs | Get Helios Upgrade Logs


# **get_services_status**
> ServicesStatusResponse get_services_status(service_name)

Get status of an ondemand service

```Unknown Privileges``` <br><br>Status for an ondemand service and images available.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.app_orchestrator_error import AppOrchestratorError
from cohesity_sdk.cluster.model.services_status_response import ServicesStatusResponse
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


service_name = "serviceName_example" # str | The name of the service to get status.

# example passing only required values which don't have defaults set
try:
	# Get status of an ondemand service
	api_response = client.one_helios.get_services_status(service_name)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling OneHeliosApi->get_services_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| The name of the service to get status. |

### Return type

[**ServicesStatusResponse**](ServicesStatusResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**0** | (empty) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_logs**
> InstallLogsResponse install_logs()

Get Helios install logs.

**Privileges:** ```CLUSTER_VIEW``` <br><br>\"Fetches install logs for services in the Helios platform.\" \"Returns an InstallLogsResponse object containing the install version,\" \"install status for each service, and related messages.\" 

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.app_orchestrator_error import AppOrchestratorError
from cohesity_sdk.cluster.model.install_logs_response import InstallLogsResponse
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get Helios install logs.
	api_response = client.one_helios.install_logs()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling OneHeliosApi->install_logs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InstallLogsResponse**](InstallLogsResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**0** | (empty) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_service_action**
> ServiceActionResponse perform_service_action(service_name)

Perform action to enable/disable an on demand service.

```Unknown Privileges``` <br><br>

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.app_orchestrator_error import AppOrchestratorError
from cohesity_sdk.cluster.model.service_action_response import ServiceActionResponse
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


service_name = "serviceName_example" # str | The name of the service.

# example passing only required values which don't have defaults set
try:
	# Perform action to enable/disable an on demand service.
	api_response = client.one_helios.perform_service_action(service_name)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling OneHeliosApi->perform_service_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| The name of the service. |

### Return type

[**ServiceActionResponse**](ServiceActionResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**0** | (empty) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_health**
> ServicesHealthGetResponse services_health()

Get Health Status for Services

**Privileges:** ```CLUSTER_VIEW``` <br><br>\"Fetches the health status for various services in the Helios\" \"platform. Returns a ServicesHealthGetResponse object containing the\" \"overall health status and health status for each service.\" 

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.services_health_get_response import ServicesHealthGetResponse
from cohesity_sdk.cluster.model.app_orchestrator_error import AppOrchestratorError
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get Health Status for Services
	api_response = client.one_helios.services_health()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling OneHeliosApi->services_health: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ServicesHealthGetResponse**](ServicesHealthGetResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**0** | (empty) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_logs**
> UpgradeLogsResponse upgrade_logs()

Get Helios Upgrade Logs

**Privileges:** ```CLUSTER_VIEW``` <br><br>\"Fetches upgrade logs for services in the Helios platform.\" \"Returns an UpgradeLogsResponse object containing the upgrade version,\" \"upgrade status for each service, and related messages.\" 

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.app_orchestrator_error import AppOrchestratorError
from cohesity_sdk.cluster.model.upgrade_logs_response import UpgradeLogsResponse
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get Helios Upgrade Logs
	api_response = client.one_helios.upgrade_logs()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling OneHeliosApi->upgrade_logs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UpgradeLogsResponse**](UpgradeLogsResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**0** | (empty) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

