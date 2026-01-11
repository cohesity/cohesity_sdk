# cohesity_sdk.cluster.SnmpConfigApi

All URIs are relative to *http://localhost/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_snmp_config**](SnmpConfigApi.md#get_snmp_config) | **GET** /snmp/config | Get Snmp Config
[**update_snmp_config**](SnmpConfigApi.md#update_snmp_config) | **PUT** /snmp/config | Update Snmp Config


# **get_snmp_config**
> SnmpConfig get_snmp_config()

Get Snmp Config

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get Snmp Config.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import snmp_config
from cohesity_sdk.cluster.cohesity.model.snmp_config import SnmpConfig
from cohesity_sdk.cluster.cohesity.model.error import Error
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
    api_instance = snmp_config.SnmpConfigApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Snmp Config
        api_response = api_instance.get_snmp_config()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SnmpConfigApi->get_snmp_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SnmpConfig**](SnmpConfig.md)

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

# **update_snmp_config**
> SnmpConfig update_snmp_config(body)

Update Snmp Config

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update Snmp Config

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import snmp_config
from cohesity_sdk.cluster.cohesity.model.snmp_config import SnmpConfig
from cohesity_sdk.cluster.cohesity.model.error import Error
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
    api_instance = snmp_config.SnmpConfigApi(api_client)
    body = SnmpConfig(
        agent_port=1,
        operation="kOperationEnable",
        read_user=SnmpUser(
            auth_password="auth_password_example",
            auth_protocol="kAuthMD5",
            context_name="context_name_example",
            engine_id="engine_id_example",
            priv_password="priv_password_example",
            priv_protocol="kPrivDES",
            security_level="kNoAuthNoPriv",
            user_name="user_name_example",
            user_type="kReadUser",
        ),
        server="server_example",
        system_info=SnmpSysInfo(
            contact="contact_example",
            description="description_example",
            engine_id_type=1,
            location="location_example",
            name="name_example",
            object_id="object_id_example",
        ),
        trap_port=1,
        trap_user=SnmpUser(
            auth_password="auth_password_example",
            auth_protocol="kAuthMD5",
            context_name="context_name_example",
            engine_id="engine_id_example",
            priv_password="priv_password_example",
            priv_protocol="kPrivDES",
            security_level="kNoAuthNoPriv",
            user_name="user_name_example",
            user_type="kReadUser",
        ),
        version="kSnmpV2",
        vip="vip_example",
        write_user=SnmpUser(
            auth_password="auth_password_example",
            auth_protocol="kAuthMD5",
            context_name="context_name_example",
            engine_id="engine_id_example",
            priv_password="priv_password_example",
            priv_protocol="kPrivDES",
            security_level="kNoAuthNoPriv",
            user_name="user_name_example",
            user_type="kReadUser",
        ),
    ) # SnmpConfig | Modify Snmp Config with given parameters.

    # example passing only required values which don't have defaults set
    try:
        # Update Snmp Config
        api_response = api_instance.update_snmp_config(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling SnmpConfigApi->update_snmp_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SnmpConfig**](SnmpConfig.md)| Modify Snmp Config with given parameters. |

### Return type

[**SnmpConfig**](SnmpConfig.md)

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

