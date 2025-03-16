# cohesity_sdk.helios.HeliosOnPremApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_helios_on_prem_config**](HeliosOnPremApi.md#get_helios_on_prem_config) | **GET** /helios-onprem/config | Retreive Helios OnPrem Configuration
[**update_helios_on_prem_config**](HeliosOnPremApi.md#update_helios_on_prem_config) | **PUT** /helios-onprem/config | Update Helios OnPrem Configuration


# **get_helios_on_prem_config**
> HeliosOnPremConfig get_helios_on_prem_config(access_cluster_id=access_cluster_id, region_id=region_id)

Retreive Helios OnPrem Configuration

View the configuration for Helios OnPrem VM Node.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.helios_on_prem_config import HeliosOnPremConfig
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
    api_instance = cohesity_sdk.helios.HeliosOnPremApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Retreive Helios OnPrem Configuration
        api_response = api_instance.get_helios_on_prem_config(access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of HeliosOnPremApi->get_helios_on_prem_config:\n")
        pprint(api_response)
    except Exception as e:
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
> HeliosOnPremConfig update_helios_on_prem_config(body, access_cluster_id=access_cluster_id, region_id=region_id)

Update Helios OnPrem Configuration

Update the configuration for Helios OnPrem VM Node.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.helios_on_prem_config import HeliosOnPremConfig
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
    api_instance = cohesity_sdk.helios.HeliosOnPremApi(api_client)
    body = cohesity_sdk.helios.HeliosOnPremConfig() # HeliosOnPremConfig | Specifies the parameters for config update.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update Helios OnPrem Configuration
        api_response = api_instance.update_helios_on_prem_config(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of HeliosOnPremApi->update_helios_on_prem_config:\n")
        pprint(api_response)
    except Exception as e:
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

