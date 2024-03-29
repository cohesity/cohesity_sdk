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

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.helios_on_prem_config import HeliosOnPremConfig
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Retreive Helios OnPrem Configuration
	api_response = client.helios_on_prem.get_helios_on_prem_config(access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosOnPremApi->get_helios_on_prem_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**HeliosOnPremConfig**](HeliosOnPremConfig.md)

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

# **update_helios_on_prem_config**
> HeliosOnPremConfig update_helios_on_prem_config(body)

Update Helios OnPrem Configuration

Update the configuration for Helios OnPrem VM Node.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.helios_on_prem_config import HeliosOnPremConfig
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = HeliosOnPremConfig(
        name="name_example",
        nodes=[
            HeliosOnPremVMNode(
                node_ip="node_ip_example",
                node_id=1,
            ),
        ],
        kubernetes_subnet_cidr="kubernetes_subnet_cidr_example",
        network_config=ClusterCreateNetworkConfig(
            ntp_servers=[
                "ntp_servers_example",
            ],
            domain_names=[
                "domain_names_example",
            ],
            vip_host_name="vip_host_name_example",
            ip_preference="Ipv4",
            use_dhcp=True,
            dhcp_network_config=ClusterDhcpNetworkConfig(
                dns_servers=[
                    "dns_servers_example",
                ],
            ),
            manual_network_config=ClusterManualNetworkConfig(
                gateway="gateway_example",
                subnet_ip="subnet_ip_example",
                subnet_mask="subnet_mask_example",
                dns_servers=[
                    "dns_servers_example",
                ],
            ),
        ),
        proxy_server_config=ClusterProxyServerConfig(
            ip="ip_example",
            port=1,
            username="username_example",
            password="password_example",
        ),
        ssh_config=HeliosOnPremSSHConfig(
        ),
    ) # HeliosOnPremConfig | Specifies the parameters for config update.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update Helios OnPrem Configuration
	api_response = client.helios_on_prem.update_helios_on_prem_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosOnPremApi->update_helios_on_prem_config: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update Helios OnPrem Configuration
	api_response = client.helios_on_prem.update_helios_on_prem_config(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosOnPremApi->update_helios_on_prem_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HeliosOnPremConfig**](HeliosOnPremConfig.md)| Specifies the parameters for config update. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**HeliosOnPremConfig**](HeliosOnPremConfig.md)

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

