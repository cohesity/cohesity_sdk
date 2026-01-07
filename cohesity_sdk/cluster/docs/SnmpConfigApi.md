# cohesity_sdk.SnmpConfigApi


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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.snmp_config import SnmpConfig
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
	# Get Snmp Config
	api_response = client.snmp_config.get_snmp_config()
	pprint(api_response)
except ApiException as e:
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.snmp_config import SnmpConfig
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


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
	api_response = client.snmp_config.update_snmp_config(body)
	pprint(api_response)
except ApiException as e:
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

