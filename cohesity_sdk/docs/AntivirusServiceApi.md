# cohesity_sdk.AntivirusServiceApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_antivirus_service_groups**](AntivirusServiceApi.md#get_antivirus_service_groups) | **GET** /antivirus-service/groups | Get Antivirus Service groups.
[**get_icap_uri_connection_status**](AntivirusServiceApi.md#get_icap_uri_connection_status) | **GET** /antivirus-service/icap-uri-connection-status | Get ICAP Uri connection status.
[**get_infected_files**](AntivirusServiceApi.md#get_infected_files) | **GET** /antivirus-service/infected-files | Get infected files.


# **get_antivirus_service_groups**
> AntivirusServiceGroups get_antivirus_service_groups()

Get Antivirus Service groups.

Get Antivirus Service groups.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.antivirus_service_groups import AntivirusServiceGroups
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
	# Get Antivirus Service groups.
	api_response = client.antivirus_service.get_antivirus_service_groups()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AntivirusServiceApi->get_antivirus_service_groups: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AntivirusServiceGroups**](AntivirusServiceGroups.md)

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

# **get_icap_uri_connection_status**
> IcapUriConnectionStatusList get_icap_uri_connection_status()

Get ICAP Uri connection status.

Get ICAP Uri connection status.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.icap_uri_connection_status_list import IcapUriConnectionStatusList
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


uris = [
        "uris_example",
    ] # [str] | Specifies a list of URIs to check connection status. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get ICAP Uri connection status.
	api_response = client.antivirus_service.get_icap_uri_connection_status(uris=uris)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AntivirusServiceApi->get_icap_uri_connection_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | **[str]**| Specifies a list of URIs to check connection status. | [optional]

### Return type

[**IcapUriConnectionStatusList**](IcapUriConnectionStatusList.md)

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

# **get_infected_files**
> InfectedFiles get_infected_files()

Get infected files.

Get infected files.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.infected_files import InfectedFiles
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


view_ids = [
        1,
    ] # [int] | Specifies a list of view ids. Only infected files from these views will be returned. (optional)
path = "path_example" # str | Specifies the file path. (optional)
states = [
        "Quarantined",
    ] # [str] | Specifies the file states. (optional)
max_count = 1 # int | Specifies the max number of files to be returned. (optional)
cookie = "cookie_example" # str | Specifies the pagination cookie. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get infected files.
	api_response = client.antivirus_service.get_infected_files(view_ids=view_ids, path=path, states=states, max_count=max_count, cookie=cookie)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AntivirusServiceApi->get_infected_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_ids** | **[int]**| Specifies a list of view ids. Only infected files from these views will be returned. | [optional]
 **path** | **str**| Specifies the file path. | [optional]
 **states** | **[str]**| Specifies the file states. | [optional]
 **max_count** | **int**| Specifies the max number of files to be returned. | [optional]
 **cookie** | **str**| Specifies the pagination cookie. | [optional]

### Return type

[**InfectedFiles**](InfectedFiles.md)

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

