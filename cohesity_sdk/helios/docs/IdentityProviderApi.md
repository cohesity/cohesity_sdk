# cohesity_sdk.IdentityProviderApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_idp**](IdentityProviderApi.md#authenticate_idp) | **POST** /mcm/idp/authenticate | Create an Identity Provider Configuration.
[**create_identity_provider**](IdentityProviderApi.md#create_identity_provider) | **POST** /idps | Configure identity provider
[**create_idp**](IdentityProviderApi.md#create_idp) | **POST** /mcm/idps | Create an Identity Provider Configuration.
[**create_idp_principal**](IdentityProviderApi.md#create_idp_principal) | **POST** /mcm/idps/principals | Create an Identity Provider Configuration.
[**delete_identity_provider**](IdentityProviderApi.md#delete_identity_provider) | **DELETE** /idps/{id} | Delete identity provider
[**delete_idp**](IdentityProviderApi.md#delete_idp) | **DELETE** /mcm/idps/{id} | Delete a IDP configuration.
[**delete_idp_principal**](IdentityProviderApi.md#delete_idp_principal) | **DELETE** /mcm/idps/principals/{sid} | Delete an IDP Principal.
[**get_identity_providers**](IdentityProviderApi.md#get_identity_providers) | **GET** /idps | Get identity providers
[**get_idp_by_id**](IdentityProviderApi.md#get_idp_by_id) | **GET** /mcm/idps/{id} | List details about single Identity Provider configuration.
[**get_idp_principal_by_sid**](IdentityProviderApi.md#get_idp_principal_by_sid) | **GET** /mcm/idps/principals/{sid} | Get IDP Principal by SID
[**get_idps**](IdentityProviderApi.md#get_idps) | **GET** /mcm/idps | Get the list of IDP configurations.
[**idps_login**](IdentityProviderApi.md#idps_login) | **GET** /idps/login | Login to cluster using idp
[**list_idp_principals**](IdentityProviderApi.md#list_idp_principals) | **GET** /mcm/idps/principals | List IDP Principals
[**update_identity_provider**](IdentityProviderApi.md#update_identity_provider) | **PUT** /idps/{id} | Update identity provider
[**update_idp**](IdentityProviderApi.md#update_idp) | **PUT** /mcm/idps/{id} | Update IDP Configuration.
[**update_idp_principal**](IdentityProviderApi.md#update_idp_principal) | **PUT** /mcm/idps/principals/{sid} | Update IDP Principal.


# **authenticate_idp**
> Error authenticate_idp(saml_response)

Create an Identity Provider Configuration.

Authenticate Identity Provider (IDP)

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


saml_response = "SAMLResponse_example" # str | Specifies the parameters to authenticate an Identity Provider.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create an Identity Provider Configuration.
	api_response = client.identity_provider.authenticate_idp(saml_response)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->authenticate_idp: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create an Identity Provider Configuration.
	api_response = client.identity_provider.authenticate_idp(saml_response, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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

# **create_identity_provider**
> IdentityProviderConfiguration create_identity_provider(body)

Configure identity provider

Configure identity provider on the cluster

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.identity_provider_configuration import IdentityProviderConfiguration
from cohesity_sdk.helios.model.create_idp_request_params import CreateIdpRequestParams
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = CreateIdpRequestParams() # CreateIdpRequestParams | Specifies parameters to configure identity provider
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Configure identity provider
	api_response = client.identity_provider.create_identity_provider(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->create_identity_provider: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Configure identity provider
	api_response = client.identity_provider.create_identity_provider(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> Idp create_idp(body)

Create an Identity Provider Configuration.

Create Identity Provider (IDP) Configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.create_or_update_idp_request import CreateOrUpdateIdpRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.idp import Idp
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = CreateOrUpdateIdpRequest() # CreateOrUpdateIdpRequest | Specifies the parameters to create an Identity Provider.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create an Identity Provider Configuration.
	api_response = client.identity_provider.create_idp(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->create_idp: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create an Identity Provider Configuration.
	api_response = client.identity_provider.create_idp(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> IdpPrincipal create_idp_principal(body)

Create an Identity Provider Configuration.

Create and IDP User or Group.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.idp_principal import IdpPrincipal
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = IdpPrincipal(
        name="name_example",
        idp_id=1,
        principal_type="User",
        roles=[
            "roles_example",
        ],
        clusters=[
            "clusters_example",
        ],
        is_active=True,
        effective_time_usecs=1,
        expired_time_usecs=1,
        profiles=[
            McmTenantProfile(
                tenant_id="tenant_id_example",
                tenant_type="Dmaas",
                clusters=[
                    McmClusterIdentifier(
                        cluster_id=1,
                        cluster_incarnation_id=1,
                        region_id="region_id_example",
                    ),
                ],
            ),
        ],
        tenant_accesses=[
            TenantAccess(
                tenant_id="tenant_id_example",
                roles=[
                    "roles_example",
                ],
                clusters=[
                    McmClusterIdentifier(
                        cluster_id=1,
                        cluster_incarnation_id=1,
                        region_id="region_id_example",
                    ),
                ],
            ),
        ],
    ) # IdpPrincipal | Specifies the parameters to create an IDP Principal.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create an Identity Provider Configuration.
	api_response = client.identity_provider.create_idp_principal(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->create_idp_principal: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create an Identity Provider Configuration.
	api_response = client.identity_provider.create_idp_principal(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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

# **delete_identity_provider**
> delete_identity_provider(id)

Delete identity provider

Delete identity provider configuration on the cluster

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies id of idp configuration
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete identity provider
	client.identity_provider.delete_identity_provider(id)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->delete_identity_provider: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete identity provider
	client.identity_provider.delete_identity_provider(id, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
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
> delete_idp(id)

Delete a IDP configuration.

Returns Success if the Identity Provider configuration is deleted.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies a unique id of the IDP.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete a IDP configuration.
	client.identity_provider.delete_idp(id)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->delete_idp: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete a IDP configuration.
	client.identity_provider.delete_idp(id, region_id=region_id)
except ApiException as e:
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
> delete_idp_principal(sid)

Delete an IDP Principal.

Returns Success if the Identity Provider Principal is deleted.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


sid = "sid_example" # str | Specifies a unique SID of the Principal.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete an IDP Principal.
	client.identity_provider.delete_idp_principal(sid)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->delete_idp_principal: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete an IDP Principal.
	client.identity_provider.delete_idp_principal(sid, region_id=region_id)
except ApiException as e:
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

# **get_identity_providers**
> IdentityProviderConfigurations get_identity_providers()

Get identity providers

Get identity providers configured on the cluster

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.identity_provider_configurations import IdentityProviderConfigurations
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
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
	api_response = client.identity_provider.get_identity_providers(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, tenant_ids=tenant_ids, names=names, domains=domains, include_all_tenants=include_all_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->get_identity_providers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
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

# **get_idp_by_id**
> Idp get_idp_by_id(id)

List details about single Identity Provider configuration.

Returns a specific Identity Provider configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.idp import Idp
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies a unique id of the IDP.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# List details about single Identity Provider configuration.
	api_response = client.identity_provider.get_idp_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->get_idp_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List details about single Identity Provider configuration.
	api_response = client.identity_provider.get_idp_by_id(id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> IdpPrincipal get_idp_principal_by_sid(sid)

Get IDP Principal by SID

List the IDP Principals which have been created.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.idp_principal import IdpPrincipal
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


sid = "sid_example" # str | Specifies the ID of the IDP Principal.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get IDP Principal by SID
	api_response = client.identity_provider.get_idp_principal_by_sid(sid)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->get_idp_principal_by_sid: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get IDP Principal by SID
	api_response = client.identity_provider.get_idp_principal_by_sid(sid, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> Idps get_idps()

Get the list of IDP configurations.

Get the list of Identity Providers (IDP) configurations.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.idps import Idps
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
ids = [
        1,
    ] # [int] | Filter by a list of IDP ids. (optional)
include_tenants = False # bool | IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user's organization should be returned. Default's to false. (optional) if omitted the server will use the default value of False

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the list of IDP configurations.
	api_response = client.identity_provider.get_idps(region_id=region_id, ids=ids, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->get_idps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **ids** | **[int]**| Filter by a list of IDP ids. | [optional]
 **include_tenants** | **bool**| IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. Default&#39;s to false. | [optional] if omitted the server will use the default value of False

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
> Error idps_login()

Login to cluster using idp

Redirects the client to the idp site with the URI to login

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
tenant_id = "tenantId_example" # str | Specifies an optional tenantId for which the SSO login should be done. If this is not specified, cluster SSO login is done. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Login to cluster using idp
	api_response = client.identity_provider.idps_login(access_cluster_id=access_cluster_id, region_id=region_id, tenant_id=tenant_id)
	pprint(api_response)
except ApiException as e:
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
> IdpPrincipals list_idp_principals()

List IDP Principals

List the IDP Principals which have been created.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.idp_principals import IdpPrincipals
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
include_tenants = True # bool | IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)
sids = [
        "sids_example",
    ] # [str] | Specifies a list of principal SIDs. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List IDP Principals
	api_response = client.identity_provider.list_idp_principals(region_id=region_id, include_tenants=include_tenants, sids=sids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->list_idp_principals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **include_tenants** | **bool**| IncludeTenants specifies if objects of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional]
 **sids** | **[str]**| Specifies a list of principal SIDs. | [optional]

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

# **update_identity_provider**
> IdentityProviderConfiguration update_identity_provider(id, body)

Update identity provider

Update identity provider configurartion on the cluster

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.identity_provider_configuration import IdentityProviderConfiguration
from cohesity_sdk.helios.model.update_idp_request_params import UpdateIdpRequestParams
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies id of idp configuration
body = UpdateIdpRequestParams() # UpdateIdpRequestParams | Specifies parameters to update identity provider configuration
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update identity provider
	api_response = client.identity_provider.update_identity_provider(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->update_identity_provider: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update identity provider
	api_response = client.identity_provider.update_identity_provider(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> Idp update_idp(id, body)

Update IDP Configuration.

Update the specified Identity Provider Configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.create_or_update_idp_request import CreateOrUpdateIdpRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.idp import Idp
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of the IDP configuration.
body = CreateOrUpdateIdpRequest() # CreateOrUpdateIdpRequest | Specifies the parameters to update IDP configuration.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update IDP Configuration.
	api_response = client.identity_provider.update_idp(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->update_idp: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update IDP Configuration.
	api_response = client.identity_provider.update_idp(id, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> IdpPrincipal update_idp_principal(sid, body)

Update IDP Principal.

Update the specified IDP Principal

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.idp_principal import IdpPrincipal
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


sid = "sid_example" # str | Specifies the SID of the IDP Principal.
body = IdpPrincipal(
        name="name_example",
        idp_id=1,
        principal_type="User",
        roles=[
            "roles_example",
        ],
        clusters=[
            "clusters_example",
        ],
        is_active=True,
        effective_time_usecs=1,
        expired_time_usecs=1,
        profiles=[
            McmTenantProfile(
                tenant_id="tenant_id_example",
                tenant_type="Dmaas",
                clusters=[
                    McmClusterIdentifier(
                        cluster_id=1,
                        cluster_incarnation_id=1,
                        region_id="region_id_example",
                    ),
                ],
            ),
        ],
        tenant_accesses=[
            TenantAccess(
                tenant_id="tenant_id_example",
                roles=[
                    "roles_example",
                ],
                clusters=[
                    McmClusterIdentifier(
                        cluster_id=1,
                        cluster_incarnation_id=1,
                        region_id="region_id_example",
                    ),
                ],
            ),
        ],
    ) # IdpPrincipal | Specifies the parameters to update IDP Principal.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update IDP Principal.
	api_response = client.identity_provider.update_idp_principal(sid, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IdentityProviderApi->update_idp_principal: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update IDP Principal.
	api_response = client.identity_provider.update_idp_principal(sid, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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

