# cohesity_sdk.helios.SupportApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_support_user_config**](SupportApi.md#get_support_user_config) | **GET** /support-user/config | Get support user configuration.
[**update_support_user_config**](SupportApi.md#update_support_user_config) | **PUT** /support-user/config | Update support user configuration.
[**validate_support_user_creds**](SupportApi.md#validate_support_user_creds) | **POST** /support-user/config/validate | Validates the support user credentials.


# **get_support_user_config**
> SupportUserConfig get_support_user_config(access_cluster_id=access_cluster_id, region_id=region_id)

Get support user configuration.

Cohesity provides a support user account for improved security and you need to use the support user account to log in to the Cohesity cluster bash shell using SSH. This endpoint returns the current support user configuration on the Cohesity cluster.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.support_user_config import SupportUserConfig
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
    api_instance = cohesity_sdk.helios.SupportApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get support user configuration.
        api_response = api_instance.get_support_user_config(access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of SupportApi->get_support_user_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->get_support_user_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**SupportUserConfig**](SupportUserConfig.md)

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

# **update_support_user_config**
> SuccessResp update_support_user_config(body, access_cluster_id=access_cluster_id, region_id=region_id)

Update support user configuration.

Update support user's configuration. This allows you to update the support user's password and/or grant sudo access to the user.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.success_resp import SuccessResp
from cohesity_sdk.helios.models.update_support_user_params import UpdateSupportUserParams
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
    api_instance = cohesity_sdk.helios.SupportApi(api_client)
    body = cohesity_sdk.helios.UpdateSupportUserParams() # UpdateSupportUserParams | Specifies the support user configuration.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update support user configuration.
        api_response = api_instance.update_support_user_config(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of SupportApi->update_support_user_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->update_support_user_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSupportUserParams**](UpdateSupportUserParams.md)| Specifies the support user configuration. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**SuccessResp**](SuccessResp.md)

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

# **validate_support_user_creds**
> SuccessResp validate_support_user_creds(body, access_cluster_id=access_cluster_id, region_id=region_id)

Validates the support user credentials.

Validates the support user credentials.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.success_resp import SuccessResp
from cohesity_sdk.helios.models.validate_support_user_cred_params import ValidateSupportUserCredParams
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
    api_instance = cohesity_sdk.helios.SupportApi(api_client)
    body = cohesity_sdk.helios.ValidateSupportUserCredParams() # ValidateSupportUserCredParams | Specifies the support user credentials.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Validates the support user credentials.
        api_response = api_instance.validate_support_user_creds(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of SupportApi->validate_support_user_creds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->validate_support_user_creds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ValidateSupportUserCredParams**](ValidateSupportUserCredParams.md)| Specifies the support user credentials. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**SuccessResp**](SuccessResp.md)

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

