# cohesity_sdk.DataSourceConnectorLocalApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_source_connector_logs**](DataSourceConnectorLocalApi.md#get_data_source_connector_logs) | **GET** /data-source-connector/logs | Lists the data-source connector logs.
[**get_data_source_connector_status**](DataSourceConnectorLocalApi.md#get_data_source_connector_status) | **GET** /data-source-connector/status | Lists the data-source connector status.
[**register_data_source_connector**](DataSourceConnectorLocalApi.md#register_data_source_connector) | **POST** /data-source-connector/registration | Register a data-source connector.


# **get_data_source_connector_logs**
> DataSourceConnectorLogs get_data_source_connector_logs()

Lists the data-source connector logs.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Lists the logs corresponding to the data-source connector creation and registration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.data_source_connector_logs import DataSourceConnectorLogs
from cohesity_sdk.cluster.model.error import Error
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
	# Lists the data-source connector logs.
	api_response = client.data_source_connector_local.get_data_source_connector_logs()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataSourceConnectorLocalApi->get_data_source_connector_logs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DataSourceConnectorLogs**](DataSourceConnectorLogs.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_source_connector_status**
> DataSourceConnectorLocalStatus get_data_source_connector_status()

Lists the data-source connector status.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Lists the data-source connector status, which includes registration as well as cluster-connectivity status.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.data_source_connector_local_status import DataSourceConnectorLocalStatus
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
	# Lists the data-source connector status.
	api_response = client.data_source_connector_local.get_data_source_connector_status()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataSourceConnectorLocalApi->get_data_source_connector_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DataSourceConnectorLocalStatus**](DataSourceConnectorLocalStatus.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_data_source_connector**
> register_data_source_connector(body)

Register a data-source connector.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Register a data-source connector with a cluster using the supplied registration token. The registration token for the data-source connection with which this connector is to be registered has to be obtained by the user by invoking the relevant '/data-source-connections' APIs.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.data_source_connector_registration_request import DataSourceConnectorRegistrationRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = DataSourceConnectorRegistrationRequest(
        registration_token="registration_token_example",
    ) # DataSourceConnectorRegistrationRequest | Specifies the parameters to register the connector.

# example passing only required values which don't have defaults set
try:
	# Register a data-source connector.
	client.data_source_connector_local.register_data_source_connector(body)
except ApiException as e:
	print("Exception when calling DataSourceConnectorLocalApi->register_data_source_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataSourceConnectorRegistrationRequest**](DataSourceConnectorRegistrationRequest.md)| Specifies the parameters to register the connector. |

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
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

