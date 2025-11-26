# cohesity_sdk.SupportApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_support_user_config**](SupportApi.md#get_support_user_config) | **GET** /support-user/config | Get support user configuration.
[**update_support_user_config**](SupportApi.md#update_support_user_config) | **PUT** /support-user/config | Update support user configuration.
[**validate_support_user_creds**](SupportApi.md#validate_support_user_creds) | **POST** /support-user/config/validate | Validates the support user credentials.


# **get_support_user_config**
> SupportUserConfig get_support_user_config()

Get support user configuration.

Cohesity provides a support user account for improved security and you need to use the support user account to log in to the Cohesity cluster bash shell using SSH. This endpoint returns the current support user configuration on the Cohesity cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.support_user_config import SupportUserConfig
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Get support user configuration.
	api_response = client.support.get_support_user_config()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SupportApi->get_support_user_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
> SuccessResp update_support_user_config(body)

Update support user configuration.

Update support user's configuration. This allows you to update the support user's password and/or grant sudo access to the user.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.success_resp import SuccessResp
from cohesity_sdk.cluster.model.update_support_user_params import UpdateSupportUserParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = UpdateSupportUserParams(
        current_password="current_password_example",
        enable_sudo_access=True,
        new_password="new_password_example",
    ) # UpdateSupportUserParams | Specifies the support user configuration.

# example passing only required values which don't have defaults set
try:
	# Update support user configuration.
	api_response = client.support.update_support_user_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SupportApi->update_support_user_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSupportUserParams**](UpdateSupportUserParams.md)| Specifies the support user configuration. |

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
> SuccessResp validate_support_user_creds(body)

Validates the support user credentials.

Validates the support user credentials.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.validate_support_user_cred_params import ValidateSupportUserCredParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.success_resp import SuccessResp
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ValidateSupportUserCredParams(
        password="password_example",
    ) # ValidateSupportUserCredParams | Specifies the support user credentials.

# example passing only required values which don't have defaults set
try:
	# Validates the support user credentials.
	api_response = client.support.validate_support_user_creds(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SupportApi->validate_support_user_creds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ValidateSupportUserCredParams**](ValidateSupportUserCredParams.md)| Specifies the support user credentials. |

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

