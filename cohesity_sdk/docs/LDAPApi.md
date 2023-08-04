# cohesity_sdk.LDAPApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ldap_connection_status**](LDAPApi.md#get_ldap_connection_status) | **GET** /ldap/{id}/connection-status | Get LDAP connection status.
[**get_ldaps**](LDAPApi.md#get_ldaps) | **GET** /ldap | Get Groups.


# **get_ldap_connection_status**
> LdapStatus get_ldap_connection_status(id)

Get LDAP connection status.

Get LDAP connection status.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.ldap_status import LdapStatus
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the LDAP id.

# example passing only required values which don't have defaults set
try:
	# Get LDAP connection status.
	api_response = client.ldap.get_ldap_connection_status(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling LDAPApi->get_ldap_connection_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the LDAP id. |

### Return type

[**LdapStatus**](LdapStatus.md)

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

# **get_ldaps**
> Ldaps get_ldaps()

Get Groups.

Get LDAPs.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.ldaps import Ldaps
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
    ] # [int] | Specifies a list of ids to filter. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which LDAPs are to be returned. (optional)
include_tenants = True # bool | IncludeTenants specifies if LDAPs of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Groups.
	api_response = client.ldap.get_ldaps(ids=ids, tenant_ids=tenant_ids, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling LDAPApi->get_ldaps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**| Specifies a list of ids to filter. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which LDAPs are to be returned. | [optional]
 **include_tenants** | **bool**| IncludeTenants specifies if LDAPs of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional]

### Return type

[**Ldaps**](Ldaps.md)

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

