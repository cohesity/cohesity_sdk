# cohesity_sdk.HeliosStatsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**mcm_get_policy_last_run_stats**](HeliosStatsApi.md#mcm_get_policy_last_run_stats) | **GET** /mcm/stats/policies/lastRun | Compute stats of last Protection Run of Protection Policies.
[**mcm_get_protection_run_last_run_stats**](HeliosStatsApi.md#mcm_get_protection_run_last_run_stats) | **GET** /mcm/stats/protection-runs/last-run | Compute stats of last Protection Run across all objects.


# **mcm_get_policy_last_run_stats**
> McmGetPolicyLastRunStatsResponseBody mcm_get_policy_last_run_stats()

Compute stats of last Protection Run of Protection Policies.

Compute stats of last Protection Run of Protection Policies.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.mcm_get_policy_last_run_stats_response_body import McmGetPolicyLastRunStatsResponseBody
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
region_ids = [
        "regionIds_example",
    ] # [str] | Filter by a list of region ids. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Compute stats of last Protection Run of Protection Policies.
	api_response = client.helios_stats.mcm_get_policy_last_run_stats(region_id=region_id, region_ids=region_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosStatsApi->mcm_get_policy_last_run_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **region_ids** | **[str]**| Filter by a list of region ids. | [optional]

### Return type

[**McmGetPolicyLastRunStatsResponseBody**](McmGetPolicyLastRunStatsResponseBody.md)

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

# **mcm_get_protection_run_last_run_stats**
> McmGetProtectionLastRunStatsResponseBody mcm_get_protection_run_last_run_stats()

Compute stats of last Protection Run across all objects.

Compute stats of last Protection Run across all objects.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.mcm_get_protection_last_run_stats_response_body import McmGetProtectionLastRunStatsResponseBody
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
region_ids = [
        "regionIds_example",
    ] # [str] | Filter by a list of region ids. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Compute stats of last Protection Run across all objects.
	api_response = client.helios_stats.mcm_get_protection_run_last_run_stats(region_id=region_id, region_ids=region_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosStatsApi->mcm_get_protection_run_last_run_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **region_ids** | **[str]**| Filter by a list of region ids. | [optional]

### Return type

[**McmGetProtectionLastRunStatsResponseBody**](McmGetProtectionLastRunStatsResponseBody.md)

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

