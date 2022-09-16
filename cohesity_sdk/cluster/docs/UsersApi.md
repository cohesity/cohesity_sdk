# cohesity_sdk.UsersApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_session**](UsersApi.md#create_session) | **POST** /users/sessions | Create a user session
[**delete_session**](UsersApi.md#delete_session) | **DELETE** /users/sessions | Delete user sessions


# **create_session**
> UserSession create_session(body)

Create a user session

Create a user session

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.create_user_session_request_params import CreateUserSessionRequestParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.user_session import UserSession
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateUserSessionRequestParams(
        username="username_example",
        password="password_example",
        domain="domain_example",
        certificate="certificate_example",
        private_key="private_key_example",
        otp_code="otp_code_example",
        otp_type="email",
    ) # CreateUserSessionRequestParams | Specifies the parameters to create a user session

# example passing only required values which don't have defaults set
try:
	# Create a user session
	api_response = client.users.create_session(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->create_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserSessionRequestParams**](CreateUserSessionRequestParams.md)| Specifies the parameters to create a user session |

### Return type

[**UserSession**](UserSession.md)

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

# **delete_session**
> delete_session()

Delete user sessions

Deletes all sessions for given user sid or system wide sessions

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


sid = "sid_example" # str | Specifies a user sid. If sid is not given system wide sessions are deleted. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete user sessions
	client.[class Tag {
    name: Users
    description: null
    externalDocs: null
}].delete_session(sid=sid)
except ApiException as e:
	print("Exception when calling UsersApi->delete_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specifies a user sid. If sid is not given system wide sessions are deleted. | [optional]

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

