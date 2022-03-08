# cohesity_sdk.HeliosUsersApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tenant_access**](HeliosUsersApi.md#get_tenant_access) | **GET** /mcm/users/tenant-access | Get a list of available tenant access available to the logged in User.
[**get_users_mixin1**](HeliosUsersApi.md#get_users_mixin1) | **GET** /mcm/users | Get Users.


# **get_tenant_access**
> TenantAccessResult get_tenant_access()

Get a list of available tenant access available to the logged in User.

List Tenant Access

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.tenant_access_result import TenantAccessResult
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str, none_type] | List of Tenant Ids to filter from. (optional)
include_inactive = True # bool, none_type | By Default, only valid tenant access are returned. If set to true, inactive or ineffective or expired tenant access would be returned as well. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a list of available tenant access available to the logged in User.
	api_response = client.helios_users.get_tenant_access(region_id=region_id, tenant_ids=tenant_ids, include_inactive=include_inactive)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosUsersApi->get_tenant_access: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **tenant_ids** | [**[str, none_type]**](str, none_type.md)| List of Tenant Ids to filter from. | [optional]
 **include_inactive** | **bool, none_type**| By Default, only valid tenant access are returned. If set to true, inactive or ineffective or expired tenant access would be returned as well. | [optional]

### Return type

[**TenantAccessResult**](TenantAccessResult.md)

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

# **get_users_mixin1**
> Users get_users_mixin1()

Get Users.

Get helios users

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.users import Users
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Users.
	api_response = client.helios_users.get_users_mixin1(region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosUsersApi->get_users_mixin1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**Users**](Users.md)

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

