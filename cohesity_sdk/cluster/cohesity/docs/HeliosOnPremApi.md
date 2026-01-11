# cohesity_sdk.cluster.HeliosOnPremApi

All URIs are relative to *http://localhost/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_helios_on_prem_config**](HeliosOnPremApi.md#get_helios_on_prem_config) | **GET** /helios-onprem/config | Retreive Helios OnPrem Configuration
[**update_helios_on_prem_config**](HeliosOnPremApi.md#update_helios_on_prem_config) | **PUT** /helios-onprem/config | Update Helios OnPrem Configuration


# **get_helios_on_prem_config**
> HeliosOnPremConfig get_helios_on_prem_config()

Retreive Helios OnPrem Configuration

**Privileges:** ```CLUSTER_VIEW``` <br><br>View the configuration for Helios OnPrem VM Node.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import helios_on_prem
from cohesity_sdk.cluster.cohesity.model.helios_on_prem_config import HeliosOnPremConfig
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = helios_on_prem.HeliosOnPremApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retreive Helios OnPrem Configuration
        api_response = api_instance.get_helios_on_prem_config()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling HeliosOnPremApi->get_helios_on_prem_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**HeliosOnPremConfig**](HeliosOnPremConfig.md)

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

# **update_helios_on_prem_config**
> HeliosOnPremConfig update_helios_on_prem_config(body)

Update Helios OnPrem Configuration

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update the configuration for Helios OnPrem VM Node.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import helios_on_prem
from cohesity_sdk.cluster.cohesity.model.helios_on_prem_config import HeliosOnPremConfig
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = helios_on_prem.HeliosOnPremApi(api_client)
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
            secondary_dhcp_network_config=ClusterDhcpNetworkConfig(
                dns_servers=[
                    "dns_servers_example",
                ],
            ),
            secondary_manual_network_config=ClusterManualNetworkConfig(
                dns_servers=[
                    "dns_servers_example",
                ],
                gateway="gateway_example",
                subnet_ip="subnet_ip_example",
                subnet_mask="subnet_mask_example",
            ),
            use_dhcp=True,
            vip_host_name="vip_host_name_example",
            vips=[
                "vips_example",
            ],
        ),
        nodes=[
            HeliosOnPremVMNode(
                node_id=1,
                node_ip="node_ip_example",
            ),
        ],
        proxy_server_config=ClusterProxyServerConfig(
            ip="ip_example",
            is_disabled=True,
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
        api_response = api_instance.update_helios_on_prem_config(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling HeliosOnPremApi->update_helios_on_prem_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HeliosOnPremConfig**](HeliosOnPremConfig.md)| Specifies the parameters for config update. |

### Return type

[**HeliosOnPremConfig**](HeliosOnPremConfig.md)

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

