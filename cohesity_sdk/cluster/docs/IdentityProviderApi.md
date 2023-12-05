# cohesity_sdk.IdentityProviderApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_identity_provider**](IdentityProviderApi.md#create_identity_provider) | **POST** /idps | Configure identity provider
[**delete_identity_provider**](IdentityProviderApi.md#delete_identity_provider) | **DELETE** /idps/{id} | Delete identity provider
[**get_identity_providers**](IdentityProviderApi.md#get_identity_providers) | **GET** /idps | Get identity providers
[**idps_login**](IdentityProviderApi.md#idps_login) | **GET** /idps/login | Login to cluster using idp
[**update_identity_provider**](IdentityProviderApi.md#update_identity_provider) | **PUT** /idps/{id} | Update identity provider


# **create_identity_provider**
> IdentityProviderConfiguration create_identity_provider(body)

Configure identity provider

Configure identity provider on the cluster

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.create_idp_request_params import CreateIdpRequestParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.identity_provider_configuration import IdentityProviderConfiguration
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

body = CreateIdpRequestParams() # CreateIdpRequestParams | Specifies parameters to configure identity provider

# example passing only required values which don't have defaults set
try:
	# Configure identity provider
	api_response = client.identity_provider.create_identity_provider(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->create_identity_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateIdpRequestParams**](CreateIdpRequestParams.md)| Specifies parameters to configure identity provider |

### Return type

[**IdentityProviderConfiguration**](IdentityProviderConfiguration.md)

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

# **delete_identity_provider**
> delete_identity_provider(id)

Delete identity provider

Delete identity provider configuration on the cluster

### Example

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

id = 1 # int | Specifies id of idp configuration

# example passing only required values which don't have defaults set
try:
	# Delete identity provider
	client.identity_provider.delete_identity_provider(id)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->delete_identity_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of idp configuration |

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

# **get_identity_providers**
> IdentityProviderConfigurations get_identity_providers()

Get identity providers

Get identity providers configured on the cluster

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.identity_provider_configurations import IdentityProviderConfigurations
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
    ] # [int] | Specifies ids of configured identity providers (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | Specifies the tenant id's to get idps configured on tenants (optional)
names = [
        "names_example",
    ] # [str] | Specifies the names of the identity providers (optional)
domains = [
        "domains_example",
    ] # [str] | Specifies domains of the idp configurations (optional)
include_all_tenants = True # bool | Specifies if idp configurations on all the tenants under the hierarchy of the logged in user should be returned (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get identity providers
	api_response = client.identity_provider.get_identity_providers(ids=ids, tenant_ids=tenant_ids, names=names, domains=domains, include_all_tenants=include_all_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->get_identity_providers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**| Specifies ids of configured identity providers | [optional]
 **tenant_ids** | **[str]**| Specifies the tenant id&#39;s to get idps configured on tenants | [optional]
 **names** | **[str]**| Specifies the names of the identity providers | [optional]
 **domains** | **[str]**| Specifies domains of the idp configurations | [optional]
 **include_all_tenants** | **bool**| Specifies if idp configurations on all the tenants under the hierarchy of the logged in user should be returned | [optional]

### Return type

[**IdentityProviderConfigurations**](IdentityProviderConfigurations.md)

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

# **idps_login**
> Error idps_login()

Login to cluster using idp

Redirects the client to the idp site with the URI to login

### Example

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

tenant_id = "tenantId_example" # str | Specifies an optional tenantId for which the SSO login should be done. If this is not specified, cluster SSO login is done. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Login to cluster using idp
	api_response = client.identity_provider.idps_login(tenant_id=tenant_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->idps_login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Specifies an optional tenantId for which the SSO login should be done. If this is not specified, cluster SSO login is done. | [optional]

### Return type

[**Error**](Error.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_identity_provider**
> IdentityProviderConfiguration update_identity_provider(id, body)

Update identity provider

Update identity provider configurartion on the cluster

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.update_idp_request_params import UpdateIdpRequestParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.identity_provider_configuration import IdentityProviderConfiguration
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

id = 1 # int | Specifies id of idp configuration
body = UpdateIdpRequestParams() # UpdateIdpRequestParams | Specifies parameters to update identity provider configuration

# example passing only required values which don't have defaults set
try:
	# Update identity provider
	api_response = client.identity_provider.update_identity_provider(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->update_identity_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of idp configuration |
 **body** | [**UpdateIdpRequestParams**](UpdateIdpRequestParams.md)| Specifies parameters to update identity provider configuration |

### Return type

[**IdentityProviderConfiguration**](IdentityProviderConfiguration.md)

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

