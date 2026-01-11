# cohesity_sdk.cluster.TenantApi

All URIs are relative to *http://localhost/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_properties_to_tenant**](TenantApi.md#assign_properties_to_tenant) | **PUT** /tenants/{id}/assignments | Update assginment of properties for a tenant.
[**create_tenant**](TenantApi.md#create_tenant) | **POST** /tenants | Create a new Tenant.
[**delete_tenant**](TenantApi.md#delete_tenant) | **DELETE** /tenants/{id} | Delete Tenant with given ID.
[**get_assigned_properties_for_tenant**](TenantApi.md#get_assigned_properties_for_tenant) | **GET** /tenants/{id}/assignments | Get tenant assignments.
[**get_on_prem_tenant_config**](TenantApi.md#get_on_prem_tenant_config) | **GET** /clusters/tenant-config | Get Tenants Config.
[**get_tenant_swift**](TenantApi.md#get_tenant_swift) | **GET** /tenants/swift | Get a Swift configuration.
[**list_tenants**](TenantApi.md#list_tenants) | **GET** /tenants | Get a list of Tenants.
[**perform_tenant_action**](TenantApi.md#perform_tenant_action) | **POST** /tenants/{id}/actions | Perform actions on a Tenant.
[**register_swift**](TenantApi.md#register_swift) | **POST** /tenants/swift/register | Register Swift service on a Keystone server.
[**unregister_swift**](TenantApi.md#unregister_swift) | **POST** /tenants/swift/unregister | Unregister Swift service from a Keystone server.
[**update_on_prem_tenant_config**](TenantApi.md#update_on_prem_tenant_config) | **POST** /clusters/tenant-config | Update Tenants Config.
[**update_tenant**](TenantApi.md#update_tenant) | **PUT** /tenants/{id} | Update Tenant.
[**update_tenant_swift**](TenantApi.md#update_tenant_swift) | **PUT** /tenants/swift | Update a Swift configuration.


# **assign_properties_to_tenant**
> TenantAssignments assign_properties_to_tenant(id, body)

Update assginment of properties for a tenant.

```Unknown Privileges``` <br><br>Assign/Unassign properties like storage domain, entities, policies etc. to the tenant. The API expects a list of all the assignments (policies etc.) that are supposed to be associated to the Tenant. The list of assignments passed get assigned to the Tenant and anything else that was already assigned gets unassigned. In case a few objects fail the assignment and some objects get assigned, error is returned for all assignments except for policies.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tenant
from cohesity_sdk.cluster.cohesity.model.tenant_assignments_params import TenantAssignmentsParams
from cohesity_sdk.cluster.cohesity.model.tenant_assignments import TenantAssignments
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenant.TenantApi(api_client)
    id = "C/" # str | The Tenant id.
    body = TenantAssignmentsParams(
        object_ids=[
            1,
        ],
        policy_ids=[
            "policy_ids_example",
        ],
        storage_domain_ids=[
            1,
        ],
        view_ids=[
            1,
        ],
        vlan_iface_names=[
            "vlan_iface_names_example",
        ],
    ) # TenantAssignmentsParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update assginment of properties for a tenant.
        api_response = api_instance.assign_properties_to_tenant(id, body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling TenantApi->assign_properties_to_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Tenant id. |
 **body** | [**TenantAssignmentsParams**](TenantAssignmentsParams.md)|  |

### Return type

[**TenantAssignments**](TenantAssignments.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tenant**
> TenantInfo create_tenant(body)

Create a new Tenant.

**Privileges:** ```ORGANIZATION_MODIFY``` <br><br>

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tenant
from cohesity_sdk.cluster.cohesity.model.unknownbasetype import UNKNOWNBASETYPE
from cohesity_sdk.cluster.cohesity.model.tenant_info import TenantInfo
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenant.TenantApi(api_client)
    body =  # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Tenant.
        api_response = api_instance.create_tenant(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling TenantApi->create_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**TenantInfo**](TenantInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tenant**
> delete_tenant(id)

Delete Tenant with given ID.

```Unknown Privileges``` <br><br>

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tenant
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenant.TenantApi(api_client)
    id = "C/" # str | The Tenant id.

    # example passing only required values which don't have defaults set
    try:
        # Delete Tenant with given ID.
        api_instance.delete_tenant(id)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling TenantApi->delete_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Tenant id. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assigned_properties_for_tenant**
> TenantAssignmentProperties get_assigned_properties_for_tenant(id)

Get tenant assignments.

```Unknown Privileges``` <br><br>Get all assigned properties like storage domain, entities, policies, objects, views etc for a given tenant.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tenant
from cohesity_sdk.cluster.cohesity.model.tenant_assignment_properties import TenantAssignmentProperties
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenant.TenantApi(api_client)
    id = "C/" # str | The Tenant id.

    # example passing only required values which don't have defaults set
    try:
        # Get tenant assignments.
        api_response = api_instance.get_assigned_properties_for_tenant(id)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling TenantApi->get_assigned_properties_for_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Tenant id. |

### Return type

[**TenantAssignmentProperties**](TenantAssignmentProperties.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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
> OnPremTenantConfig get_on_prem_tenant_config()

Get Tenants Config.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get Tenant related configurations for the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tenant
from cohesity_sdk.cluster.cohesity.model.on_prem_tenant_config import OnPremTenantConfig
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenant.TenantApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Tenants Config.
        api_response = api_instance.get_on_prem_tenant_config()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling TenantApi->get_on_prem_tenant_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OnPremTenantConfig**](OnPremTenantConfig.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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
> SwiftParams get_tenant_swift()

Get a Swift configuration.

**Privileges:** ```KEYSTONE_VIEW``` <br><br>Get a Swift configuration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tenant
from cohesity_sdk.cluster.cohesity.model.swift_params import SwiftParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenant.TenantApi(api_client)
    tenant_id = "tenantId_example" # str | Specifies the tenant Id. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a Swift configuration.
        api_response = api_instance.get_tenant_swift(tenant_id=tenant_id)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling TenantApi->get_tenant_swift: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Specifies the tenant Id. | [optional]

### Return type

[**SwiftParams**](SwiftParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tenants**
> TenantsInfo list_tenants()

Get a list of Tenants.

**Privileges:** ```ORGANIZATION_VIEW``` <br><br>

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tenant
from cohesity_sdk.cluster.cohesity.model.tenants_info import TenantsInfo
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenant.TenantApi(api_client)
    ids = [
        "ids_example",
    ] # [str, none_type] | List of tenantIds to filter. (optional)
    statuses = [
        "Active",
    ] # [str, none_type] | Filter by current status of tenant. If left blank, only active and inactive tenants are returned. (optional)
    liveness_modes = [
        "Active",
    ] # [str, none_type] | Filter by liveness modes of the tenant. This filter only applies is tenant metadata is added for external vendor such as 'IBM'. In all other cases, the values provided for this filter will be ignored. (optional)
    ownership_modes = [
        "Primary",
    ] # [str, none_type] | Filter by ownership modes of the tenant. This filter only applies is tenant metadata is added for external vendor such as 'IBM'. In all other cases, the values provided for this filter will be ignored. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of Tenants.
        api_response = api_instance.list_tenants(ids=ids, statuses=statuses, liveness_modes=liveness_modes, ownership_modes=ownership_modes)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling TenantApi->list_tenants: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**[str, none_type]**](str, none_type.md)| List of tenantIds to filter. | [optional]
 **statuses** | [**[str, none_type]**](str, none_type.md)| Filter by current status of tenant. If left blank, only active and inactive tenants are returned. | [optional]
 **liveness_modes** | [**[str, none_type]**](str, none_type.md)| Filter by liveness modes of the tenant. This filter only applies is tenant metadata is added for external vendor such as &#39;IBM&#39;. In all other cases, the values provided for this filter will be ignored. | [optional]
 **ownership_modes** | [**[str, none_type]**](str, none_type.md)| Filter by ownership modes of the tenant. This filter only applies is tenant metadata is added for external vendor such as &#39;IBM&#39;. In all other cases, the values provided for this filter will be ignored. | [optional]

### Return type

[**TenantsInfo**](TenantsInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_tenant_action**
> TenantInfo perform_tenant_action(id, body)

Perform actions on a Tenant.

```Unknown Privileges``` <br><br>Perform actions like activate and deactivate on a given Tenant.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tenant
from cohesity_sdk.cluster.cohesity.model.tenant_action_body import TenantActionBody
from cohesity_sdk.cluster.cohesity.model.tenant_info import TenantInfo
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenant.TenantApi(api_client)
    id = "C/" # str | The Tenant id.
    body = TenantActionBody(
        action="Activate",
    ) # TenantActionBody | Specifies the parameters to perform an action on a Tenant.

    # example passing only required values which don't have defaults set
    try:
        # Perform actions on a Tenant.
        api_response = api_instance.perform_tenant_action(id, body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling TenantApi->perform_tenant_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Tenant id. |
 **body** | [**TenantActionBody**](TenantActionBody.md)| Specifies the parameters to perform an action on a Tenant. |

### Return type

[**TenantInfo**](TenantInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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
> register_swift(body)

Register Swift service on a Keystone server.

**Privileges:** ```KEYSTONE_MODIFY``` <br><br>Register Swift service on Keystone server.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tenant
from cohesity_sdk.cluster.cohesity.model.register_swift_params import RegisterSwiftParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenant.TenantApi(api_client)
    body = RegisterSwiftParams(
        keystone_credentials=KeystoneCredentials(
            admin_creds=KeystoneAdminParams(
                domain="domain_example",
                password="password_example",
                username="username_example",
            ),
            scope=KeystoneScopeParams(
                domain_scope_params=DomainScopeParams(
                    domain_name="domain_name_example",
                ),
                project_scope_params=ProjectScopeParams(
                    domain_name="domain_name_example",
                    project_name="project_name_example",
                ),
                type="Project",
            ),
        ),
        tenant_id="tenant_id_example",
    ) # RegisterSwiftParams | Specifies the parameters to register a Swift service on Keystone server.

    # example passing only required values which don't have defaults set
    try:
        # Register Swift service on a Keystone server.
        api_instance.register_swift(body)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling TenantApi->register_swift: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterSwiftParams**](RegisterSwiftParams.md)| Specifies the parameters to register a Swift service on Keystone server. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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
> unregister_swift(body)

Unregister Swift service from a Keystone server.

**Privileges:** ```KEYSTONE_MODIFY``` <br><br>Unregister Swift service from Keystone server.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tenant
from cohesity_sdk.cluster.cohesity.model.unregister_swift_params import UnregisterSwiftParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenant.TenantApi(api_client)
    body = UnregisterSwiftParams(
        keystone_credentials=KeystoneCredentials(
            admin_creds=KeystoneAdminParams(
                domain="domain_example",
                password="password_example",
                username="username_example",
            ),
            scope=KeystoneScopeParams(
                domain_scope_params=DomainScopeParams(
                    domain_name="domain_name_example",
                ),
                project_scope_params=ProjectScopeParams(
                    domain_name="domain_name_example",
                    project_name="project_name_example",
                ),
                type="Project",
            ),
        ),
        tenant_id="tenant_id_example",
    ) # UnregisterSwiftParams | Specifies the parameters to unregister a Swift service from Keystone server.

    # example passing only required values which don't have defaults set
    try:
        # Unregister Swift service from a Keystone server.
        api_instance.unregister_swift(body)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling TenantApi->unregister_swift: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnregisterSwiftParams**](UnregisterSwiftParams.md)| Specifies the parameters to unregister a Swift service from Keystone server. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_on_prem_tenant_config**
> OnPremTenantConfig update_on_prem_tenant_config(body)

Update Tenants Config.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update Tenant related configurations for the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tenant
from cohesity_sdk.cluster.cohesity.model.on_prem_tenant_config import OnPremTenantConfig
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenant.TenantApi(api_client)
    body = OnPremTenantConfig(
        organizations_enabled=True,
        organizations_storage_domain_sharing_enabled=True,
    ) # OnPremTenantConfig | 

    # example passing only required values which don't have defaults set
    try:
        # Update Tenants Config.
        api_response = api_instance.update_on_prem_tenant_config(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling TenantApi->update_on_prem_tenant_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OnPremTenantConfig**](OnPremTenantConfig.md)|  |

### Return type

[**OnPremTenantConfig**](OnPremTenantConfig.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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
> TenantInfo update_tenant(id, body)

Update Tenant.

```Unknown Privileges``` <br><br>Update Tenant's properties.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tenant
from cohesity_sdk.cluster.cohesity.model.update_tenant_body import UpdateTenantBody
from cohesity_sdk.cluster.cohesity.model.tenant_info import TenantInfo
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenant.TenantApi(api_client)
    id = "C/" # str, none_type | 
    body = UpdateTenantBody() # UpdateTenantBody | 

    # example passing only required values which don't have defaults set
    try:
        # Update Tenant.
        api_response = api_instance.update_tenant(id, body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling TenantApi->update_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str, none_type**|  |
 **body** | [**UpdateTenantBody**](UpdateTenantBody.md)|  |

### Return type

[**TenantInfo**](TenantInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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
> SwiftParams update_tenant_swift(body)

Update a Swift configuration.

**Privileges:** ```KEYSTONE_MODIFY``` <br><br>Update a Swift configuration.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tenant
from cohesity_sdk.cluster.cohesity.model.swift_params import SwiftParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tenant.TenantApi(api_client)
    body = SwiftParams(
        keystone_id=1,
        operator_roles=[
            "operator_roles_example",
        ],
        tenant_id="tenant_id_example",
    ) # SwiftParams | Specifies the parameters to update a Swift configuration.

    # example passing only required values which don't have defaults set
    try:
        # Update a Swift configuration.
        api_response = api_instance.update_tenant_swift(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling TenantApi->update_tenant_swift: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SwiftParams**](SwiftParams.md)| Specifies the parameters to update a Swift configuration. |

### Return type

[**SwiftParams**](SwiftParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

