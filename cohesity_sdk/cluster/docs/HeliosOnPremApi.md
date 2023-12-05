# cohesity_sdk.HeliosOnPremApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_helios_on_prem_config**](HeliosOnPremApi.md#get_helios_on_prem_config) | **GET** /helios-onprem/config | Retreive Helios OnPrem Configuration
[**update_helios_on_prem_config**](HeliosOnPremApi.md#update_helios_on_prem_config) | **PUT** /helios-onprem/config | Update Helios OnPrem Configuration


# **get_helios_on_prem_config**
> HeliosOnPremConfig get_helios_on_prem_config()

Retreive Helios OnPrem Configuration

View the configuration for Helios OnPrem VM Node.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.helios_on_prem_config import HeliosOnPremConfig
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
	# Retreive Helios OnPrem Configuration
	api_response = client.helios_on_prem.get_helios_on_prem_config()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosOnPremApi->get_helios_on_prem_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**HeliosOnPremConfig**](HeliosOnPremConfig.md)

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

# **update_helios_on_prem_config**
> HeliosOnPremConfig update_helios_on_prem_config(body)

Update Helios OnPrem Configuration

Update the configuration for Helios OnPrem VM Node.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.helios_on_prem_config import HeliosOnPremConfig
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

body = HeliosOnPremConfig(
        kubernetes_subnet_cidr="kubernetes_subnet_cidr_example",
        name="name_example",
        network_config=ClusterCreateNetworkConfig(
            dhcp_network_config=ClusterDhcpNetworkConfig(
                dns_servers=[
                    "dns_servers_example",
                ],
            ),
            domain_names=[
                "domain_names_example",
            ],
            ip_preference="Ipv4",
            manual_network_config=ClusterManualNetworkConfig(
                dns_servers=[
                    "dns_servers_example",
                ],
                gateway="gateway_example",
                subnet_ip="subnet_ip_example",
                subnet_mask="subnet_mask_example",
            ),
            ntp_servers=[
                "ntp_servers_example",
            ],
            use_dhcp=True,
            vip_host_name="vip_host_name_example",
        ),
        nodes=[
            HeliosOnPremVMNode(
                node_id=1,
                node_ip="node_ip_example",
            ),
        ],
        proxy_server_config=ClusterProxyServerConfig(
            ip="ip_example",
            password="password_example",
            port=1,
            username="username_example",
        ),
        ssh_config=HeliosOnPremSSHConfig(
        ),
    ) # HeliosOnPremConfig | Specifies the parameters for config update.

# example passing only required values which don't have defaults set
try:
	# Update Helios OnPrem Configuration
	api_response = client.helios_on_prem.update_helios_on_prem_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosOnPremApi->update_helios_on_prem_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HeliosOnPremConfig**](HeliosOnPremConfig.md)| Specifies the parameters for config update. |

### Return type

[**HeliosOnPremConfig**](HeliosOnPremConfig.md)

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

