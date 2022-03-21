# cohesity_sdk.HeliosLoginConfigurationApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_helios_login_config**](HeliosLoginConfigurationApi.md#get_helios_login_config) | **GET** /mcm/login/config | Get Helios Login Configuration


# **get_helios_login_config**
> HeliosLoginConfiguration get_helios_login_config()

Get Helios Login Configuration

Get the login configuration for Salesforce login

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.helios_login_configuration import HeliosLoginConfiguration
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Helios Login Configuration
	api_response = client.helios_login_configuration.get_helios_login_config(region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosLoginConfigurationApi->get_helios_login_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**HeliosLoginConfiguration**](HeliosLoginConfiguration.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Helios Login Configuration |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

