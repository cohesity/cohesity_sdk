# cohesity_sdk.HeliosIdentityProvidersApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_idp**](HeliosIdentityProvidersApi.md#authenticate_idp) | **POST** /mcm/idp/authenticate | Create an Identity Provider Configuration.
[**create_idp**](HeliosIdentityProvidersApi.md#create_idp) | **POST** /mcm/idps | Create an Identity Provider Configuration.
[**create_idp_principal**](HeliosIdentityProvidersApi.md#create_idp_principal) | **POST** /mcm/idps/principals | Create an Identity Provider Configuration.
[**delete_idp**](HeliosIdentityProvidersApi.md#delete_idp) | **DELETE** /mcm/idps/{id} | Delete a IDP configuration.
[**delete_idp_principal**](HeliosIdentityProvidersApi.md#delete_idp_principal) | **DELETE** /mcm/idps/principals/{sid} | Delete an IDP Principal.
[**get_idp_by_id**](HeliosIdentityProvidersApi.md#get_idp_by_id) | **GET** /mcm/idps/{id} | List details about single Identity Provider configuration.
[**get_idp_principal_by_sid**](HeliosIdentityProvidersApi.md#get_idp_principal_by_sid) | **GET** /mcm/idps/principals/{sid} | Get IDP Principal by SID
[**get_idps**](HeliosIdentityProvidersApi.md#get_idps) | **GET** /mcm/idps | Get the list of IDP configurations.
[**list_idp_principals**](HeliosIdentityProvidersApi.md#list_idp_principals) | **GET** /mcm/idps/principals | List IDP Principals
[**update_idp**](HeliosIdentityProvidersApi.md#update_idp) | **PUT** /mcm/idps/{id} | Update IDP Configuration.
[**update_idp_principal**](HeliosIdentityProvidersApi.md#update_idp_principal) | **PUT** /mcm/idps/principals/{sid} | Update IDP Principal.


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
	api_response = client.helios_identity_providers.authenticate_idp(saml_response)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->authenticate_idp: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create an Identity Provider Configuration.
	api_response = client.helios_identity_providers.authenticate_idp(saml_response, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->authenticate_idp: %s\n" % e)
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
	api_response = client.helios_identity_providers.create_idp(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->create_idp: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create an Identity Provider Configuration.
	api_response = client.helios_identity_providers.create_idp(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->create_idp: %s\n" % e)
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
	api_response = client.helios_identity_providers.create_idp_principal(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->create_idp_principal: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create an Identity Provider Configuration.
	api_response = client.helios_identity_providers.create_idp_principal(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->create_idp_principal: %s\n" % e)
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
	client.helios_identity_providers.delete_idp(id)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->delete_idp: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete a IDP configuration.
	client.helios_identity_providers.delete_idp(id, region_id=region_id)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->delete_idp: %s\n" % e)
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
	client.helios_identity_providers.delete_idp_principal(sid)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->delete_idp_principal: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete an IDP Principal.
	client.helios_identity_providers.delete_idp_principal(sid, region_id=region_id)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->delete_idp_principal: %s\n" % e)
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
	api_response = client.helios_identity_providers.get_idp_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->get_idp_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List details about single Identity Provider configuration.
	api_response = client.helios_identity_providers.get_idp_by_id(id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->get_idp_by_id: %s\n" % e)
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
	api_response = client.helios_identity_providers.get_idp_principal_by_sid(sid)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->get_idp_principal_by_sid: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get IDP Principal by SID
	api_response = client.helios_identity_providers.get_idp_principal_by_sid(sid, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->get_idp_principal_by_sid: %s\n" % e)
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
	api_response = client.helios_identity_providers.get_idps(region_id=region_id, ids=ids, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->get_idps: %s\n" % e)
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
	api_response = client.helios_identity_providers.list_idp_principals(region_id=region_id, include_tenants=include_tenants, sids=sids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->list_idp_principals: %s\n" % e)
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
	api_response = client.helios_identity_providers.update_idp(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->update_idp: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update IDP Configuration.
	api_response = client.helios_identity_providers.update_idp(id, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->update_idp: %s\n" % e)
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
	api_response = client.helios_identity_providers.update_idp_principal(sid, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->update_idp_principal: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update IDP Principal.
	api_response = client.helios_identity_providers.update_idp_principal(sid, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosIdentityProvidersApi->update_idp_principal: %s\n" % e)
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

