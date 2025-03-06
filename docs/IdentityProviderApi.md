# cohesity_sdk.cluster.IdentityProviderApi

All URIs are relative to */v2*

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.identity_config import IdentityConfig
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.IdentityProviderApi(api_client)
    body = cohesity_sdk.cluster.IdentityConfig() # IdentityConfig | Specifies parameters to configure Identity

    try:
        # Configure Identity Provider
        api_response = api_instance.create_identity(body)
        print("The response of IdentityProviderApi->create_identity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->create_identity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdentityConfig**](IdentityConfig.md)| Specifies parameters to configure Identity | 

### Return type

[**IdentityConfig**](IdentityConfig.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.create_idp_request_params import CreateIdpRequestParams
from cohesity_sdk.cluster.models.identity_provider_configuration import IdentityProviderConfiguration
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.IdentityProviderApi(api_client)
    body = cohesity_sdk.cluster.CreateIdpRequestParams() # CreateIdpRequestParams | Specifies parameters to configure identity provider

    try:
        # Configure identity provider
        api_response = api_instance.create_identity_provider(body)
        print("The response of IdentityProviderApi->create_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->create_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateIdpRequestParams**](CreateIdpRequestParams.md)| Specifies parameters to configure identity provider | 

### Return type

[**IdentityProviderConfiguration**](IdentityProviderConfiguration.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.IdentityProviderApi(api_client)
    id = 56 # int | Specifies id of identity provider configuration

    try:
        # Delete Identity Provider
        api_instance.delete_identity(id)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->delete_identity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of identity provider configuration | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.IdentityProviderApi(api_client)
    id = 56 # int | Specifies id of idp configuration

    try:
        # Delete identity provider
        api_instance.delete_identity_provider(id)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->delete_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of idp configuration | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
> IdentityConfigs get_identities(ids=ids, tenant_ids=tenant_ids, domains=domains, include_all_tenants=include_all_tenants)

Get Identities

Get Identity Providers configured on the cluster. Currently this API only supports Open ID based SSO providers, but it will be expanded in the future to support SAML SSO providers.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.identity_configs import IdentityConfigs
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.IdentityProviderApi(api_client)
    ids = [56] # List[int] | Specifies IDs of configured identity providers (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | Specifies the tenant id's to get IDPs configured on tenants (optional)
    domains = ['domains_example'] # List[str] | Specifies domains of the IDP configurations (optional)
    include_all_tenants = True # bool | Specifies if IDP configurations on all the tenants under the hierarchy of the logged in user should be returned (optional)

    try:
        # Get Identities
        api_response = api_instance.get_identities(ids=ids, tenant_ids=tenant_ids, domains=domains, include_all_tenants=include_all_tenants)
        print("The response of IdentityProviderApi->get_identities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->get_identities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| Specifies IDs of configured identity providers | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| Specifies the tenant id&#39;s to get IDPs configured on tenants | [optional] 
 **domains** | [**List[str]**](str.md)| Specifies domains of the IDP configurations | [optional] 
 **include_all_tenants** | **bool**| Specifies if IDP configurations on all the tenants under the hierarchy of the logged in user should be returned | [optional] 

### Return type

[**IdentityConfigs**](IdentityConfigs.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
> IdentityProviderConfigurations get_identity_providers(ids=ids, tenant_ids=tenant_ids, names=names, domains=domains, include_all_tenants=include_all_tenants)

Get identity providers

Get SAML based identity providers configured on the cluster

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.identity_provider_configurations import IdentityProviderConfigurations
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.IdentityProviderApi(api_client)
    ids = [56] # List[int] | Specifies ids of configured identity providers (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | Specifies the tenant id's to get idps configured on tenants (optional)
    names = ['names_example'] # List[str] | Specifies the names of the identity providers (optional)
    domains = ['domains_example'] # List[str] | Specifies domains of the idp configurations (optional)
    include_all_tenants = True # bool | Specifies if idp configurations on all the tenants under the hierarchy of the logged in user should be returned (optional)

    try:
        # Get identity providers
        api_response = api_instance.get_identity_providers(ids=ids, tenant_ids=tenant_ids, names=names, domains=domains, include_all_tenants=include_all_tenants)
        print("The response of IdentityProviderApi->get_identity_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->get_identity_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| Specifies ids of configured identity providers | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| Specifies the tenant id&#39;s to get idps configured on tenants | [optional] 
 **names** | [**List[str]**](str.md)| Specifies the names of the identity providers | [optional] 
 **domains** | [**List[str]**](str.md)| Specifies domains of the idp configurations | [optional] 
 **include_all_tenants** | **bool**| Specifies if idp configurations on all the tenants under the hierarchy of the logged in user should be returned | [optional] 

### Return type

[**IdentityProviderConfigurations**](IdentityProviderConfigurations.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
> Error idps_login(tenant_id=tenant_id)

Login to cluster using idp

Redirects the client to the idp site with the URI to login

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.error import Error
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.IdentityProviderApi(api_client)
    tenant_id = 'tenant_id_example' # str | Specifies an optional tenantId for which the SSO login should be done. If this is not specified, cluster SSO login is done. (optional)

    try:
        # Login to cluster using idp
        api_response = api_instance.idps_login(tenant_id=tenant_id)
        print("The response of IdentityProviderApi->idps_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->idps_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Specifies an optional tenantId for which the SSO login should be done. If this is not specified, cluster SSO login is done. | [optional] 

### Return type

[**Error**](Error.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.identity_action import IdentityAction
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.IdentityProviderApi(api_client)
    body = cohesity_sdk.cluster.IdentityAction() # IdentityAction | Specifies parameters perform an identity action.

    try:
        # Perform Identity Action
        api_response = api_instance.perform_identity_action(body)
        print("The response of IdentityProviderApi->perform_identity_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->perform_identity_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdentityAction**](IdentityAction.md)| Specifies parameters perform an identity action. | 

### Return type

[**IdentityAction**](IdentityAction.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.identity_config import IdentityConfig
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.IdentityProviderApi(api_client)
    id = 56 # int | Specifies id of identity provider configuration
    body = cohesity_sdk.cluster.IdentityConfig() # IdentityConfig | Specifies parameters to update identity provider configuration

    try:
        # Update Identity Provider
        api_response = api_instance.update_identity(id, body)
        print("The response of IdentityProviderApi->update_identity:\n")
        pprint(api_response)
    except Exception as e:
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.common_identity_provider_configuration import CommonIdentityProviderConfiguration
from cohesity_sdk.cluster.models.identity_provider_configuration import IdentityProviderConfiguration
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.IdentityProviderApi(api_client)
    id = 56 # int | Specifies id of idp configuration
    body = cohesity_sdk.cluster.CommonIdentityProviderConfiguration() # CommonIdentityProviderConfiguration | Specifies parameters to update identity provider configuration

    try:
        # Update identity provider
        api_response = api_instance.update_identity_provider(id, body)
        print("The response of IdentityProviderApi->update_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->update_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of idp configuration | 
 **body** | **CommonIdentityProviderConfiguration**| Specifies parameters to update identity provider configuration | 

### Return type

[**IdentityProviderConfiguration**](IdentityProviderConfiguration.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

