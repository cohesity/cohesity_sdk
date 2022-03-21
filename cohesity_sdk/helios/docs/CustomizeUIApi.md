# cohesity_sdk.CustomizeUIApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_whitelabeling_settings**](CustomizeUIApi.md#create_whitelabeling_settings) | **POST** /mcm/customize-ui/settings | Create whitelabeling settings.
[**delete_whitelabeling_settings**](CustomizeUIApi.md#delete_whitelabeling_settings) | **DELETE** /mcm/customize-ui/settings | Delete whitelabeling settings.
[**get_whitelabeling_settings**](CustomizeUIApi.md#get_whitelabeling_settings) | **GET** /mcm/customize-ui/settings | Get whitelabeling settings.
[**update_whitelabeling_settings**](CustomizeUIApi.md#update_whitelabeling_settings) | **PATCH** /mcm/customize-ui/settings | Update whitelabeling settings.


# **create_whitelabeling_settings**
> WhitelabelingSetting create_whitelabeling_settings(body)

Create whitelabeling settings.

Create the whitelabeling setting based on passed filters

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.whitelabeling_setting import WhitelabelingSetting
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = WhitelabelingSetting(
        account_id="account_id_example",
        masthead_details=MastheadDetails(
            light_bg_color="light_bg_color_example",
            dark_bg_color="dark_bg_color_example",
            dark_text_color="dark_text_color_example",
            light_text_color="light_text_color_example",
            light_logo_src="light_logo_src_example",
            dark_logo_src="dark_logo_src_example",
        ),
        customized_url_details=CustomizedURLDetails(
            url="url_example",
            dns="dns_example",
            domain="domain_example",
        ),
        customized_login_page_details=CustomizedLoginPageDetails(
            platform_name="platform_name_example",
            color="color_example",
            login_page_src="login_page_src_example",
        ),
        documentation_labeling_details=DocumentationLabelingDetails(
            color="color_example",
            logo_src="logo_src_example",
        ),
    ) # WhitelabelingSetting | Specifies whitelabeling setting details to create.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create whitelabeling settings.
	api_response = client.customize_ui.create_whitelabeling_settings(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling CustomizeUIApi->create_whitelabeling_settings: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create whitelabeling settings.
	api_response = client.customize_ui.create_whitelabeling_settings(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling CustomizeUIApi->create_whitelabeling_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WhitelabelingSetting**](WhitelabelingSetting.md)| Specifies whitelabeling setting details to create. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**WhitelabelingSetting**](WhitelabelingSetting.md)

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

# **delete_whitelabeling_settings**
> Success delete_whitelabeling_settings()

Delete whitelabeling settings.

Delete the whitelabeling setting based on passed filters if not filters passed it will delete complete setting for that accountid

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.success import Success
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
setting_keys = [
        "mastheadDetails",
    ] # [str] | Specifies whitelabeling setting types to delete (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete whitelabeling settings.
	api_response = client.customize_ui.delete_whitelabeling_settings(region_id=region_id, setting_keys=setting_keys)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling CustomizeUIApi->delete_whitelabeling_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **setting_keys** | **[str]**| Specifies whitelabeling setting types to delete | [optional]

### Return type

[**Success**](Success.md)

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

# **get_whitelabeling_settings**
> WhitelabelingSetting get_whitelabeling_settings()

Get whitelabeling settings.

Get the whitelabeling setting based on passed filters

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.whitelabeling_setting import WhitelabelingSetting
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
setting_keys = [
        "mastheadDetails",
    ] # [str] | Specifies whitelabeling setting types to find (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get whitelabeling settings.
	api_response = client.customize_ui.get_whitelabeling_settings(region_id=region_id, setting_keys=setting_keys)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling CustomizeUIApi->get_whitelabeling_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **setting_keys** | **[str]**| Specifies whitelabeling setting types to find | [optional]

### Return type

[**WhitelabelingSetting**](WhitelabelingSetting.md)

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

# **update_whitelabeling_settings**
> WhitelabelingSetting update_whitelabeling_settings(body)

Update whitelabeling settings.

Update the whitelabeling setting based on passed filters

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.whitelabeling_setting import WhitelabelingSetting
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = WhitelabelingSetting(
        account_id="account_id_example",
        masthead_details=MastheadDetails(
            light_bg_color="light_bg_color_example",
            dark_bg_color="dark_bg_color_example",
            dark_text_color="dark_text_color_example",
            light_text_color="light_text_color_example",
            light_logo_src="light_logo_src_example",
            dark_logo_src="dark_logo_src_example",
        ),
        customized_url_details=CustomizedURLDetails(
            url="url_example",
            dns="dns_example",
            domain="domain_example",
        ),
        customized_login_page_details=CustomizedLoginPageDetails(
            platform_name="platform_name_example",
            color="color_example",
            login_page_src="login_page_src_example",
        ),
        documentation_labeling_details=DocumentationLabelingDetails(
            color="color_example",
            logo_src="logo_src_example",
        ),
    ) # WhitelabelingSetting | Specifies whitelabeling setting details to create.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update whitelabeling settings.
	api_response = client.customize_ui.update_whitelabeling_settings(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling CustomizeUIApi->update_whitelabeling_settings: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update whitelabeling settings.
	api_response = client.customize_ui.update_whitelabeling_settings(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling CustomizeUIApi->update_whitelabeling_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WhitelabelingSetting**](WhitelabelingSetting.md)| Specifies whitelabeling setting details to create. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**WhitelabelingSetting**](WhitelabelingSetting.md)

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

