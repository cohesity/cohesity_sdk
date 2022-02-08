# cohesity_sdk.UsersApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_session**](UsersApi.md#create_session) | **POST** /users/sessions | Create a user session
[**delete_session**](UsersApi.md#delete_session) | **DELETE** /users/sessions | Delete user sessions
[**get_security_principals**](UsersApi.md#get_security_principals) | **GET** /security-principals | Get Security Principals.


# **create_session**
> UserSession create_session(body)

Create a user session

Create a user session

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.user_session import UserSession
from cohesity_sdk.cohesity_client_v2.model.create_user_session_request_params import CreateUserSessionRequestParams
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
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


sid = "sid_example" # str | Specifies a user sid. If sid is not given system wide sessions are deleted. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete user sessions
	client.users.delete_session(sid=sid)
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

# **get_security_principals**
> SecurityPrincipals get_security_principals(sids)

Get Security Principals.

Get Security Principals

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.security_principals import SecurityPrincipals
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


sids = [
        "S-0-072888001528021798096225500850762068629-39333975650685139102691291732729478601482026-0912727550417577019298162864882916633228770521-191166478378563875565986836152-8784425528468720999697682-579364428489671318576363915338224935163074506805717279357060662066496241-415434479790599868759540626151494012626181911847617323796802209082-677715773090491175877238622700367804481067589385995284318716971548-9437255518186242126631124808712-209361142227111098265387333954577961103760673817300538998580525021695595165-175112804308695820986859-22048655",
    ] # [str] | Specifies a list of SIDs.

# example passing only required values which don't have defaults set
try:
	# Get Security Principals.
	api_response = client.users.get_security_principals(sids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->get_security_principals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sids** | **[str]**| Specifies a list of SIDs. |

### Return type

[**SecurityPrincipals**](SecurityPrincipals.md)

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

