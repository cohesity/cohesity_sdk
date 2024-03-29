# cohesity_sdk.IPsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_ip_settings**](IPsApi.md#configure_ip_settings) | **PUT** /network/ips | Configure an IP setting.


# **configure_ip_settings**
> IPConfigParams configure_ip_settings(body)

Configure an IP setting.

Configure an IP setting on Cohesity Cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.ip_config_params import IPConfigParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = IPConfigParams(
        interface="interface_example",
        ips=[
            "ips_example",
        ],
        node_ids=[
            "node_ids_example",
        ],
        role="role_example",
        subnet_gateway="subnet_gateway_example",
        subnet_mask_bits=1,
        ip_family=1,
    ) # IPConfigParams | Specifies the parameters to configure a IP settings on a cluster.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Configure an IP setting.
	api_response = client.ips.configure_ip_settings(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IPsApi->configure_ip_settings: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Configure an IP setting.
	api_response = client.ips.configure_ip_settings(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IPsApi->configure_ip_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPConfigParams**](IPConfigParams.md)| Specifies the parameters to configure a IP settings on a cluster. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**IPConfigParams**](IPConfigParams.md)

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

