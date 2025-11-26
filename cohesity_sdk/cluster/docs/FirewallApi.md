# cohesity_sdk.FirewallApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**remove_firewall_profiles**](FirewallApi.md#remove_firewall_profiles) | **PUT** /network/firewall/profile/remove | Remove firewall profiles.
[**update_firewall_profile**](FirewallApi.md#update_firewall_profile) | **PUT** /network/firewall/profile | Update firewall profiles &amp; their attachments.


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

