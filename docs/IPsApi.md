# cohesity_sdk.IPsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_ip_settings**](IPsApi.md#configure_ip_settings) | **PUT** /network/ips | Configure an IP setting.


# **configure_ip_settings**
> IPConfigParams configure_ip_settings(body)

Configure an IP setting.

Configure an IP setting on Cohesity Cluster.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.ip_config_params import IPConfigParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint



client = ClusterClient(cluster_vip)

body = IPConfigParams(
        interface="interface_example",
        ip_family=1,
        ips=[
            "ips_example",
        ],
        node_ids=[
            "node_ids_example",
        ],
        role="role_example",
        subnet_gateway="subnet_gateway_example",
        subnet_mask_bits=1,
    ) # IPConfigParams | Specifies the parameters to configure a IP settings on a cluster.

# example passing only required values which don't have defaults set
try:
	# Configure an IP setting.
	api_response = client.ips.configure_ip_settings(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IPsApi->configure_ip_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPConfigParams**](IPConfigParams.md)| Specifies the parameters to configure a IP settings on a cluster. |

### Return type

[**IPConfigParams**](IPConfigParams.md)

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

