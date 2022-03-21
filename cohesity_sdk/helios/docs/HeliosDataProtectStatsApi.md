# cohesity_sdk.HeliosDataProtectStatsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_protect_usage**](HeliosDataProtectStatsApi.md#get_data_protect_usage) | **GET** /mcm/data-protect/usage-stats | Data-Protect Usage Statistics
[**get_rpaas_usage**](HeliosDataProtectStatsApi.md#get_rpaas_usage) | **GET** /mcm/ransomware-shield/usage-stats | RPaaS Usage Statistics


# **get_data_protect_usage**
> DataProtectUsage get_data_protect_usage()

Data-Protect Usage Statistics

Returns the current months usage for DMaaS. This internal api is to be used for display stats on DMaaS.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.data_protect_usage import DataProtectUsage
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
from_usecs = 1 # int, none_type | Start time to query for consumption of the current month (optional)
to_usecs = 1 # int, none_type | End time to query for consumption of the current month (optional)
region_ids = [
        "regionIds_example",
    ] # [str], none_type | Specifies the list of region ids. Only applicable in case of DMaaS. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Data-Protect Usage Statistics
	api_response = client.helios_data_protect_stats.get_data_protect_usage(region_id=region_id, from_usecs=from_usecs, to_usecs=to_usecs, region_ids=region_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosDataProtectStatsApi->get_data_protect_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **from_usecs** | **int, none_type**| Start time to query for consumption of the current month | [optional]
 **to_usecs** | **int, none_type**| End time to query for consumption of the current month | [optional]
 **region_ids** | **[str], none_type**| Specifies the list of region ids. Only applicable in case of DMaaS. | [optional]

### Return type

[**DataProtectUsage**](DataProtectUsage.md)

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

# **get_rpaas_usage**
> RpaasUsage get_rpaas_usage()

RPaaS Usage Statistics

Returns the data usage usage for RPaaS.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.rpaas_usage import RpaasUsage
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
from_time_usecs = 1 # int, none_type | Start time in microseconds to query for RPaaS data consumption. (optional)
to_time_usecs = 1 # int, none_type | End time in microseconds to query for RPaaS data consumption. (optional)
region_ids = [
        "regionIds_example",
    ] # [str], none_type | Specifies the list of region ids. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# RPaaS Usage Statistics
	api_response = client.helios_data_protect_stats.get_rpaas_usage(region_id=region_id, from_time_usecs=from_time_usecs, to_time_usecs=to_time_usecs, region_ids=region_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosDataProtectStatsApi->get_rpaas_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **from_time_usecs** | **int, none_type**| Start time in microseconds to query for RPaaS data consumption. | [optional]
 **to_time_usecs** | **int, none_type**| End time in microseconds to query for RPaaS data consumption. | [optional]
 **region_ids** | **[str], none_type**| Specifies the list of region ids. | [optional]

### Return type

[**RpaasUsage**](RpaasUsage.md)

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

