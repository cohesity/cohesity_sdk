# cohesity_sdk.LDAPApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ldap_provider**](LDAPApi.md#create_ldap_provider) | **POST** /ldap | Create Ldap provider.
[**delete_ldap_provider**](LDAPApi.md#delete_ldap_provider) | **DELETE** /ldap/{id} | Delete LDAP provider.
[**get_ldap_connection_status**](LDAPApi.md#get_ldap_connection_status) | **GET** /ldap/{id}/connection-status | Get LDAP connection status.
[**get_ldaps**](LDAPApi.md#get_ldaps) | **GET** /ldap | Get Groups.
[**update_ldap_provider**](LDAPApi.md#update_ldap_provider) | **PUT** /ldap | Update Ldap provider.


# **create_ldap_provider**
> Ldap create_ldap_provider(body)

Create Ldap provider.

Create Ldap provider with given parameters.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.ldap import Ldap
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint



client = ClusterClient(cluster_vip)

body = Ldap() # Ldap | Specifies the parameters to create Ldap provider.

# example passing only required values which don't have defaults set
try:
	# Create Ldap provider.
	api_response = client.ldap.create_ldap_provider(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling LDAPApi->create_ldap_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Ldap**](Ldap.md)| Specifies the parameters to create Ldap provider. |

### Return type

[**Ldap**](Ldap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ldap_provider**
> delete_ldap_provider(id)

Delete LDAP provider.

Delete LDAP provider which will be identified by given Id.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint



client = ClusterClient(cluster_vip)

id = 1 # int | Specifies the LDAP Id.

# example passing only required values which don't have defaults set
try:
	# Delete LDAP provider.
	client.ldap.delete_ldap_provider(id)
except ApiException as e:
	print("Exception when calling LDAPApi->delete_ldap_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the LDAP Id. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ldap_connection_status**
> LdapStatus get_ldap_connection_status(id)

Get LDAP connection status.

Get LDAP connection status.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.ldap_status import LdapStatus
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint



client = ClusterClient(cluster_vip)

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

No authorization required

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

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.ldaps import Ldaps
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint



client = ClusterClient(cluster_vip)

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ldap_provider**
> Ldap update_ldap_provider(body)

Update Ldap provider.

Modify Ldap provider with given parameters.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.ldap import Ldap
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint



client = ClusterClient(cluster_vip)

body = Ldap() # Ldap | Specifies the parameters to update Ldap provider.

# example passing only required values which don't have defaults set
try:
	# Update Ldap provider.
	api_response = client.ldap.update_ldap_provider(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling LDAPApi->update_ldap_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Ldap**](Ldap.md)| Specifies the parameters to update Ldap provider. |

### Return type

[**Ldap**](Ldap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

