# cohesity_sdk.AwsRegistrationApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**onboard_aws_customer**](AwsRegistrationApi.md#onboard_aws_customer) | **POST** /mcm/aws-registration | Onboards a new AWS Customer to DMaaS
[**verify_aws_token**](AwsRegistrationApi.md#verify_aws_token) | **POST** /mcm/aws-registration/verify | Onboards a new AWS Customer to DMaaS


# **onboard_aws_customer**
> Error onboard_aws_customer(x_amzn_marketplace_token)

Onboards a new AWS Customer to DMaaS

Captures the onboarding request from AWS Market place.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


x_amzn_marketplace_token = "x_amzn_marketplace_token_example" # str | The Amazon Marketplace token with Product info.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Onboards a new AWS Customer to DMaaS
	api_response = client.aws_registration.onboard_aws_customer(x_amzn_marketplace_token)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AwsRegistrationApi->onboard_aws_customer: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Onboards a new AWS Customer to DMaaS
	api_response = client.aws_registration.onboard_aws_customer(x_amzn_marketplace_token, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AwsRegistrationApi->onboard_aws_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_amzn_marketplace_token** | **str**| The Amazon Marketplace token with Product info. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**Error**](Error.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_aws_token**
> HeliosAwsResponse verify_aws_token(body)

Onboards a new AWS Customer to DMaaS

Captures the onboarding request from AWS Market place.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.helios_aws_request import HeliosAwsRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.helios_aws_response import HeliosAwsResponse
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = HeliosAwsRequest(
        token="token_example",
    ) # HeliosAwsRequest | Specifies the parameters to create an Identity Provider.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Onboards a new AWS Customer to DMaaS
	api_response = client.aws_registration.verify_aws_token(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AwsRegistrationApi->verify_aws_token: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Onboards a new AWS Customer to DMaaS
	api_response = client.aws_registration.verify_aws_token(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AwsRegistrationApi->verify_aws_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HeliosAwsRequest**](HeliosAwsRequest.md)| Specifies the parameters to create an Identity Provider. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**HeliosAwsResponse**](HeliosAwsResponse.md)

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

