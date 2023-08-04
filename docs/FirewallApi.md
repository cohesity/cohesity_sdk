# cohesity_sdk.FirewallApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**list_firewall_ip_sets**](FirewallApi.md#list_firewall_ip_sets) | **GET** /network/firewall/ip-sets | List all firewall IP sets
[**list_firewall_profiles**](FirewallApi.md#list_firewall_profiles) | **GET** /network/firewall/profiles | List all firewall profiles.
[**remove_firewall_profiles**](FirewallApi.md#remove_firewall_profiles) | **PUT** /network/firewall/profile/remove | Remove firewall profiles.
[**reset_firewall_profile**](FirewallApi.md#reset_firewall_profile) | **POST** /network/firewall/profiles/reset | Reset firewall profiles.
[**update_firewall_ip_sets**](FirewallApi.md#update_firewall_ip_sets) | **PUT** /network/firewall/ip-sets | Update firewall IP sets
[**update_firewall_profile**](FirewallApi.md#update_firewall_profile) | **PUT** /network/firewall/profile | Update firewall profiles &amp; their attachments.
[**update_firewall_profiles**](FirewallApi.md#update_firewall_profiles) | **PUT** /network/firewall/profiles | Update firewall profiles &amp; their attachments.


# **list_firewall_ip_sets**
> FirewallIPSets list_firewall_ip_sets()

List all firewall IP sets

List all firewall IP sets.

### Example

* Api Key Authentication (APIKeyHeader):
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

# **list_firewall_profiles**
> FirewallProfiles list_firewall_profiles()

List all firewall profiles.

List the firewall profiles & their attachments.

### Example

* Api Key Authentication (APIKeyHeader):
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

# **remove_firewall_profiles**
> SuccessResp remove_firewall_profiles(body)

Remove firewall profiles.

Remove firewall profiles and their attachments.

### Example

* Api Key Authentication (APIKeyHeader):
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

# **reset_firewall_profile**
> reset_firewall_profile()

Reset firewall profiles.

Reset firewall profiles, ip-sets & their attachments.

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

# **update_firewall_ip_sets**
> FirewallIPSets update_firewall_ip_sets(body)

Update firewall IP sets

Update firewall IP sets.

### Example

* Api Key Authentication (APIKeyHeader):
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


body = FirewallIPSets(
        ip_sets=[
            FirewallIPSet(
                name="name_example",
                subnets=[
                    "subnets_example",
                ],
            ),
        ],
    ) # FirewallIPSets | Specifies the update request parameters.

# example passing only required values which don't have defaults set
try:
	# Update firewall IP sets
	api_response = client.firewall.update_firewall_ip_sets(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling FirewallApi->update_firewall_ip_sets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirewallIPSets**](FirewallIPSets.md)| Specifies the update request parameters. |

### Return type

[**FirewallIPSets**](FirewallIPSets.md)

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

# **update_firewall_profile**
> FirewallProfileParams update_firewall_profile(body)

Update firewall profiles & their attachments.

Update the firewall profiles and/or their attachments.

### Example

* Api Key Authentication (APIKeyHeader):
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
        name="name_example",
        direction="INPUT",
        ports=[
            "ports_example",
        ],
        action="allow",
        description="description_example",
        subnets=[
            "subnets_example",
        ],
        interface_groups=[
            "interface_groups_example",
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

# **update_firewall_profiles**
> FirewallProfiles update_firewall_profiles(body)

Update firewall profiles & their attachments.

Update the firewall profiles and/or their attachments.

### Example

* Api Key Authentication (APIKeyHeader):
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


body = FirewallProfiles(
        profiles=[
            FirewallProfile(
                name="name_example",
                gateway_params=[
                    GatewayParams(
                        port="port_example",
                        direction="INPUT",
                    ),
                ],
                attachments=[
                    Attachment(
                        interfaces=[
                            "interfaces_example",
                        ],
                        interface_groups=[
                            "interface_groups_example",
                        ],
                        ipset_names=[
                            "ipset_names_example",
                        ],
                        description="description_example",
                        action="allow",
                    ),
                ],
            ),
        ],
    ) # FirewallProfiles | Specifies the parameters to configure firewall profiles and/or their attachments.

# example passing only required values which don't have defaults set
try:
	# Update firewall profiles & their attachments.
	api_response = client.firewall.update_firewall_profiles(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling FirewallApi->update_firewall_profiles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FirewallProfiles**](FirewallProfiles.md)| Specifies the parameters to configure firewall profiles and/or their attachments. |

### Return type

[**FirewallProfiles**](FirewallProfiles.md)

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

