# cohesity_sdk.helios.IdentityProviderApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_idp**](IdentityProviderApi.md#authenticate_idp) | **POST** /mcm/idp/authenticate | Create an Identity Provider Configuration.
[**create_identity**](IdentityProviderApi.md#create_identity) | **POST** /identity-providers | Configure Identity Provider
[**create_identity_provider**](IdentityProviderApi.md#create_identity_provider) | **POST** /idps | Configure identity provider
[**create_idp**](IdentityProviderApi.md#create_idp) | **POST** /mcm/idps | Create an Identity Provider Configuration.
[**create_idp_principal**](IdentityProviderApi.md#create_idp_principal) | **POST** /mcm/idps/principals | Create an Identity Provider Configuration.
[**delete_identity**](IdentityProviderApi.md#delete_identity) | **DELETE** /identity-providers/{id} | Delete Identity Provider
[**delete_identity_provider**](IdentityProviderApi.md#delete_identity_provider) | **DELETE** /idps/{id} | Delete identity provider
[**delete_idp**](IdentityProviderApi.md#delete_idp) | **DELETE** /mcm/idps/{id} | Delete a IDP configuration.
[**delete_idp_principal**](IdentityProviderApi.md#delete_idp_principal) | **DELETE** /mcm/idps/principals/{sid} | Delete an IDP Principal.
[**get_identities**](IdentityProviderApi.md#get_identities) | **GET** /identity-providers | Get Identities
[**get_identity_providers**](IdentityProviderApi.md#get_identity_providers) | **GET** /idps | Get identity providers
[**get_idp_by_id**](IdentityProviderApi.md#get_idp_by_id) | **GET** /mcm/idps/{id} | List details about single Identity Provider configuration.
[**get_idp_principal_by_sid**](IdentityProviderApi.md#get_idp_principal_by_sid) | **GET** /mcm/idps/principals/{sid} | Get IDP Principal by SID
[**get_idps**](IdentityProviderApi.md#get_idps) | **GET** /mcm/idps | Get the list of IDP configurations.
[**idps_login**](IdentityProviderApi.md#idps_login) | **GET** /idps/login | Login to cluster using idp
[**list_idp_principals**](IdentityProviderApi.md#list_idp_principals) | **GET** /mcm/idps/principals | List IDP Principals
[**perform_identity_action**](IdentityProviderApi.md#perform_identity_action) | **POST** /identity-providers/actions | Perform Identity Action
[**update_identity**](IdentityProviderApi.md#update_identity) | **PUT** /identity-providers/{id} | Update Identity Provider
[**update_identity_provider**](IdentityProviderApi.md#update_identity_provider) | **PUT** /idps/{id} | Update identity provider
[**update_idp**](IdentityProviderApi.md#update_idp) | **PUT** /mcm/idps/{id} | Update IDP Configuration.
[**update_idp_principal**](IdentityProviderApi.md#update_idp_principal) | **PUT** /mcm/idps/principals/{sid} | Update IDP Principal.


# **authenticate_idp**
> Error authenticate_idp(saml_response, region_id=region_id)

Create an Identity Provider Configuration.

Authenticate Identity Provider (IDP)

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.error import Error
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    saml_response = 'saml_response_example' # str | Specifies the parameters to authenticate an Identity Provider.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Create an Identity Provider Configuration.
        api_response = api_instance.authenticate_idp(saml_response, region_id=region_id)
        print("The response of IdentityProviderApi->authenticate_idp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->authenticate_idp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_response** | **str**| Specifies the parameters to authenticate an Identity Provider. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

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

# **create_identity**
> IdentityConfig create_identity(body, access_cluster_id=access_cluster_id, region_id=region_id)

Configure Identity Provider

Configure Identity Provider on the cluster. Currently this API is only for Open ID providers, but will be expanded to include SAML providers in the future.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.identity_config import IdentityConfig
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    body = cohesity_sdk.helios.IdentityConfig() # IdentityConfig | Specifies parameters to configure Identity
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Configure Identity Provider
        api_response = api_instance.create_identity(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of IdentityProviderApi->create_identity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->create_identity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdentityConfig**](IdentityConfig.md)| Specifies parameters to configure Identity | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

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
> IdentityProviderConfiguration create_identity_provider(body, access_cluster_id=access_cluster_id, region_id=region_id)

Configure identity provider

Configure SAML based identity provider on the cluster

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.create_idp_request_params import CreateIdpRequestParams
from cohesity_sdk.helios.models.identity_provider_configuration import IdentityProviderConfiguration
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    body = cohesity_sdk.helios.CreateIdpRequestParams() # CreateIdpRequestParams | Specifies parameters to configure identity provider
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Configure identity provider
        api_response = api_instance.create_identity_provider(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of IdentityProviderApi->create_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->create_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateIdpRequestParams**](CreateIdpRequestParams.md)| Specifies parameters to configure identity provider | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

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

# **create_idp**
> Idp create_idp(body, region_id=region_id)

Create an Identity Provider Configuration.

Create Identity Provider (IDP) Configuration.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.create_or_update_idp_request import CreateOrUpdateIdpRequest
from cohesity_sdk.helios.models.idp import Idp
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    body = cohesity_sdk.helios.CreateOrUpdateIdpRequest() # CreateOrUpdateIdpRequest | Specifies the parameters to create an Identity Provider.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Create an Identity Provider Configuration.
        api_response = api_instance.create_idp(body, region_id=region_id)
        print("The response of IdentityProviderApi->create_idp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->create_idp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrUpdateIdpRequest**](CreateOrUpdateIdpRequest.md)| Specifies the parameters to create an Identity Provider. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**Idp**](Idp.md)

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

# **create_idp_principal**
> IdpPrincipal create_idp_principal(body, region_id=region_id)

Create an Identity Provider Configuration.

Create and IDP User or Group.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.idp_principal import IdpPrincipal
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    body = cohesity_sdk.helios.IdpPrincipal() # IdpPrincipal | Specifies the parameters to create an IDP Principal.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Create an Identity Provider Configuration.
        api_response = api_instance.create_idp_principal(body, region_id=region_id)
        print("The response of IdentityProviderApi->create_idp_principal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->create_idp_principal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdpPrincipal**](IdpPrincipal.md)| Specifies the parameters to create an IDP Principal. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**IdpPrincipal**](IdpPrincipal.md)

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
> delete_identity(id, access_cluster_id=access_cluster_id, region_id=region_id)

Delete Identity Provider

Delete identity provider configuration on the cluster. Currently this API only supports Open ID based SSO providers, but it will be expanded in the future to support SAML SSO providers.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    id = 56 # int | Specifies id of identity provider configuration
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Delete Identity Provider
        api_instance.delete_identity(id, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->delete_identity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of identity provider configuration | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

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
> delete_identity_provider(id, access_cluster_id=access_cluster_id, region_id=region_id)

Delete identity provider

Delete SAML based identity provider configuration on the cluster

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    id = 56 # int | Specifies id of idp configuration
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Delete identity provider
        api_instance.delete_identity_provider(id, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->delete_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of idp configuration | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

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

# **delete_idp**
> delete_idp(id, region_id=region_id)

Delete a IDP configuration.

Returns Success if the Identity Provider configuration is deleted.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    id = 56 # int | Specifies a unique id of the IDP.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Delete a IDP configuration.
        api_instance.delete_idp(id, region_id=region_id)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->delete_idp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the IDP. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

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

# **delete_idp_principal**
> delete_idp_principal(sid, region_id=region_id)

Delete an IDP Principal.

Returns Success if the Identity Provider Principal is deleted.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    sid = 'sid_example' # str | Specifies a unique SID of the Principal.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Delete an IDP Principal.
        api_instance.delete_idp_principal(sid, region_id=region_id)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->delete_idp_principal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specifies a unique SID of the Principal. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

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
> IdentityConfigs get_identities(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, tenant_ids=tenant_ids, domains=domains, include_all_tenants=include_all_tenants)

Get Identities

Get Identity Providers configured on the cluster. Currently this API only supports Open ID based SSO providers, but it will be expanded in the future to support SAML SSO providers.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.identity_configs import IdentityConfigs
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    ids = [56] # List[int] | Specifies IDs of configured identity providers (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | Specifies the tenant id's to get IDPs configured on tenants (optional)
    domains = ['domains_example'] # List[str] | Specifies domains of the IDP configurations (optional)
    include_all_tenants = True # bool | Specifies if IDP configurations on all the tenants under the hierarchy of the logged in user should be returned (optional)

    try:
        # Get Identities
        api_response = api_instance.get_identities(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, tenant_ids=tenant_ids, domains=domains, include_all_tenants=include_all_tenants)
        print("The response of IdentityProviderApi->get_identities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->get_identities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **ids** | [**List[int]**](int.md)| Specifies IDs of configured identity providers | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| Specifies the tenant id&#39;s to get IDPs configured on tenants | [optional] 
 **domains** | [**List[str]**](str.md)| Specifies domains of the IDP configurations | [optional] 
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
> IdentityProviderConfigurations get_identity_providers(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, tenant_ids=tenant_ids, names=names, domains=domains, include_all_tenants=include_all_tenants)

Get identity providers

Get SAML based identity providers configured on the cluster

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.identity_provider_configurations import IdentityProviderConfigurations
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    ids = [56] # List[int] | Specifies ids of configured identity providers (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | Specifies the tenant id's to get idps configured on tenants (optional)
    names = ['names_example'] # List[str] | Specifies the names of the identity providers (optional)
    domains = ['domains_example'] # List[str] | Specifies domains of the idp configurations (optional)
    include_all_tenants = True # bool | Specifies if idp configurations on all the tenants under the hierarchy of the logged in user should be returned (optional)

    try:
        # Get identity providers
        api_response = api_instance.get_identity_providers(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, tenant_ids=tenant_ids, names=names, domains=domains, include_all_tenants=include_all_tenants)
        print("The response of IdentityProviderApi->get_identity_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->get_identity_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **ids** | [**List[int]**](int.md)| Specifies ids of configured identity providers | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| Specifies the tenant id&#39;s to get idps configured on tenants | [optional] 
 **names** | [**List[str]**](str.md)| Specifies the names of the identity providers | [optional] 
 **domains** | [**List[str]**](str.md)| Specifies domains of the idp configurations | [optional] 
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

# **get_idp_by_id**
> Idp get_idp_by_id(id, region_id=region_id)

List details about single Identity Provider configuration.

Returns a specific Identity Provider configuration.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.idp import Idp
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    id = 56 # int | Specifies a unique id of the IDP.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # List details about single Identity Provider configuration.
        api_response = api_instance.get_idp_by_id(id, region_id=region_id)
        print("The response of IdentityProviderApi->get_idp_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->get_idp_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the IDP. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**Idp**](Idp.md)

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

# **get_idp_principal_by_sid**
> IdpPrincipal get_idp_principal_by_sid(sid, region_id=region_id)

Get IDP Principal by SID

List the IDP Principals which have been created.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.idp_principal import IdpPrincipal
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    sid = 'sid_example' # str | Specifies the ID of the IDP Principal.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get IDP Principal by SID
        api_response = api_instance.get_idp_principal_by_sid(sid, region_id=region_id)
        print("The response of IdentityProviderApi->get_idp_principal_by_sid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->get_idp_principal_by_sid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specifies the ID of the IDP Principal. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**IdpPrincipal**](IdpPrincipal.md)

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

# **get_idps**
> Idps get_idps(region_id=region_id, ids=ids, include_tenants=include_tenants)

Get the list of IDP configurations.

Get the list of Identity Providers (IDP) configurations.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.idps import Idps
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    ids = [56] # List[int] | Filter by a list of IDP ids. (optional)
    include_tenants = False # bool | IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user's organization should be returned. Default's to false. (optional) (default to False)

    try:
        # Get the list of IDP configurations.
        api_response = api_instance.get_idps(region_id=region_id, ids=ids, include_tenants=include_tenants)
        print("The response of IdentityProviderApi->get_idps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->get_idps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **ids** | [**List[int]**](int.md)| Filter by a list of IDP ids. | [optional] 
 **include_tenants** | **bool**| IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. Default&#39;s to false. | [optional] [default to False]

### Return type

[**Idps**](Idps.md)

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
> Error idps_login(access_cluster_id=access_cluster_id, region_id=region_id, tenant_id=tenant_id)

Login to cluster using idp

Redirects the client to the idp site with the URI to login

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.error import Error
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    tenant_id = 'tenant_id_example' # str | Specifies an optional tenantId for which the SSO login should be done. If this is not specified, cluster SSO login is done. (optional)

    try:
        # Login to cluster using idp
        api_response = api_instance.idps_login(access_cluster_id=access_cluster_id, region_id=region_id, tenant_id=tenant_id)
        print("The response of IdentityProviderApi->idps_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->idps_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
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

# **list_idp_principals**
> IdpPrincipals list_idp_principals(region_id=region_id, include_tenants=include_tenants, sids=sids)

List IDP Principals

List the IDP Principals which have been created.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.idp_principals import IdpPrincipals
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    include_tenants = True # bool | IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)
    sids = ['sids_example'] # List[str] | Specifies a list of principal SIDs. (optional)

    try:
        # List IDP Principals
        api_response = api_instance.list_idp_principals(region_id=region_id, include_tenants=include_tenants, sids=sids)
        print("The response of IdentityProviderApi->list_idp_principals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->list_idp_principals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **include_tenants** | **bool**| IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional] 
 **sids** | [**List[str]**](str.md)| Specifies a list of principal SIDs. | [optional] 

### Return type

[**IdpPrincipals**](IdpPrincipals.md)

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

# **perform_identity_action**
> IdentityAction perform_identity_action(body, access_cluster_id=access_cluster_id, region_id=region_id)

Perform Identity Action

Perform an action on an Identity Provider. Currently this API only supports Open ID based SSO providers, but it will be expanded in the future to support SAML SSO providers.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.identity_action import IdentityAction
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    body = cohesity_sdk.helios.IdentityAction() # IdentityAction | Specifies parameters perform an identity action.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Perform Identity Action
        api_response = api_instance.perform_identity_action(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of IdentityProviderApi->perform_identity_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->perform_identity_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdentityAction**](IdentityAction.md)| Specifies parameters perform an identity action. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

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
> IdentityConfig update_identity(id, body, access_cluster_id=access_cluster_id, region_id=region_id)

Update Identity Provider

Update Identity Provider on the cluster. Currently this API only supports Open ID based SSO providers, but it will be expanded in the future to support SAML SSO providers.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.identity_config import IdentityConfig
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    id = 56 # int | Specifies id of identity provider configuration
    body = cohesity_sdk.helios.IdentityConfig() # IdentityConfig | Specifies parameters to update identity provider configuration
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update Identity Provider
        api_response = api_instance.update_identity(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
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
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

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
> IdentityProviderConfiguration update_identity_provider(id, body, access_cluster_id=access_cluster_id, region_id=region_id)

Update identity provider

Update SAML based identity provider configurartion on the cluster

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.identity_provider_configuration import IdentityProviderConfiguration
from cohesity_sdk.helios.models.update_idp_request_params import UpdateIdpRequestParams
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    id = 56 # int | Specifies id of idp configuration
    body = cohesity_sdk.helios.UpdateIdpRequestParams() # UpdateIdpRequestParams | Specifies parameters to update identity provider configuration
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update identity provider
        api_response = api_instance.update_identity_provider(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of IdentityProviderApi->update_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->update_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of idp configuration | 
 **body** | [**UpdateIdpRequestParams**](UpdateIdpRequestParams.md)| Specifies parameters to update identity provider configuration | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

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

# **update_idp**
> Idp update_idp(id, body, region_id=region_id)

Update IDP Configuration.

Update the specified Identity Provider Configuration.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.create_or_update_idp_request import CreateOrUpdateIdpRequest
from cohesity_sdk.helios.models.idp import Idp
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    id = 56 # int | Specifies the id of the IDP configuration.
    body = cohesity_sdk.helios.CreateOrUpdateIdpRequest() # CreateOrUpdateIdpRequest | Specifies the parameters to update IDP configuration.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update IDP Configuration.
        api_response = api_instance.update_idp(id, body, region_id=region_id)
        print("The response of IdentityProviderApi->update_idp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->update_idp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the IDP configuration. | 
 **body** | [**CreateOrUpdateIdpRequest**](CreateOrUpdateIdpRequest.md)| Specifies the parameters to update IDP configuration. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**Idp**](Idp.md)

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

# **update_idp_principal**
> IdpPrincipal update_idp_principal(sid, body, region_id=region_id)

Update IDP Principal.

Update the specified IDP Principal

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.idp_principal import IdpPrincipal
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IdentityProviderApi(api_client)
    sid = 'sid_example' # str | Specifies the SID of the IDP Principal.
    body = cohesity_sdk.helios.IdpPrincipal() # IdpPrincipal | Specifies the parameters to update IDP Principal.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update IDP Principal.
        api_response = api_instance.update_idp_principal(sid, body, region_id=region_id)
        print("The response of IdentityProviderApi->update_idp_principal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->update_idp_principal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specifies the SID of the IDP Principal. | 
 **body** | [**IdpPrincipal**](IdpPrincipal.md)| Specifies the parameters to update IDP Principal. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**IdpPrincipal**](IdpPrincipal.md)

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

