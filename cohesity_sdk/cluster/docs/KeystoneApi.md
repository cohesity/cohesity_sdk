# cohesity_sdk.KeystoneApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_keystone**](KeystoneApi.md#create_keystone) | **POST** /keystones | Create a Keystone configuration.
[**delete_keystone**](KeystoneApi.md#delete_keystone) | **DELETE** /keystones/{id} | Delete a Keystone configuration.
[**get_keystones**](KeystoneApi.md#get_keystones) | **GET** /keystones | Get Keystones.
[**get_keystones_by_id**](KeystoneApi.md#get_keystones_by_id) | **GET** /keystones/{id} | Get a Keystone by its id.
[**update_keystone**](KeystoneApi.md#update_keystone) | **PUT** /keystones/{id} | Update a Keystone configuration.


# **create_keystone**
> Keystone create_keystone(body)

Create a Keystone configuration.

Create a Keystone configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.keystone import Keystone
from cohesity_sdk.cluster.model.create_keystone_request import CreateKeystoneRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateKeystoneRequest() # CreateKeystoneRequest | Specifies the paremters to create a Keystone configuration.

# example passing only required values which don't have defaults set
try:
	# Create a Keystone configuration.
	api_response = client.keystone.create_keystone(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling KeystoneApi->create_keystone: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateKeystoneRequest**](CreateKeystoneRequest.md)| Specifies the paremters to create a Keystone configuration. |

### Return type

[**Keystone**](Keystone.md)

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

# **delete_keystone**
> delete_keystone(id, admin_password)

Delete a Keystone configuration.

Delete a Keystone configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the Keystone id.
admin_password = "adminPassword_example" # str | Specifies the password of Keystone administrator.

# example passing only required values which don't have defaults set
try:
	# Delete a Keystone configuration.
	client.keystone.delete_keystone(id, admin_password)
except ApiException as e:
	print("Exception when calling KeystoneApi->delete_keystone: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the Keystone id. |
 **admin_password** | **str**| Specifies the password of Keystone administrator. |

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

# **get_keystones**
> Keystones get_keystones()

Get Keystones.

Get Keystones.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.keystones import Keystones
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


names = [
        "names_example",
    ] # [str] | Specifies a list of Keystone names. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
include_tenants = True # bool | If true, the response will include Keystones which were created by all tenants which the current user has permission to see. If false, then only Keystones created by the current user will be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Keystones.
	api_response = client.keystone.get_keystones(names=names, tenant_ids=tenant_ids, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling KeystoneApi->get_keystones: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **[str]**| Specifies a list of Keystone names. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which objects are to be returned. | [optional]
 **include_tenants** | **bool**| If true, the response will include Keystones which were created by all tenants which the current user has permission to see. If false, then only Keystones created by the current user will be returned. | [optional]

### Return type

[**Keystones**](Keystones.md)

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

# **get_keystones_by_id**
> Keystone get_keystones_by_id(id)

Get a Keystone by its id.

Get a Keystone by its id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.keystone import Keystone
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the Keystone id.

# example passing only required values which don't have defaults set
try:
	# Get a Keystone by its id.
	api_response = client.keystone.get_keystones_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling KeystoneApi->get_keystones_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the Keystone id. |

### Return type

[**Keystone**](Keystone.md)

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

# **update_keystone**
> Keystone update_keystone(id, body)

Update a Keystone configuration.

Update a Keystone configuration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.keystone import Keystone
from cohesity_sdk.cluster.model.update_keystone_request import UpdateKeystoneRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the Keystone id.
body = UpdateKeystoneRequest() # UpdateKeystoneRequest | Specifies the paremters to update a Keystone configuration.

# example passing only required values which don't have defaults set
try:
	# Update a Keystone configuration.
	api_response = client.keystone.update_keystone(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling KeystoneApi->update_keystone: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the Keystone id. |
 **body** | [**UpdateKeystoneRequest**](UpdateKeystoneRequest.md)| Specifies the paremters to update a Keystone configuration. |

### Return type

[**Keystone**](Keystone.md)

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

