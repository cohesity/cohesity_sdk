# cohesity_sdk.KerberosProviderApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_kerberos_provider_by_id**](KerberosProviderApi.md#get_kerberos_provider_by_id) | **GET** /kerberos-providers/{id} | Get the Registered Kerberos Provider by id.
[**get_kerberos_providers**](KerberosProviderApi.md#get_kerberos_providers) | **GET** /kerberos-providers | Get the list of Kerberos Providers.
[**register_kerberos_provider**](KerberosProviderApi.md#register_kerberos_provider) | **POST** /kerberos-providers/register | Register a Kerberos Authentication Provider.
[**unregister_kerberos_provider**](KerberosProviderApi.md#unregister_kerberos_provider) | **POST** /kerberos-providers/{id}/unregister | Unregister a Kerberos Provider.
[**update_kerberos_provider**](KerberosProviderApi.md#update_kerberos_provider) | **PUT** /kerberos-providers/{id} | Update the Kerberos Provider Registration.


# **get_kerberos_provider_by_id**
> KerberosProvider get_kerberos_provider_by_id(id)

Get the Registered Kerberos Provider by id.

Get the Registered Kerberos Provider by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.kerberos_provider import KerberosProvider
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies the id which will be of the pattern cluster_id:clusterincarnation_id:resource_id.

# example passing only required values which don't have defaults set
try:
	# Get the Registered Kerberos Provider by id.
	api_response = client.kerberos_provider.get_kerberos_provider_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling KerberosProviderApi->get_kerberos_provider_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id which will be of the pattern cluster_id:clusterincarnation_id:resource_id. |

### Return type

[**KerberosProvider**](KerberosProvider.md)

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

# **get_kerberos_providers**
> KerberosProviders get_kerberos_providers()

Get the list of Kerberos Providers.

Get the list of Kerberos Authentication Providers.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.kerberos_providers import KerberosProviders
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


realm_names = [
        "realmNames_example",
    ] # [str] | Filter by a list of realm names. (optional)
has_ldap = True # bool, none_type | Filter by whether LDAP is associated with the provider. (optional)
ids = [
        1,
    ] # [int] | Filter by a list of Kerberos Provider Ids. (optional)
kdc_servers = [
        "kdcServers_example",
    ] # [str] | Filter by a list of KDC servers. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the list of Kerberos Providers.
	api_response = client.kerberos_provider.get_kerberos_providers(realm_names=realm_names, has_ldap=has_ldap, ids=ids, kdc_servers=kdc_servers)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling KerberosProviderApi->get_kerberos_providers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm_names** | **[str]**| Filter by a list of realm names. | [optional]
 **has_ldap** | **bool, none_type**| Filter by whether LDAP is associated with the provider. | [optional]
 **ids** | **[int]**| Filter by a list of Kerberos Provider Ids. | [optional]
 **kdc_servers** | **[str]**| Filter by a list of KDC servers. | [optional]

### Return type

[**KerberosProviders**](KerberosProviders.md)

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

# **register_kerberos_provider**
> KerberosProvider register_kerberos_provider(body)

Register a Kerberos Authentication Provider.

Register a Kerberos Authentication Provider.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.kerberos_provider import KerberosProvider
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.register_or_update_kerberos_provider_request import RegisterOrUpdateKerberosProviderRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = RegisterOrUpdateKerberosProviderRequest() # RegisterOrUpdateKerberosProviderRequest | Specifies the parameters to Register a Kerberos Provider.

# example passing only required values which don't have defaults set
try:
	# Register a Kerberos Authentication Provider.
	api_response = client.kerberos_provider.register_kerberos_provider(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling KerberosProviderApi->register_kerberos_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterOrUpdateKerberosProviderRequest**](RegisterOrUpdateKerberosProviderRequest.md)| Specifies the parameters to Register a Kerberos Provider. |

### Return type

[**KerberosProvider**](KerberosProvider.md)

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

# **unregister_kerberos_provider**
> UnregisterKerberosProvider unregister_kerberos_provider(id, body)

Unregister a Kerberos Provider.

Unregister a Kerberos Provider.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.unregister_kerberos_request import UnregisterKerberosRequest
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.unregister_kerberos_provider import UnregisterKerberosProvider
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies the id.
body = UnregisterKerberosRequest(
        admin_password="admin_password_example",
        admin_principal="admin_principal_example",
    ) # UnregisterKerberosRequest | Request to unregister a Kerberos Provider.

# example passing only required values which don't have defaults set
try:
	# Unregister a Kerberos Provider.
	api_response = client.kerberos_provider.unregister_kerberos_provider(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling KerberosProviderApi->unregister_kerberos_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id. |
 **body** | [**UnregisterKerberosRequest**](UnregisterKerberosRequest.md)| Request to unregister a Kerberos Provider. |

### Return type

[**UnregisterKerberosProvider**](UnregisterKerberosProvider.md)

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

# **update_kerberos_provider**
> KerberosProvider update_kerberos_provider(id, body)

Update the Kerberos Provider Registration.

Update the Kerberos Provider Registration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.kerberos_provider import KerberosProvider
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.register_or_update_kerberos_provider_request import RegisterOrUpdateKerberosProviderRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "4:072888001528021798096225500850762068629:39333975650685139102691291732729478601482026" # str | Specifies the id which will be of the pattern cluster_id:clusterincarnation_id:resource_id.
body = RegisterOrUpdateKerberosProviderRequest() # RegisterOrUpdateKerberosProviderRequest | Request to update a Kerberos Provider.

# example passing only required values which don't have defaults set
try:
	# Update the Kerberos Provider Registration.
	api_response = client.kerberos_provider.update_kerberos_provider(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling KerberosProviderApi->update_kerberos_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id which will be of the pattern cluster_id:clusterincarnation_id:resource_id. |
 **body** | [**RegisterOrUpdateKerberosProviderRequest**](RegisterOrUpdateKerberosProviderRequest.md)| Request to update a Kerberos Provider. |

### Return type

[**KerberosProvider**](KerberosProvider.md)

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

