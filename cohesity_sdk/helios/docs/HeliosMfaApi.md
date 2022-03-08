# cohesity_sdk.HeliosMfaApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mfa_preferences**](HeliosMfaApi.md#get_mfa_preferences) | **GET** /mcm/mfa | Get MFA Preferences
[**update_mfa_preferences**](HeliosMfaApi.md#update_mfa_preferences) | **PUT** /mcm/mfa | Update MFA Preferences


# **get_mfa_preferences**
> HeliosMfa get_mfa_preferences()

Get MFA Preferences

Gets the Multi Factor Authentication configuration for the account.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.helios_mfa import HeliosMfa
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get MFA Preferences
	api_response = client.helios_mfa.get_mfa_preferences(region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosMfaApi->get_mfa_preferences: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**HeliosMfa**](HeliosMfa.md)

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

# **update_mfa_preferences**
> HeliosMfa update_mfa_preferences(body)

Update MFA Preferences

Updates the Multi Factor Authentication configuration for the account.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.helios_mfa import HeliosMfa
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = HeliosMfa(
        mfa=True,
        authentication_types=[
            "email",
        ],
        retain_user_mfa_settings=False,
    ) # HeliosMfa | Specifies the parameters to support MFA.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update MFA Preferences
	api_response = client.helios_mfa.update_mfa_preferences(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosMfaApi->update_mfa_preferences: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update MFA Preferences
	api_response = client.helios_mfa.update_mfa_preferences(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosMfaApi->update_mfa_preferences: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HeliosMfa**](HeliosMfa.md)| Specifies the parameters to support MFA. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**HeliosMfa**](HeliosMfa.md)

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

