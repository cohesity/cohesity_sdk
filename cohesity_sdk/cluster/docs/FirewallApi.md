# cohesity_sdk.FirewallApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_firewall_profile**](FirewallApi.md#create_firewall_profile) | **POST** /network/firewall/profiles | Create a firewall profile.
[**list_firewall_ip_sets**](FirewallApi.md#list_firewall_ip_sets) | **GET** /network/firewall/ip-sets | List all firewall IP sets
[**list_firewall_profiles**](FirewallApi.md#list_firewall_profiles) | **GET** /network/firewall/profiles | List all firewall profiles.
[**list_firewall_settings**](FirewallApi.md#list_firewall_settings) | **GET** /network/firewall | List all firewall settings.
[**remove_firewall_profile_by_name**](FirewallApi.md#remove_firewall_profile_by_name) | **DELETE** /network/firewall/profiles/{name} | Remove firewall profile.
[**remove_firewall_profiles**](FirewallApi.md#remove_firewall_profiles) | **PUT** /network/firewall/profile/remove | Remove firewall profiles.
[**reset_firewall_profile**](FirewallApi.md#reset_firewall_profile) | **POST** /network/firewall/profiles/reset | Reset firewall profiles.
[**update_firewall_profile**](FirewallApi.md#update_firewall_profile) | **PUT** /network/firewall/profile | Update firewall profiles &amp; their attachments.
[**update_firewall_profile_by_name**](FirewallApi.md#update_firewall_profile_by_name) | **PUT** /network/firewall/profiles/{name} | Update the firewall profile.
[**update_firewall_settings**](FirewallApi.md#update_firewall_settings) | **PUT** /network/firewall | Update firewall settings.


# **create_firewall_profile**
> FirewallProfileParams create_firewall_profile(body)

Create a firewall profile.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Create a firewall profile.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.firewall_profile_params import FirewallProfileParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = FirewallProfileParams(
        action="allow",
        description="description_example",
        direction="INPUT",
        interface_groups=[
            "interface_groups_example",
        ],
        name="name_example",
        ports=[
            "ports_example",
        ],
        subnets=[
            "subnets_example",
        ],
    ) # FirewallProfileParams | Specifies the parameters to configure firewall profiles.

# example passing only required values which don't have defaults set
try:
	# Create a firewall profile.
	api_response = client.firewall.create_firewall_profile(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling FirewallApi->create_firewall_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirewallProfileParams**](FirewallProfileParams.md)| Specifies the parameters to configure firewall profiles. |

### Return type

[**FirewallProfileParams**](FirewallProfileParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_firewall_ip_sets**
> FirewallIPSets list_firewall_ip_sets()

List all firewall IP sets

**Privileges:** ```CLUSTER_VIEW``` <br><br>List all firewall IP sets.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.firewall_ip_sets import FirewallIPSets
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# List all firewall IP sets
	api_response = client.firewall.list_firewall_ip_sets()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling FirewallApi->list_firewall_ip_sets: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**FirewallIPSets**](FirewallIPSets.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_firewall_profiles**
> FirewallProfiles list_firewall_profiles()

List all firewall profiles.

**Privileges:** ```CLUSTER_VIEW``` <br><br>List the firewall profiles & their attachments.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.firewall_profiles import FirewallProfiles
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# List all firewall profiles.
	api_response = client.firewall.list_firewall_profiles()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling FirewallApi->list_firewall_profiles: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**FirewallProfiles**](FirewallProfiles.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_firewall_settings**
> FirewallEntry list_firewall_settings()

List all firewall settings.

**Privileges:** ```CLUSTER_VIEW``` <br><br>List the firewall settings available in the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.firewall_entry import FirewallEntry
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# List all firewall settings.
	api_response = client.firewall.list_firewall_settings()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling FirewallApi->list_firewall_settings: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**FirewallEntry**](FirewallEntry.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_firewall_profile_by_name**
> remove_firewall_profile_by_name(name)

Remove firewall profile.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Remove firewall profile.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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


name = "name_example" # str | Specifies the name of the profile.

# example passing only required values which don't have defaults set
try:
	# Remove firewall profile.
	client.firewall.remove_firewall_profile_by_name(name)
except ApiException as e:
	print("Exception when calling FirewallApi->remove_firewall_profile_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the name of the profile. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_firewall_profiles**
> SuccessResp remove_firewall_profiles(body)

Remove firewall profiles.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Remove firewall profiles and their attachments - deprecated - use delete /network/firewall/profiles/{name}

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.success_resp import SuccessResp
from cohesity_sdk.cluster.model.firewall_profile_names_params import FirewallProfileNamesParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = FirewallProfileNamesParams(
        names=[
            "names_example",
        ],
    ) # FirewallProfileNamesParams | Specifies the parameters to remove firewall profiles and their attachments.

# example passing only required values which don't have defaults set
try:
	# Remove firewall profiles.
	api_response = client.firewall.remove_firewall_profiles(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling FirewallApi->remove_firewall_profiles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirewallProfileNamesParams**](FirewallProfileNamesParams.md)| Specifies the parameters to remove firewall profiles and their attachments. |

### Return type

[**SuccessResp**](SuccessResp.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_firewall_profile**
> reset_firewall_profile()

Reset firewall profiles.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Reset firewall profiles, ip-sets & their attachments.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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



# example, this endpoint has no required or optional parameters
try:
	# Reset firewall profiles.
	client.firewall.reset_firewall_profile()
except ApiException as e:
	print("Exception when calling FirewallApi->reset_firewall_profile: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_firewall_profile**
> FirewallProfileParams update_firewall_profile(body)

Update firewall profiles & their attachments.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update the firewall profiles and/or their attachments  - deprecated - use put /network/firewall/profiles/{name}

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.firewall_profile_params import FirewallProfileParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = FirewallProfileParams(
        action="allow",
        description="description_example",
        direction="INPUT",
        interface_groups=[
            "interface_groups_example",
        ],
        name="name_example",
        ports=[
            "ports_example",
        ],
        subnets=[
            "subnets_example",
        ],
    ) # FirewallProfileParams | Specifies the parameters to configure firewall profiles and/or their attachments.

# example passing only required values which don't have defaults set
try:
	# Update firewall profiles & their attachments.
	api_response = client.firewall.update_firewall_profile(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling FirewallApi->update_firewall_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirewallProfileParams**](FirewallProfileParams.md)| Specifies the parameters to configure firewall profiles and/or their attachments. |

### Return type

[**FirewallProfileParams**](FirewallProfileParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_firewall_profile_by_name**
> FirewallProfileParams update_firewall_profile_by_name(name, body)

Update the firewall profile.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update the firewall profile.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.firewall_profile_params import FirewallProfileParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


name = "name_example" # str | Specifies the name of the profile.
body = FirewallProfileParams(
        action="allow",
        description="description_example",
        direction="INPUT",
        interface_groups=[
            "interface_groups_example",
        ],
        name="name_example",
        ports=[
            "ports_example",
        ],
        subnets=[
            "subnets_example",
        ],
    ) # FirewallProfileParams | Specifies the parameters to configure firewall profiles.

# example passing only required values which don't have defaults set
try:
	# Update the firewall profile.
	api_response = client.firewall.update_firewall_profile_by_name(name, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling FirewallApi->update_firewall_profile_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the name of the profile. |
 **body** | [**FirewallProfileParams**](FirewallProfileParams.md)| Specifies the parameters to configure firewall profiles. |

### Return type

[**FirewallProfileParams**](FirewallProfileParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_firewall_settings**
> FirewallEntry update_firewall_settings(body)

Update firewall settings.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update the firewall settings available in the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.firewall_entry import FirewallEntry
from cohesity_sdk.cluster.model.update_firewall_request import UpdateFirewallRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = UpdateFirewallRequest(
        entry=FirewallEntry(
            attachments=[
                Attachment(
                    action="allow",
                    description="description_example",
                    interface_groups=[
                        "interface_groups_example",
                    ],
                    interfaces=[
                        "interfaces_example",
                    ],
                    ipset_names=[
                        "ipset_names_example",
                    ],
                    profile="profile_example",
                    subnets=[
                        "subnets_example",
                    ],
                ),
            ],
            ipsets=[
                FirewallIPSet(
                    name="name_example",
                    subnets=[
                        "subnets_example",
                    ],
                ),
            ],
            profiles=[
                FirewallProfile(
                    directions=[
                        "INPUT",
                    ],
                    name="name_example",
                    ports=[
                        "ports_example",
                    ],
                ),
            ],
        ),
        update_attachment=False,
        update_ipset=False,
        update_profile=False,
    ) # UpdateFirewallRequest | Specifies the parameters to configure firewall settings.

# example passing only required values which don't have defaults set
try:
	# Update firewall settings.
	api_response = client.firewall.update_firewall_settings(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling FirewallApi->update_firewall_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateFirewallRequest**](UpdateFirewallRequest.md)| Specifies the parameters to configure firewall settings. |

### Return type

[**FirewallEntry**](FirewallEntry.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

