# cohesity_sdk.cluster.ActiveDirectoryApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_active_directory_principals**](ActiveDirectoryApi.md#add_active_directory_principals) | **POST** /active-directory-principals | Add multiple groups or users on the Cohesity Cluster for the specified Active Directory principals. In addition, assign Cohesity roles to the users or groups to define their Cohesity privileges.
[**create_active_directory**](ActiveDirectoryApi.md#create_active_directory) | **POST** /active-directories | Create an Active Directory.
[**delete_active_directory**](ActiveDirectoryApi.md#delete_active_directory) | **DELETE** /active-directories/{id} | Delete an Active Directory.
[**get_active_directory**](ActiveDirectoryApi.md#get_active_directory) | **GET** /active-directories | Get the list of Active Directories.
[**get_active_directory_by_id**](ActiveDirectoryApi.md#get_active_directory_by_id) | **GET** /active-directories/{id} | Get an Active Directory by id.
[**get_active_directory_principals**](ActiveDirectoryApi.md#get_active_directory_principals) | **GET** /active-directory-principals | Get the list of user and group principals from the Active Directory that match the specified filter criteria.
[**get_centrify_zones**](ActiveDirectoryApi.md#get_centrify_zones) | **GET** /centrify-zones | Get Centrify Zones.
[**get_domain_controllers**](ActiveDirectoryApi.md#get_domain_controllers) | **GET** /domain-controllers | Get Domain Controllers of specified domains.
[**get_trusted_domains**](ActiveDirectoryApi.md#get_trusted_domains) | **GET** /trusted-domains | Get Trusted Domains.
[**trigger_trusted_domains_discovery**](ActiveDirectoryApi.md#trigger_trusted_domains_discovery) | **PUT** /trusted-domains | Rediscover trusted domains.
[**update_active_directory**](ActiveDirectoryApi.md#update_active_directory) | **PUT** /active-directories/{id} | Update an Active Directory.
[**update_trusted_domains**](ActiveDirectoryApi.md#update_trusted_domains) | **POST** /trusted-domains | Update trusted domains.


# **add_active_directory_principals**
> List[AddedActiveDirectoryPrincipal] add_active_directory_principals(body)

Add multiple groups or users on the Cohesity Cluster for the specified Active Directory principals. In addition, assign Cohesity roles to the users or groups to define their Cohesity privileges.

After a group or user has been added to a Cohesity Cluster, the referenced Active Directory principal can be used by the Cohesity Cluster. In addition, this operation maps Cohesity roles with a group or user and this mapping defines the privileges allowed on the Cohesity Cluster for the group or user. For example if an 'management' group is created on the Cohesity Cluster for the Active Directory 'management' principal group and is associated with the Cohesity 'View' role, all users in the referenced Active Directory 'management' principal group can log in to the Cohesity Dashboard but will only have view-only privileges. These users cannot create new Protection Jobs, Policies, Views, etc. NOTE: Local Cohesity users and groups cannot be created by this operation. Local Cohesity users or groups do not have an associated Active Directory principals and are created directly in the default LOCAL domain.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.add_active_directory_principals_parameters import AddActiveDirectoryPrincipalsParameters
from cohesity_sdk.cluster.models.added_active_directory_principal import AddedActiveDirectoryPrincipal
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ActiveDirectoryApi(api_client)
    body = [cohesity_sdk.cluster.AddActiveDirectoryPrincipalsParameters()] # List[AddActiveDirectoryPrincipalsParameters] | 

    try:
        # Add multiple groups or users on the Cohesity Cluster for the specified Active Directory principals. In addition, assign Cohesity roles to the users or groups to define their Cohesity privileges.
        api_response = api_instance.add_active_directory_principals(body)
        print("The response of ActiveDirectoryApi->add_active_directory_principals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveDirectoryApi->add_active_directory_principals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**List[AddActiveDirectoryPrincipalsParameters]**](AddActiveDirectoryPrincipalsParameters.md)|  | 

### Return type

[**List[AddedActiveDirectoryPrincipal]**](AddedActiveDirectoryPrincipal.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_active_directory**
> ActiveDirectory create_active_directory(body)

Create an Active Directory.

Create an Active Directory.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.active_directory import ActiveDirectory
from cohesity_sdk.cluster.models.create_active_directory_request import CreateActiveDirectoryRequest
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ActiveDirectoryApi(api_client)
    body = cohesity_sdk.cluster.CreateActiveDirectoryRequest() # CreateActiveDirectoryRequest | Specifies the parameters to create an Active Directory.

    try:
        # Create an Active Directory.
        api_response = api_instance.create_active_directory(body)
        print("The response of ActiveDirectoryApi->create_active_directory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveDirectoryApi->create_active_directory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateActiveDirectoryRequest**](CreateActiveDirectoryRequest.md)| Specifies the parameters to create an Active Directory. | 

### Return type

[**ActiveDirectory**](ActiveDirectory.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_active_directory**
> delete_active_directory(id, active_directory_admin_username, active_directory_admin_password, force_remove=force_remove)

Delete an Active Directory.

Delete an Active Directory.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ActiveDirectoryApi(api_client)
    id = 56 # int | Specifies id of an Active Directory.
    active_directory_admin_username = 'active_directory_admin_username_example' # str | Specifies the username of the Active Directory Admin.
    active_directory_admin_password = 'active_directory_admin_password_example' # str | Specifies the password of the Active Directory Admin.
    force_remove = True # bool | To force delete the Active directory from cluster. This will skip all the checks that prevents cluster from leaving an AD domain. (optional)

    try:
        # Delete an Active Directory.
        api_instance.delete_active_directory(id, active_directory_admin_username, active_directory_admin_password, force_remove=force_remove)
    except Exception as e:
        print("Exception when calling ActiveDirectoryApi->delete_active_directory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of an Active Directory. | 
 **active_directory_admin_username** | **str**| Specifies the username of the Active Directory Admin. | 
 **active_directory_admin_password** | **str**| Specifies the password of the Active Directory Admin. | 
 **force_remove** | **bool**| To force delete the Active directory from cluster. This will skip all the checks that prevents cluster from leaving an AD domain. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_directory**
> ActiveDirectories get_active_directory(domain_names=domain_names, ids=ids, tenant_ids=tenant_ids, include_tenants=include_tenants)

Get the list of Active Directories.

Get the list of Active Directories.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.active_directories import ActiveDirectories
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ActiveDirectoryApi(api_client)
    domain_names = ['domain_names_example'] # List[str] | Filter by a list of Active Directory domain names. (optional)
    ids = [56] # List[int] | Filter by a list of Active Directory Ids. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which Active Directories are to be returned. (optional)
    include_tenants = True # bool | If true, the response will include Active Directories which were created by all tenants which the current user has permission to see. If false, then only Active Directories created by the current user will be returned. (optional)

    try:
        # Get the list of Active Directories.
        api_response = api_instance.get_active_directory(domain_names=domain_names, ids=ids, tenant_ids=tenant_ids, include_tenants=include_tenants)
        print("The response of ActiveDirectoryApi->get_active_directory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveDirectoryApi->get_active_directory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_names** | [**List[str]**](str.md)| Filter by a list of Active Directory domain names. | [optional] 
 **ids** | [**List[int]**](int.md)| Filter by a list of Active Directory Ids. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which Active Directories are to be returned. | [optional] 
 **include_tenants** | **bool**| If true, the response will include Active Directories which were created by all tenants which the current user has permission to see. If false, then only Active Directories created by the current user will be returned. | [optional] 

### Return type

[**ActiveDirectories**](ActiveDirectories.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_directory_by_id**
> ActiveDirectory get_active_directory_by_id(id, include_centrify_zones=include_centrify_zones, include_domain_controllers=include_domain_controllers, include_security_principals=include_security_principals, prefix=prefix, object_class=object_class)

Get an Active Directory by id.

Get an Active Directory by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.active_directory import ActiveDirectory
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ActiveDirectoryApi(api_client)
    id = 56 # int | Specifies id of an Active Directory.
    include_centrify_zones = True # bool | Specifies whether to include Centrify Zones of the Active Directory in response. (optional)
    include_domain_controllers = True # bool | Specifies whether to include Domain Controllers of the Active Directory in response. (optional)
    include_security_principals = True # bool | Specifies whether to include Security Principals of the Active Directory in response. (optional)
    prefix = 'prefix_example' # str | Specifies a prefix, only security principals with name or sAMAccountName having this prefix (ignoring cases) will be returned. This field is appliciable and mandatory if 'includeSecurityPrincipals' is set to true. (optional)
    object_class = ['object_class_example'] # List[str] | Specifies a list of object classes, only security principals with object class in this list will be returned. This field is appliciable if 'includeSecurityPrincipals' is set to true. (optional)

    try:
        # Get an Active Directory by id.
        api_response = api_instance.get_active_directory_by_id(id, include_centrify_zones=include_centrify_zones, include_domain_controllers=include_domain_controllers, include_security_principals=include_security_principals, prefix=prefix, object_class=object_class)
        print("The response of ActiveDirectoryApi->get_active_directory_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveDirectoryApi->get_active_directory_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of an Active Directory. | 
 **include_centrify_zones** | **bool**| Specifies whether to include Centrify Zones of the Active Directory in response. | [optional] 
 **include_domain_controllers** | **bool**| Specifies whether to include Domain Controllers of the Active Directory in response. | [optional] 
 **include_security_principals** | **bool**| Specifies whether to include Security Principals of the Active Directory in response. | [optional] 
 **prefix** | **str**| Specifies a prefix, only security principals with name or sAMAccountName having this prefix (ignoring cases) will be returned. This field is appliciable and mandatory if &#39;includeSecurityPrincipals&#39; is set to true. | [optional] 
 **object_class** | [**List[str]**](str.md)| Specifies a list of object classes, only security principals with object class in this list will be returned. This field is appliciable if &#39;includeSecurityPrincipals&#39; is set to true. | [optional] 

### Return type

[**ActiveDirectory**](ActiveDirectory.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_directory_principals**
> ActiveDirectoryPrincipals get_active_directory_principals(domain_name=domain_name, sids=sids, search_term=search_term, include_computers=include_computers, include_service_accounts=include_service_accounts, object_class=object_class)

Get the list of user and group principals from the Active Directory that match the specified filter criteria.

Get the list of user and group principals from the Active Directory that match the specified filter criteria.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.active_directory_principals import ActiveDirectoryPrincipals
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ActiveDirectoryApi(api_client)
    domain_name = 'domain_name_example' # str | Specifies the domain name of the principals to search. If specified the principals in that domain are searched. Domain could be an Active Directory domain joined by the Cluster or any one of the trusted domains of the Active Directory domain or the LOCAL domain. If not specified, all the domains are searched. (optional)
    sids = ['sids_example'] # List[str] | Optionally filter by a list of security identifiers (SIDs) found in the specified domain. Only principals matching the specified SIDs are returned. If specified, a 'searchTerm' parameter should not be specified. Note: Duplicate SIDs will be ignored. (optional)
    search_term = 'search_term_example' # str | Optionally filter by matching a substring. Only principals with a name or sAMAccountName that matches part or all of the specified substring are returned. If specified, a 'sids' parameter should not be specified (optional)
    include_computers = True # bool | Specifies if Computer/GMSA accounts need to be included in this search. (optional)
    include_service_accounts = True # bool | Specifies if service accounts should be included in the search result. (optional)
    object_class = 'object_class_example' # str | Specifies the type of principal, a user or a group. (optional)

    try:
        # Get the list of user and group principals from the Active Directory that match the specified filter criteria.
        api_response = api_instance.get_active_directory_principals(domain_name=domain_name, sids=sids, search_term=search_term, include_computers=include_computers, include_service_accounts=include_service_accounts, object_class=object_class)
        print("The response of ActiveDirectoryApi->get_active_directory_principals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveDirectoryApi->get_active_directory_principals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| Specifies the domain name of the principals to search. If specified the principals in that domain are searched. Domain could be an Active Directory domain joined by the Cluster or any one of the trusted domains of the Active Directory domain or the LOCAL domain. If not specified, all the domains are searched. | [optional] 
 **sids** | [**List[str]**](str.md)| Optionally filter by a list of security identifiers (SIDs) found in the specified domain. Only principals matching the specified SIDs are returned. If specified, a &#39;searchTerm&#39; parameter should not be specified. Note: Duplicate SIDs will be ignored. | [optional] 
 **search_term** | **str**| Optionally filter by matching a substring. Only principals with a name or sAMAccountName that matches part or all of the specified substring are returned. If specified, a &#39;sids&#39; parameter should not be specified | [optional] 
 **include_computers** | **bool**| Specifies if Computer/GMSA accounts need to be included in this search. | [optional] 
 **include_service_accounts** | **bool**| Specifies if service accounts should be included in the search result. | [optional] 
 **object_class** | **str**| Specifies the type of principal, a user or a group. | [optional] 

### Return type

[**ActiveDirectoryPrincipals**](ActiveDirectoryPrincipals.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_centrify_zones**
> CentrifyZones get_centrify_zones(domain_name)

Get Centrify Zones.

Get Centrify zones for a specified domain.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.centrify_zones import CentrifyZones
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ActiveDirectoryApi(api_client)
    domain_name = 'domain_name_example' # str | Specifies the FQDN of the domain name.

    try:
        # Get Centrify Zones.
        api_response = api_instance.get_centrify_zones(domain_name)
        print("The response of ActiveDirectoryApi->get_centrify_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveDirectoryApi->get_centrify_zones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| Specifies the FQDN of the domain name. | 

### Return type

[**CentrifyZones**](CentrifyZones.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_controllers**
> DomainControllersResponse get_domain_controllers(domain_names, connection_id=connection_id)

Get Domain Controllers of specified domains.

Get Domain Controllers of specified domains.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.domain_controllers_response import DomainControllersResponse
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ActiveDirectoryApi(api_client)
    domain_names = ['domain_names_example'] # List[str] | Specifies a list of domain names.
    connection_id = 56 # int | Specifies the Id of the connection which the connector belongs to. (optional)

    try:
        # Get Domain Controllers of specified domains.
        api_response = api_instance.get_domain_controllers(domain_names, connection_id=connection_id)
        print("The response of ActiveDirectoryApi->get_domain_controllers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveDirectoryApi->get_domain_controllers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_names** | [**List[str]**](str.md)| Specifies a list of domain names. | 
 **connection_id** | **int**| Specifies the Id of the connection which the connector belongs to. | [optional] 

### Return type

[**DomainControllersResponse**](DomainControllersResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trusted_domains**
> TrustedDomainParams get_trusted_domains(domain_name)

Get Trusted Domains.

Get Trusted Domains for a specified domain.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.trusted_domain_params import TrustedDomainParams
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ActiveDirectoryApi(api_client)
    domain_name = 'domain_name_example' # str | Specifies the FQDN of an Active directory domain.

    try:
        # Get Trusted Domains.
        api_response = api_instance.get_trusted_domains(domain_name)
        print("The response of ActiveDirectoryApi->get_trusted_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveDirectoryApi->get_trusted_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| Specifies the FQDN of an Active directory domain. | 

### Return type

[**TrustedDomainParams**](TrustedDomainParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_trusted_domains_discovery**
> trigger_trusted_domains_discovery(domain_name, rediscover)

Rediscover trusted domains.

Re-trigger the trusted domains of an Active Directory.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ActiveDirectoryApi(api_client)
    domain_name = 'domain_name_example' # str | Specifies the FQDN of an Active directory domain.
    rediscover = True # bool | Specifies if trusted domains should be rediscovered.

    try:
        # Rediscover trusted domains.
        api_instance.trigger_trusted_domains_discovery(domain_name, rediscover)
    except Exception as e:
        print("Exception when calling ActiveDirectoryApi->trigger_trusted_domains_discovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| Specifies the FQDN of an Active directory domain. | 
 **rediscover** | **bool**| Specifies if trusted domains should be rediscovered. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request Accepted |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_active_directory**
> ActiveDirectory update_active_directory(id, body)

Update an Active Directory.

Update an Active Directory.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.active_directory import ActiveDirectory
from cohesity_sdk.cluster.models.update_active_directory_request import UpdateActiveDirectoryRequest
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ActiveDirectoryApi(api_client)
    id = 56 # int | Specifies id of an Active Directory.
    body = cohesity_sdk.cluster.UpdateActiveDirectoryRequest() # UpdateActiveDirectoryRequest | Request to update an Active Directory.

    try:
        # Update an Active Directory.
        api_response = api_instance.update_active_directory(id, body)
        print("The response of ActiveDirectoryApi->update_active_directory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveDirectoryApi->update_active_directory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of an Active Directory. | 
 **body** | [**UpdateActiveDirectoryRequest**](UpdateActiveDirectoryRequest.md)| Request to update an Active Directory. | 

### Return type

[**ActiveDirectory**](ActiveDirectory.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_trusted_domains**
> TrustedDomainParams update_trusted_domains(domain_name, body)

Update trusted domains.

To update trusted domains of an Active Directory.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.trusted_domain_params import TrustedDomainParams
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ActiveDirectoryApi(api_client)
    domain_name = 'domain_name_example' # str | Specifies the FQDN of an Active directory domain.
    body = cohesity_sdk.cluster.TrustedDomainParams() # TrustedDomainParams | Specifies the trusted domains params.

    try:
        # Update trusted domains.
        api_response = api_instance.update_trusted_domains(domain_name, body)
        print("The response of ActiveDirectoryApi->update_trusted_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveDirectoryApi->update_trusted_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| Specifies the FQDN of an Active directory domain. | 
 **body** | [**TrustedDomainParams**](TrustedDomainParams.md)| Specifies the trusted domains params. | 

### Return type

[**TrustedDomainParams**](TrustedDomainParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

