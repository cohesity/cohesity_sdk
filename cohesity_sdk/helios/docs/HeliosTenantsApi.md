# cohesity_sdk.HeliosTenantsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_cluster_to_tenant**](HeliosTenantsApi.md#assign_cluster_to_tenant) | **POST** /mcm/tenants/{id}/clusters | Assign a Cluster to a tenant.
[**confirm_tenant**](HeliosTenantsApi.md#confirm_tenant) | **POST** /mcm/tenants/{id}/manage | Enable Helios Management for Tenant.
[**create_helios_tenant**](HeliosTenantsApi.md#create_helios_tenant) | **POST** /mcm/tenants | Create a new Tenant on Helios.
[**delete_helios_tenant**](HeliosTenantsApi.md#delete_helios_tenant) | **DELETE** /mcm/tenants/{id} | Delete a Tenant on Helios.
[**get_account_tenant_config**](HeliosTenantsApi.md#get_account_tenant_config) | **GET** /mcm/accounts/tenant-config | Get Tenants Config.
[**get_clusters_tenant_config**](HeliosTenantsApi.md#get_clusters_tenant_config) | **GET** /mcm/clusters/tenant-config | Get Tenant&#39;s config for all clusters.
[**get_helios_tenants**](HeliosTenantsApi.md#get_helios_tenants) | **GET** /mcm/tenants | Get a list of tenants.
[**get_tenant_stats**](HeliosTenantsApi.md#get_tenant_stats) | **GET** /mcm/tenants/stats | Get Tenant Statistics.
[**helios_assign_properties_to_tenant**](HeliosTenantsApi.md#helios_assign_properties_to_tenant) | **PUT** /mcm/tenants/{id}/assignments | Assign properties to a tenant.
[**perform_helios_tenant_action**](HeliosTenantsApi.md#perform_helios_tenant_action) | **POST** /mcm/tenants/{id}/actions | Perform actions on a Helios Tenant.
[**update_account_tenant_config**](HeliosTenantsApi.md#update_account_tenant_config) | **PATCH** /mcm/accounts/tenant-config | Update Tenant&#39;s Config.
[**update_clusters_tenant_config**](HeliosTenantsApi.md#update_clusters_tenant_config) | **POST** /mcm/clusters/tenant-config | Update Tenant&#39;s config for clusters.
[**update_helios_tenant**](HeliosTenantsApi.md#update_helios_tenant) | **PATCH** /mcm/tenants/{id} | Update Tenant properties on Helios.


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
	api_response = client.helios_tenants.assign_cluster_to_tenant(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->assign_cluster_to_tenant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Assign a Cluster to a tenant.
	api_response = client.helios_tenants.assign_cluster_to_tenant(id, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->assign_cluster_to_tenant: %s\n" % e)
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
	api_response = client.helios_tenants.confirm_tenant(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->confirm_tenant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Enable Helios Management for Tenant.
	api_response = client.helios_tenants.confirm_tenant(id, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->confirm_tenant: %s\n" % e)
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
        tenant_id_suffix="Cu2LC4aWwWL9Y864DZtaGR",
        description="description_example",
    ) # CreateTenantParams | 
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a new Tenant on Helios.
	api_response = client.helios_tenants.create_helios_tenant(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->create_helios_tenant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a new Tenant on Helios.
	api_response = client.helios_tenants.create_helios_tenant(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->create_helios_tenant: %s\n" % e)
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
	client.helios_tenants.delete_helios_tenant(id)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->delete_helios_tenant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete a Tenant on Helios.
	client.helios_tenants.delete_helios_tenant(id, region_id=region_id, delete_cluster_tenants=delete_cluster_tenants)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->delete_helios_tenant: %s\n" % e)
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
	api_response = client.helios_tenants.get_account_tenant_config(region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->get_account_tenant_config: %s\n" % e)
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
	api_response = client.helios_tenants.get_clusters_tenant_config(region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->get_clusters_tenant_config: %s\n" % e)
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
	api_response = client.helios_tenants.get_helios_tenants(region_id=region_id, cluster_identifiers=cluster_identifiers, tenant_ids=tenant_ids, statuses=statuses, managed_on_helios=managed_on_helios, include_deleted_systems=include_deleted_systems)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->get_helios_tenants: %s\n" % e)
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
	api_response = client.helios_tenants.get_tenant_stats(region_id=region_id, tenant_ids=tenant_ids, include_deleted=include_deleted)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->get_tenant_stats: %s\n" % e)
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
	api_response = client.helios_tenants.helios_assign_properties_to_tenant(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->helios_assign_properties_to_tenant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Assign properties to a tenant.
	api_response = client.helios_tenants.helios_assign_properties_to_tenant(id, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->helios_assign_properties_to_tenant: %s\n" % e)
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
	api_response = client.helios_tenants.perform_helios_tenant_action(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->perform_helios_tenant_action: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Perform actions on a Helios Tenant.
	api_response = client.helios_tenants.perform_helios_tenant_action(id, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->perform_helios_tenant_action: %s\n" % e)
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
	api_response = client.helios_tenants.update_account_tenant_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->update_account_tenant_config: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update Tenant's Config.
	api_response = client.helios_tenants.update_account_tenant_config(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->update_account_tenant_config: %s\n" % e)
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
	api_response = client.helios_tenants.update_clusters_tenant_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->update_clusters_tenant_config: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update Tenant's config for clusters.
	api_response = client.helios_tenants.update_clusters_tenant_config(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->update_clusters_tenant_config: %s\n" % e)
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
	api_response = client.helios_tenants.update_helios_tenant(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->update_helios_tenant: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update Tenant properties on Helios.
	api_response = client.helios_tenants.update_helios_tenant(id, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosTenantsApi->update_helios_tenant: %s\n" % e)
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

