# cohesity_sdk.SyslogApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**add_syslog_server**](SyslogApi.md#add_syslog_server) | **POST** /syslog | Add Syslog Server
[**get_supported_syslog_program_names**](SyslogApi.md#get_supported_syslog_program_names) | **GET** /syslog/program-names | Get supported program names.
[**get_syslog_audit_tags**](SyslogApi.md#get_syslog_audit_tags) | **GET** /syslog/audit-tags | Get cluster audit tags.
[**get_syslog_server_by_id**](SyslogApi.md#get_syslog_server_by_id) | **GET** /syslog/{id} | Get a syslog server by id.
[**get_syslog_server_status_by_id**](SyslogApi.md#get_syslog_server_status_by_id) | **GET** /syslog/{id}/status | Get a syslog server reachability status.
[**get_syslog_servers**](SyslogApi.md#get_syslog_servers) | **GET** /syslog | Get list of syslog servers.
[**patch_syslog_server_by_id**](SyslogApi.md#patch_syslog_server_by_id) | **PATCH** /syslog/{id} | Patch a syslog server by id.
[**remove_syslog_server**](SyslogApi.md#remove_syslog_server) | **DELETE** /syslog/{id} | Remove syslog server by id
[**remove_syslog_servers**](SyslogApi.md#remove_syslog_servers) | **DELETE** /syslog | Remove syslog servers
[**update_syslog_audit_tags**](SyslogApi.md#update_syslog_audit_tags) | **POST** /syslog/audit-tags | Update cluster audit tags.
[**update_syslog_server_by_id**](SyslogApi.md#update_syslog_server_by_id) | **PUT** /syslog/{id} | Update a syslog server by id.


# **add_syslog_server**
> SyslogServer add_syslog_server(body)

Add Syslog Server

Add a new syslog server

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.syslog_server import SyslogServer
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = SyslogServer(
        id=1,
        ip="ip_example",
        port=1,
        protocol="protocol_example",
        name="name_example",
        enabled=True,
        facility_list=[
            "facility_list_example",
        ],
        program_name_list=[
            "program_name_list_example",
        ],
        msg_pattern_list=[
            "msg_pattern_list_example",
        ],
        raw_msg_pattern_list=[
            "raw_msg_pattern_list_example",
        ],
        is_tls_enabled=True,
        ca_certificate="ca_certificate_example",
    ) # SyslogServer | Specifies parameters to add syslog server.

# example passing only required values which don't have defaults set
try:
	# Add Syslog Server
	api_response = client.syslog.add_syslog_server(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SyslogApi->add_syslog_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SyslogServer**](SyslogServer.md)| Specifies parameters to add syslog server. |

### Return type

[**SyslogServer**](SyslogServer.md)

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

# **get_supported_syslog_program_names**
> [str] get_supported_syslog_program_names()

Get supported program names.

Get supported program names to configure for a syslog server.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get supported program names.
	api_response = client.syslog.get_supported_syslog_program_names()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SyslogApi->get_supported_syslog_program_names: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[str]**

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

# **get_syslog_audit_tags**
> SyslogAuditTag get_syslog_audit_tags()

Get cluster audit tags.

Get cluster audit tags.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.syslog_audit_tag import SyslogAuditTag
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get cluster audit tags.
	api_response = client.syslog.get_syslog_audit_tags()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SyslogApi->get_syslog_audit_tags: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SyslogAuditTag**](SyslogAuditTag.md)

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

# **get_syslog_server_by_id**
> SyslogServer get_syslog_server_by_id(id)

Get a syslog server by id.

Get a syslog server by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.syslog_server import SyslogServer
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of syslog server.

# example passing only required values which don't have defaults set
try:
	# Get a syslog server by id.
	api_response = client.syslog.get_syslog_server_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SyslogApi->get_syslog_server_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of syslog server. |

### Return type

[**SyslogServer**](SyslogServer.md)

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

# **get_syslog_server_status_by_id**
> SyslogServerStatus get_syslog_server_status_by_id(id)

Get a syslog server reachability status.

Check syslog server reachability by given Id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.syslog_server_status import SyslogServerStatus
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of syslog server.

# example passing only required values which don't have defaults set
try:
	# Get a syslog server reachability status.
	api_response = client.syslog.get_syslog_server_status_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SyslogApi->get_syslog_server_status_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of syslog server. |

### Return type

[**SyslogServerStatus**](SyslogServerStatus.md)

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

# **get_syslog_servers**
> SyslogServers get_syslog_servers()

Get list of syslog servers.

Get list of syslog servers.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.syslog_servers import SyslogServers
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get list of syslog servers.
	api_response = client.syslog.get_syslog_servers()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SyslogApi->get_syslog_servers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SyslogServers**](SyslogServers.md)

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

# **patch_syslog_server_by_id**
> SyslogServer patch_syslog_server_by_id(id)

Patch a syslog server by id.

Patch syslog server by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.syslog_server import SyslogServer
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of syslog server.
body = SyslogServer(
        id=1,
        ip="ip_example",
        port=1,
        protocol="protocol_example",
        name="name_example",
        enabled=True,
        facility_list=[
            "facility_list_example",
        ],
        program_name_list=[
            "program_name_list_example",
        ],
        msg_pattern_list=[
            "msg_pattern_list_example",
        ],
        raw_msg_pattern_list=[
            "raw_msg_pattern_list_example",
        ],
        is_tls_enabled=True,
        ca_certificate="ca_certificate_example",
    ) # SyslogServer | Specifies the body of syslog server fields to patch. (optional)

# example passing only required values which don't have defaults set
try:
	# Patch a syslog server by id.
	api_response = client.syslog.patch_syslog_server_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SyslogApi->patch_syslog_server_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Patch a syslog server by id.
	api_response = client.syslog.patch_syslog_server_by_id(id, body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SyslogApi->patch_syslog_server_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of syslog server. |
 **body** | [**SyslogServer**](SyslogServer.md)| Specifies the body of syslog server fields to patch. | [optional]

### Return type

[**SyslogServer**](SyslogServer.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_syslog_server**
> remove_syslog_server(id)

Remove syslog server by id

Delete syslog server by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies a unique id of the syslog server.

# example passing only required values which don't have defaults set
try:
	# Remove syslog server by id
	client.syslog.remove_syslog_server(id)
except ApiException as e:
	print("Exception when calling SyslogApi->remove_syslog_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the syslog server. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_syslog_servers**
> remove_syslog_servers()

Remove syslog servers

Delete all syslog servers.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Remove syslog servers
	client.syslog.remove_syslog_servers()
except ApiException as e:
	print("Exception when calling SyslogApi->remove_syslog_servers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_syslog_audit_tags**
> SyslogAuditTag update_syslog_audit_tags()

Update cluster audit tags.

Update cluster audit tags.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.syslog_audit_tag import SyslogAuditTag
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = SyslogAuditTag(
        cluster_audit="cluster_audit_example",
        filer_audit="filer_audit_example",
        data_protection_events_audit="data_protection_events_audit_example",
        alert_audit="alert_audit_example",
    ) # SyslogAuditTag | Specifies syslog audit tag to update. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update cluster audit tags.
	api_response = client.syslog.update_syslog_audit_tags(body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SyslogApi->update_syslog_audit_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SyslogAuditTag**](SyslogAuditTag.md)| Specifies syslog audit tag to update. | [optional]

### Return type

[**SyslogAuditTag**](SyslogAuditTag.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_syslog_server_by_id**
> SyslogServer update_syslog_server_by_id(id)

Update a syslog server by id.

Update syslog server by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.syslog_server import SyslogServer
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of syslog server.
body = SyslogServer(
        id=1,
        ip="ip_example",
        port=1,
        protocol="protocol_example",
        name="name_example",
        enabled=True,
        facility_list=[
            "facility_list_example",
        ],
        program_name_list=[
            "program_name_list_example",
        ],
        msg_pattern_list=[
            "msg_pattern_list_example",
        ],
        raw_msg_pattern_list=[
            "raw_msg_pattern_list_example",
        ],
        is_tls_enabled=True,
        ca_certificate="ca_certificate_example",
    ) # SyslogServer | Specifies the body of syslog server body to update. (optional)

# example passing only required values which don't have defaults set
try:
	# Update a syslog server by id.
	api_response = client.syslog.update_syslog_server_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SyslogApi->update_syslog_server_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update a syslog server by id.
	api_response = client.syslog.update_syslog_server_by_id(id, body=body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SyslogApi->update_syslog_server_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of syslog server. |
 **body** | [**SyslogServer**](SyslogServer.md)| Specifies the body of syslog server body to update. | [optional]

### Return type

[**SyslogServer**](SyslogServer.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

