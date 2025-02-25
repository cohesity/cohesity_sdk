# cohesity_sdk.IdentityProviderApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_identity**](IdentityProviderApi.md#create_identity) | **POST** /identity-providers | Configure Identity Provider
[**create_identity_provider**](IdentityProviderApi.md#create_identity_provider) | **POST** /idps | Configure identity provider
[**delete_identity**](IdentityProviderApi.md#delete_identity) | **DELETE** /identity-providers/{id} | Delete Identity Provider
[**delete_identity_provider**](IdentityProviderApi.md#delete_identity_provider) | **DELETE** /idps/{id} | Delete identity provider
[**get_identities**](IdentityProviderApi.md#get_identities) | **GET** /identity-providers | Get Identities
[**get_identity_providers**](IdentityProviderApi.md#get_identity_providers) | **GET** /idps | Get identity providers
[**idps_login**](IdentityProviderApi.md#idps_login) | **GET** /idps/login | Login to cluster using idp
[**perform_identity_action**](IdentityProviderApi.md#perform_identity_action) | **POST** /identity-providers/actions | Perform Identity Action
[**update_identity**](IdentityProviderApi.md#update_identity) | **PUT** /identity-providers/{id} | Update Identity Provider
[**update_identity_provider**](IdentityProviderApi.md#update_identity_provider) | **PUT** /idps/{id} | Update identity provider


# **create_identity**
> IdentityConfig create_identity(body)

Configure Identity Provider

Configure Identity Provider on the cluster. Currently this API is only for Open ID providers, but will be expanded to include SAML providers in the future.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.identity_config import IdentityConfig
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = IdentityConfig(
        domain="domain_example",
        identity_provider_type="OpenIdConnect",
        is_enabled=True,
        last_modified_timestamp_usecs=1,
        o_auth2_params=OAuth2Provider(
            audiences=[
                OAuthAudience(
                    audience_id="audience_id_example",
                    client_ids=[
                        "client_ids_example",
                    ],
                ),
            ],
            polling_frequency_mins=1440,
            public_key_url="public_key_url_example",
        ),
        open_id_connect_params=OpenIdProvider(
            audience_ids=[
                "audience_ids_example",
            ],
            polling_frequency_mins=1440,
            public_key_url="public_key_url_example",
        ),
        tenant_id="tenant_id_example",
    ) # IdentityConfig | Specifies parameters to configure Identity

# example passing only required values which don't have defaults set
try:
	# Configure Identity Provider
	api_response = client.identity_provider.create_identity(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->create_identity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdentityConfig**](IdentityConfig.md)| Specifies parameters to configure Identity |

### Return type

[**IdentityConfig**](IdentityConfig.md)

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

# **create_identity_provider**
> IdentityProviderConfiguration create_identity_provider(body)

Configure identity provider

Configure SAML based identity provider on the cluster

### Example

* Api Key Authentication (APIKeyHeader):
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

# **delete_identity**
> delete_identity(id)

Delete Identity Provider

Delete identity provider configuration on the cluster. Currently this API only supports Open ID based SSO providers, but it will be expanded in the future to support SAML SSO providers.

### Example

* Api Key Authentication (APIKeyHeader):
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


id = 1 # int | Specifies id of identity provider configuration

# example passing only required values which don't have defaults set
try:
	# Delete Identity Provider
	client.identity_provider.delete_identity(id)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->delete_identity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of identity provider configuration |

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

# **delete_identity_provider**
> delete_identity_provider(id)

Delete identity provider

Delete SAML based identity provider configuration on the cluster

### Example

* Api Key Authentication (APIKeyHeader):
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

# **get_identities**
> IdentityConfigs get_identities()

Get Identities

Get Identity Providers configured on the cluster. Currently this API only supports Open ID based SSO providers, but it will be expanded in the future to support SAML SSO providers.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.identity_configs import IdentityConfigs
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
    ] # [int] | Specifies IDs of configured identity providers (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | Specifies the tenant id's to get IDPs configured on tenants (optional)
domains = [
        "domains_example",
    ] # [str] | Specifies domains of the IDP configurations (optional)
include_all_tenants = True # bool | Specifies if IDP configurations on all the tenants under the hierarchy of the logged in user should be returned (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Identities
	api_response = client.identity_provider.get_identities(ids=ids, tenant_ids=tenant_ids, domains=domains, include_all_tenants=include_all_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->get_identities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**| Specifies IDs of configured identity providers | [optional]
 **tenant_ids** | **[str]**| Specifies the tenant id&#39;s to get IDPs configured on tenants | [optional]
 **domains** | **[str]**| Specifies domains of the IDP configurations | [optional]
 **include_all_tenants** | **bool**| Specifies if IDP configurations on all the tenants under the hierarchy of the logged in user should be returned | [optional]

### Return type

[**IdentityConfigs**](IdentityConfigs.md)

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

# **get_identity_providers**
> IdentityProviderConfigurations get_identity_providers()

Get identity providers

Get SAML based identity providers configured on the cluster

### Example

* Api Key Authentication (APIKeyHeader):
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

# **idps_login**
> Error idps_login()

Login to cluster using idp

Redirects the client to the idp site with the URI to login

### Example

* Api Key Authentication (APIKeyHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_identity_action**
> IdentityAction perform_identity_action(body)

Perform Identity Action

Perform an action on an Identity Provider. Currently this API only supports Open ID based SSO providers, but it will be expanded in the future to support SAML SSO providers.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.identity_action import IdentityAction
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = IdentityAction(
        identity_provider_type="OpenIdConnect",
        o_auth2_params=OAuth2Action(
            action="RefreshPublicKeys",
        ),
        open_id_connect_params=OpenIdConnectAction(
            action="RefreshPublicKeys",
        ),
    ) # IdentityAction | Specifies parameters perform an identity action.

# example passing only required values which don't have defaults set
try:
	# Perform Identity Action
	api_response = client.identity_provider.perform_identity_action(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->perform_identity_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdentityAction**](IdentityAction.md)| Specifies parameters perform an identity action. |

### Return type

[**IdentityAction**](IdentityAction.md)

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

# **update_identity**
> IdentityConfig update_identity(id, body)

Update Identity Provider

Update Identity Provider on the cluster. Currently this API only supports Open ID based SSO providers, but it will be expanded in the future to support SAML SSO providers.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.identity_config import IdentityConfig
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies id of identity provider configuration
body = IdentityConfig(
        domain="domain_example",
        identity_provider_type="OpenIdConnect",
        is_enabled=True,
        last_modified_timestamp_usecs=1,
        o_auth2_params=OAuth2Provider(
            audiences=[
                OAuthAudience(
                    audience_id="audience_id_example",
                    client_ids=[
                        "client_ids_example",
                    ],
                ),
            ],
            polling_frequency_mins=1440,
            public_key_url="public_key_url_example",
        ),
        open_id_connect_params=OpenIdProvider(
            audience_ids=[
                "audience_ids_example",
            ],
            polling_frequency_mins=1440,
            public_key_url="public_key_url_example",
        ),
        tenant_id="tenant_id_example",
    ) # IdentityConfig | Specifies parameters to update identity provider configuration

# example passing only required values which don't have defaults set
try:
	# Update Identity Provider
	api_response = client.identity_provider.update_identity(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->update_identity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of identity provider configuration |
 **body** | [**IdentityConfig**](IdentityConfig.md)| Specifies parameters to update identity provider configuration |

### Return type

[**IdentityConfig**](IdentityConfig.md)

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

# **update_identity_provider**
> IdentityProviderConfiguration update_identity_provider(id, body)

Update identity provider

Update SAML based identity provider configurartion on the cluster

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.identity_provider_configuration import IdentityProviderConfiguration
from cohesity_sdk.cluster.model.common_identity_provider_configuration import CommonIdentityProviderConfiguration
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies id of idp configuration
body = CommonIdentityProviderConfiguration(
        allow_local_user_login=True,
        certificate="certificate_example",
        certificate_filename="certificate_filename_example",
        is_enabled=True,
        issuer_id="issuer_id_example",
        roles=[
            "roles_example",
        ],
        saml_attribute_name="saml_attribute_name_example",
        sign_request=True,
        sso_url="sso_url_example",
    ) # CommonIdentityProviderConfiguration | Specifies parameters to update identity provider configuration

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
 **body** | [**CommonIdentityProviderConfiguration**](CommonIdentityProviderConfiguration.md)| Specifies parameters to update identity provider configuration |

### Return type

[**IdentityProviderConfiguration**](IdentityProviderConfiguration.md)

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

