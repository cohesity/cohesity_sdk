# cohesity_sdk.TenantApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_properties_to_tenant**](TenantApi.md#assign_properties_to_tenant) | **PUT** /tenants/{id}/assignments | Update assginment of properties for a tenant.
[**create_tenant**](TenantApi.md#create_tenant) | **POST** /tenants | Create a new Tenant.
[**delete_tenant**](TenantApi.md#delete_tenant) | **DELETE** /tenants/{id} | Delete Tenant with given ID.
[**get_assigned_properties_for_tenant**](TenantApi.md#get_assigned_properties_for_tenant) | **GET** /tenants/{id}/assignments | Get tenant assignments.
[**get_on_prem_tenant_config**](TenantApi.md#get_on_prem_tenant_config) | **GET** /clusters/tenant-config | Get Tenants Config.
[**get_tenant_by_id**](TenantApi.md#get_tenant_by_id) | **GET** /tenants/{id} | Get Tenant by ID.
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

Assign/Unassign properties like storage domain, entities, policies etc. to the tenant. The API expects a list of all the assignments (policies etc.) that are supposed to be associated to the Tenant. The list of assignments passed get assigned to the Tenant and anything else that was already assigned gets unassigned. In case a few objects fail the assignment and some objects get assigned, error is returned for all assignments except for policies.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.tenant_assignments import TenantAssignments
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.tenant_assignments_params import TenantAssignmentsParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


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
	api_response = client.tenant.assign_properties_to_tenant(id, body)
	pprint(api_response)
except ApiException as e:
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

# **create_tenant**
> TenantInfo create_tenant(body)

Create a new Tenant.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.create_tenant_parameters import CreateTenantParameters
from cohesity_sdk.cluster.model.tenant_info import TenantInfo
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateTenantParameters() # CreateTenantParameters | 

# example passing only required values which don't have defaults set
try:
	# Create a new Tenant.
	api_response = client.tenant.create_tenant(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->create_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTenantParameters**](CreateTenantParameters.md)|  |

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

# **delete_tenant**
> delete_tenant(id)

Delete Tenant with given ID.

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


id = "C/" # str | The Tenant id.

# example passing only required values which don't have defaults set
try:
	# Delete Tenant with given ID.
	client.tenant.delete_tenant(id)
except ApiException as e:
	print("Exception when calling TenantApi->delete_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Tenant id. |

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

# **get_assigned_properties_for_tenant**
> TenantAssignmentProperties get_assigned_properties_for_tenant(id)

Get tenant assignments.

Get all assigned properties like storage domain, entities, policies, objects, views etc for a given tenant.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.tenant_assignment_properties import TenantAssignmentProperties
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "C/" # str | The Tenant id.

# example passing only required values which don't have defaults set
try:
	# Get tenant assignments.
	api_response = client.tenant.get_assigned_properties_for_tenant(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->get_assigned_properties_for_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Tenant id. |

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

# **get_on_prem_tenant_config**
> OnPremTenantConfig get_on_prem_tenant_config()

Get Tenants Config.

Get Tenant related configurations for the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.on_prem_tenant_config import OnPremTenantConfig
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get Tenants Config.
	api_response = client.tenant.get_on_prem_tenant_config()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->get_on_prem_tenant_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
> TenantInfo get_tenant_by_id(id)

Get Tenant by ID.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.tenant_info import TenantInfo
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "C/" # str | The Tenant id.

# example passing only required values which don't have defaults set
try:
	# Get Tenant by ID.
	api_response = client.tenant.get_tenant_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->get_tenant_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Tenant id. |

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

# **get_tenant_swift**
> SwiftParams get_tenant_swift()

Get a Swift configuration.

Get a Swift configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.swift_params import SwiftParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


tenant_id = "tenantId_example" # str | Specifies the tenant Id. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a Swift configuration.
	api_response = client.tenant.get_tenant_swift(tenant_id=tenant_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->get_tenant_swift: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **list_tenants**
> TenantsInfo list_tenants()

Get a list of Tenants.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.tenants_info import TenantsInfo
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


ids = [
        "ids_example",
    ] # [str, none_type] | List of tenantIds to filter. (optional)
statuses = [
        "Active",
    ] # [str, none_type] | Filter by current status of tenant. If left blank, only active and inactive tenants are returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a list of Tenants.
	api_response = client.tenant.list_tenants(ids=ids, statuses=statuses)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->list_tenants: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**[str, none_type]**](str, none_type.md)| List of tenantIds to filter. | [optional]
 **statuses** | [**[str, none_type]**](str, none_type.md)| Filter by current status of tenant. If left blank, only active and inactive tenants are returned. | [optional]

### Return type

[**TenantsInfo**](TenantsInfo.md)

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

# **perform_tenant_action**
> TenantInfo perform_tenant_action(id, body)

Perform actions on a Tenant.

Perform actions like activate and deactivate on a given Tenant.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.tenant_info import TenantInfo
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.tenant_action_body import TenantActionBody
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "C/" # str | The Tenant id.
body = TenantActionBody(
        action="Activate",
    ) # TenantActionBody | Specifies the parameters to perform an action on a Tenant.

# example passing only required values which don't have defaults set
try:
	# Perform actions on a Tenant.
	api_response = client.tenant.perform_tenant_action(id, body)
	pprint(api_response)
except ApiException as e:
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
> register_swift(body)

Register Swift service on a Keystone server.

Register Swift service on Keystone server.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.register_swift_params import RegisterSwiftParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = RegisterSwiftParams(
        keystone_credentials=KeystoneCredentials(
            admin_creds={},
            scope={},
        ),
        tenant_id="tenant_id_example",
    ) # RegisterSwiftParams | Specifies the parameters to register a Swift service on Keystone server.

# example passing only required values which don't have defaults set
try:
	# Register Swift service on a Keystone server.
	client.tenant.register_swift(body)
except ApiException as e:
	print("Exception when calling TenantApi->register_swift: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterSwiftParams**](RegisterSwiftParams.md)| Specifies the parameters to register a Swift service on Keystone server. |

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
> unregister_swift(body)

Unregister Swift service from a Keystone server.

Unregister Swift service from Keystone server.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.unregister_swift_params import UnregisterSwiftParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = UnregisterSwiftParams(
        keystone_credentials=KeystoneCredentials(
            admin_creds={},
            scope={},
        ),
        tenant_id="tenant_id_example",
    ) # UnregisterSwiftParams | Specifies the parameters to unregister a Swift service from Keystone server.

# example passing only required values which don't have defaults set
try:
	# Unregister Swift service from a Keystone server.
	client.tenant.unregister_swift(body)
except ApiException as e:
	print("Exception when calling TenantApi->unregister_swift: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnregisterSwiftParams**](UnregisterSwiftParams.md)| Specifies the parameters to unregister a Swift service from Keystone server. |

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

# **update_on_prem_tenant_config**
> OnPremTenantConfig update_on_prem_tenant_config(body)

Update Tenants Config.

Update Tenant related configurations for the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.on_prem_tenant_config import OnPremTenantConfig
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = OnPremTenantConfig(
        organizations_enabled=True,
        organizations_storage_domain_sharing_enabled=True,
    ) # OnPremTenantConfig | 

# example passing only required values which don't have defaults set
try:
	# Update Tenants Config.
	api_response = client.tenant.update_on_prem_tenant_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->update_on_prem_tenant_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OnPremTenantConfig**](OnPremTenantConfig.md)|  |

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
> TenantInfo update_tenant(id, body)

Update Tenant.

Update Tenant's properties.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.tenant_info import TenantInfo
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.update_tenant_body import UpdateTenantBody
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "C/" # str, none_type | 
body = UpdateTenantBody() # UpdateTenantBody | 

# example passing only required values which don't have defaults set
try:
	# Update Tenant.
	api_response = client.tenant.update_tenant(id, body)
	pprint(api_response)
except ApiException as e:
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
> SwiftParams update_tenant_swift(body)

Update a Swift configuration.

Update a Swift configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.swift_params import SwiftParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


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
	api_response = client.tenant.update_tenant_swift(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->update_tenant_swift: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SwiftParams**](SwiftParams.md)| Specifies the parameters to update a Swift configuration. |

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

