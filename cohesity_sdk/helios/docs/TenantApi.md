# cohesity_sdk.helios.TenantApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_cluster_to_tenant**](TenantApi.md#assign_cluster_to_tenant) | **POST** /mcm/tenants/{id}/clusters | Assign a Cluster to a tenant.
[**assign_properties_to_tenant**](TenantApi.md#assign_properties_to_tenant) | **PUT** /tenants/{id}/assignments | Update assginment of properties for a tenant.
[**confirm_tenant**](TenantApi.md#confirm_tenant) | **POST** /mcm/tenants/{id}/manage | Enable Helios Management for Tenant.
[**create_helios_tenant**](TenantApi.md#create_helios_tenant) | **POST** /mcm/tenants | Create a new Tenant on Helios.
[**create_tenant**](TenantApi.md#create_tenant) | **POST** /tenants | Create a new Tenant.
[**delete_helios_tenant**](TenantApi.md#delete_helios_tenant) | **DELETE** /mcm/tenants/{id} | Delete a Tenant on Helios.
[**delete_tenant**](TenantApi.md#delete_tenant) | **DELETE** /tenants/{id} | Delete Tenant with given ID.
[**get_account_tenant_config**](TenantApi.md#get_account_tenant_config) | **GET** /mcm/accounts/tenant-config | Get Tenants Config.
[**get_assigned_properties_for_tenant**](TenantApi.md#get_assigned_properties_for_tenant) | **GET** /tenants/{id}/assignments | Get tenant assignments.
[**get_clusters_tenant_config**](TenantApi.md#get_clusters_tenant_config) | **GET** /mcm/clusters/tenant-config | Get Tenant&#39;s config for all clusters.
[**get_helios_tenants**](TenantApi.md#get_helios_tenants) | **GET** /mcm/tenants | Get a list of tenants.
[**get_on_prem_tenant_config**](TenantApi.md#get_on_prem_tenant_config) | **GET** /clusters/tenant-config | Get Tenants Config.
[**get_tenant_by_id**](TenantApi.md#get_tenant_by_id) | **GET** /tenants/{id} | Get Tenant by ID.
[**get_tenant_stats**](TenantApi.md#get_tenant_stats) | **GET** /mcm/tenants/stats | Get Tenant Statistics.
[**get_tenant_swift**](TenantApi.md#get_tenant_swift) | **GET** /tenants/swift | Get a Swift configuration.
[**helios_assign_properties_to_tenant**](TenantApi.md#helios_assign_properties_to_tenant) | **PUT** /mcm/tenants/{id}/assignments | Assign properties to a tenant.
[**list_tenants**](TenantApi.md#list_tenants) | **GET** /tenants | Get a list of Tenants.
[**perform_helios_tenant_action**](TenantApi.md#perform_helios_tenant_action) | **POST** /mcm/tenants/{id}/actions | Perform actions on a Helios Tenant.
[**perform_tenant_action**](TenantApi.md#perform_tenant_action) | **POST** /tenants/{id}/actions | Perform actions on a Tenant.
[**register_swift**](TenantApi.md#register_swift) | **POST** /tenants/swift/register | Register Swift service on a Keystone server.
[**unregister_swift**](TenantApi.md#unregister_swift) | **POST** /tenants/swift/unregister | Unregister Swift service from a Keystone server.
[**update_account_tenant_config**](TenantApi.md#update_account_tenant_config) | **PATCH** /mcm/accounts/tenant-config | Update Tenant&#39;s Config.
[**update_clusters_tenant_config**](TenantApi.md#update_clusters_tenant_config) | **POST** /mcm/clusters/tenant-config | Update Tenant&#39;s config for clusters.
[**update_helios_tenant**](TenantApi.md#update_helios_tenant) | **PATCH** /mcm/tenants/{id} | Update Tenant properties on Helios.
[**update_on_prem_tenant_config**](TenantApi.md#update_on_prem_tenant_config) | **POST** /clusters/tenant-config | Update Tenants Config.
[**update_tenant**](TenantApi.md#update_tenant) | **PUT** /tenants/{id} | Update Tenant.
[**update_tenant_swift**](TenantApi.md#update_tenant_swift) | **PUT** /tenants/swift | Update a Swift configuration.


# **assign_cluster_to_tenant**
> HeliosTenant assign_cluster_to_tenant(id, body, region_id=region_id)

Assign a Cluster to a tenant.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.assign_cluster_to_tenant_params_body import AssignClusterToTenantParamsBody
from cohesity_sdk.helios.models.helios_tenant import HeliosTenant
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    id = 'id_example' # str | 
    body = cohesity_sdk.helios.AssignClusterToTenantParamsBody() # AssignClusterToTenantParamsBody | 
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Assign a Cluster to a tenant.
        api_response = api_instance.assign_cluster_to_tenant(id, body, region_id=region_id)
        print("The response of TenantApi->assign_cluster_to_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->assign_cluster_to_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**AssignClusterToTenantParamsBody**](AssignClusterToTenantParamsBody.md)|  | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**HeliosTenant**](HeliosTenant.md)

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

# **assign_properties_to_tenant**
> TenantAssignments assign_properties_to_tenant(id, body, access_cluster_id=access_cluster_id, region_id=region_id)

Update assginment of properties for a tenant.

Assign/Unassign properties like storage domain, entities, policies etc. to the tenant. The API expects a list of all the assignments (policies etc.) that are supposed to be associated to the Tenant. The list of assignments passed get assigned to the Tenant and anything else that was already assigned gets unassigned. In case a few objects fail the assignment and some objects get assigned, error is returned for all assignments except for policies.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.tenant_assignments import TenantAssignments
from cohesity_sdk.helios.models.tenant_assignments_params import TenantAssignmentsParams
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    id = 'id_example' # str | The Tenant id.
    body = cohesity_sdk.helios.TenantAssignmentsParams() # TenantAssignmentsParams | 
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update assginment of properties for a tenant.
        api_response = api_instance.assign_properties_to_tenant(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of TenantApi->assign_properties_to_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->assign_properties_to_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Tenant id. | 
 **body** | [**TenantAssignmentsParams**](TenantAssignmentsParams.md)|  | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**TenantAssignments**](TenantAssignments.md)

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

# **confirm_tenant**
> HeliosTenant confirm_tenant(id, body, region_id=region_id)

Enable Helios Management for Tenant.

For a specific, TenantId enable it to be managed by Helios.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.confirm_tenant_params_body import ConfirmTenantParamsBody
from cohesity_sdk.helios.models.helios_tenant import HeliosTenant
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    id = 'id_example' # str | 
    body = cohesity_sdk.helios.ConfirmTenantParamsBody() # ConfirmTenantParamsBody | 
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Enable Helios Management for Tenant.
        api_response = api_instance.confirm_tenant(id, body, region_id=region_id)
        print("The response of TenantApi->confirm_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->confirm_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ConfirmTenantParamsBody**](ConfirmTenantParamsBody.md)|  | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**HeliosTenant**](HeliosTenant.md)

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

# **create_helios_tenant**
> HeliosTenant create_helios_tenant(body, region_id=region_id)

Create a new Tenant on Helios.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.create_tenant_params import CreateTenantParams
from cohesity_sdk.helios.models.helios_tenant import HeliosTenant
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    body = cohesity_sdk.helios.CreateTenantParams() # CreateTenantParams | 
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Create a new Tenant on Helios.
        api_response = api_instance.create_helios_tenant(body, region_id=region_id)
        print("The response of TenantApi->create_helios_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->create_helios_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTenantParams**](CreateTenantParams.md)|  | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**HeliosTenant**](HeliosTenant.md)

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

# **create_tenant**
> TenantInfo create_tenant(body, access_cluster_id=access_cluster_id, region_id=region_id)

Create a new Tenant.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.create_tenant_request import CreateTenantRequest
from cohesity_sdk.helios.models.tenant_info import TenantInfo
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    body = cohesity_sdk.helios.CreateTenantRequest() # CreateTenantRequest | 
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Create a new Tenant.
        api_response = api_instance.create_tenant(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of TenantApi->create_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->create_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTenantRequest**](CreateTenantRequest.md)|  | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**TenantInfo**](TenantInfo.md)

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

# **delete_helios_tenant**
> delete_helios_tenant(id, region_id=region_id, delete_cluster_tenants=delete_cluster_tenants)

Delete a Tenant on Helios.

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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    id = 'id_example' # str | 
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    delete_cluster_tenants = True # bool | Whether or not to delete the tenants on the cluster, default is true. (optional) (default to True)

    try:
        # Delete a Tenant on Helios.
        api_instance.delete_helios_tenant(id, region_id=region_id, delete_cluster_tenants=delete_cluster_tenants)
    except Exception as e:
        print("Exception when calling TenantApi->delete_helios_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **delete_cluster_tenants** | **bool**| Whether or not to delete the tenants on the cluster, default is true. | [optional] [default to True]

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

# **delete_tenant**
> delete_tenant(id, access_cluster_id=access_cluster_id, region_id=region_id)

Delete Tenant with given ID.

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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    id = 'id_example' # str | The Tenant id.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Delete Tenant with given ID.
        api_instance.delete_tenant(id, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
        print("Exception when calling TenantApi->delete_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Tenant id. | 
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

# **get_account_tenant_config**
> TenantConfig get_account_tenant_config(region_id=region_id)

Get Tenants Config.

Get Tenant related configurations for the account.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.tenant_config import TenantConfig
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get Tenants Config.
        api_response = api_instance.get_account_tenant_config(region_id=region_id)
        print("The response of TenantApi->get_account_tenant_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_account_tenant_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**TenantConfig**](TenantConfig.md)

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

# **get_assigned_properties_for_tenant**
> TenantAssignmentProperties get_assigned_properties_for_tenant(id, access_cluster_id=access_cluster_id, region_id=region_id)

Get tenant assignments.

Get all assigned properties like storage domain, entities, policies, objects, views etc for a given tenant.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.tenant_assignment_properties import TenantAssignmentProperties
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    id = 'id_example' # str | The Tenant id.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get tenant assignments.
        api_response = api_instance.get_assigned_properties_for_tenant(id, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of TenantApi->get_assigned_properties_for_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_assigned_properties_for_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Tenant id. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**TenantAssignmentProperties**](TenantAssignmentProperties.md)

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

# **get_clusters_tenant_config**
> ClustersTenantConfigs get_clusters_tenant_config(region_id=region_id)

Get Tenant's config for all clusters.

Get Tenant related configurations for all the clusters.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.clusters_tenant_configs import ClustersTenantConfigs
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get Tenant's config for all clusters.
        api_response = api_instance.get_clusters_tenant_config(region_id=region_id)
        print("The response of TenantApi->get_clusters_tenant_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_clusters_tenant_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**ClustersTenantConfigs**](ClustersTenantConfigs.md)

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

# **get_helios_tenants**
> ListTenantData get_helios_tenants(region_id=region_id, cluster_identifiers=cluster_identifiers, tenant_ids=tenant_ids, statuses=statuses, managed_on_helios=managed_on_helios, include_deleted_systems=include_deleted_systems)

Get a list of tenants.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.list_tenant_data import ListTenantData
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    cluster_identifiers = ['cluster_identifiers_example'] # List[str] | Specifies the list of cluster identifiers. The format is clusterId:clusterIncarnationId. (optional)
    tenant_ids = ['tenant_ids_example'] # List[Optional[str]] | List of Tenant Ids to filter from. (optional)
    statuses = ['statuses_example'] # List[Optional[str]] | Status of the tenant on Helios. Active and Inactive tenants are returned if this field is not specified. Also, if specified, only helios managed tenants are returned. (optional)
    managed_on_helios = True # bool | Whether managed on helios or not. (optional)
    include_deleted_systems = True # bool | Whether tenants deleted on clusters should be included. (optional)

    try:
        # Get a list of tenants.
        api_response = api_instance.get_helios_tenants(region_id=region_id, cluster_identifiers=cluster_identifiers, tenant_ids=tenant_ids, statuses=statuses, managed_on_helios=managed_on_helios, include_deleted_systems=include_deleted_systems)
        print("The response of TenantApi->get_helios_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_helios_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **cluster_identifiers** | [**List[str]**](str.md)| Specifies the list of cluster identifiers. The format is clusterId:clusterIncarnationId. | [optional] 
 **tenant_ids** | [**List[Optional[str]]**](str.md)| List of Tenant Ids to filter from. | [optional] 
 **statuses** | [**List[Optional[str]]**](str.md)| Status of the tenant on Helios. Active and Inactive tenants are returned if this field is not specified. Also, if specified, only helios managed tenants are returned. | [optional] 
 **managed_on_helios** | **bool**| Whether managed on helios or not. | [optional] 
 **include_deleted_systems** | **bool**| Whether tenants deleted on clusters should be included. | [optional] 

### Return type

[**ListTenantData**](ListTenantData.md)

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

# **get_on_prem_tenant_config**
> OnPremTenantConfig get_on_prem_tenant_config(access_cluster_id=access_cluster_id, region_id=region_id)

Get Tenants Config.

Get Tenant related configurations for the cluster.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.on_prem_tenant_config import OnPremTenantConfig
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get Tenants Config.
        api_response = api_instance.get_on_prem_tenant_config(access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of TenantApi->get_on_prem_tenant_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_on_prem_tenant_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**OnPremTenantConfig**](OnPremTenantConfig.md)

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

# **get_tenant_by_id**
> TenantInfo get_tenant_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)

Get Tenant by ID.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.tenant_info import TenantInfo
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    id = 'id_example' # str | The Tenant id.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get Tenant by ID.
        api_response = api_instance.get_tenant_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of TenantApi->get_tenant_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_tenant_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Tenant id. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**TenantInfo**](TenantInfo.md)

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

# **get_tenant_stats**
> List[HeliosTenantResources] get_tenant_stats(region_id=region_id, tenant_ids=tenant_ids, include_deleted=include_deleted)

Get Tenant Statistics.

Get Statistics on Sources and Storage Domains assigned to the Tenants belonging to an account.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.helios_tenant_resources import HeliosTenantResources
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | List of Tenant Ids to filter from. (optional)
    include_deleted = False # bool | If deleted tenants stats need to be included. (optional) (default to False)

    try:
        # Get Tenant Statistics.
        api_response = api_instance.get_tenant_stats(region_id=region_id, tenant_ids=tenant_ids, include_deleted=include_deleted)
        print("The response of TenantApi->get_tenant_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_tenant_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| List of Tenant Ids to filter from. | [optional] 
 **include_deleted** | **bool**| If deleted tenants stats need to be included. | [optional] [default to False]

### Return type

[**List[HeliosTenantResources]**](HeliosTenantResources.md)

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

# **get_tenant_swift**
> SwiftParams get_tenant_swift(access_cluster_id=access_cluster_id, region_id=region_id, tenant_id=tenant_id)

Get a Swift configuration.

Get a Swift configuration.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.swift_params import SwiftParams
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    tenant_id = 'tenant_id_example' # str | Specifies the tenant Id. (optional)

    try:
        # Get a Swift configuration.
        api_response = api_instance.get_tenant_swift(access_cluster_id=access_cluster_id, region_id=region_id, tenant_id=tenant_id)
        print("The response of TenantApi->get_tenant_swift:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_tenant_swift: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **tenant_id** | **str**| Specifies the tenant Id. | [optional] 

### Return type

[**SwiftParams**](SwiftParams.md)

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

# **helios_assign_properties_to_tenant**
> HeliosTenantAssignmentsResult helios_assign_properties_to_tenant(id, body, region_id=region_id)

Assign properties to a tenant.

Assign properties like policies etc. to a tenant on a given cluster. The API expects a list of all the assignments (policies etc.) that are supposed to be associated to the Tenant. The list of assignments passed get assigned to the Tenant and anything else that was already assigned gets unassigned.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.helios_tenant_assignments_params import HeliosTenantAssignmentsParams
from cohesity_sdk.helios.models.helios_tenant_assignments_result import HeliosTenantAssignmentsResult
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    id = 'id_example' # str | The Tenant id.
    body = cohesity_sdk.helios.HeliosTenantAssignmentsParams() # HeliosTenantAssignmentsParams | 
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Assign properties to a tenant.
        api_response = api_instance.helios_assign_properties_to_tenant(id, body, region_id=region_id)
        print("The response of TenantApi->helios_assign_properties_to_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->helios_assign_properties_to_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Tenant id. | 
 **body** | [**HeliosTenantAssignmentsParams**](HeliosTenantAssignmentsParams.md)|  | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**HeliosTenantAssignmentsResult**](HeliosTenantAssignmentsResult.md)

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

# **list_tenants**
> List[TenantInfo] list_tenants(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, statuses=statuses)

Get a list of Tenants.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.tenant_info import TenantInfo
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    ids = ['ids_example'] # List[Optional[str]] | List of tenantIds to filter. (optional)
    statuses = ['statuses_example'] # List[Optional[str]] | Filter by current status of tenant. If left blank, only active and inactive tenants are returned. (optional)

    try:
        # Get a list of Tenants.
        api_response = api_instance.list_tenants(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, statuses=statuses)
        print("The response of TenantApi->list_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->list_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **ids** | [**List[Optional[str]]**](str.md)| List of tenantIds to filter. | [optional] 
 **statuses** | [**List[Optional[str]]**](str.md)| Filter by current status of tenant. If left blank, only active and inactive tenants are returned. | [optional] 

### Return type

[**List[TenantInfo]**](TenantInfo.md)

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

# **perform_helios_tenant_action**
> HeliosTenant perform_helios_tenant_action(id, body, region_id=region_id)

Perform actions on a Helios Tenant.

Perform actions like activate and deactivate on a given Tenant on Helios.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.helios_tenant import HeliosTenant
from cohesity_sdk.helios.models.tenant_action_body import TenantActionBody
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    id = 'id_example' # str | The Tenant id.
    body = cohesity_sdk.helios.TenantActionBody() # TenantActionBody | Specifies the parameters to perform an action on a Tenant.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Perform actions on a Helios Tenant.
        api_response = api_instance.perform_helios_tenant_action(id, body, region_id=region_id)
        print("The response of TenantApi->perform_helios_tenant_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->perform_helios_tenant_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Tenant id. | 
 **body** | [**TenantActionBody**](TenantActionBody.md)| Specifies the parameters to perform an action on a Tenant. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**HeliosTenant**](HeliosTenant.md)

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

# **perform_tenant_action**
> TenantInfo perform_tenant_action(id, body, access_cluster_id=access_cluster_id, region_id=region_id)

Perform actions on a Tenant.

Perform actions like activate and deactivate on a given Tenant.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.tenant_action_body import TenantActionBody
from cohesity_sdk.helios.models.tenant_info import TenantInfo
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    id = 'id_example' # str | The Tenant id.
    body = cohesity_sdk.helios.TenantActionBody() # TenantActionBody | Specifies the parameters to perform an action on a Tenant.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Perform actions on a Tenant.
        api_response = api_instance.perform_tenant_action(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of TenantApi->perform_tenant_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->perform_tenant_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Tenant id. | 
 **body** | [**TenantActionBody**](TenantActionBody.md)| Specifies the parameters to perform an action on a Tenant. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**TenantInfo**](TenantInfo.md)

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

# **register_swift**
> register_swift(body, access_cluster_id=access_cluster_id, region_id=region_id)

Register Swift service on a Keystone server.

Register Swift service on Keystone server.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.register_swift_params import RegisterSwiftParams
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    body = cohesity_sdk.helios.RegisterSwiftParams() # RegisterSwiftParams | Specifies the parameters to register a Swift service on Keystone server.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Register Swift service on a Keystone server.
        api_instance.register_swift(body, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
        print("Exception when calling TenantApi->register_swift: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterSwiftParams**](RegisterSwiftParams.md)| Specifies the parameters to register a Swift service on Keystone server. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_swift**
> unregister_swift(body, access_cluster_id=access_cluster_id, region_id=region_id)

Unregister Swift service from a Keystone server.

Unregister Swift service from Keystone server.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.unregister_swift_params import UnregisterSwiftParams
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    body = cohesity_sdk.helios.UnregisterSwiftParams() # UnregisterSwiftParams | Specifies the parameters to unregister a Swift service from Keystone server.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Unregister Swift service from a Keystone server.
        api_instance.unregister_swift(body, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
        print("Exception when calling TenantApi->unregister_swift: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnregisterSwiftParams**](UnregisterSwiftParams.md)| Specifies the parameters to unregister a Swift service from Keystone server. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_tenant_config**
> TenantConfig update_account_tenant_config(body, region_id=region_id)

Update Tenant's Config.

Update Tenant related configurations for the account.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.tenant_config import TenantConfig
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    body = cohesity_sdk.helios.TenantConfig() # TenantConfig | 
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update Tenant's Config.
        api_response = api_instance.update_account_tenant_config(body, region_id=region_id)
        print("The response of TenantApi->update_account_tenant_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->update_account_tenant_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TenantConfig**](TenantConfig.md)|  | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**TenantConfig**](TenantConfig.md)

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

# **update_clusters_tenant_config**
> UpdateClustersTenantConfigsResponse update_clusters_tenant_config(body, region_id=region_id)

Update Tenant's config for clusters.

Update Tenant related configurations for a list of clusters.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.clusters_tenant_configs import ClustersTenantConfigs
from cohesity_sdk.helios.models.update_clusters_tenant_configs_response import UpdateClustersTenantConfigsResponse
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    body = cohesity_sdk.helios.ClustersTenantConfigs() # ClustersTenantConfigs | 
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update Tenant's config for clusters.
        api_response = api_instance.update_clusters_tenant_config(body, region_id=region_id)
        print("The response of TenantApi->update_clusters_tenant_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->update_clusters_tenant_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClustersTenantConfigs**](ClustersTenantConfigs.md)|  | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**UpdateClustersTenantConfigsResponse**](UpdateClustersTenantConfigsResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_helios_tenant**
> HeliosTenant update_helios_tenant(id, body, region_id=region_id)

Update Tenant properties on Helios.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.helios_tenant import HeliosTenant
from cohesity_sdk.helios.models.update_helios_tenant_body import UpdateHeliosTenantBody
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    id = 'id_example' # str | 
    body = cohesity_sdk.helios.UpdateHeliosTenantBody() # UpdateHeliosTenantBody | 
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update Tenant properties on Helios.
        api_response = api_instance.update_helios_tenant(id, body, region_id=region_id)
        print("The response of TenantApi->update_helios_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->update_helios_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**UpdateHeliosTenantBody**](UpdateHeliosTenantBody.md)|  | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**HeliosTenant**](HeliosTenant.md)

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

# **update_on_prem_tenant_config**
> OnPremTenantConfig update_on_prem_tenant_config(body, access_cluster_id=access_cluster_id, region_id=region_id)

Update Tenants Config.

Update Tenant related configurations for the cluster.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.on_prem_tenant_config import OnPremTenantConfig
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    body = cohesity_sdk.helios.OnPremTenantConfig() # OnPremTenantConfig | 
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update Tenants Config.
        api_response = api_instance.update_on_prem_tenant_config(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of TenantApi->update_on_prem_tenant_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->update_on_prem_tenant_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OnPremTenantConfig**](OnPremTenantConfig.md)|  | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**OnPremTenantConfig**](OnPremTenantConfig.md)

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

# **update_tenant**
> TenantInfo update_tenant(id, body, access_cluster_id=access_cluster_id, region_id=region_id)

Update Tenant.

Update Tenant's properties.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.tenant_info import TenantInfo
from cohesity_sdk.helios.models.update_tenant_body import UpdateTenantBody
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    id = 'id_example' # str | 
    body = cohesity_sdk.helios.UpdateTenantBody() # UpdateTenantBody | 
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update Tenant.
        api_response = api_instance.update_tenant(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of TenantApi->update_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->update_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**UpdateTenantBody**](UpdateTenantBody.md)|  | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**TenantInfo**](TenantInfo.md)

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

# **update_tenant_swift**
> SwiftParams update_tenant_swift(body, access_cluster_id=access_cluster_id, region_id=region_id)

Update a Swift configuration.

Update a Swift configuration.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.swift_params import SwiftParams
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
    api_instance = cohesity_sdk.helios.TenantApi(api_client)
    body = cohesity_sdk.helios.SwiftParams() # SwiftParams | Specifies the parameters to update a Swift configuration.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update a Swift configuration.
        api_response = api_instance.update_tenant_swift(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of TenantApi->update_tenant_swift:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->update_tenant_swift: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SwiftParams**](SwiftParams.md)| Specifies the parameters to update a Swift configuration. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**SwiftParams**](SwiftParams.md)

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

