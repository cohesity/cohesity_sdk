# cohesity_sdk.GroupsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_groups**](GroupsApi.md#get_groups) | **GET** /groups | Get Groups.


# **get_groups**
> Groups get_groups()

Get Groups.

Get Groups.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.groups import Groups
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
domain = "domain_example" # str | Specifies the Group domain to filter. (optional)
names = [
        "names_example",
    ] # [str] | Specifies a list of names to filter. (optional)
roles = [
        "roles_example",
    ] # [str] | Specifies a list of roles to filter. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which groups are to be returned. (optional)
include_tenants = True # bool | IncludeTenants specifies if groups of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Groups.
	api_response = client.groups.get_groups(access_cluster_id=access_cluster_id, region_id=region_id, domain=domain, names=names, roles=roles, tenant_ids=tenant_ids, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling GroupsApi->get_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **domain** | **str**| Specifies the Group domain to filter. | [optional]
 **names** | **[str]**| Specifies a list of names to filter. | [optional]
 **roles** | **[str]**| Specifies a list of roles to filter. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which groups are to be returned. | [optional]
 **include_tenants** | **bool**| IncludeTenants specifies if groups of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional]

### Return type

[**Groups**](Groups.md)

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

