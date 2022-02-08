# cohesity_sdk.MfaApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_email_otp**](MfaApi.md#create_email_otp) | **POST** /email-otp | Creates a new OTP to be sent to the user email.
[**create_totp_key**](MfaApi.md#create_totp_key) | **POST** /totp-key | Create a new TOTP secret URI and store the secret key.
[**get_mfa_config**](MfaApi.md#get_mfa_config) | **GET** /mfa-config | Returns the current MFA configuration.
[**get_support_mfa_config**](MfaApi.md#get_support_mfa_config) | **GET** /support-user/mfa | Returns the current MFA configuration.
[**send_email_otp**](MfaApi.md#send_email_otp) | **POST** /send-email-otp | Creates a new OTP to be sent to the user email.
[**send_support_email_otp**](MfaApi.md#send_support_email_otp) | **POST** /support-user/send-email-otp | Creates a new OTP to be sent to the linux support user email.
[**update_mfa_config**](MfaApi.md#update_mfa_config) | **PUT** /mfa-config | Stores the updated MFA configuration.
[**update_support_mfa_config**](MfaApi.md#update_support_mfa_config) | **PATCH** /support-user/mfa | Stores the updated MFA configuration.
[**verify_support_user_totp**](MfaApi.md#verify_support_user_totp) | **POST** /support-user/verify-totp | Verify the totp code for support user.


# **create_email_otp**
> create_email_otp()

Creates a new OTP to be sent to the user email.

Creates a new One Time Password for the user email. This is used for API login.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.create_email_otp_request_body import CreateEmailOtpRequestBody
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateEmailOtpRequestBody(
        username="username_example",
        password="password_example",
        domain="domain_example",
    ) # CreateEmailOtpRequestBody | Specifies the parameters to send email OTP. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Creates a new OTP to be sent to the user email.
	client.mfa.create_email_otp(body=body)
except ApiException as e:
	print("Exception when calling MfaApi->create_email_otp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEmailOtpRequestBody**](CreateEmailOtpRequestBody.md)| Specifies the parameters to send email OTP. | [optional]

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
**204** | Successfully sent an email to the configured address |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_totp_key**
> TotpKeyInfo create_totp_key(body)

Create a new TOTP secret URI and store the secret key.

Create a TOTP key.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.totp_key_info import TotpKeyInfo
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.create_totp_key_request_body import CreateTotpKeyRequestBody
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateTotpKeyRequestBody(
        totp_key_name="totp_key_name_example",
    ) # CreateTotpKeyRequestBody | Specifies the key id for creating the TOTP key.

# example passing only required values which don't have defaults set
try:
	# Create a new TOTP secret URI and store the secret key.
	api_response = client.mfa.create_totp_key(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling MfaApi->create_totp_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTotpKeyRequestBody**](CreateTotpKeyRequestBody.md)| Specifies the key id for creating the TOTP key. |

### Return type

[**TotpKeyInfo**](TotpKeyInfo.md)

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

# **get_mfa_config**
> MfaConfigInfo get_mfa_config()

Returns the current MFA configuration.

Returns the current MFA configuration for the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.mfa_config_info import MfaConfigInfo
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Returns the current MFA configuration.
	api_response = client.mfa.get_mfa_config()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling MfaApi->get_mfa_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MfaConfigInfo**](MfaConfigInfo.md)

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

# **get_support_mfa_config**
> SupportMfaConfigInfo get_support_mfa_config()

Returns the current MFA configuration.

Returns the current MFA configuration for support user.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.support_mfa_config_info import SupportMfaConfigInfo
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Returns the current MFA configuration.
	api_response = client.mfa.get_support_mfa_config()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling MfaApi->get_support_mfa_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SupportMfaConfigInfo**](SupportMfaConfigInfo.md)

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

# **send_email_otp**
> send_email_otp()

Creates a new OTP to be sent to the user email.

Creates a new One Time Password for the user email

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Creates a new OTP to be sent to the user email.
	client.mfa.send_email_otp()
except ApiException as e:
	print("Exception when calling MfaApi->send_email_otp: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**204** | Successfully sent an email to the configured address |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_support_email_otp**
> send_support_email_otp()

Creates a new OTP to be sent to the linux support user email.

Creates a new one time password for linux support user email

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)



# example, this endpoint has no required or optional parameters
try:
	# Creates a new OTP to be sent to the linux support user email.
	client.mfa.send_support_email_otp()
except ApiException as e:
	print("Exception when calling MfaApi->send_support_email_otp: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**204** | Successfully sent an email to the configured address |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mfa_config**
> MfaConfigInfo update_mfa_config(body)

Stores the updated MFA configuration.

Stores the updated MFA configuration for the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.mfa_config_info import MfaConfigInfo
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = MfaConfigInfo(
        enabled=False,
        authentication_types=[
            "email",
        ],
        retain_user_mfa_settings=True,
    ) # MfaConfigInfo | The update request for the MFA Settings

# example passing only required values which don't have defaults set
try:
	# Stores the updated MFA configuration.
	api_response = client.mfa.update_mfa_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling MfaApi->update_mfa_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MfaConfigInfo**](MfaConfigInfo.md)| The update request for the MFA Settings |

### Return type

[**MfaConfigInfo**](MfaConfigInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_support_mfa_config**
> UpdateMFAResult update_support_mfa_config(body)

Stores the updated MFA configuration.

Update MFA configuration for support user.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.update_mfa_result import UpdateMFAResult
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.support_mfa_config_info import SupportMfaConfigInfo
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = SupportMfaConfigInfo(
        enabled=False,
        mfa_type="email",
        email="email_example",
    ) # SupportMfaConfigInfo | The update request for the MFA Settings

# example passing only required values which don't have defaults set
try:
	# Stores the updated MFA configuration.
	api_response = client.mfa.update_support_mfa_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling MfaApi->update_support_mfa_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupportMfaConfigInfo**](SupportMfaConfigInfo.md)| The update request for the MFA Settings |

### Return type

[**UpdateMFAResult**](UpdateMFAResult.md)

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

# **verify_support_user_totp**
> VerifyTotpResult verify_support_user_totp(body)

Verify the totp code for support user.

Verify totp code for support user.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.verify_totp_result import VerifyTotpResult
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.verify_totp_request import VerifyTotpRequest
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = VerifyTotpRequest(
        totp_code="totp_code_example",
    ) # VerifyTotpRequest | Totp code to be verified.

# example passing only required values which don't have defaults set
try:
	# Verify the totp code for support user.
	api_response = client.mfa.verify_support_user_totp(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling MfaApi->verify_support_user_totp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyTotpRequest**](VerifyTotpRequest.md)| Totp code to be verified. |

### Return type

[**VerifyTotpResult**](VerifyTotpResult.md)

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

