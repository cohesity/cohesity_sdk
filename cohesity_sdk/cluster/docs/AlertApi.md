# cohesity_sdk.cluster.AlertApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alert_notification_rule**](AlertApi.md#create_alert_notification_rule) | **POST** /alerts/config/notification-rules | Add a notification rule
[**create_alert_resolution**](AlertApi.md#create_alert_resolution) | **POST** /alerts/resolutions | Create alert resolution.
[**get_active_alert_stats**](AlertApi.md#get_active_alert_stats) | **GET** /stats/alerts | Get active alert statistics.
[**get_alert_categories**](AlertApi.md#get_alert_categories) | **GET** /alert-categories | Get alert categories.
[**get_alert_notification_rules**](AlertApi.md#get_alert_notification_rules) | **GET** /alerts/config/notification-rules | List all notification rules
[**get_alert_resolution**](AlertApi.md#get_alert_resolution) | **GET** /alerts/resolutions/{id} | Get alert resolution by resolution Id
[**get_alert_resolutions**](AlertApi.md#get_alert_resolutions) | **GET** /alerts/resolutions | Get alert resolutions.
[**get_alert_summary**](AlertApi.md#get_alert_summary) | **GET** /alerts-summary | Get alerts summary.
[**get_alert_types**](AlertApi.md#get_alert_types) | **GET** /alert-types | Get alert types.
[**get_alerts**](AlertApi.md#get_alerts) | **GET** /alerts | Get alerts.
[**remove_alert_notification_rule**](AlertApi.md#remove_alert_notification_rule) | **DELETE** /alerts/config/notification-rules/{id} | Remove a notification rule
[**update_alert_notification_rule**](AlertApi.md#update_alert_notification_rule) | **PUT** /alerts/config/notification-rules/{id} | Update a notification rule
[**update_alert_resolution**](AlertApi.md#update_alert_resolution) | **PUT** /alerts/resolutions/{id} | Update alert resolution.


# **create_alert_notification_rule**
> NotificationRule create_alert_notification_rule(body)

Add a notification rule

**Privileges:** ```ALERT_MODIFY``` <br><br>Create a new notification rule rules that send emails, SNMP, Syslog, and/or cURL HTTP POST requests to a webhook URL based on the alert categories, severities, and names.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.notification_rule import NotificationRule
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
    body = cohesity_sdk.cluster.NotificationRule() # NotificationRule | Specifies the alert notification rule config.

    try:
        # Add a notification rule
        api_response = api_instance.create_alert_notification_rule(body)
        print("The response of AlertApi->create_alert_notification_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->create_alert_notification_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationRule**](NotificationRule.md)| Specifies the alert notification rule config. | 

### Return type

[**NotificationRule**](NotificationRule.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_alert_resolution**
> AlertResolutionOnPrem create_alert_resolution(body)

Create alert resolution.

**Privileges:** ```ALERT_MODIFY``` <br><br>Create alert resolution.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.alert_resolution_on_prem import AlertResolutionOnPrem
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
    body = cohesity_sdk.cluster.AlertResolutionOnPrem() # AlertResolutionOnPrem | \"Provides Resolution details and the list of Alerts resolved\" \"by a Resolution which are specified by Alert Ids.\" 

    try:
        # Create alert resolution.
        api_response = api_instance.create_alert_resolution(body)
        print("The response of AlertApi->create_alert_resolution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->create_alert_resolution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertResolutionOnPrem**](AlertResolutionOnPrem.md)| \&quot;Provides Resolution details and the list of Alerts resolved\&quot; \&quot;by a Resolution which are specified by Alert Ids.\&quot;  | 

### Return type

[**AlertResolutionOnPrem**](AlertResolutionOnPrem.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_alert_stats**
> ActiveAlertsStats get_active_alert_stats(start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs)

Get active alert statistics.

**Privileges:** ```ALERT_VIEW``` <br><br>Get statistics of active alerts. If no query parameters are provided, defaults to the last 10 days.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.active_alerts_stats import ActiveAlertsStats
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
    start_time_usecs = 56 # int | Specifies the start time in miliseconds to filter the alert statistics. (optional)
    end_time_usecs = 56 # int | Specifies the end time in miliseconds to filter the alert statistics.. (optional)

    try:
        # Get active alert statistics.
        api_response = api_instance.get_active_alert_stats(start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs)
        print("The response of AlertApi->get_active_alert_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->get_active_alert_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time_usecs** | **int**| Specifies the start time in miliseconds to filter the alert statistics. | [optional] 
 **end_time_usecs** | **int**| Specifies the end time in miliseconds to filter the alert statistics.. | [optional] 

### Return type

[**ActiveAlertsStats**](ActiveAlertsStats.md)

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

# **get_alert_categories**
> List[AlertCategories] get_alert_categories()

Get alert categories.

**Privileges:** ```ALERT_VIEW``` <br><br>Get all alert categories.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.alert_categories import AlertCategories
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

    try:
        # Get alert categories.
        api_response = api_instance.get_alert_categories()
        print("The response of AlertApi->get_alert_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->get_alert_categories: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AlertCategories]**](AlertCategories.md)

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

# **get_alert_notification_rules**
> List[NotificationRule] get_alert_notification_rules(ids=ids)

List all notification rules

**Privileges:** ```ALERT_VIEW``` <br><br>List all notification rules configured.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.notification_rule import NotificationRule
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
    ids = [56] # List[int] | Specifies the ids of the notification rules. If this is not specified, all the notification rules will be returned.  (optional)

    try:
        # List all notification rules
        api_response = api_instance.get_alert_notification_rules(ids=ids)
        print("The response of AlertApi->get_alert_notification_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->get_alert_notification_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| Specifies the ids of the notification rules. If this is not specified, all the notification rules will be returned.  | [optional] 

### Return type

[**List[NotificationRule]**](NotificationRule.md)

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

# **get_alert_resolution**
> AlertResolutionOnPrem get_alert_resolution(id)

Get alert resolution by resolution Id

**Privileges:** ```ALERT_VIEW``` <br><br>Get alert resolution.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.alert_resolution_on_prem import AlertResolutionOnPrem
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
    id = 56 # int | Unique Id of the Alert Resolution.

    try:
        # Get alert resolution by resolution Id
        api_response = api_instance.get_alert_resolution(id)
        print("The response of AlertApi->get_alert_resolution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->get_alert_resolution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique Id of the Alert Resolution. | 

### Return type

[**AlertResolutionOnPrem**](AlertResolutionOnPrem.md)

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

# **get_alert_resolutions**
> List[AlertResolutionOnPrem] get_alert_resolutions(resolution_id_list=resolution_id_list, alert_id_list=alert_id_list, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, max_resolutions=max_resolutions, tenant_ids=tenant_ids, all_under_hierarchy=all_under_hierarchy)

Get alert resolutions.

**Privileges:** ```ALERT_VIEW``` <br><br>Get alert resolutions.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.alert_resolution_on_prem import AlertResolutionOnPrem
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
    resolution_id_list = [56] # List[int] | Specifies list of Alert Resolution ids to filter resolutions by.  (optional)
    alert_id_list = ['alert_id_list_example'] # List[str] | Specifies list of Alert ids to filter resolutions by. (optional)
    start_time_usecs = 56 # int | Specifies Start Time Unix epoch in microseconds to filter resolutions by.  (optional)
    end_time_usecs = 56 # int | Specifies End Time Unix epoch in microseconds to filter resolutions by.  (optional)
    max_resolutions = 56 # int | Specifies the number of resolutions to be returned in reverse chronological order.  (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | Specifies the tenant ids to filter resolutions  (optional)
    all_under_hierarchy = True # bool | Specifies if objects of all the tenants under the hierarchy of the logged in user's organization should be returned.  (optional)

    try:
        # Get alert resolutions.
        api_response = api_instance.get_alert_resolutions(resolution_id_list=resolution_id_list, alert_id_list=alert_id_list, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, max_resolutions=max_resolutions, tenant_ids=tenant_ids, all_under_hierarchy=all_under_hierarchy)
        print("The response of AlertApi->get_alert_resolutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->get_alert_resolutions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resolution_id_list** | [**List[int]**](int.md)| Specifies list of Alert Resolution ids to filter resolutions by.  | [optional] 
 **alert_id_list** | [**List[str]**](str.md)| Specifies list of Alert ids to filter resolutions by. | [optional] 
 **start_time_usecs** | **int**| Specifies Start Time Unix epoch in microseconds to filter resolutions by.  | [optional] 
 **end_time_usecs** | **int**| Specifies End Time Unix epoch in microseconds to filter resolutions by.  | [optional] 
 **max_resolutions** | **int**| Specifies the number of resolutions to be returned in reverse chronological order.  | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| Specifies the tenant ids to filter resolutions  | [optional] 
 **all_under_hierarchy** | **bool**| Specifies if objects of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned.  | [optional] 

### Return type

[**List[AlertResolutionOnPrem]**](AlertResolutionOnPrem.md)

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

# **get_alert_summary**
> AlertsSummaryResponse get_alert_summary(start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, include_tenants=include_tenants, tenant_ids=tenant_ids, states_list=states_list)

Get alerts summary.

**Privileges:** ```ALERT_VIEW``` <br><br>Get alerts summary grouped by category.

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

# **get_alert_types**
> List[AlertType] get_alert_types(categories=categories)

Get alert types.

**Privileges:** ```ALERT_VIEW``` <br><br>Get all defined alert types.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.alert_type import AlertType
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
    categories = ['categories_example'] # List[str] | Filter by list of alert categories. Provide as comma-separated values. (optional)

    try:
        # Get alert types.
        api_response = api_instance.get_alert_types(categories=categories)
        print("The response of AlertApi->get_alert_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->get_alert_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categories** | [**List[str]**](str.md)| Filter by list of alert categories. Provide as comma-separated values. | [optional] 

### Return type

[**List[AlertType]**](AlertType.md)

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

# **get_alerts**
> AlertList get_alerts(alert_ids=alert_ids, alert_types=alert_types, alert_categories=alert_categories, alert_states=alert_states, alert_severities=alert_severities, alert_type_buckets=alert_type_buckets, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, max_alerts=max_alerts, property_key=property_key, property_value=property_value, alert_name=alert_name, resolution_ids=resolution_ids, tenant_ids=tenant_ids, all_under_hierarchy=all_under_hierarchy)

Get alerts.

**Privileges:** ```ALERT_VIEW``` <br><br>

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.alert_list import AlertList
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
    alert_ids = ['alert_ids_example'] # List[str] | Filter by list of alert ids. (optional)
    alert_types = [56] # List[int] | Filter by list of alert types. (optional)
    alert_categories = ['alert_categories_example'] # List[str] | Filter by list of alert categories. (optional)
    alert_states = ['alert_states_example'] # List[str] | Filter by list of alert states. (optional)
    alert_severities = ['alert_severities_example'] # List[str] | Filter by list of alert severity types. (optional)
    alert_type_buckets = ['alert_type_buckets_example'] # List[str] | Filter by list of alert type buckets. (optional)
    start_time_usecs = 56 # int | Specifies start time Unix epoch time in microseconds to filter alerts by. (optional)
    end_time_usecs = 56 # int | Specifies end time Unix epoch time in microseconds to filter alerts by. (optional)
    max_alerts = 56 # int | Specifies maximum number of alerts to return.The default value is 100 and maximum allowed value is 1000 (optional)
    property_key = 'property_key_example' # str | Specifies name of the property to filter alerts by. (optional)
    property_value = 'property_value_example' # str | Specifies value of the property to filter alerts by. (optional)
    alert_name = 'alert_name_example' # str | Specifies name of alert to filter alerts by. (optional)
    resolution_ids = [56] # List[int] | Specifies alert resolution ids to filter alerts by. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | Filter by tenant ids. (optional)
    all_under_hierarchy = True # bool | Filter by objects of all the tenants under the hierarchy of the logged in user's organization. (optional)

    try:
        # Get alerts.
        api_response = api_instance.get_alerts(alert_ids=alert_ids, alert_types=alert_types, alert_categories=alert_categories, alert_states=alert_states, alert_severities=alert_severities, alert_type_buckets=alert_type_buckets, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, max_alerts=max_alerts, property_key=property_key, property_value=property_value, alert_name=alert_name, resolution_ids=resolution_ids, tenant_ids=tenant_ids, all_under_hierarchy=all_under_hierarchy)
        print("The response of AlertApi->get_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->get_alerts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_ids** | [**List[str]**](str.md)| Filter by list of alert ids. | [optional] 
 **alert_types** | [**List[int]**](int.md)| Filter by list of alert types. | [optional] 
 **alert_categories** | [**List[str]**](str.md)| Filter by list of alert categories. | [optional] 
 **alert_states** | [**List[str]**](str.md)| Filter by list of alert states. | [optional] 
 **alert_severities** | [**List[str]**](str.md)| Filter by list of alert severity types. | [optional] 
 **alert_type_buckets** | [**List[str]**](str.md)| Filter by list of alert type buckets. | [optional] 
 **start_time_usecs** | **int**| Specifies start time Unix epoch time in microseconds to filter alerts by. | [optional] 
 **end_time_usecs** | **int**| Specifies end time Unix epoch time in microseconds to filter alerts by. | [optional] 
 **max_alerts** | **int**| Specifies maximum number of alerts to return.The default value is 100 and maximum allowed value is 1000 | [optional] 
 **property_key** | **str**| Specifies name of the property to filter alerts by. | [optional] 
 **property_value** | **str**| Specifies value of the property to filter alerts by. | [optional] 
 **alert_name** | **str**| Specifies name of alert to filter alerts by. | [optional] 
 **resolution_ids** | [**List[int]**](int.md)| Specifies alert resolution ids to filter alerts by. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| Filter by tenant ids. | [optional] 
 **all_under_hierarchy** | **bool**| Filter by objects of all the tenants under the hierarchy of the logged in user&#39;s organization. | [optional] 

### Return type

[**AlertList**](AlertList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_alert_notification_rule**
> remove_alert_notification_rule(id)

Remove a notification rule

**Privileges:** ```ALERT_MODIFY``` <br><br>Remove an alert notification rule specified by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
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
    id = 56 # int | Unique Id of the notification rule.

    try:
        # Remove a notification rule
        api_instance.remove_alert_notification_rule(id)
    except Exception as e:
        print("Exception when calling AlertApi->remove_alert_notification_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique Id of the notification rule. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_notification_rule**
> NotificationRule update_alert_notification_rule(id, body)

Update a notification rule

**Privileges:** ```ALERT_MODIFY``` <br><br>Update Notification rule specified by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.notification_rule import NotificationRule
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
    id = 56 # int | Unique Id of the notification rule.
    body = cohesity_sdk.cluster.NotificationRule() # NotificationRule | Specifies the parameters to update notification rule.

    try:
        # Update a notification rule
        api_response = api_instance.update_alert_notification_rule(id, body)
        print("The response of AlertApi->update_alert_notification_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->update_alert_notification_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique Id of the notification rule. | 
 **body** | [**NotificationRule**](NotificationRule.md)| Specifies the parameters to update notification rule. | 

### Return type

[**NotificationRule**](NotificationRule.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_resolution**
> AlertResolutionOnPrem update_alert_resolution(id, body)

Update alert resolution.

**Privileges:** ```ALERT_MODIFY``` <br><br>Update alert resolution.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.alert_resolution_on_prem import AlertResolutionOnPrem
from cohesity_sdk.cluster.models.update_alert_resolution_request import UpdateAlertResolutionRequest
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
    id = 56 # int | Unique Id of the Alert Resolution.
    body = cohesity_sdk.cluster.UpdateAlertResolutionRequest() # UpdateAlertResolutionRequest | Provides Resolution details and the list of Alerts resolved by a Resolution which are specified by Alert Ids. 

    try:
        # Update alert resolution.
        api_response = api_instance.update_alert_resolution(id, body)
        print("The response of AlertApi->update_alert_resolution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->update_alert_resolution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique Id of the Alert Resolution. | 
 **body** | [**UpdateAlertResolutionRequest**](UpdateAlertResolutionRequest.md)| Provides Resolution details and the list of Alerts resolved by a Resolution which are specified by Alert Ids.  | 

### Return type

[**AlertResolutionOnPrem**](AlertResolutionOnPrem.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

