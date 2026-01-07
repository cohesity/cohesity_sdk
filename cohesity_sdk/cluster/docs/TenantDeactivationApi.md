# cohesity_sdk.TenantDeactivationApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**initiate_multi_tenant_deactivation**](TenantDeactivationApi.md#initiate_multi_tenant_deactivation) | **POST** /tenants/deactivations | 
[**initiate_tenant_deactivation**](TenantDeactivationApi.md#initiate_tenant_deactivation) | **POST** /tenants/{id}/deactivation | 


# **initiate_multi_tenant_deactivation**
> InitiateMultiTenantDeactivation initiate_multi_tenant_deactivation()



**Privileges:** ```ORGANIZATION_MODIFY``` <br><br>This API is to be used for initiating batch tenant deactivation workflow and orchestrating it

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.initiate_multi_tenant_deactivation import InitiateMultiTenantDeactivation
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


liveness_mode = "Active" # str, none_type | Liveness mode for the tenants on this cluster. (optional)
ownership_mode = "Primary" # str, none_type | Ownership mode for the tenants on this cluster. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	api_response = client.tenant_deactivation.initiate_multi_tenant_deactivation(liveness_mode=liveness_mode, ownership_mode=ownership_mode)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantDeactivationApi->initiate_multi_tenant_deactivation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **liveness_mode** | **str, none_type**| Liveness mode for the tenants on this cluster. | [optional]
 **ownership_mode** | **str, none_type**| Ownership mode for the tenants on this cluster. | [optional]

### Return type

[**InitiateMultiTenantDeactivation**](InitiateMultiTenantDeactivation.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_tenant_deactivation**
> InitiateTenantDeactivation initiate_tenant_deactivation(id)



```Unknown Privileges``` <br><br>This API is to be used for initiating a tenant deactivation workflow and orchestrating it. This API is not be confused with the tenants/{id}/actions API which only updates the tenant state in cluster config and mark it as active/ inactive.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.initiate_tenant_deactivation import InitiateTenantDeactivation
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
	api_response = client.tenant_deactivation.initiate_tenant_deactivation(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling TenantDeactivationApi->initiate_tenant_deactivation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Tenant id. |

### Return type

[**InitiateTenantDeactivation**](InitiateTenantDeactivation.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

