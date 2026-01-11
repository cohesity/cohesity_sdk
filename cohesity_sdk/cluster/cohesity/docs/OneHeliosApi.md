# cohesity_sdk.cluster.OneHeliosApi

All URIs are relative to *http://localhost/v2*

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
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import one_helios
from cohesity_sdk.cluster.cohesity.model.app_orchestrator_error import AppOrchestratorError
from cohesity_sdk.cluster.cohesity.model.services_status_response import ServicesStatusResponse
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
    api_instance = one_helios.OneHeliosApi(api_client)
    service_name = "serviceName_example" # str | The name of the service to get status.

    # example passing only required values which don't have defaults set
    try:
        # Get status of an ondemand service
        api_response = api_instance.get_services_status(service_name)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
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
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import one_helios
from cohesity_sdk.cluster.cohesity.model.app_orchestrator_error import AppOrchestratorError
from cohesity_sdk.cluster.cohesity.model.install_logs_response import InstallLogsResponse
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
    api_instance = one_helios.OneHeliosApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Helios install logs.
        api_response = api_instance.install_logs()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
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
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import one_helios
from cohesity_sdk.cluster.cohesity.model.app_orchestrator_error import AppOrchestratorError
from cohesity_sdk.cluster.cohesity.model.service_action_response import ServiceActionResponse
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
    api_instance = one_helios.OneHeliosApi(api_client)
    service_name = "serviceName_example" # str | The name of the service.

    # example passing only required values which don't have defaults set
    try:
        # Perform action to enable/disable an on demand service.
        api_response = api_instance.perform_service_action(service_name)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
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
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import one_helios
from cohesity_sdk.cluster.cohesity.model.app_orchestrator_error import AppOrchestratorError
from cohesity_sdk.cluster.cohesity.model.services_health_get_response import ServicesHealthGetResponse
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
    api_instance = one_helios.OneHeliosApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Health Status for Services
        api_response = api_instance.services_health()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
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
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import one_helios
from cohesity_sdk.cluster.cohesity.model.app_orchestrator_error import AppOrchestratorError
from cohesity_sdk.cluster.cohesity.model.upgrade_logs_response import UpgradeLogsResponse
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
    api_instance = one_helios.OneHeliosApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Helios Upgrade Logs
        api_response = api_instance.upgrade_logs()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
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

