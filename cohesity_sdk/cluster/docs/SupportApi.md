# cohesity_sdk.SupportApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_unlock_linux_user**](SupportApi.md#execute_unlock_linux_user) | **PUT** /support-user/state | Unlock the linux user account if the user gets locked out.
[**get_support_user_config**](SupportApi.md#get_support_user_config) | **GET** /support-user/config | Get support user configuration.
[**update_support_user_config**](SupportApi.md#update_support_user_config) | **PUT** /support-user/config | Update support user configuration.
[**validate_support_user_creds**](SupportApi.md#validate_support_user_creds) | **POST** /support-user/config/validate | Validates the support user credentials.


# **execute_unlock_linux_user**
> SuccessResp execute_unlock_linux_user(body)

Unlock the linux user account if the user gets locked out.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Unlock the linux user account if the user gets locked out and make it active.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.success_resp import SuccessResp
from cohesity_sdk.cluster.model.unlock_linux_user_params import UnlockLinuxUserParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = UnlockLinuxUserParams(
        state="Active",
        username="username_example",
    ) # UnlockLinuxUserParams | Specifies the linux user and its state.

# example passing only required values which don't have defaults set
try:
	# Unlock the linux user account if the user gets locked out.
	api_response = client.support.execute_unlock_linux_user(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling SupportApi->execute_unlock_linux_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnlockLinuxUserParams**](UnlockLinuxUserParams.md)| Specifies the linux user and its state. |

### Return type

[**SuccessResp**](SuccessResp.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_support_user_config**
> SupportUserConfig get_support_user_config()

Get support user configuration.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Cohesity provides a support user account for improved security and you need to use the support user account to log in to the Cohesity cluster bash shell using SSH. This endpoint returns the current support user configuration on the Cohesity cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update support user's configuration. This allows you to update the support user's password and/or grant sudo access to the user.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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
        sudo_access_end_timestamp_msecs=1,
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Validates the support user credentials.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

