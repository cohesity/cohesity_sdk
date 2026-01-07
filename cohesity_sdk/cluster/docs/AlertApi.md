# cohesity_sdk.AlertApi


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
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.notification_rule import NotificationRule
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = NotificationRule(
        alert_names=[
            "alert_names_example",
        ],
        categories=[
            "kDisk",
        ],
        email_delivery_targets=[
            EmailDeliveryTarget(
                email_address="email_address_example",
                locale="locale_example",
                recipient_type="kTo",
            ),
        ],
        rule_name="rule_name_example",
        severities=[
            "kCritical",
        ],
        snmp_enabled=True,
        syslog_enabled=True,
        tenant_id="tenant_id_example",
        webhook_delivery_targets=[
            WebhookDeliveryTarget(
                curl_options="curl_options_example",
                webhook_url="webhook_url_example",
            ),
        ],
    ) # NotificationRule | Specifies the alert notification rule config.

# example passing only required values which don't have defaults set
try:
	# Add a notification rule
	api_response = client.alert.create_alert_notification_rule(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AlertApi->create_alert_notification_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationRule**](NotificationRule.md)| Specifies the alert notification rule config. |

### Return type

[**NotificationRule**](NotificationRule.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.alert_resolution_on_prem import AlertResolutionOnPrem
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = AlertResolutionOnPrem(
        alert_id_list=[
            "alert_id_list_example",
        ],
        resolution_details=AlertResolutionDetailsV2(
            resolution_details="resolution_details_example",
            resolution_id=1,
            resolution_summary="resolution_summary_example",
            timestamp_usecs=1,
            user_name="user_name_example",
        ),
        tenant_ids=[
            "tenant_ids_example",
        ],
    ) # AlertResolutionOnPrem | \"Provides Resolution details and the list of Alerts resolved\" \"by a Resolution which are specified by Alert Ids.\" 

# example passing only required values which don't have defaults set
try:
	# Create alert resolution.
	api_response = client.alert.create_alert_resolution(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AlertApi->create_alert_resolution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertResolutionOnPrem**](AlertResolutionOnPrem.md)| \&quot;Provides Resolution details and the list of Alerts resolved\&quot; \&quot;by a Resolution which are specified by Alert Ids.\&quot;  |

### Return type

[**AlertResolutionOnPrem**](AlertResolutionOnPrem.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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
> ActiveAlertsStats get_active_alert_stats()

Get active alert statistics.

**Privileges:** ```ALERT_VIEW``` <br><br>Get statistics of active alerts. If no query parameters are provided, defaults to the last 10 days.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.active_alerts_stats import ActiveAlertsStats
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


start_time_usecs = 1 # int | Specifies the start time in miliseconds to filter the alert statistics. (optional)
end_time_usecs = 1 # int | Specifies the end time in miliseconds to filter the alert statistics.. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get active alert statistics.
	api_response = client.alert.get_active_alert_stats(start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs)
	pprint(api_response)
except ApiException as e:
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

# **get_alert_categories**
> [AlertCategories] get_alert_categories()

Get alert categories.

**Privileges:** ```ALERT_VIEW``` <br><br>Get all alert categories.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.alert_categories import AlertCategories
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
	# Get alert categories.
	api_response = client.alert.get_alert_categories()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AlertApi->get_alert_categories: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[AlertCategories]**](AlertCategories.md)

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

# **get_alert_notification_rules**
> [NotificationRule] get_alert_notification_rules()

List all notification rules

**Privileges:** ```ALERT_VIEW``` <br><br>List all notification rules configured.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.notification_rule import NotificationRule
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


ids = [
        1,
    ] # [int] | Specifies the ids of the notification rules. If this is not specified, all the notification rules will be returned.  (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List all notification rules
	api_response = client.alert.get_alert_notification_rules(ids=ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AlertApi->get_alert_notification_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**| Specifies the ids of the notification rules. If this is not specified, all the notification rules will be returned.  | [optional]

### Return type

[**[NotificationRule]**](NotificationRule.md)

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

# **get_alert_resolution**
> AlertResolutionOnPrem get_alert_resolution(id)

Get alert resolution by resolution Id

**Privileges:** ```ALERT_VIEW``` <br><br>Get alert resolution.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.alert_resolution_on_prem import AlertResolutionOnPrem
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Unique Id of the Alert Resolution.

# example passing only required values which don't have defaults set
try:
	# Get alert resolution by resolution Id
	api_response = client.alert.get_alert_resolution(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AlertApi->get_alert_resolution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique Id of the Alert Resolution. |

### Return type

[**AlertResolutionOnPrem**](AlertResolutionOnPrem.md)

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

# **get_alert_resolutions**
> [AlertResolutionOnPrem] get_alert_resolutions()

Get alert resolutions.

**Privileges:** ```ALERT_VIEW``` <br><br>Get alert resolutions.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.alert_resolution_on_prem import AlertResolutionOnPrem
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


resolution_id_list = [
        1,
    ] # [int] | Specifies list of Alert Resolution ids to filter resolutions by.  (optional)
alert_id_list = [
        "alertIdList_example",
    ] # [str] | Specifies list of Alert ids to filter resolutions by. (optional)
start_time_usecs = 1 # int, none_type | Specifies Start Time Unix epoch in microseconds to filter resolutions by.  (optional)
end_time_usecs = 1 # int, none_type | Specifies End Time Unix epoch in microseconds to filter resolutions by.  (optional)
max_resolutions = 1 # int, none_type | Specifies the number of resolutions to be returned in reverse chronological order.  (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | Specifies the tenant ids to filter resolutions  (optional)
all_under_hierarchy = True # bool, none_type | Specifies if objects of all the tenants under the hierarchy of the logged in user's organization should be returned.  (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get alert resolutions.
	api_response = client.alert.get_alert_resolutions(resolution_id_list=resolution_id_list, alert_id_list=alert_id_list, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, max_resolutions=max_resolutions, tenant_ids=tenant_ids, all_under_hierarchy=all_under_hierarchy)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AlertApi->get_alert_resolutions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resolution_id_list** | **[int]**| Specifies list of Alert Resolution ids to filter resolutions by.  | [optional]
 **alert_id_list** | **[str]**| Specifies list of Alert ids to filter resolutions by. | [optional]
 **start_time_usecs** | **int, none_type**| Specifies Start Time Unix epoch in microseconds to filter resolutions by.  | [optional]
 **end_time_usecs** | **int, none_type**| Specifies End Time Unix epoch in microseconds to filter resolutions by.  | [optional]
 **max_resolutions** | **int, none_type**| Specifies the number of resolutions to be returned in reverse chronological order.  | [optional]
 **tenant_ids** | **[str]**| Specifies the tenant ids to filter resolutions  | [optional]
 **all_under_hierarchy** | **bool, none_type**| Specifies if objects of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned.  | [optional]

### Return type

[**[AlertResolutionOnPrem]**](AlertResolutionOnPrem.md)

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

# **get_alert_summary**
> AlertsSummaryResponse get_alert_summary()

Get alerts summary.

**Privileges:** ```ALERT_VIEW``` <br><br>Get alerts summary grouped by category.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.alerts_summary_response import AlertsSummaryResponse
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


start_time_usecs = 1 # int | Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day. (optional)
end_time_usecs = 1 # int | Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time. (optional)
include_tenants = True # bool, none_type | IncludeTenants specifies if alerts of all the tenants under the hierarchy of the logged in user's organization should be used to compute summary. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str], none_type | TenantIds contains ids of the tenants for which alerts are to be used to compute summary. (optional)
states_list = [
        "kResolved",
    ] # [str], none_type | Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get alerts summary.
	api_response = client.alert.get_alert_summary(start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, include_tenants=include_tenants, tenant_ids=tenant_ids, states_list=states_list)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AlertApi->get_alert_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time_usecs** | **int**| Filter by start time. Specify the start time as a Unix epoch Timestamp (in microseconds). By default it is current time minus a day. | [optional]
 **end_time_usecs** | **int**| Filter by end time. Specify the end time as a Unix epoch Timestamp (in microseconds). By default it is current time. | [optional]
 **include_tenants** | **bool, none_type**| IncludeTenants specifies if alerts of all the tenants under the hierarchy of the logged in user&#39;s organization should be used to compute summary. | [optional]
 **tenant_ids** | **[str], none_type**| TenantIds contains ids of the tenants for which alerts are to be used to compute summary. | [optional]
 **states_list** | **[str], none_type**| Specifies list of alert states to filter alerts by. If not specified, only open alerts will be used to get summary. | [optional]

### Return type

[**AlertsSummaryResponse**](AlertsSummaryResponse.md)

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

# **get_alert_types**
> [AlertType] get_alert_types()

Get alert types.

**Privileges:** ```ALERT_VIEW``` <br><br>Get all defined alert types.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.alert_type import AlertType
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


categories = [
        "kDisk",
    ] # [str] | Filter by list of alert categories. Provide as comma-separated values. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get alert types.
	api_response = client.alert.get_alert_types(categories=categories)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AlertApi->get_alert_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categories** | **[str]**| Filter by list of alert categories. Provide as comma-separated values. | [optional]

### Return type

[**[AlertType]**](AlertType.md)

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

# **get_alerts**
> AlertList get_alerts()

Get alerts.

**Privileges:** ```ALERT_VIEW``` <br><br>

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.alert_list import AlertList
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


alert_ids = [
        "alertIds_example",
    ] # [str] | Filter by list of alert ids. (optional)
alert_types = [
        1,
    ] # [int] | Filter by list of alert types. (optional)
alert_categories = [
        "kDisk",
    ] # [str] | Filter by list of alert categories. (optional)
alert_states = [
        "kResolved",
    ] # [str] | Filter by list of alert states. (optional)
alert_severities = [
        "kCritical",
    ] # [str] | Filter by list of alert severity types. (optional)
alert_type_buckets = [
        "kHardware",
    ] # [str] | Filter by list of alert type buckets. (optional)
start_time_usecs = 1 # int, none_type | Specifies start time Unix epoch time in microseconds to filter alerts by. (optional)
end_time_usecs = 1 # int, none_type | Specifies end time Unix epoch time in microseconds to filter alerts by. (optional)
max_alerts = 1 # int, none_type | Specifies maximum number of alerts to return.The default value is 100 and maximum allowed value is 1000 (optional)
property_key = "propertyKey_example" # str, none_type | Specifies name of the property to filter alerts by. (optional)
property_value = "propertyValue_example" # str, none_type | Specifies value of the property to filter alerts by. (optional)
alert_name = "alertName_example" # str | Specifies name of alert to filter alerts by. (optional)
resolution_ids = [
        1,
    ] # [int] | Specifies alert resolution ids to filter alerts by. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | Filter by tenant ids. (optional)
all_under_hierarchy = True # bool, none_type | Filter by objects of all the tenants under the hierarchy of the logged in user's organization. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get alerts.
	api_response = client.alert.get_alerts(alert_ids=alert_ids, alert_types=alert_types, alert_categories=alert_categories, alert_states=alert_states, alert_severities=alert_severities, alert_type_buckets=alert_type_buckets, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, max_alerts=max_alerts, property_key=property_key, property_value=property_value, alert_name=alert_name, resolution_ids=resolution_ids, tenant_ids=tenant_ids, all_under_hierarchy=all_under_hierarchy)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AlertApi->get_alerts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_ids** | **[str]**| Filter by list of alert ids. | [optional]
 **alert_types** | **[int]**| Filter by list of alert types. | [optional]
 **alert_categories** | **[str]**| Filter by list of alert categories. | [optional]
 **alert_states** | **[str]**| Filter by list of alert states. | [optional]
 **alert_severities** | **[str]**| Filter by list of alert severity types. | [optional]
 **alert_type_buckets** | **[str]**| Filter by list of alert type buckets. | [optional]
 **start_time_usecs** | **int, none_type**| Specifies start time Unix epoch time in microseconds to filter alerts by. | [optional]
 **end_time_usecs** | **int, none_type**| Specifies end time Unix epoch time in microseconds to filter alerts by. | [optional]
 **max_alerts** | **int, none_type**| Specifies maximum number of alerts to return.The default value is 100 and maximum allowed value is 1000 | [optional]
 **property_key** | **str, none_type**| Specifies name of the property to filter alerts by. | [optional]
 **property_value** | **str, none_type**| Specifies value of the property to filter alerts by. | [optional]
 **alert_name** | **str**| Specifies name of alert to filter alerts by. | [optional]
 **resolution_ids** | **[int]**| Specifies alert resolution ids to filter alerts by. | [optional]
 **tenant_ids** | **[str]**| Filter by tenant ids. | [optional]
 **all_under_hierarchy** | **bool, none_type**| Filter by objects of all the tenants under the hierarchy of the logged in user&#39;s organization. | [optional]

### Return type

[**AlertList**](AlertList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Unique Id of the notification rule.

# example passing only required values which don't have defaults set
try:
	# Remove a notification rule
	client.alert.remove_alert_notification_rule(id)
except ApiException as e:
	print("Exception when calling AlertApi->remove_alert_notification_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique Id of the notification rule. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.notification_rule import NotificationRule
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Unique Id of the notification rule.
body = NotificationRule(
        alert_names=[
            "alert_names_example",
        ],
        categories=[
            "kDisk",
        ],
        email_delivery_targets=[
            EmailDeliveryTarget(
                email_address="email_address_example",
                locale="locale_example",
                recipient_type="kTo",
            ),
        ],
        rule_name="rule_name_example",
        severities=[
            "kCritical",
        ],
        snmp_enabled=True,
        syslog_enabled=True,
        tenant_id="tenant_id_example",
        webhook_delivery_targets=[
            WebhookDeliveryTarget(
                curl_options="curl_options_example",
                webhook_url="webhook_url_example",
            ),
        ],
    ) # NotificationRule | Specifies the parameters to update notification rule.

# example passing only required values which don't have defaults set
try:
	# Update a notification rule
	api_response = client.alert.update_alert_notification_rule(id, body)
	pprint(api_response)
except ApiException as e:
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.inline_object import InlineObject
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.alert_resolution_on_prem import AlertResolutionOnPrem
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Unique Id of the Alert Resolution.
body = InlineObject(
        alert_id_list=[
            "alert_id_list_example",
        ],
        resolution_id=1,
    ) # InlineObject | 

# example passing only required values which don't have defaults set
try:
	# Update alert resolution.
	api_response = client.alert.update_alert_resolution(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AlertApi->update_alert_resolution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique Id of the Alert Resolution. |
 **body** | [**InlineObject**](InlineObject.md)|  |

### Return type

[**AlertResolutionOnPrem**](AlertResolutionOnPrem.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

