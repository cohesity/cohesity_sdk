# cohesity_sdk.helios.AlertApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_helios_alert_resolution**](AlertApi.md#create_helios_alert_resolution) | **PUT** /mcm/alerts/resolutions | Create an Helios Alert Resolution.
[**get_alert_summary**](AlertApi.md#get_alert_summary) | **GET** /alerts-summary | Get alerts summary.
[**get_helios_alert_resolution**](AlertApi.md#get_helios_alert_resolution) | **GET** /mcm/alerts/resolutions | List the Alert Resolutions in Cohesity system.
[**get_helios_alerts**](AlertApi.md#get_helios_alerts) | **GET** /mcm/alerts | Get list of helios alerts.
[**get_helios_alerts_summary**](AlertApi.md#get_helios_alerts_summary) | **GET** /mcm/stats/alerts-summary | Get alerts summary on Helios.


# **create_helios_alert_resolution**
> AlertResolution create_helios_alert_resolution(body, region_id=region_id)

Create an Helios Alert Resolution.

Apply resolution to Helios alerts, create the resolution if it dose not exists

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.alert_resolution import AlertResolution
from cohesity_sdk.helios.models.create_helios_alert_resolution_params import CreateHeliosAlertResolutionParams
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.AlertApi(api_client)
    body = cohesity_sdk.helios.CreateHeliosAlertResolutionParams() # CreateHeliosAlertResolutionParams | Helios Alert resolution to be created, with alerts to resolve. Alerts.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Create an Helios Alert Resolution.
        api_response = api_instance.create_helios_alert_resolution(body, region_id=region_id)
        print("The response of AlertApi->create_helios_alert_resolution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->create_helios_alert_resolution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateHeliosAlertResolutionParams**](CreateHeliosAlertResolutionParams.md)| Helios Alert resolution to be created, with alerts to resolve. Alerts. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**AlertResolution**](AlertResolution.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_summary**
> AlertsSummaryResponse get_alert_summary(access_cluster_id=access_cluster_id, region_id=region_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, include_tenants=include_tenants, tenant_ids=tenant_ids, states_list=states_list)

Get alerts summary.

Get alerts summary grouped by category.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.alerts_summary_response import AlertsSummaryResponse
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.AlertApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    start_time_usecs = 56 # int | Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day. (optional)
    end_time_usecs = 56 # int | Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time. (optional)
    include_tenants = True # bool | IncludeTenants specifies if alerts of all the tenants under the hierarchy of the logged in user's organization should be used to compute summary. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which alerts are to be used to compute summary. (optional)
    states_list = ['states_list_example'] # List[str] | Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary. (optional)

    try:
        # Get alerts summary.
        api_response = api_instance.get_alert_summary(access_cluster_id=access_cluster_id, region_id=region_id, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, include_tenants=include_tenants, tenant_ids=tenant_ids, states_list=states_list)
        print("The response of AlertApi->get_alert_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->get_alert_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **start_time_usecs** | **int**| Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day. | [optional] 
 **end_time_usecs** | **int**| Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time. | [optional] 
 **include_tenants** | **bool**| IncludeTenants specifies if alerts of all the tenants under the hierarchy of the logged in user&#39;s organization should be used to compute summary. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which alerts are to be used to compute summary. | [optional] 
 **states_list** | [**List[str]**](str.md)| Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary. | [optional] 

### Return type

[**AlertsSummaryResponse**](AlertsSummaryResponse.md)

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

# **get_helios_alert_resolution**
> List[AlertResolutionsList] get_helios_alert_resolution(max_resolutions, region_id=region_id, resolution_name=resolution_name, resolution_id=resolution_id)

List the Alert Resolutions in Cohesity system.

Returns the Helios Alert Resolution objects found in Cohesity system that match the filter criteria from given parameters. If no filter parameters are specified, MaxResolutions Alert Resolution objects are returned. Each object provides details about the Alert Resolution info and the resolved alert info.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.alert_resolutions_list import AlertResolutionsList
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.AlertApi(api_client)
    max_resolutions = 56 # int | Specifies the max number of Resolutions to be returned, from the latest created to the earliest created
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    resolution_name = 'resolution_name_example' # str | Specifies Alert Resolution Name to query. (optional)
    resolution_id = 'resolution_id_example' # str | Specifies Alert Resolution id to query. (optional)

    try:
        # List the Alert Resolutions in Cohesity system.
        api_response = api_instance.get_helios_alert_resolution(max_resolutions, region_id=region_id, resolution_name=resolution_name, resolution_id=resolution_id)
        print("The response of AlertApi->get_helios_alert_resolution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->get_helios_alert_resolution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_resolutions** | **int**| Specifies the max number of Resolutions to be returned, from the latest created to the earliest created | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **resolution_name** | **str**| Specifies Alert Resolution Name to query. | [optional] 
 **resolution_id** | **str**| Specifies Alert Resolution id to query. | [optional] 

### Return type

[**List[AlertResolutionsList]**](AlertResolutionsList.md)

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

# **get_helios_alerts**
> AlertsList get_helios_alerts(region_id=region_id, alert_id_list=alert_id_list, alert_state_list=alert_state_list, alert_type_list=alert_type_list, alert_severity_list=alert_severity_list, region_ids=region_ids, cluster_identifiers=cluster_identifiers, start_date_usecs=start_date_usecs, end_date_usecs=end_date_usecs, max_alerts=max_alerts, alert_category_list=alert_category_list, alert_type_bucket_list=alert_type_bucket_list, alert_property_key_list=alert_property_key_list, alert_property_value_list=alert_property_value_list)

Get list of helios alerts.

Get the list of helios alerts.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.alerts_list import AlertsList
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.AlertApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    alert_id_list = ['alert_id_list_example'] # List[str] | Filter by list of alert ids. (optional)
    alert_state_list = ['alert_state_list_example'] # List[str] | Filter by list of alert states. (optional)
    alert_type_list = [56] # List[int] | Filter by list of alert types. (optional)
    alert_severity_list = ['alert_severity_list_example'] # List[str] | Filter by list of alert severity types. (optional)
    region_ids = ['region_ids_example'] # List[str] | Filter by list of region ids. (optional)
    cluster_identifiers = ['cluster_identifiers_example'] # List[str] | Filter by list of cluster ids. (optional)
    start_date_usecs = 56 # int | Specifies the start time of the alerts to be returned. All the alerts returned are raised after the specified start time. This value should be in Unix timestamp epoch in microseconds. (optional)
    end_date_usecs = 56 # int | Specifies the end time of the alerts to be returned. All the alerts returned are raised before the specified end time. This value should be in Unix timestamp epoch in microseconds. (optional)
    max_alerts = 56 # int | Specifies maximum number of alerts to return (optional)
    alert_category_list = ['alert_category_list_example'] # List[Optional[str]] | Filter by list of alert categories. (optional)
    alert_type_bucket_list = ['alert_type_bucket_list_example'] # List[Optional[str]] | Filter by list of alert type buckets. (optional)
    alert_property_key_list = ['alert_property_key_list_example'] # List[Optional[str]] | Specifies list of the alert property keys to query. (optional)
    alert_property_value_list = ['alert_property_value_list_example'] # List[Optional[str]] | Specifies list of the alert property value, multiple values for one key should be joined by '|'. (optional)

    try:
        # Get list of helios alerts.
        api_response = api_instance.get_helios_alerts(region_id=region_id, alert_id_list=alert_id_list, alert_state_list=alert_state_list, alert_type_list=alert_type_list, alert_severity_list=alert_severity_list, region_ids=region_ids, cluster_identifiers=cluster_identifiers, start_date_usecs=start_date_usecs, end_date_usecs=end_date_usecs, max_alerts=max_alerts, alert_category_list=alert_category_list, alert_type_bucket_list=alert_type_bucket_list, alert_property_key_list=alert_property_key_list, alert_property_value_list=alert_property_value_list)
        print("The response of AlertApi->get_helios_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->get_helios_alerts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **alert_id_list** | [**List[str]**](str.md)| Filter by list of alert ids. | [optional] 
 **alert_state_list** | [**List[str]**](str.md)| Filter by list of alert states. | [optional] 
 **alert_type_list** | [**List[int]**](int.md)| Filter by list of alert types. | [optional] 
 **alert_severity_list** | [**List[str]**](str.md)| Filter by list of alert severity types. | [optional] 
 **region_ids** | [**List[str]**](str.md)| Filter by list of region ids. | [optional] 
 **cluster_identifiers** | [**List[str]**](str.md)| Filter by list of cluster ids. | [optional] 
 **start_date_usecs** | **int**| Specifies the start time of the alerts to be returned. All the alerts returned are raised after the specified start time. This value should be in Unix timestamp epoch in microseconds. | [optional] 
 **end_date_usecs** | **int**| Specifies the end time of the alerts to be returned. All the alerts returned are raised before the specified end time. This value should be in Unix timestamp epoch in microseconds. | [optional] 
 **max_alerts** | **int**| Specifies maximum number of alerts to return | [optional] 
 **alert_category_list** | [**List[Optional[str]]**](str.md)| Filter by list of alert categories. | [optional] 
 **alert_type_bucket_list** | [**List[Optional[str]]**](str.md)| Filter by list of alert type buckets. | [optional] 
 **alert_property_key_list** | [**List[Optional[str]]**](str.md)| Specifies list of the alert property keys to query. | [optional] 
 **alert_property_value_list** | [**List[Optional[str]]**](str.md)| Specifies list of the alert property value, multiple values for one key should be joined by &#39;|&#39;. | [optional] 

### Return type

[**AlertsList**](AlertsList.md)

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

# **get_helios_alerts_summary**
> AlertsSummaryResponse get_helios_alerts_summary(region_id=region_id, cluster_identifiers=cluster_identifiers, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, states_list=states_list)

Get alerts summary on Helios.

Get alerts summary grouped by category.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.alerts_summary_response import AlertsSummaryResponse
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.AlertApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    cluster_identifiers = ['cluster_identifiers_example'] # List[str] | Specifies the list of cluster identifiers. Format is clusterId:clusterIncarnationId. (optional)
    start_time_usecs = 56 # int | Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day. (optional)
    end_time_usecs = 56 # int | Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time. (optional)
    states_list = ['states_list_example'] # List[str] | Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary. (optional)

    try:
        # Get alerts summary on Helios.
        api_response = api_instance.get_helios_alerts_summary(region_id=region_id, cluster_identifiers=cluster_identifiers, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, states_list=states_list)
        print("The response of AlertApi->get_helios_alerts_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->get_helios_alerts_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **cluster_identifiers** | [**List[str]**](str.md)| Specifies the list of cluster identifiers. Format is clusterId:clusterIncarnationId. | [optional] 
 **start_time_usecs** | **int**| Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day. | [optional] 
 **end_time_usecs** | **int**| Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time. | [optional] 
 **states_list** | [**List[str]**](str.md)| Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary. | [optional] 

### Return type

[**AlertsSummaryResponse**](AlertsSummaryResponse.md)

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

