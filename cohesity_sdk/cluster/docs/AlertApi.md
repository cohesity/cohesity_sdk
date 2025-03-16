# cohesity_sdk.cluster.AlertApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alert_summary**](AlertApi.md#get_alert_summary) | **GET** /alerts-summary | Get alerts summary.


# **get_alert_summary**
> AlertsSummaryResponse get_alert_summary(start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, include_tenants=include_tenants, tenant_ids=tenant_ids, states_list=states_list)

Get alerts summary.

Get alerts summary grouped by category.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.alerts_summary_response import AlertsSummaryResponse
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
    api_instance = cohesity_sdk.cluster.AlertApi(api_client)
    start_time_usecs = 56 # int | Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day. (optional)
    end_time_usecs = 56 # int | Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time. (optional)
    include_tenants = True # bool | IncludeTenants specifies if alerts of all the tenants under the hierarchy of the logged in user's organization should be used to compute summary. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which alerts are to be used to compute summary. (optional)
    states_list = ['states_list_example'] # List[str] | Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary. (optional)

    try:
        # Get alerts summary.
        api_response = api_instance.get_alert_summary(start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, include_tenants=include_tenants, tenant_ids=tenant_ids, states_list=states_list)
        print("The response of AlertApi->get_alert_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->get_alert_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time_usecs** | **int**| Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day. | [optional] 
 **end_time_usecs** | **int**| Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time. | [optional] 
 **include_tenants** | **bool**| IncludeTenants specifies if alerts of all the tenants under the hierarchy of the logged in user&#39;s organization should be used to compute summary. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which alerts are to be used to compute summary. | [optional] 
 **states_list** | [**List[str]**](str.md)| Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary. | [optional] 

### Return type

[**AlertsSummaryResponse**](AlertsSummaryResponse.md)

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

