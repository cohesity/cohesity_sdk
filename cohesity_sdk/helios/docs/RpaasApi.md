# cohesity_sdk.RpaasApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**add_rpaas_regions**](RpaasApi.md#add_rpaas_regions) | **POST** /mcm/ransomware-shield/regions | Add rpaas regions for an account.
[**complete_rpaas_onboard**](RpaasApi.md#complete_rpaas_onboard) | **POST** /mcm/ransomware-shield/complete | Complete onboarding for RPaaS.
[**get_rpaas_onboard**](RpaasApi.md#get_rpaas_onboard) | **GET** /mcm/ransomware-shield/complete | Get the RPaaS onboarding status.
[**get_rpaas_regions**](RpaasApi.md#get_rpaas_regions) | **GET** /mcm/ransomware-shield/regions | Get the Rpaas regions.
[**verify_s3_credentials**](RpaasApi.md#verify_s3_credentials) | **POST** /mcm/ransomware-shield/verify-s3-credentials | Verify getting RPaaS S3 credentials.


# **add_rpaas_regions**
> RpaasRegionInfoList add_rpaas_regions(body)

Add rpaas regions for an account.

Add Cohesity RPaaS service in a given set of regions for the logged in account.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.add_rpaas_regions_request import AddRpaasRegionsRequest
from cohesity_sdk.helios.model.rpaas_region_info_list import RpaasRegionInfoList
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = AddRpaasRegionsRequest(
        regions=[
            AddRegionParams(
                region_id="us-east-1",
                kms_key_info=KmsKeyBasicInfo(
                    kms_key_type="Cohesity",
                ),
            ),
        ],
    ) # AddRpaasRegionsRequest | Specifies the parameters to add RPaas service in the regions.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Add rpaas regions for an account.
	api_response = client.rpaas.add_rpaas_regions(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RpaasApi->add_rpaas_regions: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Add rpaas regions for an account.
	api_response = client.rpaas.add_rpaas_regions(body, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> complete_rpaas_onboard()

Complete onboarding for RPaaS.

Complete onboarding for RPaaS for the logged in user.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Complete onboarding for RPaaS.
	client.rpaas.complete_rpaas_onboard(region_id=region_id)
except ApiException as e:
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

# **get_rpaas_onboard**
> RpaasOnboardInfo get_rpaas_onboard()

Get the RPaaS onboarding status.

Get the onboarding status for RPaaS for the logged in user.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.rpaas_onboard_info import RpaasOnboardInfo
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the RPaaS onboarding status.
	api_response = client.rpaas.get_rpaas_onboard(region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> RpaasRegionInfoList get_rpaas_regions()

Get the Rpaas regions.

Get the list of Rpaas regions enabled for the logged in account.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.rpaas_region_info_list import RpaasRegionInfoList
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
region_ids = [
        "us-east-1",
    ] # [str, none_type], none_type | List of region IDs to filter the response. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the Rpaas regions.
	api_response = client.rpaas.get_rpaas_regions(region_id=region_id, region_ids=region_ids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling RpaasApi->get_rpaas_regions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **region_ids** | [**[str, none_type], none_type**](str, none_type.md)| List of region IDs to filter the response. | [optional]

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

# **verify_s3_credentials**
> verify_s3_credentials(body)

Verify getting RPaaS S3 credentials.

Verify getting RPaaS S3 credentials by checking restored objects and search jobs.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.verify_s3_credentials_request import VerifyS3CredentialsRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = VerifyS3CredentialsRequest(
        cluster_id=1,
        cluster_incarnation_id=1,
        vault_id=1,
    ) # VerifyS3CredentialsRequest | Specifies the parameters to verify getting RPaaS S3 credentials.
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Verify getting RPaaS S3 credentials.
	client.rpaas.verify_s3_credentials(body)
except ApiException as e:
	print("Exception when calling RpaasApi->verify_s3_credentials: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Verify getting RPaaS S3 credentials.
	client.rpaas.verify_s3_credentials(body, region_id=region_id)
except ApiException as e:
	print("Exception when calling RpaasApi->verify_s3_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyS3CredentialsRequest**](VerifyS3CredentialsRequest.md)| Specifies the parameters to verify getting RPaaS S3 credentials. |
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

