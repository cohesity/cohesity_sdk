# cohesity_sdk.helios.RpaasApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_rpaas_regions**](RpaasApi.md#add_rpaas_regions) | **POST** /mcm/ransomware-shield/regions | Add rpaas regions for an account.
[**complete_rpaas_onboard**](RpaasApi.md#complete_rpaas_onboard) | **POST** /mcm/ransomware-shield/complete | Complete onboarding for RPaaS.
[**get_fort_knox_vaults**](RpaasApi.md#get_fort_knox_vaults) | **GET** /mcm/fknox/vaults | Get FortKnox vaults.
[**get_rpaas_onboard**](RpaasApi.md#get_rpaas_onboard) | **GET** /mcm/ransomware-shield/complete | Get the RPaaS onboarding status.
[**get_rpaas_regions**](RpaasApi.md#get_rpaas_regions) | **GET** /mcm/ransomware-shield/regions | Get the Rpaas regions.


# **add_rpaas_regions**
> RpaasRegionInfoList add_rpaas_regions(body, region_id=region_id)

Add rpaas regions for an account.

Add Cohesity RPaaS service in a given set of regions for the logged in account.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.add_rpaas_regions_request import AddRpaasRegionsRequest
from cohesity_sdk.helios.models.rpaas_region_info_list import RpaasRegionInfoList
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
    api_instance = cohesity_sdk.helios.RpaasApi(api_client)
    body = cohesity_sdk.helios.AddRpaasRegionsRequest() # AddRpaasRegionsRequest | Specifies the parameters to add RPaas service in the regions.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Add rpaas regions for an account.
        api_response = api_instance.add_rpaas_regions(body, region_id=region_id)
        print("The response of RpaasApi->add_rpaas_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RpaasApi->add_rpaas_regions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddRpaasRegionsRequest**](AddRpaasRegionsRequest.md)| Specifies the parameters to add RPaas service in the regions. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**RpaasRegionInfoList**](RpaasRegionInfoList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_rpaas_onboard**
> complete_rpaas_onboard(region_id=region_id)

Complete onboarding for RPaaS.

Complete onboarding for RPaaS for the logged in user.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
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
    api_instance = cohesity_sdk.helios.RpaasApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Complete onboarding for RPaaS.
        api_instance.complete_rpaas_onboard(region_id=region_id)
    except Exception as e:
        print("Exception when calling RpaasApi->complete_rpaas_onboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

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

# **get_fort_knox_vaults**
> FortKnoxVaultInfoList get_fort_knox_vaults(region_id=region_id, region_ids=region_ids)

Get FortKnox vaults.

Get the list of FortKnox vaults for the logged in account.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.fort_knox_vault_info_list import FortKnoxVaultInfoList
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
    api_instance = cohesity_sdk.helios.RpaasApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    region_ids = ['region_ids_example'] # List[Optional[str]] | List of region IDs to filter the response. (optional)

    try:
        # Get FortKnox vaults.
        api_response = api_instance.get_fort_knox_vaults(region_id=region_id, region_ids=region_ids)
        print("The response of RpaasApi->get_fort_knox_vaults:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RpaasApi->get_fort_knox_vaults: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **region_ids** | [**List[Optional[str]]**](str.md)| List of region IDs to filter the response. | [optional] 

### Return type

[**FortKnoxVaultInfoList**](FortKnoxVaultInfoList.md)

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

# **get_rpaas_onboard**
> RpaasOnboardInfo get_rpaas_onboard(region_id=region_id)

Get the RPaaS onboarding status.

Get the onboarding status for RPaaS for the logged in user.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.rpaas_onboard_info import RpaasOnboardInfo
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
    api_instance = cohesity_sdk.helios.RpaasApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get the RPaaS onboarding status.
        api_response = api_instance.get_rpaas_onboard(region_id=region_id)
        print("The response of RpaasApi->get_rpaas_onboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RpaasApi->get_rpaas_onboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**RpaasOnboardInfo**](RpaasOnboardInfo.md)

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

# **get_rpaas_regions**
> RpaasRegionInfoList get_rpaas_regions(region_id=region_id, region_ids=region_ids)

Get the Rpaas regions.

Get the list of Rpaas regions enabled for the logged in account.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.rpaas_region_info_list import RpaasRegionInfoList
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
    api_instance = cohesity_sdk.helios.RpaasApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    region_ids = ['region_ids_example'] # List[Optional[str]] | List of region IDs to filter the response. (optional)

    try:
        # Get the Rpaas regions.
        api_response = api_instance.get_rpaas_regions(region_id=region_id, region_ids=region_ids)
        print("The response of RpaasApi->get_rpaas_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RpaasApi->get_rpaas_regions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **region_ids** | [**List[Optional[str]]**](str.md)| List of region IDs to filter the response. | [optional] 

### Return type

[**RpaasRegionInfoList**](RpaasRegionInfoList.md)

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

