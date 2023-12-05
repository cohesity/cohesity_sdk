# cohesity_sdk.ActiveDirectoryApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_active_directory**](ActiveDirectoryApi.md#create_active_directory) | **POST** /active-directories | Create an Active Directory.
[**delete_active_directory**](ActiveDirectoryApi.md#delete_active_directory) | **DELETE** /active-directories/{id} | Delete an Active Directory.
[**get_active_directory**](ActiveDirectoryApi.md#get_active_directory) | **GET** /active-directories | Get the list of Active Directories.
[**get_active_directory_by_id**](ActiveDirectoryApi.md#get_active_directory_by_id) | **GET** /active-directories/{id} | Get an Active Directory by id.
[**get_domain_controllers**](ActiveDirectoryApi.md#get_domain_controllers) | **GET** /domain-controllers | Get Domain Controllers of specified domains.
[**update_active_directory**](ActiveDirectoryApi.md#update_active_directory) | **PUT** /active-directories/{id} | Update an Active Directory.


# **create_active_directory**
> ActiveDirectory create_active_directory(body)

Create an Active Directory.

Create an Active Directory.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.create_active_directory_request import CreateActiveDirectoryRequest
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.active_directory import ActiveDirectory
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

body = CreateActiveDirectoryRequest() # CreateActiveDirectoryRequest | Specifies the parameters to create an Active Directory.

# example passing only required values which don't have defaults set
try:
	# Create an Active Directory.
	api_response = client.active_directory.create_active_directory(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ActiveDirectoryApi->create_active_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateActiveDirectoryRequest**](CreateActiveDirectoryRequest.md)| Specifies the parameters to create an Active Directory. |

### Return type

[**ActiveDirectory**](ActiveDirectory.md)

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

# **delete_active_directory**
> delete_active_directory(id, active_directory_admin_username, active_directory_admin_password)

Delete an Active Directory.

Delete an Active Directory.

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

id = 1 # int | Specifies id of an Active Directory.
active_directory_admin_username = "activeDirectoryAdminUsername_example" # str | Specifies the username of the Active Directory Admin.
active_directory_admin_password = "activeDirectoryAdminPassword_example" # str | Specifies the password of the Active Directory Admin.
force_remove = True # bool | To force delete the Active directory from cluster. This will skip all the checks that prevents cluster from leaving an AD domain. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete an Active Directory.
	client.active_directory.delete_active_directory(id, active_directory_admin_username, active_directory_admin_password)
except ApiException as e:
	print("Exception when calling ActiveDirectoryApi->delete_active_directory: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete an Active Directory.
	client.active_directory.delete_active_directory(id, active_directory_admin_username, active_directory_admin_password, force_remove=force_remove)
except ApiException as e:
	print("Exception when calling ActiveDirectoryApi->delete_active_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of an Active Directory. |
 **active_directory_admin_username** | **str**| Specifies the username of the Active Directory Admin. |
 **active_directory_admin_password** | **str**| Specifies the password of the Active Directory Admin. |
 **force_remove** | **bool**| To force delete the Active directory from cluster. This will skip all the checks that prevents cluster from leaving an AD domain. | [optional]

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

# **get_active_directory**
> ActiveDirectories get_active_directory()

Get the list of Active Directories.

Get the list of Active Directories.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.active_directories import ActiveDirectories
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

domain_names = [
        "CWzyBAw2ZuufUOHOEhA8IcFQXnuaZcdyyvKX7HzKpul80FcVjSkp5IHYCD.y.FZfUofvKERjsmInY9s-EmMH6kw8gsnXv2Z7jRPd.LXGp8ZohR8pb-ziKqEde8fXg9wO.fa2-zRi2iAxU4NCUavTrirUe4ba7JnjrgEdBCJE-ArE6U3CZ-Vnrj9RmauFxv7y.0CjOv6MeuI.nb.pUIQ8yNXhXoEdbZpGptfI4pvLXGuLk-kN.ijcMEEkIauW5ApNaDi5ackLaR2kw9-zmvqRnM-dar09VaHC0.q.c.D42Jml4PJXMbVMO8G0e5q9Z4WMWovY63Gk6ixTd5NxRU25mQYd6VBLRGkQ5b.WH2v5iUaMQ6iIJ-7auxDSR-lIIfhhw9bP3XhsKpT6YkX2ymMVo.u.Px8OyxaBZ75cAiG.hlvrLQxb.H.E.DjhCbEZunVXTqV3VI.z.OzY-c9WhD1h649M9.q.K7NG9dihNlL1YPO1GvRUDnbsR0-SswaNr.w.7NPZw-HNPtVfykpnotMPK4Aqhv7VjToBNn1oLFWRpSx-dyd2clYhZAGia.PPB5iVX1lhmY7Gh2I3pT2SDuv66tyxEBpX6RQusWUzrY2IaluFJfz8Zwxi.YNhQCndVdQ8Zqh8o9Fu3-luW1PzrlptgIbB7lMjnQXJdim087U4e00bXq.E63P2Qk0LGzQ-Q5b8qpf900OPrJ7NsXeu0SeHiClor8kJwu9CQe1tTxWj.9.WObZMXxUrUZPuO24g6xCEEGYs5NZ9BhURG1p1vKPKEsaka3T.uXM15Q-LQUOofFYT6wb4OCgvTgDaAqbKuYuD.TTDCxuHecKtov6lMCwqpGvF10AyNzV.KKNXeFooO85mDfP6.L.T.WUItRxglXsbfmNlQ5dxg25oBYSAJH9pP2AsvJ1ScQkpd0.Yb48VqkgYNMd7LrDcYKGedFO0HBfI81yv9G-D76SNMA.zPPPdI22mRwNS.q.Pp92k53h1KEc7ag0ak9d.wLnPl34V25Jc4YC3rXILhaa6Jcc4hzAqllACM9319wGio4p44OFkGlf.3lbtJZS0AaW9X3CHj-n2hyQAB8SPpfjusH.H.B.Xb-Hj0LrcV6H8x",
    ] # [str] | Filter by a list of Active Directory domain names. (optional)
ids = [
        1,
    ] # [int] | Filter by a list of Active Directory Ids. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which Active Directories are to be returned. (optional)
include_tenants = True # bool | If true, the response will include Active Directories which were created by all tenants which the current user has permission to see. If false, then only Active Directories created by the current user will be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the list of Active Directories.
	api_response = client.active_directory.get_active_directory(domain_names=domain_names, ids=ids, tenant_ids=tenant_ids, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ActiveDirectoryApi->get_active_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_names** | **[str]**| Filter by a list of Active Directory domain names. | [optional]
 **ids** | **[int]**| Filter by a list of Active Directory Ids. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which Active Directories are to be returned. | [optional]
 **include_tenants** | **bool**| If true, the response will include Active Directories which were created by all tenants which the current user has permission to see. If false, then only Active Directories created by the current user will be returned. | [optional]

### Return type

[**ActiveDirectories**](ActiveDirectories.md)

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

# **get_active_directory_by_id**
> ActiveDirectory get_active_directory_by_id(id)

Get an Active Directory by id.

Get an Active Directory by id.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.active_directory import ActiveDirectory
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

id = 1 # int | Specifies id of an Active Directory.
include_centrify_zones = True # bool | Specifies whether to include Centrify Zones of the Active Directory in response. (optional)
include_domain_controllers = True # bool | Specifies whether to include Domain Controllers of the Active Directory in response. (optional)
include_security_principals = True # bool | Specifies whether to include Security Principals of the Active Directory in response. (optional)
prefix = "prefix_example" # str | Specifies a prefix, only security principals with name or sAMAccountName having this prefix (ignoring cases) will be returned. This field is appliciable and mandatory if 'includeSecurityPrincipals' is set to true. (optional)
object_class = [
        "User",
    ] # [str] | Specifies a list of object classes, only security principals with object class in this list will be returned. This field is appliciable if 'includeSecurityPrincipals' is set to true. (optional)

# example passing only required values which don't have defaults set
try:
	# Get an Active Directory by id.
	api_response = client.active_directory.get_active_directory_by_id(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ActiveDirectoryApi->get_active_directory_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get an Active Directory by id.
	api_response = client.active_directory.get_active_directory_by_id(id, include_centrify_zones=include_centrify_zones, include_domain_controllers=include_domain_controllers, include_security_principals=include_security_principals, prefix=prefix, object_class=object_class)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ActiveDirectoryApi->get_active_directory_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of an Active Directory. |
 **include_centrify_zones** | **bool**| Specifies whether to include Centrify Zones of the Active Directory in response. | [optional]
 **include_domain_controllers** | **bool**| Specifies whether to include Domain Controllers of the Active Directory in response. | [optional]
 **include_security_principals** | **bool**| Specifies whether to include Security Principals of the Active Directory in response. | [optional]
 **prefix** | **str**| Specifies a prefix, only security principals with name or sAMAccountName having this prefix (ignoring cases) will be returned. This field is appliciable and mandatory if &#39;includeSecurityPrincipals&#39; is set to true. | [optional]
 **object_class** | **[str]**| Specifies a list of object classes, only security principals with object class in this list will be returned. This field is appliciable if &#39;includeSecurityPrincipals&#39; is set to true. | [optional]

### Return type

[**ActiveDirectory**](ActiveDirectory.md)

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

# **get_domain_controllers**
> DomainControllersResponse get_domain_controllers(domain_names)

Get Domain Controllers of specified domains.

Get Domain Controllers of specified domains.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.domain_controllers_response import DomainControllersResponse
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

domain_names = [
        "CWzyBAw2ZuufUOHOEhA8IcFQXnuaZcdyyvKX7HzKpul80FcVjSkp5IHYCD.y.FZfUofvKERjsmInY9s-EmMH6kw8gsnXv2Z7jRPd.LXGp8ZohR8pb-ziKqEde8fXg9wO.fa2-zRi2iAxU4NCUavTrirUe4ba7JnjrgEdBCJE-ArE6U3CZ-Vnrj9RmauFxv7y.0CjOv6MeuI.nb.pUIQ8yNXhXoEdbZpGptfI4pvLXGuLk-kN.ijcMEEkIauW5ApNaDi5ackLaR2kw9-zmvqRnM-dar09VaHC0.q.c.D42Jml4PJXMbVMO8G0e5q9Z4WMWovY63Gk6ixTd5NxRU25mQYd6VBLRGkQ5b.WH2v5iUaMQ6iIJ-7auxDSR-lIIfhhw9bP3XhsKpT6YkX2ymMVo.u.Px8OyxaBZ75cAiG.hlvrLQxb.H.E.DjhCbEZunVXTqV3VI.z.OzY-c9WhD1h649M9.q.K7NG9dihNlL1YPO1GvRUDnbsR0-SswaNr.w.7NPZw-HNPtVfykpnotMPK4Aqhv7VjToBNn1oLFWRpSx-dyd2clYhZAGia.PPB5iVX1lhmY7Gh2I3pT2SDuv66tyxEBpX6RQusWUzrY2IaluFJfz8Zwxi.YNhQCndVdQ8Zqh8o9Fu3-luW1PzrlptgIbB7lMjnQXJdim087U4e00bXq.E63P2Qk0LGzQ-Q5b8qpf900OPrJ7NsXeu0SeHiClor8kJwu9CQe1tTxWj.9.WObZMXxUrUZPuO24g6xCEEGYs5NZ9BhURG1p1vKPKEsaka3T.uXM15Q-LQUOofFYT6wb4OCgvTgDaAqbKuYuD.TTDCxuHecKtov6lMCwqpGvF10AyNzV.KKNXeFooO85mDfP6.L.T.WUItRxglXsbfmNlQ5dxg25oBYSAJH9pP2AsvJ1ScQkpd0.Yb48VqkgYNMd7LrDcYKGedFO0HBfI81yv9G-D76SNMA.zPPPdI22mRwNS.q.Pp92k53h1KEc7ag0ak9d.wLnPl34V25Jc4YC3rXILhaa6Jcc4hzAqllACM9319wGio4p44OFkGlf.3lbtJZS0AaW9X3CHj-n2hyQAB8SPpfjusH.H.B.Xb-Hj0LrcV6H8x",
    ] # [str] | Specifies a list of domain names.
connection_id = 1 # int, none_type | Specifies the Id of the connection which the connector belongs to. (optional)

# example passing only required values which don't have defaults set
try:
	# Get Domain Controllers of specified domains.
	api_response = client.active_directory.get_domain_controllers(domain_names)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ActiveDirectoryApi->get_domain_controllers: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Domain Controllers of specified domains.
	api_response = client.active_directory.get_domain_controllers(domain_names, connection_id=connection_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ActiveDirectoryApi->get_domain_controllers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_names** | **[str]**| Specifies a list of domain names. |
 **connection_id** | **int, none_type**| Specifies the Id of the connection which the connector belongs to. | [optional]

### Return type

[**DomainControllersResponse**](DomainControllersResponse.md)

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

# **update_active_directory**
> ActiveDirectory update_active_directory(id, body)

Update an Active Directory.

Update an Active Directory.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.update_active_directory_request import UpdateActiveDirectoryRequest
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.active_directory import ActiveDirectory
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

id = 1 # int | Specifies id of an Active Directory.
body = UpdateActiveDirectoryRequest() # UpdateActiveDirectoryRequest | Request to update an Active Directory.

# example passing only required values which don't have defaults set
try:
	# Update an Active Directory.
	api_response = client.active_directory.update_active_directory(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ActiveDirectoryApi->update_active_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies id of an Active Directory. |
 **body** | [**UpdateActiveDirectoryRequest**](UpdateActiveDirectoryRequest.md)| Request to update an Active Directory. |

### Return type

[**ActiveDirectory**](ActiveDirectory.md)

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

