# cohesity_sdk.helios.IPsApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_ip_settings**](IPsApi.md#configure_ip_settings) | **PUT** /network/ips | Configure an IP setting.


# **configure_ip_settings**
> IPConfigParams configure_ip_settings(body, access_cluster_id=access_cluster_id, region_id=region_id)

Configure an IP setting.

Configure an IP setting on Cohesity Cluster.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.ip_config_params import IPConfigParams
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
    host = "/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.IPsApi(api_client)
    body = cohesity_sdk.helios.IPConfigParams() # IPConfigParams | Specifies the parameters to configure a IP settings on a cluster.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Configure an IP setting.
        api_response = api_instance.configure_ip_settings(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of IPsApi->configure_ip_settings:\n")
        pprint(api_response)
    except Exception as e:
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

