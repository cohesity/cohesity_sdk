# cohesity_sdk.ActiveDirectoryApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**add_active_directory_principals**](ActiveDirectoryApi.md#add_active_directory_principals) | **POST** /active-directory-principals | Add multiple groups or users on the Cohesity Cluster for the specified Active Directory principals. In addition, assign Cohesity roles to the users or groups to define their Cohesity privileges.
[**create_active_directory**](ActiveDirectoryApi.md#create_active_directory) | **POST** /active-directories | Create an Active Directory.
[**delete_active_directory**](ActiveDirectoryApi.md#delete_active_directory) | **DELETE** /active-directories/{id} | Delete an Active Directory.
[**get_active_directory**](ActiveDirectoryApi.md#get_active_directory) | **GET** /active-directories | Get the list of Active Directories.
[**get_active_directory_by_id**](ActiveDirectoryApi.md#get_active_directory_by_id) | **GET** /active-directories/{id} | Get an Active Directory by id.
[**get_active_directory_principals**](ActiveDirectoryApi.md#get_active_directory_principals) | **GET** /active-directory-principals | Get the list of user and group principals from the Active Directory that match the specified filter criteria.
[**get_centrify_zones**](ActiveDirectoryApi.md#get_centrify_zones) | **GET** /centrify-zones | Get Centrify Zones.
[**get_domain_controllers**](ActiveDirectoryApi.md#get_domain_controllers) | **GET** /domain-controllers | Get Domain Controllers of specified domains.
[**get_trusted_domains**](ActiveDirectoryApi.md#get_trusted_domains) | **GET** /trusted-domains | Get Trusted Domains.
[**trigger_trusted_domains_discovery**](ActiveDirectoryApi.md#trigger_trusted_domains_discovery) | **PUT** /trusted-domains | Rediscover trusted domains.
[**update_active_directory**](ActiveDirectoryApi.md#update_active_directory) | **PUT** /active-directories/{id} | Update an Active Directory.
[**update_trusted_domains**](ActiveDirectoryApi.md#update_trusted_domains) | **POST** /trusted-domains | Update trusted domains.


# **add_active_directory_principals**
> [AddedActiveDirectoryPrincipal] add_active_directory_principals(body)

Add multiple groups or users on the Cohesity Cluster for the specified Active Directory principals. In addition, assign Cohesity roles to the users or groups to define their Cohesity privileges.

After a group or user has been added to a Cohesity Cluster, the referenced Active Directory principal can be used by the Cohesity Cluster. In addition, this operation maps Cohesity roles with a group or user and this mapping defines the privileges allowed on the Cohesity Cluster for the group or user. For example if an 'management' group is created on the Cohesity Cluster for the Active Directory 'management' principal group and is associated with the Cohesity 'View' role, all users in the referenced Active Directory 'management' principal group can log in to the Cohesity Dashboard but will only have view-only privileges. These users cannot create new Protection Jobs, Policies, Views, etc. NOTE: Local Cohesity users and groups cannot be created by this operation. Local Cohesity users or groups do not have an associated Active Directory principals and are created directly in the default LOCAL domain.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.added_active_directory_principal import AddedActiveDirectoryPrincipal
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.add_active_directory_principals_parameters import AddActiveDirectoryPrincipalsParameters
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = [
        AddActiveDirectoryPrincipalsParameters(
            description="description_example",
            domain_name="CAMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJykO4IVP7YNsKQHh9BsD.y.Fo3_QLOpkBmKIPOf2Flbsh1TpRS00PDvgoKGNXd.LoPJE-_eVrdJNcY9CLxYxBbcfSO.fGSCF7dC-lSY-7ZlQJLW1_GNchKk5EBLDz1ctzsIY4oIgcl12VtuaSfjvmymTJy.0c17VJpcqI.nb.p6lFYtIUw23vATP5cgpgctxW3q4fsZS5N.ivg2bA4mI-r1orbd3s4Kdu4Q19mfvL0A7Rpn3Av26g7OJWs0.q.c.DCuuRrMkJf5gzLvv2wYTNPqhvoybcy8QU60_1u6BhIo-27B5JIFoxlv9-BJb.WelW6lINX6D1Elv8Z4qYvYNwb3t4awGG-6yh0-gMEzQ8uhi90o.u.Ps5LWBoOt62fDnG.hM59JJWb.H.E.DpwFCTpIA0Gnqa9PI.z.OR3UYpt1vrS1pQR9.q.KfgrgcyvfHmHL7bSaRv9kZ_KaNGkIi19r.w.7x8qCkWG3nkJgXYUf-2g1bLoF4Q2SDvsQvki_Gvu3xSglBiD_kTqWft7a.Pq8DkTxH9-GEgnhdskTUa-JGB99tBTH1m8LyVjqKCRWp6XS1rwkzrnn4hi.Y7cYVKPWx4kXAhG_GEdV9fi1LUY2eBXIK-aaNx-IAoUxtYKQpsS2HM0cq.E88aJmQRbOi5pM9K4SWNKj0UeVyhnBjVWguY2vNQIw3D_aRMF2Tm7Selj.9.WLRs2IImu0zJ-sEvqrLoPmgi4JrQNmT_4QLVs0oSHjB6pC-T.uXNIZ-mK8w9K1xfp9OikxJ6eiOUAchnVGrwD.TWHJ7Z1SeTeQr7h2GhDiufc8pTDOUV.KwyEct13aGy9ShD6.L.T.WuS1qDT5br69Zb9J7ztaciXoL3UMxQsS4RhgPVNkMuBN0.Y_vT6kENTnbd0jYevK4Igno2LdfSDI1Cs6huybGb1zA.zcz_sYPOWoI5S.q.PLcYufJVmh2PNuin04Qd.wjetJ2wYXno2W6zwIrDKlbs9CPExuzXJjOmov9hu5QjJ_xMDMiy-rwf.3gfVA0tbOL0WzdgU9sGpVxk-V0XsgBCaMH.H.B.X2AHCmB9lVwewx",
            name="name_example",
            object_class="User",
            restricted=True,
            roles=[
                "roles_example",
            ],
        ),
    ] # [AddActiveDirectoryPrincipalsParameters] | 

# example passing only required values which don't have defaults set
try:
	# Add multiple groups or users on the Cohesity Cluster for the specified Active Directory principals. In addition, assign Cohesity roles to the users or groups to define their Cohesity privileges.
	api_response = client.active_directory.add_active_directory_principals(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ActiveDirectoryApi->add_active_directory_principals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[AddActiveDirectoryPrincipalsParameters]**](AddActiveDirectoryPrincipalsParameters.md)|  |

### Return type

[**[AddedActiveDirectoryPrincipal]**](AddedActiveDirectoryPrincipal.md)

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

# **create_active_directory**
> ActiveDirectory create_active_directory(body)

Create an Active Directory.

Create an Active Directory.

### Example

* Api Key Authentication (APIKeyHeader):
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

# **delete_active_directory**
> delete_active_directory(id, active_directory_admin_username, active_directory_admin_password)

Delete an Active Directory.

Delete an Active Directory.

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

# **get_active_directory**
> ActiveDirectories get_active_directory()

Get the list of Active Directories.

Get the list of Active Directories.

### Example

* Api Key Authentication (APIKeyHeader):
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
        "CAMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJykO4IVP7YNsKQHh9BsD.y.Fo3_QLOpkBmKIPOf2Flbsh1TpRS00PDvgoKGNXd.LoPJE-_eVrdJNcY9CLxYxBbcfSO.fGSCF7dC-lSY-7ZlQJLW1_GNchKk5EBLDz1ctzsIY4oIgcl12VtuaSfjvmymTJy.0c17VJpcqI.nb.p6lFYtIUw23vATP5cgpgctxW3q4fsZS5N.ivg2bA4mI-r1orbd3s4Kdu4Q19mfvL0A7Rpn3Av26g7OJWs0.q.c.DCuuRrMkJf5gzLvv2wYTNPqhvoybcy8QU60_1u6BhIo-27B5JIFoxlv9-BJb.WelW6lINX6D1Elv8Z4qYvYNwb3t4awGG-6yh0-gMEzQ8uhi90o.u.Ps5LWBoOt62fDnG.hM59JJWb.H.E.DpwFCTpIA0Gnqa9PI.z.OR3UYpt1vrS1pQR9.q.KfgrgcyvfHmHL7bSaRv9kZ_KaNGkIi19r.w.7x8qCkWG3nkJgXYUf-2g1bLoF4Q2SDvsQvki_Gvu3xSglBiD_kTqWft7a.Pq8DkTxH9-GEgnhdskTUa-JGB99tBTH1m8LyVjqKCRWp6XS1rwkzrnn4hi.Y7cYVKPWx4kXAhG_GEdV9fi1LUY2eBXIK-aaNx-IAoUxtYKQpsS2HM0cq.E88aJmQRbOi5pM9K4SWNKj0UeVyhnBjVWguY2vNQIw3D_aRMF2Tm7Selj.9.WLRs2IImu0zJ-sEvqrLoPmgi4JrQNmT_4QLVs0oSHjB6pC-T.uXNIZ-mK8w9K1xfp9OikxJ6eiOUAchnVGrwD.TWHJ7Z1SeTeQr7h2GhDiufc8pTDOUV.KwyEct13aGy9ShD6.L.T.WuS1qDT5br69Zb9J7ztaciXoL3UMxQsS4RhgPVNkMuBN0.Y_vT6kENTnbd0jYevK4Igno2LdfSDI1Cs6huybGb1zA.zcz_sYPOWoI5S.q.PLcYufJVmh2PNuin04Qd.wjetJ2wYXno2W6zwIrDKlbs9CPExuzXJjOmov9hu5QjJ_xMDMiy-rwf.3gfVA0tbOL0WzdgU9sGpVxk-V0XsgBCaMH.H.B.X2AHCmB9lVwewx",
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

# **get_active_directory_by_id**
> ActiveDirectory get_active_directory_by_id(id)

Get an Active Directory by id.

Get an Active Directory by id.

### Example

* Api Key Authentication (APIKeyHeader):
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

# **get_active_directory_principals**
> ActiveDirectoryPrincipals get_active_directory_principals()

Get the list of user and group principals from the Active Directory that match the specified filter criteria.

Get the list of user and group principals from the Active Directory that match the specified filter criteria.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.active_directory_principals import ActiveDirectoryPrincipals
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


domain_name = "CAMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJykO4IVP7YNsKQHh9BsD.y.Fo3_QLOpkBmKIPOf2Flbsh1TpRS00PDvgoKGNXd.LoPJE-_eVrdJNcY9CLxYxBbcfSO.fGSCF7dC-lSY-7ZlQJLW1_GNchKk5EBLDz1ctzsIY4oIgcl12VtuaSfjvmymTJy.0c17VJpcqI.nb.p6lFYtIUw23vATP5cgpgctxW3q4fsZS5N.ivg2bA4mI-r1orbd3s4Kdu4Q19mfvL0A7Rpn3Av26g7OJWs0.q.c.DCuuRrMkJf5gzLvv2wYTNPqhvoybcy8QU60_1u6BhIo-27B5JIFoxlv9-BJb.WelW6lINX6D1Elv8Z4qYvYNwb3t4awGG-6yh0-gMEzQ8uhi90o.u.Ps5LWBoOt62fDnG.hM59JJWb.H.E.DpwFCTpIA0Gnqa9PI.z.OR3UYpt1vrS1pQR9.q.KfgrgcyvfHmHL7bSaRv9kZ_KaNGkIi19r.w.7x8qCkWG3nkJgXYUf-2g1bLoF4Q2SDvsQvki_Gvu3xSglBiD_kTqWft7a.Pq8DkTxH9-GEgnhdskTUa-JGB99tBTH1m8LyVjqKCRWp6XS1rwkzrnn4hi.Y7cYVKPWx4kXAhG_GEdV9fi1LUY2eBXIK-aaNx-IAoUxtYKQpsS2HM0cq.E88aJmQRbOi5pM9K4SWNKj0UeVyhnBjVWguY2vNQIw3D_aRMF2Tm7Selj.9.WLRs2IImu0zJ-sEvqrLoPmgi4JrQNmT_4QLVs0oSHjB6pC-T.uXNIZ-mK8w9K1xfp9OikxJ6eiOUAchnVGrwD.TWHJ7Z1SeTeQr7h2GhDiufc8pTDOUV.KwyEct13aGy9ShD6.L.T.WuS1qDT5br69Zb9J7ztaciXoL3UMxQsS4RhgPVNkMuBN0.Y_vT6kENTnbd0jYevK4Igno2LdfSDI1Cs6huybGb1zA.zcz_sYPOWoI5S.q.PLcYufJVmh2PNuin04Qd.wjetJ2wYXno2W6zwIrDKlbs9CPExuzXJjOmov9hu5QjJ_xMDMiy-rwf.3gfVA0tbOL0WzdgU9sGpVxk-V0XsgBCaMH.H.B.X2AHCmB9lVwewx" # str | Specifies the domain name of the principals to search. If specified the principals in that domain are searched. Domain could be an Active Directory domain joined by the Cluster or any one of the trusted domains of the Active Directory domain or the LOCAL domain. If not specified, all the domains are searched. (optional)
sids = [
        "sids_example",
    ] # [str] | Optionally filter by a list of security identifiers (SIDs) found in the specified domain. Only principals matching the specified SIDs are returned. If specified, a 'searchTerm' parameter should not be specified. Note: Duplicate SIDs will be ignored. (optional)
search_term = "searchTerm_example" # str | Optionally filter by matching a substring. Only principals with a name or sAMAccountName that matches part or all of the specified substring are returned. If specified, a 'sids' parameter should not be specified (optional)
include_computers = True # bool | Specifies if Computer/GMSA accounts need to be included in this search. (optional)
include_service_accounts = True # bool | Specifies if service accounts should be included in the search result. (optional)
object_class = "User" # str | Specifies the type of principal, a user or a group. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the list of user and group principals from the Active Directory that match the specified filter criteria.
	api_response = client.active_directory.get_active_directory_principals(domain_name=domain_name, sids=sids, search_term=search_term, include_computers=include_computers, include_service_accounts=include_service_accounts, object_class=object_class)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ActiveDirectoryApi->get_active_directory_principals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| Specifies the domain name of the principals to search. If specified the principals in that domain are searched. Domain could be an Active Directory domain joined by the Cluster or any one of the trusted domains of the Active Directory domain or the LOCAL domain. If not specified, all the domains are searched. | [optional]
 **sids** | **[str]**| Optionally filter by a list of security identifiers (SIDs) found in the specified domain. Only principals matching the specified SIDs are returned. If specified, a &#39;searchTerm&#39; parameter should not be specified. Note: Duplicate SIDs will be ignored. | [optional]
 **search_term** | **str**| Optionally filter by matching a substring. Only principals with a name or sAMAccountName that matches part or all of the specified substring are returned. If specified, a &#39;sids&#39; parameter should not be specified | [optional]
 **include_computers** | **bool**| Specifies if Computer/GMSA accounts need to be included in this search. | [optional]
 **include_service_accounts** | **bool**| Specifies if service accounts should be included in the search result. | [optional]
 **object_class** | **str**| Specifies the type of principal, a user or a group. | [optional]

### Return type

[**ActiveDirectoryPrincipals**](ActiveDirectoryPrincipals.md)

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

# **get_centrify_zones**
> CentrifyZones get_centrify_zones(domain_name)

Get Centrify Zones.

Get Centrify zones for a specified domain.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.centrify_zones import CentrifyZones
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


domain_name = "CAMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJykO4IVP7YNsKQHh9BsD.y.Fo3_QLOpkBmKIPOf2Flbsh1TpRS00PDvgoKGNXd.LoPJE-_eVrdJNcY9CLxYxBbcfSO.fGSCF7dC-lSY-7ZlQJLW1_GNchKk5EBLDz1ctzsIY4oIgcl12VtuaSfjvmymTJy.0c17VJpcqI.nb.p6lFYtIUw23vATP5cgpgctxW3q4fsZS5N.ivg2bA4mI-r1orbd3s4Kdu4Q19mfvL0A7Rpn3Av26g7OJWs0.q.c.DCuuRrMkJf5gzLvv2wYTNPqhvoybcy8QU60_1u6BhIo-27B5JIFoxlv9-BJb.WelW6lINX6D1Elv8Z4qYvYNwb3t4awGG-6yh0-gMEzQ8uhi90o.u.Ps5LWBoOt62fDnG.hM59JJWb.H.E.DpwFCTpIA0Gnqa9PI.z.OR3UYpt1vrS1pQR9.q.KfgrgcyvfHmHL7bSaRv9kZ_KaNGkIi19r.w.7x8qCkWG3nkJgXYUf-2g1bLoF4Q2SDvsQvki_Gvu3xSglBiD_kTqWft7a.Pq8DkTxH9-GEgnhdskTUa-JGB99tBTH1m8LyVjqKCRWp6XS1rwkzrnn4hi.Y7cYVKPWx4kXAhG_GEdV9fi1LUY2eBXIK-aaNx-IAoUxtYKQpsS2HM0cq.E88aJmQRbOi5pM9K4SWNKj0UeVyhnBjVWguY2vNQIw3D_aRMF2Tm7Selj.9.WLRs2IImu0zJ-sEvqrLoPmgi4JrQNmT_4QLVs0oSHjB6pC-T.uXNIZ-mK8w9K1xfp9OikxJ6eiOUAchnVGrwD.TWHJ7Z1SeTeQr7h2GhDiufc8pTDOUV.KwyEct13aGy9ShD6.L.T.WuS1qDT5br69Zb9J7ztaciXoL3UMxQsS4RhgPVNkMuBN0.Y_vT6kENTnbd0jYevK4Igno2LdfSDI1Cs6huybGb1zA.zcz_sYPOWoI5S.q.PLcYufJVmh2PNuin04Qd.wjetJ2wYXno2W6zwIrDKlbs9CPExuzXJjOmov9hu5QjJ_xMDMiy-rwf.3gfVA0tbOL0WzdgU9sGpVxk-V0XsgBCaMH.H.B.X2AHCmB9lVwewx" # str | Specifies the FQDN of the domain name.

# example passing only required values which don't have defaults set
try:
	# Get Centrify Zones.
	api_response = client.active_directory.get_centrify_zones(domain_name)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ActiveDirectoryApi->get_centrify_zones: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| Specifies the FQDN of the domain name. |

### Return type

[**CentrifyZones**](CentrifyZones.md)

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

# **get_domain_controllers**
> DomainControllersResponse get_domain_controllers(domain_names)

Get Domain Controllers of specified domains.

Get Domain Controllers of specified domains.

### Example

* Api Key Authentication (APIKeyHeader):
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
        "CAMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJykO4IVP7YNsKQHh9BsD.y.Fo3_QLOpkBmKIPOf2Flbsh1TpRS00PDvgoKGNXd.LoPJE-_eVrdJNcY9CLxYxBbcfSO.fGSCF7dC-lSY-7ZlQJLW1_GNchKk5EBLDz1ctzsIY4oIgcl12VtuaSfjvmymTJy.0c17VJpcqI.nb.p6lFYtIUw23vATP5cgpgctxW3q4fsZS5N.ivg2bA4mI-r1orbd3s4Kdu4Q19mfvL0A7Rpn3Av26g7OJWs0.q.c.DCuuRrMkJf5gzLvv2wYTNPqhvoybcy8QU60_1u6BhIo-27B5JIFoxlv9-BJb.WelW6lINX6D1Elv8Z4qYvYNwb3t4awGG-6yh0-gMEzQ8uhi90o.u.Ps5LWBoOt62fDnG.hM59JJWb.H.E.DpwFCTpIA0Gnqa9PI.z.OR3UYpt1vrS1pQR9.q.KfgrgcyvfHmHL7bSaRv9kZ_KaNGkIi19r.w.7x8qCkWG3nkJgXYUf-2g1bLoF4Q2SDvsQvki_Gvu3xSglBiD_kTqWft7a.Pq8DkTxH9-GEgnhdskTUa-JGB99tBTH1m8LyVjqKCRWp6XS1rwkzrnn4hi.Y7cYVKPWx4kXAhG_GEdV9fi1LUY2eBXIK-aaNx-IAoUxtYKQpsS2HM0cq.E88aJmQRbOi5pM9K4SWNKj0UeVyhnBjVWguY2vNQIw3D_aRMF2Tm7Selj.9.WLRs2IImu0zJ-sEvqrLoPmgi4JrQNmT_4QLVs0oSHjB6pC-T.uXNIZ-mK8w9K1xfp9OikxJ6eiOUAchnVGrwD.TWHJ7Z1SeTeQr7h2GhDiufc8pTDOUV.KwyEct13aGy9ShD6.L.T.WuS1qDT5br69Zb9J7ztaciXoL3UMxQsS4RhgPVNkMuBN0.Y_vT6kENTnbd0jYevK4Igno2LdfSDI1Cs6huybGb1zA.zcz_sYPOWoI5S.q.PLcYufJVmh2PNuin04Qd.wjetJ2wYXno2W6zwIrDKlbs9CPExuzXJjOmov9hu5QjJ_xMDMiy-rwf.3gfVA0tbOL0WzdgU9sGpVxk-V0XsgBCaMH.H.B.X2AHCmB9lVwewx",
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

# **get_trusted_domains**
> TrustedDomainParams get_trusted_domains(domain_name)

Get Trusted Domains.

Get Trusted Domains for a specified domain.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.trusted_domain_params import TrustedDomainParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


domain_name = "domainName_example" # str | Specifies the FQDN of an Active directory domain.

# example passing only required values which don't have defaults set
try:
	# Get Trusted Domains.
	api_response = client.active_directory.get_trusted_domains(domain_name)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ActiveDirectoryApi->get_trusted_domains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| Specifies the FQDN of an Active directory domain. |

### Return type

[**TrustedDomainParams**](TrustedDomainParams.md)

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

# **trigger_trusted_domains_discovery**
> trigger_trusted_domains_discovery(domain_name, rediscover)

Rediscover trusted domains.

Re-trigger the trusted domains of an Active Directory.

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


domain_name = "domainName_example" # str | Specifies the FQDN of an Active directory domain.
rediscover = True # bool | Specifies if trusted domains should be rediscovered.

# example passing only required values which don't have defaults set
try:
	# Rediscover trusted domains.
	client.active_directory.trigger_trusted_domains_discovery(domain_name, rediscover)
except ApiException as e:
	print("Exception when calling ActiveDirectoryApi->trigger_trusted_domains_discovery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| Specifies the FQDN of an Active directory domain. |
 **rediscover** | **bool**| Specifies if trusted domains should be rediscovered. |

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
**202** | Request Accepted |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_active_directory**
> ActiveDirectory update_active_directory(id, body)

Update an Active Directory.

Update an Active Directory.

### Example

* Api Key Authentication (APIKeyHeader):
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

# **update_trusted_domains**
> TrustedDomainParams update_trusted_domains(domain_name, body)

Update trusted domains.

To update trusted domains of an Active Directory.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.trusted_domain_params import TrustedDomainParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


domain_name = "domainName_example" # str, none_type | Specifies the FQDN of an Active directory domain.
body = TrustedDomainParams(
        blacklisted_domains=[
            "blacklisted_domains_example",
        ],
        enabled=True,
        only_use_whitelisted_domains=True,
        trusted_domains=[
            TrustedDomain(
                domain_controllers_deny_list=[
                    "domain_controllers_deny_list_example",
                ],
                domain_name="domain_name_example",
                preferred_domain_controllers=[
                    DomainController(
                        name="name_example",
                    ),
                ],
            ),
        ],
        whitelisted_domains=[
            "CAMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJykO4IVP7YNsKQHh9BsD.y.Fo3_QLOpkBmKIPOf2Flbsh1TpRS00PDvgoKGNXd.LoPJE-_eVrdJNcY9CLxYxBbcfSO.fGSCF7dC-lSY-7ZlQJLW1_GNchKk5EBLDz1ctzsIY4oIgcl12VtuaSfjvmymTJy.0c17VJpcqI.nb.p6lFYtIUw23vATP5cgpgctxW3q4fsZS5N.ivg2bA4mI-r1orbd3s4Kdu4Q19mfvL0A7Rpn3Av26g7OJWs0.q.c.DCuuRrMkJf5gzLvv2wYTNPqhvoybcy8QU60_1u6BhIo-27B5JIFoxlv9-BJb.WelW6lINX6D1Elv8Z4qYvYNwb3t4awGG-6yh0-gMEzQ8uhi90o.u.Ps5LWBoOt62fDnG.hM59JJWb.H.E.DpwFCTpIA0Gnqa9PI.z.OR3UYpt1vrS1pQR9.q.KfgrgcyvfHmHL7bSaRv9kZ_KaNGkIi19r.w.7x8qCkWG3nkJgXYUf-2g1bLoF4Q2SDvsQvki_Gvu3xSglBiD_kTqWft7a.Pq8DkTxH9-GEgnhdskTUa-JGB99tBTH1m8LyVjqKCRWp6XS1rwkzrnn4hi.Y7cYVKPWx4kXAhG_GEdV9fi1LUY2eBXIK-aaNx-IAoUxtYKQpsS2HM0cq.E88aJmQRbOi5pM9K4SWNKj0UeVyhnBjVWguY2vNQIw3D_aRMF2Tm7Selj.9.WLRs2IImu0zJ-sEvqrLoPmgi4JrQNmT_4QLVs0oSHjB6pC-T.uXNIZ-mK8w9K1xfp9OikxJ6eiOUAchnVGrwD.TWHJ7Z1SeTeQr7h2GhDiufc8pTDOUV.KwyEct13aGy9ShD6.L.T.WuS1qDT5br69Zb9J7ztaciXoL3UMxQsS4RhgPVNkMuBN0.Y_vT6kENTnbd0jYevK4Igno2LdfSDI1Cs6huybGb1zA.zcz_sYPOWoI5S.q.PLcYufJVmh2PNuin04Qd.wjetJ2wYXno2W6zwIrDKlbs9CPExuzXJjOmov9hu5QjJ_xMDMiy-rwf.3gfVA0tbOL0WzdgU9sGpVxk-V0XsgBCaMH.H.B.X2AHCmB9lVwewx",
        ],
    ) # TrustedDomainParams | Specifies the trusted domains params.

# example passing only required values which don't have defaults set
try:
	# Update trusted domains.
	api_response = client.active_directory.update_trusted_domains(domain_name, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ActiveDirectoryApi->update_trusted_domains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str, none_type**| Specifies the FQDN of an Active directory domain. |
 **body** | [**TrustedDomainParams**](TrustedDomainParams.md)| Specifies the trusted domains params. |

### Return type

[**TrustedDomainParams**](TrustedDomainParams.md)

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

