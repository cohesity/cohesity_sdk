# cohesity_sdk.helios.RoleApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](RoleApi.md#create_role) | **POST** /roles | Create a Role.
[**delete_role**](RoleApi.md#delete_role) | **DELETE** /roles/{name} | Delete a Role.
[**get_roles**](RoleApi.md#get_roles) | **GET** /roles | Get Roles.
[**update_role**](RoleApi.md#update_role) | **PUT** /roles/{name} | Update a Role.


# **create_role**
> Role create_role(body, access_cluster_id=access_cluster_id, region_id=region_id)

Create a Role.

Create a Role.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.create_role_parameters import CreateRoleParameters
from cohesity_sdk.helios.models.role import Role
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
    api_instance = cohesity_sdk.helios.RoleApi(api_client)
    body = cohesity_sdk.helios.CreateRoleParameters() # CreateRoleParameters | Specifies the request body to create a Role.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Create a Role.
        api_response = api_instance.create_role(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of RoleApi->create_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->create_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRoleParameters**](CreateRoleParameters.md)| Specifies the request body to create a Role. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**Role**](Role.md)

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

# **delete_role**
> delete_role(name, access_cluster_id=access_cluster_id, region_id=region_id)

Delete a Role.

Delete a Role.

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
    api_instance = cohesity_sdk.helios.RoleApi(api_client)
    name = 'name_example' # str | Specifies the name of Role to delete.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Delete a Role.
        api_instance.delete_role(name, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
        print("Exception when calling RoleApi->delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the name of Role to delete. | 
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

# **get_roles**
> Roles get_roles(access_cluster_id=access_cluster_id, region_id=region_id, names=names, tenant_ids=tenant_ids, include_tenants=include_tenants)

Get Roles.

Get Roles.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.roles import Roles
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
    api_instance = cohesity_sdk.helios.RoleApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    names = ['names_example'] # List[str] | Specifies a list of Role names. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which Roles are to be returned. (optional)
    include_tenants = True # bool | If true, the response will include Roles which were created by all tenants which the current user has permission to see. If false, then only Roles created by the current user will be returned. (optional)

    try:
        # Get Roles.
        api_response = api_instance.get_roles(access_cluster_id=access_cluster_id, region_id=region_id, names=names, tenant_ids=tenant_ids, include_tenants=include_tenants)
        print("The response of RoleApi->get_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->get_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **names** | [**List[str]**](str.md)| Specifies a list of Role names. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which Roles are to be returned. | [optional] 
 **include_tenants** | **bool**| If true, the response will include Roles which were created by all tenants which the current user has permission to see. If false, then only Roles created by the current user will be returned. | [optional] 

### Return type

[**Roles**](Roles.md)

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

# **update_role**
> Role update_role(name, body, access_cluster_id=access_cluster_id, region_id=region_id)

Update a Role.

Update a Role.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.role import Role
from cohesity_sdk.helios.models.update_role_parameters import UpdateRoleParameters
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
    api_instance = cohesity_sdk.helios.RoleApi(api_client)
    name = 'name_example' # str | Specifies the name of Role to update.
    body = cohesity_sdk.helios.UpdateRoleParameters() # UpdateRoleParameters | Specifies the request body to update a Role.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update a Role.
        api_response = api_instance.update_role(name, body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of RoleApi->update_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->update_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the name of Role to update. | 
 **body** | [**UpdateRoleParameters**](UpdateRoleParameters.md)| Specifies the request body to update a Role. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**Role**](Role.md)

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

