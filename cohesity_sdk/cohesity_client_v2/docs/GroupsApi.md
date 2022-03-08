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
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.groups import Groups
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


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
	api_response = client.groups.get_groups(domain=domain, names=names, roles=roles, tenant_ids=tenant_ids, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling GroupsApi->get_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

