# cohesity_sdk.TenantApi


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
[**reassociate_key**](TenantApi.md#reassociate_key) | **POST** /mcm/tenants/reassociate-key | Reassociate the api key to another tenant.
[**register_swift**](TenantApi.md#register_swift) | **POST** /tenants/swift/register | Register Swift service on a Keystone server.
[**trigger_tenant_backfill_task**](TenantApi.md#trigger_tenant_backfill_task) | **POST** /mcm/tenants/backfill-tasks | Trigger a tenant backfill task.
[**unregister_swift**](TenantApi.md#unregister_swift) | **POST** /tenants/swift/unregister | Unregister Swift service from a Keystone server.
[**update_account_tenant_config**](TenantApi.md#update_account_tenant_config) | **PATCH** /mcm/accounts/tenant-config | Update Tenant&#39;s Config.
[**update_clusters_tenant_config**](TenantApi.md#update_clusters_tenant_config) | **POST** /mcm/clusters/tenant-config | Update Tenant&#39;s config for clusters.
[**update_helios_tenant**](TenantApi.md#update_helios_tenant) | **PATCH** /mcm/tenants/{id} | Update Tenant properties on Helios.
[**update_on_prem_tenant_config**](TenantApi.md#update_on_prem_tenant_config) | **POST** /clusters/tenant-config | Update Tenants Config.
[**update_tenant**](TenantApi.md#update_tenant) | **PUT** /tenants/{id} | Update Tenant.
[**update_tenant_swift**](TenantApi.md#update_tenant_swift) | **PUT** /tenants/swift | Update a Swift configuration.


# **assign_cluster_to_tenant**
> HeliosTenant assign_cluster_to_tenant(id, body)

Assign a Cluster to a tenant.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.helios_tenant import HeliosTenant
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.assign_cluster_to_tenant_params_body import AssignClusterToTenantParamsBody
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "C:2LC4aWwWL9Y864DZtaGRyyGFZKkkp4zca0U0gGb/" # str, none_type | 
body = AssignClusterToTenantParamsBody(
        cluster_identifier="4:072888001528021798096225500850762068629",
        network=TenantNetwork(
            connector_enabled=True,
            cluster_hostname="cluster_hostname_example",
            cluster_ips=[
                "cluster_ips_example",
            ],
        ),
    ) # AssignClusterToTenantParamsBody | 
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Assign a Cluster to a tenant.
	api_response = client.tenant.assign_cluster_to_tenant(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->assign_cluster_to_tenant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Assign a Cluster to a tenant.
	api_response = client.tenant.assign_cluster_to_tenant(id, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->assign_cluster_to_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str, none_type**|  |
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
> TenantAssignments assign_properties_to_tenant(id, body)

Update assginment of properties for a tenant.

Assign/Unassign properties like storage domain, entities, policies etc. to the tenant. The API expects a list of all the assignments (policies etc.) that are supposed to be associated to the Tenant. The list of assignments passed get assigned to the Tenant and anything else that was already assigned gets unassigned. In case a few objects fail the assignment and some objects get assigned, error is returned for all assignments except for policies.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.tenant_assignments_params import TenantAssignmentsParams
from cohesity_sdk.helios.model.tenant_assignments import TenantAssignments
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "C/" # str | The Tenant id.
body = TenantAssignmentsParams(
        storage_domain_ids=[
            1,
        ],
        object_ids=[
            1,
        ],
        vlan_iface_names=[
            "vlan_iface_names_example",
        ],
        view_ids=[
            1,
        ],
        policy_ids=[
            "policy_ids_example",
        ],
    ) # TenantAssignmentsParams | 
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update assginment of properties for a tenant.
	api_response = client.tenant.assign_properties_to_tenant(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->assign_properties_to_tenant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update assginment of properties for a tenant.
	api_response = client.tenant.assign_properties_to_tenant(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> HeliosTenant confirm_tenant(id, body)

Enable Helios Management for Tenant.

For a specific, TenantId enable it to be managed by Helios.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.helios_tenant import HeliosTenant
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.confirm_tenant_params_body import ConfirmTenantParamsBody
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "C:2LC4aWwWL9Y864DZtaGRyyGFZKkkp4zca0U0gGb/" # str, none_type | 
body = ConfirmTenantParamsBody(
        name="name_example",
        description="description_example",
    ) # ConfirmTenantParamsBody | 
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Enable Helios Management for Tenant.
	api_response = client.tenant.confirm_tenant(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->confirm_tenant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Enable Helios Management for Tenant.
	api_response = client.tenant.confirm_tenant(id, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->confirm_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str, none_type**|  |
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
> HeliosTenant create_helios_tenant(body)

Create a new Tenant on Helios.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.create_tenant_params import CreateTenantParams
from cohesity_sdk.helios.model.helios_tenant import HeliosTenant
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = CreateTenantParams(
        name="name_example",
        tenant_id_suffix="tenant_id_suffix_example",
        description="description_example",
        is_managed_on_helios=True,
    ) # CreateTenantParams | 
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a new Tenant on Helios.
	api_response = client.tenant.create_helios_tenant(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->create_helios_tenant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a new Tenant on Helios.
	api_response = client.tenant.create_helios_tenant(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> TenantInfo create_tenant(body)

Create a new Tenant.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.tenant_info import TenantInfo
from cohesity_sdk.helios.model.unknownbasetype import UNKNOWNBASETYPE
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body =  # UNKNOWN_BASE_TYPE | 
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a new Tenant.
	api_response = client.tenant.create_tenant(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->create_tenant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a new Tenant.
	api_response = client.tenant.create_tenant(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->create_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |
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
> delete_helios_tenant(id)

Delete a Tenant on Helios.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "C:2LC4aWwWL9Y864DZtaGRyyGFZKkkp4zca0U0gGb/" # str | 
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
delete_cluster_tenants = True # bool | Whether or not to delete the tenants on the cluster, default is true. (optional) if omitted the server will use the default value of True

# example passing only required values which don't have defaults set
try:
	# Delete a Tenant on Helios.
	client.tenant.delete_helios_tenant(id)
except ApiException as e:
	print("Exception when calling TenantApi->delete_helios_tenant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete a Tenant on Helios.
	client.tenant.delete_helios_tenant(id, region_id=region_id, delete_cluster_tenants=delete_cluster_tenants)
except ApiException as e:
	print("Exception when calling TenantApi->delete_helios_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **delete_cluster_tenants** | **bool**| Whether or not to delete the tenants on the cluster, default is true. | [optional] if omitted the server will use the default value of True

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
> delete_tenant(id)

Delete Tenant with given ID.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "C/" # str | The Tenant id.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete Tenant with given ID.
	client.tenant.delete_tenant(id)
except ApiException as e:
	print("Exception when calling TenantApi->delete_tenant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete Tenant with given ID.
	client.tenant.delete_tenant(id, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
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
> TenantConfig get_account_tenant_config()

Get Tenants Config.

Get Tenant related configurations for the account.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.tenant_config import TenantConfig
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Tenants Config.
	api_response = client.tenant.get_account_tenant_config(region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> TenantAssignmentProperties get_assigned_properties_for_tenant(id)

Get tenant assignments.

Get all assigned properties like storage domain, entities, policies, objects, views etc for a given tenant.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.tenant_assignment_properties import TenantAssignmentProperties
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "C/" # str | The Tenant id.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get tenant assignments.
	api_response = client.tenant.get_assigned_properties_for_tenant(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->get_assigned_properties_for_tenant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get tenant assignments.
	api_response = client.tenant.get_assigned_properties_for_tenant(id, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> ClustersTenantConfigs get_clusters_tenant_config()

Get Tenant's config for all clusters.

Get Tenant related configurations for all the clusters.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.clusters_tenant_configs import ClustersTenantConfigs
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Tenant's config for all clusters.
	api_response = client.tenant.get_clusters_tenant_config(region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> ListTenantData get_helios_tenants()

Get a list of tenants.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.list_tenant_data import ListTenantData
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
cluster_identifiers = [
        "4:072888001528021798096225500850762068629",
    ] # [str] | Specifies the list of cluster identifiers. The format is clusterId:clusterIncarnationId. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str, none_type] | List of Tenant Ids to filter from. (optional)
statuses = [
        "Active",
    ] # [str, none_type] | Status of the tenant on Helios. Active and Inactive tenants are returned if this field is not specified. Also, if specified, only helios managed tenants are returned. (optional)
managed_on_helios = True # bool, none_type | Whether managed on helios or not. (optional)
include_deleted_systems = True # bool, none_type | Whether tenants deleted on clusters should be included. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a list of tenants.
	api_response = client.tenant.get_helios_tenants(region_id=region_id, cluster_identifiers=cluster_identifiers, tenant_ids=tenant_ids, statuses=statuses, managed_on_helios=managed_on_helios, include_deleted_systems=include_deleted_systems)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->get_helios_tenants: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **cluster_identifiers** | **[str]**| Specifies the list of cluster identifiers. The format is clusterId:clusterIncarnationId. | [optional]
 **tenant_ids** | [**[str, none_type]**](str, none_type.md)| List of Tenant Ids to filter from. | [optional]
 **statuses** | [**[str, none_type]**](str, none_type.md)| Status of the tenant on Helios. Active and Inactive tenants are returned if this field is not specified. Also, if specified, only helios managed tenants are returned. | [optional]
 **managed_on_helios** | **bool, none_type**| Whether managed on helios or not. | [optional]
 **include_deleted_systems** | **bool, none_type**| Whether tenants deleted on clusters should be included. | [optional]

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
> OnPremTenantConfig get_on_prem_tenant_config()

Get Tenants Config.

Get Tenant related configurations for the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.on_prem_tenant_config import OnPremTenantConfig
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Tenants Config.
	api_response = client.tenant.get_on_prem_tenant_config(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> TenantInfo get_tenant_by_id(id)

Get Tenant by ID.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.tenant_info import TenantInfo
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "C/" # str | The Tenant id.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get Tenant by ID.
	api_response = client.tenant.get_tenant_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->get_tenant_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Tenant by ID.
	api_response = client.tenant.get_tenant_by_id(id, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> HeliosTenantsStats get_tenant_stats()

Get Tenant Statistics.

Get Statistics on Sources and Storage Domains assigned to the Tenants belonging to an account.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.helios_tenants_stats import HeliosTenantsStats
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
tenant_ids = [
        "C:2LC4aWwWL9Y864DZtaGRyyGFZKkkp4zca0U0gGb/",
    ] # [str], none_type | List of Tenant Ids to filter from. (optional)
include_deleted = False # bool, none_type | If deleted tenants stats need to be included. (optional) if omitted the server will use the default value of False

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Tenant Statistics.
	api_response = client.tenant.get_tenant_stats(region_id=region_id, tenant_ids=tenant_ids, include_deleted=include_deleted)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->get_tenant_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **tenant_ids** | **[str], none_type**| List of Tenant Ids to filter from. | [optional]
 **include_deleted** | **bool, none_type**| If deleted tenants stats need to be included. | [optional] if omitted the server will use the default value of False

### Return type

[**HeliosTenantsStats**](HeliosTenantsStats.md)

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.swift_params import SwiftParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
tenant_id = "tenantId_example" # str | Specifies the tenant Id. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a Swift configuration.
	api_response = client.tenant.get_tenant_swift(access_cluster_id=access_cluster_id, region_id=region_id, tenant_id=tenant_id)
	pprint(api_response)
except ApiException as e:
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
> HeliosTenantAssignmentsResult helios_assign_properties_to_tenant(id, body)

Assign properties to a tenant.

Assign properties like policies etc. to a tenant on a given cluster. The API expects a list of all the assignments (policies etc.) that are supposed to be associated to the Tenant. The list of assignments passed get assigned to the Tenant and anything else that was already assigned gets unassigned.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.helios_tenant_assignments_result import HeliosTenantAssignmentsResult
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.helios_tenant_assignments_params import HeliosTenantAssignmentsParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | The Tenant id.
body = HeliosTenantAssignmentsParams(
        cluster_identifier="4:072888001528021798096225500850762068629",
        policy_ids=[
            "policy_ids_example",
        ],
    ) # HeliosTenantAssignmentsParams | 
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Assign properties to a tenant.
	api_response = client.tenant.helios_assign_properties_to_tenant(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->helios_assign_properties_to_tenant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Assign properties to a tenant.
	api_response = client.tenant.helios_assign_properties_to_tenant(id, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> TenantsInfo list_tenants()

Get a list of Tenants.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.tenants_info import TenantsInfo
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
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
	api_response = client.tenant.list_tenants(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, statuses=statuses)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->list_tenants: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
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

# **perform_helios_tenant_action**
> HeliosTenant perform_helios_tenant_action(id, body)

Perform actions on a Helios Tenant.

Perform actions like activate and deactivate on a given Tenant on Helios.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.helios_tenant import HeliosTenant
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.tenant_action_body import TenantActionBody
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | The Tenant id.
body = TenantActionBody(
        action="Activate",
    ) # TenantActionBody | Specifies the parameters to perform an action on a Tenant.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Perform actions on a Helios Tenant.
	api_response = client.tenant.perform_helios_tenant_action(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->perform_helios_tenant_action: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Perform actions on a Helios Tenant.
	api_response = client.tenant.perform_helios_tenant_action(id, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> TenantInfo perform_tenant_action(id, body)

Perform actions on a Tenant.

Perform actions like activate and deactivate on a given Tenant.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.tenant_info import TenantInfo
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.tenant_action_body import TenantActionBody
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "C/" # str | The Tenant id.
body = TenantActionBody(
        action="Activate",
    ) # TenantActionBody | Specifies the parameters to perform an action on a Tenant.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Perform actions on a Tenant.
	api_response = client.tenant.perform_tenant_action(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->perform_tenant_action: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Perform actions on a Tenant.
	api_response = client.tenant.perform_tenant_action(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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

# **reassociate_key**
> ReassociateKeyResponseBody reassociate_key(body)

Reassociate the api key to another tenant.

Reassociate the api key to another tenant.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.reassociate_key_request import ReassociateKeyRequest
from cohesity_sdk.helios.model.reassociate_key_response_body import ReassociateKeyResponseBody
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = ReassociateKeyRequest(
        api_key="api_key_example",
    ) # ReassociateKeyRequest | Specifies the parameters to re-associate api key.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Reassociate the api key to another tenant.
	api_response = client.tenant.reassociate_key(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->reassociate_key: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Reassociate the api key to another tenant.
	api_response = client.tenant.reassociate_key(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->reassociate_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReassociateKeyRequest**](ReassociateKeyRequest.md)| Specifies the parameters to re-associate api key. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**ReassociateKeyResponseBody**](ReassociateKeyResponseBody.md)

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.register_swift_params import RegisterSwiftParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = RegisterSwiftParams(
        tenant_id="tenant_id_example",
        keystone_credentials=KeystoneCredentials(
            admin_creds={},
            scope={},
        ),
    ) # RegisterSwiftParams | Specifies the parameters to register a Swift service on Keystone server.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Register Swift service on a Keystone server.
	client.tenant.register_swift(body)
except ApiException as e:
	print("Exception when calling TenantApi->register_swift: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Register Swift service on a Keystone server.
	client.tenant.register_swift(body, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
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

# **trigger_tenant_backfill_task**
> TenantBackfillBody trigger_tenant_backfill_task(body)

Trigger a tenant backfill task.

Trigger a tenant backfill task on Helios.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.tenant_backfill_body import TenantBackfillBody
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = TenantBackfillBody(
        task_type="SourceRegistration",
    ) # TenantBackfillBody | Specifies the parameters to trigger a tenant backfill task.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Trigger a tenant backfill task.
	api_response = client.tenant.trigger_tenant_backfill_task(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->trigger_tenant_backfill_task: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Trigger a tenant backfill task.
	api_response = client.tenant.trigger_tenant_backfill_task(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->trigger_tenant_backfill_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TenantBackfillBody**](TenantBackfillBody.md)| Specifies the parameters to trigger a tenant backfill task. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**TenantBackfillBody**](TenantBackfillBody.md)

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

# **unregister_swift**
> unregister_swift(body)

Unregister Swift service from a Keystone server.

Unregister Swift service from Keystone server.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.unregister_swift_params import UnregisterSwiftParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = UnregisterSwiftParams(
        tenant_id="tenant_id_example",
        keystone_credentials=KeystoneCredentials(
            admin_creds={},
            scope={},
        ),
    ) # UnregisterSwiftParams | Specifies the parameters to unregister a Swift service from Keystone server.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Unregister Swift service from a Keystone server.
	client.tenant.unregister_swift(body)
except ApiException as e:
	print("Exception when calling TenantApi->unregister_swift: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Unregister Swift service from a Keystone server.
	client.tenant.unregister_swift(body, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
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
> TenantConfig update_account_tenant_config(body)

Update Tenant's Config.

Update Tenant related configurations for the account.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.tenant_config import TenantConfig
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = TenantConfig(
        organizations_enabled=True,
    ) # TenantConfig | 
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update Tenant's Config.
	api_response = client.tenant.update_account_tenant_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->update_account_tenant_config: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update Tenant's Config.
	api_response = client.tenant.update_account_tenant_config(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> UpdateClustersTenantConfigsResponse update_clusters_tenant_config(body)

Update Tenant's config for clusters.

Update Tenant related configurations for a list of clusters.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.update_clusters_tenant_configs_response import UpdateClustersTenantConfigsResponse
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.clusters_tenant_configs import ClustersTenantConfigs
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = ClustersTenantConfigs(
        clusters=[
            ClusterTenantConfig(
                cluster_identifier="4:072888001528021798096225500850762068629",
                organizations_enabled=True,
                organizations_storage_domain_sharing_enabled=False,
            ),
        ],
    ) # ClustersTenantConfigs | 
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update Tenant's config for clusters.
	api_response = client.tenant.update_clusters_tenant_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->update_clusters_tenant_config: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update Tenant's config for clusters.
	api_response = client.tenant.update_clusters_tenant_config(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> HeliosTenant update_helios_tenant(id, body)

Update Tenant properties on Helios.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.update_tenant_params import UpdateTenantParams
from cohesity_sdk.helios.model.helios_tenant import HeliosTenant
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "C:2LC4aWwWL9Y864DZtaGRyyGFZKkkp4zca0U0gGb/" # str, none_type | 
body = UpdateTenantParams(
        name="name_example",
        description="description_example",
    ) # UpdateTenantParams | 
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update Tenant properties on Helios.
	api_response = client.tenant.update_helios_tenant(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->update_helios_tenant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update Tenant properties on Helios.
	api_response = client.tenant.update_helios_tenant(id, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->update_helios_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str, none_type**|  |
 **body** | [**UpdateTenantParams**](UpdateTenantParams.md)|  |
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
> OnPremTenantConfig update_on_prem_tenant_config(body)

Update Tenants Config.

Update Tenant related configurations for the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.on_prem_tenant_config import OnPremTenantConfig
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = OnPremTenantConfig(
        organizations_enabled=True,
        organizations_storage_domain_sharing_enabled=True,
    ) # OnPremTenantConfig | 
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update Tenants Config.
	api_response = client.tenant.update_on_prem_tenant_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->update_on_prem_tenant_config: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update Tenants Config.
	api_response = client.tenant.update_on_prem_tenant_config(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> TenantInfo update_tenant(id, body)

Update Tenant.

Update Tenant's properties.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.tenant_info import TenantInfo
from cohesity_sdk.helios.model.update_tenant_body import UpdateTenantBody
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "C/" # str, none_type | 
body = UpdateTenantBody() # UpdateTenantBody | 
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update Tenant.
	api_response = client.tenant.update_tenant(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->update_tenant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update Tenant.
	api_response = client.tenant.update_tenant(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->update_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str, none_type**|  |
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
> SwiftParams update_tenant_swift(body)

Update a Swift configuration.

Update a Swift configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.swift_params import SwiftParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = SwiftParams(
        tenant_id="tenant_id_example",
        keystone_id=1,
        operator_roles=[
            "operator_roles_example",
        ],
    ) # SwiftParams | Specifies the parameters to update a Swift configuration.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update a Swift configuration.
	api_response = client.tenant.update_tenant_swift(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantApi->update_tenant_swift: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update a Swift configuration.
	api_response = client.tenant.update_tenant_swift(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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

