# cohesity_sdk.HeliosSignupApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mcm_signup**](HeliosSignupApi.md#create_mcm_signup) | **POST** /mcm/signup | Create a signup request for MCM.
[**get_mcm_signups**](HeliosSignupApi.md#get_mcm_signups) | **GET** /mcm/signup | List MCM signup requests.
[**update_mcm_signup**](HeliosSignupApi.md#update_mcm_signup) | **PUT** /mcm/signup/{id} | Update MCM signup request.


# **create_mcm_signup**
> McmSignup create_mcm_signup(body)

Create a signup request for MCM.

Create a signup request for MCM.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.create_mcm_signup_request import CreateMcmSignupRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.mcm_signup import McmSignup
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = CreateMcmSignupRequest() # CreateMcmSignupRequest | Specifies the parameters to create a signup request for MCM.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a signup request for MCM.
	api_response = client.helios_signup.create_mcm_signup(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosSignupApi->create_mcm_signup: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a signup request for MCM.
	api_response = client.helios_signup.create_mcm_signup(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosSignupApi->create_mcm_signup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMcmSignupRequest**](CreateMcmSignupRequest.md)| Specifies the parameters to create a signup request for MCM. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**McmSignup**](McmSignup.md)

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

# **get_mcm_signups**
> McmSignups get_mcm_signups()

List MCM signup requests.

List MCM signup requests.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.mcm_signups import McmSignups
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
emails = [
        "emails_example",
    ] # [str] | Specifies a list of email ids to filter the signup requests. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List MCM signup requests.
	api_response = client.helios_signup.get_mcm_signups(region_id=region_id, emails=emails)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosSignupApi->get_mcm_signups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **emails** | **[str]**| Specifies a list of email ids to filter the signup requests. | [optional]

### Return type

[**McmSignups**](McmSignups.md)

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

# **update_mcm_signup**
> McmSignup update_mcm_signup(id, body)

Update MCM signup request.

Update MCM signup request.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.update_mcm_signup_request import UpdateMcmSignupRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.mcm_signup import McmSignup
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of the MCM signup request.
body = UpdateMcmSignupRequest() # UpdateMcmSignupRequest | Specifies the parameters to update a signup request for MCM.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update MCM signup request.
	api_response = client.helios_signup.update_mcm_signup(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosSignupApi->update_mcm_signup: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update MCM signup request.
	api_response = client.helios_signup.update_mcm_signup(id, body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling HeliosSignupApi->update_mcm_signup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the MCM signup request. |
 **body** | [**UpdateMcmSignupRequest**](UpdateMcmSignupRequest.md)| Specifies the parameters to update a signup request for MCM. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**McmSignup**](McmSignup.md)

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

