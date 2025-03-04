# cohesity_sdk.MFAApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_email_otp**](MFAApi.md#create_email_otp) | **POST** /email-otp | Creates a new OTP to be sent to the user email.
[**create_totp_key**](MFAApi.md#create_totp_key) | **POST** /totp-key | Create a new TOTP secret URI and store the secret key.
[**get_mfa_config**](MFAApi.md#get_mfa_config) | **GET** /mfa-config | Returns the current MFA configuration.
[**get_support_mfa_config**](MFAApi.md#get_support_mfa_config) | **GET** /support-user/mfa | Returns the current MFA configuration.
[**send_email_otp**](MFAApi.md#send_email_otp) | **POST** /send-email-otp | Creates a new OTP to be sent to the user email.
[**send_support_email_otp**](MFAApi.md#send_support_email_otp) | **POST** /support-user/send-email-otp | Creates a new OTP to be sent to the linux support user email.
[**update_mfa_config**](MFAApi.md#update_mfa_config) | **PUT** /mfa-config | Stores the updated MFA configuration.
[**update_support_mfa_config**](MFAApi.md#update_support_mfa_config) | **PATCH** /support-user/mfa | Stores the updated MFA configuration.
[**verify_support_user_totp**](MFAApi.md#verify_support_user_totp) | **POST** /support-user/verify-totp | Verify the totp code for support user.


# **create_email_otp**
> create_email_otp(body=body)

Creates a new OTP to be sent to the user email.

Creates a new One Time Password for the user email. This is used for API login.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.create_email_otp_request_body import CreateEmailOtpRequestBody
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.MFAApi(api_client)
    body = cohesity_sdk.CreateEmailOtpRequestBody() # CreateEmailOtpRequestBody | Specifies the parameters to send email OTP. (optional)

    try:
        # Creates a new OTP to be sent to the user email.
        api_instance.create_email_otp(body=body)
    except Exception as e:
        print("Exception when calling MFAApi->create_email_otp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEmailOtpRequestBody**](CreateEmailOtpRequestBody.md)| Specifies the parameters to send email OTP. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.create_totp_key_request_body import CreateTotpKeyRequestBody
from cohesity_sdk.models.totp_key_info import TotpKeyInfo
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.MFAApi(api_client)
    body = cohesity_sdk.CreateTotpKeyRequestBody() # CreateTotpKeyRequestBody | Specifies the key id for creating the TOTP key.

    try:
        # Create a new TOTP secret URI and store the secret key.
        api_response = api_instance.create_totp_key(body)
        print("The response of MFAApi->create_totp_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAApi->create_totp_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTotpKeyRequestBody**](CreateTotpKeyRequestBody.md)| Specifies the key id for creating the TOTP key. | 

### Return type

[**TotpKeyInfo**](TotpKeyInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.mfa_config_info import MfaConfigInfo
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.MFAApi(api_client)

    try:
        # Returns the current MFA configuration.
        api_response = api_instance.get_mfa_config()
        print("The response of MFAApi->get_mfa_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAApi->get_mfa_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MfaConfigInfo**](MfaConfigInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.support_mfa_config_info import SupportMfaConfigInfo
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.MFAApi(api_client)

    try:
        # Returns the current MFA configuration.
        api_response = api_instance.get_support_mfa_config()
        print("The response of MFAApi->get_support_mfa_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAApi->get_support_mfa_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SupportMfaConfigInfo**](SupportMfaConfigInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.MFAApi(api_client)

    try:
        # Creates a new OTP to be sent to the user email.
        api_instance.send_email_otp()
    except Exception as e:
        print("Exception when calling MFAApi->send_email_otp: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.MFAApi(api_client)

    try:
        # Creates a new OTP to be sent to the linux support user email.
        api_instance.send_support_email_otp()
    except Exception as e:
        print("Exception when calling MFAApi->send_support_email_otp: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.mfa_config_info import MfaConfigInfo
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.MFAApi(api_client)
    body = cohesity_sdk.MfaConfigInfo() # MfaConfigInfo | The update request for the MFA Settings

    try:
        # Stores the updated MFA configuration.
        api_response = api_instance.update_mfa_config(body)
        print("The response of MFAApi->update_mfa_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAApi->update_mfa_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MfaConfigInfo**](MfaConfigInfo.md)| The update request for the MFA Settings | 

### Return type

[**MfaConfigInfo**](MfaConfigInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.support_mfa_config_info import SupportMfaConfigInfo
from cohesity_sdk.models.update_mfa_result import UpdateMFAResult
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.MFAApi(api_client)
    body = cohesity_sdk.SupportMfaConfigInfo() # SupportMfaConfigInfo | The update request for the MFA Settings

    try:
        # Stores the updated MFA configuration.
        api_response = api_instance.update_support_mfa_config(body)
        print("The response of MFAApi->update_support_mfa_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAApi->update_support_mfa_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupportMfaConfigInfo**](SupportMfaConfigInfo.md)| The update request for the MFA Settings | 

### Return type

[**UpdateMFAResult**](UpdateMFAResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk
from cohesity_sdk.models.verify_totp_request import VerifyTotpRequest
from cohesity_sdk.models.verify_totp_result import VerifyTotpResult
from cohesity_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.Configuration(
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.MFAApi(api_client)
    body = cohesity_sdk.VerifyTotpRequest() # VerifyTotpRequest | Totp code to be verified.

    try:
        # Verify the totp code for support user.
        api_response = api_instance.verify_support_user_totp(body)
        print("The response of MFAApi->verify_support_user_totp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAApi->verify_support_user_totp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyTotpRequest**](VerifyTotpRequest.md)| Totp code to be verified. | 

### Return type

[**VerifyTotpResult**](VerifyTotpResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

