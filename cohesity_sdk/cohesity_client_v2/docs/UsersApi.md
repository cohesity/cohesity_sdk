# cohesity_sdk.UsersApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_session**](UsersApi.md#create_session) | **POST** /users/sessions | Create a user session
[**create_user_api_key**](UsersApi.md#create_user_api_key) | **POST** /users/{userSid}/api-keys | Create a new user API key.
[**delete_session**](UsersApi.md#delete_session) | **DELETE** /users/sessions | Delete user sessions
[**delete_user_api_key_by_id**](UsersApi.md#delete_user_api_key_by_id) | **DELETE** /users/{userSid}/api-keys/{id} | Delete a user API key.
[**get_all_api_keys**](UsersApi.md#get_all_api_keys) | **GET** /api-keys | Get the list of all API keys which are created or owned by the user.
[**get_security_principals**](UsersApi.md#get_security_principals) | **GET** /security-principals | Get Security Principals.
[**get_user_api_key_by_id**](UsersApi.md#get_user_api_key_by_id) | **GET** /users/{userSid}/api-keys/{id} | Get the API key by id.
[**get_user_api_keys**](UsersApi.md#get_user_api_keys) | **GET** /users/{userSid}/api-keys | Get the list of API keys owned by the user.
[**get_user_ui_config**](UsersApi.md#get_user_ui_config) | **GET** /users/ui-config | Get user UI config.
[**get_users**](UsersApi.md#get_users) | **GET** /users | Get Users.
[**rotate_user_api_key**](UsersApi.md#rotate_user_api_key) | **POST** /users/{userSid}/api-keys/{id}/rotate | Refresh an existing user API key.
[**update_user_api_key_by_id**](UsersApi.md#update_user_api_key_by_id) | **PUT** /users/{userSid}/api-keys/{id} | Update a user API key.
[**update_user_ui_config**](UsersApi.md#update_user_ui_config) | **PUT** /users/ui-config | Update user UI config.


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

# **create_user_api_key**
> CreatedUserAPIKey create_user_api_key(user_sid, body)

Create a new user API key.

Create a new user API key.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.created_user_api_key import CreatedUserAPIKey
from cohesity_sdk.cohesity_client_v2.model.create_or_update_api_key_request import CreateOrUpdateAPIKeyRequest
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


user_sid = "userSid_example" # str | Specify the SID of the API key owner.
body = CreateOrUpdateAPIKeyRequest(
        name="name_example",
        is_active=True,
        expiry_time_msecs=1,
    ) # CreateOrUpdateAPIKeyRequest | Request to create a new API Key

# example passing only required values which don't have defaults set
try:
	# Create a new user API key.
	api_response = client.users.create_user_api_key(user_sid, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->create_user_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_sid** | **str**| Specify the SID of the API key owner. |
 **body** | [**CreateOrUpdateAPIKeyRequest**](CreateOrUpdateAPIKeyRequest.md)| Request to create a new API Key |

### Return type

[**CreatedUserAPIKey**](CreatedUserAPIKey.md)

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

# **delete_user_api_key_by_id**
> delete_user_api_key_by_id(user_sid, id)

Delete a user API key.

Delete a user API key.

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


user_sid = "userSid_example" # str | Specify the SID of the API key owner.
id = "id_example" # str | Specify the id of the API key.

# example passing only required values which don't have defaults set
try:
	# Delete a user API key.
	client.users.delete_user_api_key_by_id(user_sid, id)
except ApiException as e:
	print("Exception when calling UsersApi->delete_user_api_key_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_sid** | **str**| Specify the SID of the API key owner. |
 **id** | **str**| Specify the id of the API key. |

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

# **get_all_api_keys**
> UserAPIKeys get_all_api_keys()

Get the list of all API keys which are created or owned by the user.

Get the list of all API keys which are created or owned by the user.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.user_api_keys import UserAPIKeys
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


owner_sids = [
        "ownerSids_example",
    ] # [str] | Filter by list of owner (user) SIDs (optional)
is_active = True # bool | If true, the response will only include API keys which are active. Returns all keys if the query param is not set. (optional)
is_expired = True # bool | If true, the response will only include API keys which has been expired. Returns all keys if the query param is not set. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the list of all API keys which are created or owned by the user.
	api_response = client.users.get_all_api_keys(owner_sids=owner_sids, is_active=is_active, is_expired=is_expired)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->get_all_api_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_sids** | **[str]**| Filter by list of owner (user) SIDs | [optional]
 **is_active** | **bool**| If true, the response will only include API keys which are active. Returns all keys if the query param is not set. | [optional]
 **is_expired** | **bool**| If true, the response will only include API keys which has been expired. Returns all keys if the query param is not set. | [optional]

### Return type

[**UserAPIKeys**](UserAPIKeys.md)

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

# **get_user_api_key_by_id**
> UserAPIKey get_user_api_key_by_id(id, user_sid)

Get the API key by id.

Get the API key by id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.user_api_key import UserAPIKey
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "id_example" # str | Specify the id of the API key.
user_sid = "userSid_example" # str | Specify the SID of the API key owner.

# example passing only required values which don't have defaults set
try:
	# Get the API key by id.
	api_response = client.users.get_user_api_key_by_id(id, user_sid)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->get_user_api_key_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify the id of the API key. |
 **user_sid** | **str**| Specify the SID of the API key owner. |

### Return type

[**UserAPIKey**](UserAPIKey.md)

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

# **get_user_api_keys**
> UserAPIKeys get_user_api_keys(user_sid)

Get the list of API keys owned by the user.

Returns the list of API keys owned by the user. For security reasons there is no way to retrieve the key itself after it's created.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.user_api_keys import UserAPIKeys
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


user_sid = "userSid_example" # str | Specify the SID of the API key owner.
ids = [
        "ids_example",
    ] # [str] | Filter by API Key Ids (optional)
is_active = True # bool | If true, the response will only include API keys which are active. Returns all keys if the query param is not set. (optional)
is_expired = True # bool | If true, the response will only include API keys which has been expired. Returns all keys if the query param is not set. (optional)

# example passing only required values which don't have defaults set
try:
	# Get the list of API keys owned by the user.
	api_response = client.users.get_user_api_keys(user_sid)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->get_user_api_keys: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the list of API keys owned by the user.
	api_response = client.users.get_user_api_keys(user_sid, ids=ids, is_active=is_active, is_expired=is_expired)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->get_user_api_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_sid** | **str**| Specify the SID of the API key owner. |
 **ids** | **[str]**| Filter by API Key Ids | [optional]
 **is_active** | **bool**| If true, the response will only include API keys which are active. Returns all keys if the query param is not set. | [optional]
 **is_expired** | **bool**| If true, the response will only include API keys which has been expired. Returns all keys if the query param is not set. | [optional]

### Return type

[**UserAPIKeys**](UserAPIKeys.md)

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

# **get_user_ui_config**
> UserUiConfig get_user_ui_config()

Get user UI config.

Get customized UI config for the logged in user.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.user_ui_config import UserUiConfig
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
	# Get user UI config.
	api_response = client.users.get_user_ui_config()
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->get_user_ui_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UserUiConfig**](UserUiConfig.md)

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

# **get_users**
> UsersList get_users()

Get Users.

Get Users.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.users_list import UsersList
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


domain = "domain_example" # str | Specifies the user domain to filter. (optional)
usernames = [
        "usernames_example",
    ] # [str] | Specifies a list of usernames to filter. (optional)
match_partial_names = True # bool | If true, the names in usernames are matched by any partial rather than exactly matched. (optional)
email_addresses = [
        "emailAddresses_example",
    ] # [str] | Specifies a list of email addresses to filter. (optional)
roles = [
        "roles_example",
    ] # [str] | Specifies a list of roles to filter. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which users are to be returned. (optional)
include_tenants = True # bool | IncludeTenants specifies if users of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Users.
	api_response = client.users.get_users(domain=domain, usernames=usernames, match_partial_names=match_partial_names, email_addresses=email_addresses, roles=roles, tenant_ids=tenant_ids, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->get_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Specifies the user domain to filter. | [optional]
 **usernames** | **[str]**| Specifies a list of usernames to filter. | [optional]
 **match_partial_names** | **bool**| If true, the names in usernames are matched by any partial rather than exactly matched. | [optional]
 **email_addresses** | **[str]**| Specifies a list of email addresses to filter. | [optional]
 **roles** | **[str]**| Specifies a list of roles to filter. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which users are to be returned. | [optional]
 **include_tenants** | **bool**| IncludeTenants specifies if users of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional]

### Return type

[**UsersList**](UsersList.md)

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

# **rotate_user_api_key**
> CreatedUserAPIKey rotate_user_api_key(user_sid, id)

Refresh an existing user API key.

Refresh an existing user API key.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.created_user_api_key import CreatedUserAPIKey
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


user_sid = "userSid_example" # str | Specify the SID of the API key owner.
id = "id_example" # str | Specify the id of the API key.

# example passing only required values which don't have defaults set
try:
	# Refresh an existing user API key.
	api_response = client.users.rotate_user_api_key(user_sid, id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->rotate_user_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_sid** | **str**| Specify the SID of the API key owner. |
 **id** | **str**| Specify the id of the API key. |

### Return type

[**CreatedUserAPIKey**](CreatedUserAPIKey.md)

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

# **update_user_api_key_by_id**
> UserAPIKey update_user_api_key_by_id(id, user_sid, body)

Update a user API key.

Update a user API key.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.user_api_key import UserAPIKey
from cohesity_sdk.cohesity_client_v2.model.create_or_update_api_key_request import CreateOrUpdateAPIKeyRequest
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "id_example" # str | Specify the id of the API key.
user_sid = "userSid_example" # str | Specify the SID of the API key owner.
body = CreateOrUpdateAPIKeyRequest(
        name="name_example",
        is_active=True,
        expiry_time_msecs=1,
    ) # CreateOrUpdateAPIKeyRequest | Request to update a user API key

# example passing only required values which don't have defaults set
try:
	# Update a user API key.
	api_response = client.users.update_user_api_key_by_id(id, user_sid, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->update_user_api_key_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify the id of the API key. |
 **user_sid** | **str**| Specify the SID of the API key owner. |
 **body** | [**CreateOrUpdateAPIKeyRequest**](CreateOrUpdateAPIKeyRequest.md)| Request to update a user API key |

### Return type

[**UserAPIKey**](UserAPIKey.md)

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

# **update_user_ui_config**
> UserUiConfig update_user_ui_config(body)

Update user UI config.

Update customized UI config for the logged in user.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.user_ui_config import UserUiConfig
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = UserUiConfig(
        preferences="preferences_example",
        locale="locale_example",
    ) # UserUiConfig | Specifies the user UI config.

# example passing only required values which don't have defaults set
try:
	# Update user UI config.
	api_response = client.users.update_user_ui_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->update_user_ui_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserUiConfig**](UserUiConfig.md)| Specifies the user UI config. |

### Return type

[**UserUiConfig**](UserUiConfig.md)

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

