# cohesity_sdk.RoleApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](RoleApi.md#create_role) | **POST** /roles | Create a Role.
[**delete_role**](RoleApi.md#delete_role) | **DELETE** /roles/{name} | Delete a Role.
[**get_roles**](RoleApi.md#get_roles) | **GET** /roles | Get Roles.
[**update_role**](RoleApi.md#update_role) | **PUT** /roles/{name} | Update a Role.


# **create_role**
> Role create_role(body)

Create a Role.

Create a Role.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.role import Role
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.create_role_params import CreateRoleParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

body = CreateRoleParams() # CreateRoleParams | Specifies the request body to create a Role.

# example passing only required values which don't have defaults set
try:
	# Create a Role.
	api_response = client.role.create_role(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RoleApi->create_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRoleParams**](CreateRoleParams.md)| Specifies the request body to create a Role. |

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

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
> delete_role(name)

Delete a Role.

Delete a Role.

### Example

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

name = "name_example" # str | Specifies the name of Role to delete.

# example passing only required values which don't have defaults set
try:
	# Delete a Role.
	client.role.delete_role(name)
except ApiException as e:
	print("Exception when calling RoleApi->delete_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the name of Role to delete. |

### Return type

void (empty response body)

### Authorization

No authorization required

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
> Roles get_roles()

Get Roles.

Get Roles.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.roles import Roles
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

names = [
        "names_example",
    ] # [str] | Specifies a list of Role names. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which Roles are to be returned. (optional)
include_tenants = True # bool | If true, the response will include Roles which were created by all tenants which the current user has permission to see. If false, then only Roles created by the current user will be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Roles.
	api_response = client.role.get_roles(names=names, tenant_ids=tenant_ids, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RoleApi->get_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **[str]**| Specifies a list of Role names. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which Roles are to be returned. | [optional]
 **include_tenants** | **bool**| If true, the response will include Roles which were created by all tenants which the current user has permission to see. If false, then only Roles created by the current user will be returned. | [optional]

### Return type

[**Roles**](Roles.md)

### Authorization

No authorization required

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
> Role update_role(name, body)

Update a Role.

Update a Role.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.update_role_params import UpdateRoleParams
from cohesity_sdk.cluster.model.role import Role
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

name = "name_example" # str | Specifies the name of Role to update.
body = UpdateRoleParams(
        description="description_example",
        privileges=[
            "privileges_example",
        ],
    ) # UpdateRoleParams | Specifies the request body to update a Role.

# example passing only required values which don't have defaults set
try:
	# Update a Role.
	api_response = client.role.update_role(name, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RoleApi->update_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the name of Role to update. |
 **body** | [**UpdateRoleParams**](UpdateRoleParams.md)| Specifies the request body to update a Role. |

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

