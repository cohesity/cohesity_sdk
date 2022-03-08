# cohesity_sdk.HeliosProtectionSourcesApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**mcm_delete_protection_source_registration**](HeliosProtectionSourcesApi.md#mcm_delete_protection_source_registration) | **DELETE** /mcm/data-protect/sources/registrations/{id} | Delete Protection Source Registration.
[**mcm_get_agent_image_details**](HeliosProtectionSourcesApi.md#mcm_get_agent_image_details) | **GET** /mcm/data-protect/agents/images | Get agent images details.
[**mcm_get_protection_source_registration**](HeliosProtectionSourcesApi.md#mcm_get_protection_source_registration) | **GET** /mcm/data-protect/sources/registrations/{id} | Get a Protection Source registration.
[**mcm_get_protection_sources**](HeliosProtectionSourcesApi.md#mcm_get_protection_sources) | **GET** /mcm/data-protect/sources | Get a List of Protection Sources.
[**mcm_register_protection_source**](HeliosProtectionSourcesApi.md#mcm_register_protection_source) | **POST** /mcm/data-protect/sources/registrations | Register a Protection Source.
[**mcm_test_source_connection**](HeliosProtectionSourcesApi.md#mcm_test_source_connection) | **POST** /mcm/data-protect/sources/test-connection | Test connection to a source.
[**update_protection_source_registration_mixin1**](HeliosProtectionSourcesApi.md#update_protection_source_registration_mixin1) | **PUT** /mcm/data-protect/sources/registrations/{id} | Update Protection Source registration.


# **mcm_delete_protection_source_registration**
> mcm_delete_protection_source_registration(id)

Delete Protection Source Registration.

Delete Protection Source Registration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies the ID of the Protection Source Registration.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete Protection Source Registration.
	client.helios_protection_sources.mcm_delete_protection_source_registration(id)
except ApiException as e:
	print("Exception when calling HeliosProtectionSourcesApi->mcm_delete_protection_source_registration: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete Protection Source Registration.
	client.helios_protection_sources.mcm_delete_protection_source_registration(id, region_id=region_id)
except ApiException as e:
	print("Exception when calling HeliosProtectionSourcesApi->mcm_delete_protection_source_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the ID of the Protection Source Registration. |
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

# **mcm_get_agent_image_details**
> McmAgentImagesResponse mcm_get_agent_image_details()

Get agent images details.

Get agent information on Helios.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.mcm_agent_images_response import McmAgentImagesResponse
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
platform = "Windows" # str | Specifies a platform for which agent information need to be fetched. (optional)
package_type = "Script" # str | Specifies a package type for which agent information need to be fetched. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get agent images details.
	api_response = client.helios_protection_sources.mcm_get_agent_image_details(region_id=region_id, platform=platform, package_type=package_type)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosProtectionSourcesApi->mcm_get_agent_image_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **platform** | **str**| Specifies a platform for which agent information need to be fetched. | [optional]
 **package_type** | **str**| Specifies a package type for which agent information need to be fetched. | [optional]

### Return type

[**McmAgentImagesResponse**](McmAgentImagesResponse.md)

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

# **mcm_get_protection_source_registration**
> McmSourceRegistration mcm_get_protection_source_registration(id)

Get a Protection Source registration.

Get a Protection Source registration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.mcm_source_registration import McmSourceRegistration
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies the id of the Protection Source registration.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get a Protection Source registration.
	api_response = client.helios_protection_sources.mcm_get_protection_source_registration(id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosProtectionSourcesApi->mcm_get_protection_source_registration: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a Protection Source registration.
	api_response = client.helios_protection_sources.mcm_get_protection_source_registration(id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosProtectionSourcesApi->mcm_get_protection_source_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the Protection Source registration. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**McmSourceRegistration**](McmSourceRegistration.md)

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

# **mcm_get_protection_sources**
> McmSources mcm_get_protection_sources()

Get a List of Protection Sources.

Get a List of Protection Sources.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.mcm_sources import McmSources
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
environments = [
        "kVMware",
    ] # [str] | Specifies the list of environment type of the Protection Source. (optional)
ids = [
        "ids_example",
    ] # [str] | Specifies the list of ids to filter Protection Sources. (optional)
region_ids = [
        "regionIds_example",
    ] # [str] | Filter by a list of region ids. (optional)
exclude_protection_stats = True # bool | Whether to exclude Protection Sources protection stats in response. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get a List of Protection Sources.
	api_response = client.helios_protection_sources.mcm_get_protection_sources(region_id=region_id, environments=environments, ids=ids, region_ids=region_ids, exclude_protection_stats=exclude_protection_stats)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosProtectionSourcesApi->mcm_get_protection_sources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **environments** | **[str]**| Specifies the list of environment type of the Protection Source. | [optional]
 **ids** | **[str]**| Specifies the list of ids to filter Protection Sources. | [optional]
 **region_ids** | **[str]**| Filter by a list of region ids. | [optional]
 **exclude_protection_stats** | **bool**| Whether to exclude Protection Sources protection stats in response. | [optional]

### Return type

[**McmSources**](McmSources.md)

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

# **mcm_register_protection_source**
> McmSourceRegistration mcm_register_protection_source(body)

Register a Protection Source.

Register a Protection Source.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.mcm_source_registration_request_params import McmSourceRegistrationRequestParams
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.mcm_source_registration import McmSourceRegistration
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = McmSourceRegistrationRequestParams() # McmSourceRegistrationRequestParams | Specifies the parameters to register a Protection Source.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
access_cluster_id = 1 # int | Specifies the destination cluster id on which this Source needs to be registered. (optional)

# example passing only required values which don't have defaults set
try:
	# Register a Protection Source.
	api_response = client.helios_protection_sources.mcm_register_protection_source(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosProtectionSourcesApi->mcm_register_protection_source: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Register a Protection Source.
	api_response = client.helios_protection_sources.mcm_register_protection_source(body, region_id=region_id, access_cluster_id=access_cluster_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosProtectionSourcesApi->mcm_register_protection_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**McmSourceRegistrationRequestParams**](McmSourceRegistrationRequestParams.md)| Specifies the parameters to register a Protection Source. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **access_cluster_id** | **int**| Specifies the destination cluster id on which this Source needs to be registered. | [optional]

### Return type

[**McmSourceRegistration**](McmSourceRegistration.md)

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

# **mcm_test_source_connection**
> SourceConnectionResponseParams mcm_test_source_connection(body)

Test connection to a source.

Specifies the endpoint to test the source connectivity.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.source_connection_request_params import SourceConnectionRequestParams
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.source_connection_response_params import SourceConnectionResponseParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = SourceConnectionRequestParams() # SourceConnectionRequestParams | Specifies the parameters to test connectivity of a Protection Source.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
access_cluster_id = 1 # int | Specifies the destination cluster id on which this Source needs to be registered. (optional)

# example passing only required values which don't have defaults set
try:
	# Test connection to a source.
	api_response = client.helios_protection_sources.mcm_test_source_connection(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosProtectionSourcesApi->mcm_test_source_connection: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Test connection to a source.
	api_response = client.helios_protection_sources.mcm_test_source_connection(body, region_id=region_id, access_cluster_id=access_cluster_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosProtectionSourcesApi->mcm_test_source_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SourceConnectionRequestParams**](SourceConnectionRequestParams.md)| Specifies the parameters to test connectivity of a Protection Source. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **access_cluster_id** | **int**| Specifies the destination cluster id on which this Source needs to be registered. | [optional]

### Return type

[**SourceConnectionResponseParams**](SourceConnectionResponseParams.md)

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

# **update_protection_source_registration_mixin1**
> McmSourceRegistration update_protection_source_registration_mixin1(id, body)

Update Protection Source registration.

Update Protection Source registration.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.mcm_source_registration_update_request_params import McmSourceRegistrationUpdateRequestParams
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.mcm_source_registration import McmSourceRegistration
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specifies the id of the Protection Source registration.
body = McmSourceRegistrationUpdateRequestParams() # McmSourceRegistrationUpdateRequestParams | Specifies the parameters to update the registration.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update Protection Source registration.
	api_response = client.helios_protection_sources.update_protection_source_registration_mixin1(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosProtectionSourcesApi->update_protection_source_registration_mixin1: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update Protection Source registration.
	api_response = client.helios_protection_sources.update_protection_source_registration_mixin1(id, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosProtectionSourcesApi->update_protection_source_registration_mixin1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the id of the Protection Source registration. |
 **body** | [**McmSourceRegistrationUpdateRequestParams**](McmSourceRegistrationUpdateRequestParams.md)| Specifies the parameters to update the registration. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**McmSourceRegistration**](McmSourceRegistration.md)

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

