# cohesity_sdk.UserApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group**](UserApi.md#create_group) | **POST** /groups | Create Groups
[**create_session**](UserApi.md#create_session) | **POST** /users/sessions | Create a user session
[**create_user_api_key**](UserApi.md#create_user_api_key) | **POST** /users/{userSid}/api-keys | Create a new user API key.
[**create_users**](UserApi.md#create_users) | **POST** /users | Add one or more users to Cohesity Cluster.
[**delete_group**](UserApi.md#delete_group) | **DELETE** /groups/{sid} | Delete Group
[**delete_groups**](UserApi.md#delete_groups) | **POST** /groups/delete | Delete Groups
[**delete_session**](UserApi.md#delete_session) | **DELETE** /users/sessions | Delete user sessions
[**delete_user**](UserApi.md#delete_user) | **DELETE** /users/{sid} | Delete a Cohesity (LOCAL/IdP/AD) user.
[**delete_user_api_key_by_id**](UserApi.md#delete_user_api_key_by_id) | **DELETE** /users/{userSid}/api-keys/{id} | Delete a user API key.
[**delete_users**](UserApi.md#delete_users) | **POST** /users/delete | Delete one or more Cohesity users.
[**get_active_sessions_count**](UserApi.md#get_active_sessions_count) | **GET** /users/sessions | Get sessions count
[**get_all_api_keys**](UserApi.md#get_all_api_keys) | **GET** /api-keys | Get the list of all API keys which are created or owned by the user.
[**get_group_by_sid**](UserApi.md#get_group_by_sid) | **GET** /groups/{sid} | Get Group by SID
[**get_groups**](UserApi.md#get_groups) | **GET** /groups | Get Groups.
[**get_principal_sources**](UserApi.md#get_principal_sources) | **GET** /security-principals/{sid}/sources | Fetch sources &amp; views assigned to a user/group.
[**get_security_principals**](UserApi.md#get_security_principals) | **GET** /security-principals | Get Security Principals.
[**get_user_api_key_by_id**](UserApi.md#get_user_api_key_by_id) | **GET** /users/{userSid}/api-keys/{id} | Get the API key by id.
[**get_user_api_keys**](UserApi.md#get_user_api_keys) | **GET** /users/{userSid}/api-keys | Get the list of API keys owned by the user.
[**get_user_by_sid**](UserApi.md#get_user_by_sid) | **GET** /users/{sid} | Get User by SID.
[**get_users**](UserApi.md#get_users) | **GET** /users | Get Users.
[**regenerate_s3_key**](UserApi.md#regenerate_s3_key) | **POST** /users/{sid}/s3-secret-key | Reset S3 secret access key
[**rotate_user_api_key**](UserApi.md#rotate_user_api_key) | **POST** /users/{userSid}/api-keys/{id}/rotate | Refresh an existing user API key.
[**update_group**](UserApi.md#update_group) | **PUT** /groups/{sid} | Update Group
[**update_principal_sources**](UserApi.md#update_principal_sources) | **PUT** /security-principals/{sid}/sources | Update protection sources assigned to a user/group.
[**update_user**](UserApi.md#update_user) | **PUT** /users/{sid} | Update User information.
[**update_user_api_key_by_id**](UserApi.md#update_user_api_key_by_id) | **PUT** /users/{userSid}/api-keys/{id} | Update a user API key.


# **create_group**
> Groups create_group(body)

Create Groups

If an Active Directory/IdP domain is specified, a new group is added to the Cohesity Cluster for the specified Active Directory/IdP group principal. If the LOCAL domain is specified, a new group is created directly in the default LOCAL domain on the Cohesity Cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.create_groups_params import CreateGroupsParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.groups import Groups
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateGroupsParams([
        CreateGroupParams(
            description="description_example",
            domain="domain_example",
            local_group_params=LocalGroupParams(
                user_sids=[
                    "user_sids_example",
                ],
            ),
            name="name_example",
            restricted=True,
            roles=[
                "roles_example",
            ],
            tenant_ids=[
                "tenant_ids_example",
            ],
        ),
    ]) # CreateGroupsParams | Specifies the new group parameters.

# example passing only required values which don't have defaults set
try:
	# Create Groups
	api_response = client.user.create_group(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->create_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateGroupsParams**](CreateGroupsParams.md)| Specifies the new group parameters. |

### Return type

[**Groups**](Groups.md)

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

# **create_session**
> UserSession create_session(body)

Create a user session

Create a user session

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.create_user_session_request_params import CreateUserSessionRequestParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.user_session import UserSession
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateUserSessionRequestParams(
        certificate="certificate_example",
        domain="domain_example",
        otp_code="otp_code_example",
        otp_type="email",
        password="password_example",
        private_key="private_key_example",
        username="username_example",
    ) # CreateUserSessionRequestParams | Specifies the parameters to create a user session

# example passing only required values which don't have defaults set
try:
	# Create a user session
	api_response = client.user.create_session(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->create_session: %s\n" % e)
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.created_user_api_key import CreatedUserAPIKey
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.create_or_update_api_key_request import CreateOrUpdateAPIKeyRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


user_sid = "userSid_example" # str | Specify the SID of the API key owner.
body = CreateOrUpdateAPIKeyRequest(
        expiry_time_msecs=1,
        is_active=True,
        name="name_example",
    ) # CreateOrUpdateAPIKeyRequest | Request to create a new API Key

# example passing only required values which don't have defaults set
try:
	# Create a new user API key.
	api_response = client.user.create_user_api_key(user_sid, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->create_user_api_key: %s\n" % e)
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

# **create_users**
> UsersList create_users(body)

Add one or more users to Cohesity Cluster.

Add one or more users to Cohesity Cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.users_list import UsersList
from cohesity_sdk.cluster.model.create_users_parameters import CreateUsersParameters
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateUsersParameters([
        CreateUserParameters(
            allow_smb_access_token=True,
            description="description_example",
            domain="domain_example",
            effective_time_msecs=1,
            expiry_time_msecs=1,
            local_user_params=LocalUserParams(),
            locked=True,
            restricted=True,
            roles=[
                "roles_example",
            ],
            username="username_example",
        ),
    ]) # CreateUsersParameters | If an Active Directory or an IdP domain is specified, a new user is added to the Cohesity Cluster against the specified Active Directory/IdP user principal. If the LOCAL domain is specified, a new user is created directly in the default LOCAL domain on the Cohesity Cluster.

# example passing only required values which don't have defaults set
try:
	# Add one or more users to Cohesity Cluster.
	api_response = client.user.create_users(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->create_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUsersParameters**](CreateUsersParameters.md)| If an Active Directory or an IdP domain is specified, a new user is added to the Cohesity Cluster against the specified Active Directory/IdP user principal. If the LOCAL domain is specified, a new user is created directly in the default LOCAL domain on the Cohesity Cluster. |

### Return type

[**UsersList**](UsersList.md)

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

# **delete_group**
> delete_group(sid)

Delete Group

If the group on the Cohesity Cluster was added for an Active Directory/IdP group, the referenced principal group on the Active Directory/IdP domain is NOT deleted. Only the group on the Cohesity Cluster is deleted.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


sid = "sid_example" # str | Specify the SID of the group.

# example passing only required values which don't have defaults set
try:
	# Delete Group
	client.user.delete_group(sid)
except ApiException as e:
	print("Exception when calling UserApi->delete_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specify the SID of the group. |

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

# **delete_groups**
> delete_groups(body)

Delete Groups

If the Cohesity group was created against an Active Directory/IdP, the referenced principal group on the Active Directory/IdP domain is NOT deleted. Only the group on the Cohesity Cluster is deleted.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.delete_groups_request import DeleteGroupsRequest
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = DeleteGroupsRequest(
        sids=[
            "sids_example",
        ],
    ) # DeleteGroupsRequest | Specifies the delete request payload.

# example passing only required values which don't have defaults set
try:
	# Delete Groups
	client.user.delete_groups(body)
except ApiException as e:
	print("Exception when calling UserApi->delete_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteGroupsRequest**](DeleteGroupsRequest.md)| Specifies the delete request payload. |

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

# **delete_session**
> delete_session()

Delete user sessions

Deletes all sessions for given user sid or system wide sessions

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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
	client.user.delete_session(sid=sid)
except ApiException as e:
	print("Exception when calling UserApi->delete_session: %s\n" % e)
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

# **delete_user**
> delete_user(sid)

Delete a Cohesity (LOCAL/IdP/AD) user.

Delete a Cohesity user.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


sid = "sid_example" # str | Specify the SID of the user.

# example passing only required values which don't have defaults set
try:
	# Delete a Cohesity (LOCAL/IdP/AD) user.
	client.user.delete_user(sid)
except ApiException as e:
	print("Exception when calling UserApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specify the SID of the user. |

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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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
	client.user.delete_user_api_key_by_id(user_sid, id)
except ApiException as e:
	print("Exception when calling UserApi->delete_user_api_key_by_id: %s\n" % e)
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

# **delete_users**
> delete_users(body)

Delete one or more Cohesity users.

Delete one or more Cohesity users.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.delete_users_request import DeleteUsersRequest
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = DeleteUsersRequest(
        sids=[
            "sids_example",
        ],
    ) # DeleteUsersRequest | If the Cohesity user was created against an Active Directory/IdP user, the referenced principal user on the Active Directory/IdP domain is NOT deleted. Only the user on the Cohesity Cluster is deleted.

# example passing only required values which don't have defaults set
try:
	# Delete one or more Cohesity users.
	client.user.delete_users(body)
except ApiException as e:
	print("Exception when calling UserApi->delete_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteUsersRequest**](DeleteUsersRequest.md)| If the Cohesity user was created against an Active Directory/IdP user, the referenced principal user on the Active Directory/IdP domain is NOT deleted. Only the user on the Cohesity Cluster is deleted. |

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

# **get_active_sessions_count**
> ActiveSessionsCountParams get_active_sessions_count()

Get sessions count

Get the number of user sessions.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.active_sessions_count_params import ActiveSessionsCountParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


sids = [
        "sids_example",
    ] # [str] | Filter sessions based on user sids. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get sessions count
	api_response = client.user.get_active_sessions_count(sids=sids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->get_active_sessions_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sids** | **[str]**| Filter sessions based on user sids. | [optional]

### Return type

[**ActiveSessionsCountParams**](ActiveSessionsCountParams.md)

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

# **get_all_api_keys**
> UserAPIKeys get_all_api_keys()

Get the list of all API keys which are created or owned by the user.

Get the list of all API keys which are created or owned by the user.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.user_api_keys import UserAPIKeys
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


ids = [
        "ids_example",
    ] # [str] | Filter by API Key Ids (optional)
owner_sids = [
        "ownerSids_example",
    ] # [str] | Filter by list of owner (user) SIDs (optional)
is_active = True # bool | If true, the response will only include API keys which are active. Returns all keys if the query param is not set. (optional)
is_expired = True # bool | If true, the response will only include API keys which has been expired. Returns all keys if the query param is not set. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the list of all API keys which are created or owned by the user.
	api_response = client.user.get_all_api_keys(ids=ids, owner_sids=owner_sids, is_active=is_active, is_expired=is_expired)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->get_all_api_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[str]**| Filter by API Key Ids | [optional]
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

# **get_group_by_sid**
> GroupParams get_group_by_sid(sid)

Get Group by SID

Get Group by SID.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.group_params import GroupParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


sid = "sid_example" # str | Specify the SID of the group.

# example passing only required values which don't have defaults set
try:
	# Get Group by SID
	api_response = client.user.get_group_by_sid(sid)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->get_group_by_sid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specify the SID of the group. |

### Return type

[**GroupParams**](GroupParams.md)

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

# **get_groups**
> Groups get_groups()

Get Groups.

Get groups on the Cohesity cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.groups import Groups
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


names = [
        "names_example",
    ] # [str] | Specifies a list of group names to filter. (optional)
roles = [
        "roles_example",
    ] # [str] | Specifies a list of roles to filter. (optional)
domain = "domain_example" # str | Specifies the group domain to filter. (optional)
sids = [
        "sids_example",
    ] # [str] | Specifies a list of sids to filter. (optional)
match_partial_names = True # bool | If true, the names in group names are matched by any partial rather than exactly matched. Default is false. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which groups are to be returned. (optional)
include_tenants = True # bool | IncludeTenants specifies if groups of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Groups.
	api_response = client.user.get_groups(names=names, roles=roles, domain=domain, sids=sids, match_partial_names=match_partial_names, tenant_ids=tenant_ids, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->get_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **[str]**| Specifies a list of group names to filter. | [optional]
 **roles** | **[str]**| Specifies a list of roles to filter. | [optional]
 **domain** | **str**| Specifies the group domain to filter. | [optional]
 **sids** | **[str]**| Specifies a list of sids to filter. | [optional]
 **match_partial_names** | **bool**| If true, the names in group names are matched by any partial rather than exactly matched. Default is false. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which groups are to be returned. | [optional]
 **include_tenants** | **bool**| IncludeTenants specifies if groups of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional]

### Return type

[**Groups**](Groups.md)

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

# **get_principal_sources**
> AssignedSources get_principal_sources(sid)

Fetch sources & views assigned to a user/group.

Fetches all the sources assigned to a principal.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.assigned_sources import AssignedSources
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


sid = "sid_example" # str | Specify the SID of the principal.

# example passing only required values which don't have defaults set
try:
	# Fetch sources & views assigned to a user/group.
	api_response = client.user.get_principal_sources(sid)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->get_principal_sources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specify the SID of the principal. |

### Return type

[**AssignedSources**](AssignedSources.md)

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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.security_principals import SecurityPrincipals
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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
	api_response = client.user.get_security_principals(sids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->get_security_principals: %s\n" % e)
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.user_api_key import UserAPIKey
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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
	api_response = client.user.get_user_api_key_by_id(id, user_sid)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->get_user_api_key_by_id: %s\n" % e)
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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.user_api_keys import UserAPIKeys
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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
	api_response = client.user.get_user_api_keys(user_sid)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->get_user_api_keys: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the list of API keys owned by the user.
	api_response = client.user.get_user_api_keys(user_sid, ids=ids, is_active=is_active, is_expired=is_expired)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->get_user_api_keys: %s\n" % e)
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

# **get_user_by_sid**
> UserParams get_user_by_sid(sid)

Get User by SID.

Get User by SID.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.user_params import UserParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


sid = "sid_example" # str | Specify the SID of the user.

# example passing only required values which don't have defaults set
try:
	# Get User by SID.
	api_response = client.user.get_user_by_sid(sid)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->get_user_by_sid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specify the SID of the user. |

### Return type

[**UserParams**](UserParams.md)

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
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.users_list import UsersList
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


domain = "domain_example" # str | Specifies the user domain to filter. (optional)
sids = [
        "sids_example",
    ] # [str] | Specifies a list of sids to filter. (optional)
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
	api_response = client.user.get_users(domain=domain, sids=sids, usernames=usernames, match_partial_names=match_partial_names, email_addresses=email_addresses, roles=roles, tenant_ids=tenant_ids, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->get_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Specifies the user domain to filter. | [optional]
 **sids** | **[str]**| Specifies a list of sids to filter. | [optional]
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

# **regenerate_s3_key**
> SecretKeyEntity regenerate_s3_key(sid)

Reset S3 secret access key

Reset the S3 secret access key for the specified user on the Cohesity Cluster. Admin users who have the Manage Users privilege can generate keys for other users. When generating a new key, anyone using the old key will lose access until they retrieve and use the newly generated key. The user must have the following privilege to access this endpoint, 'Manage S3 Keys'.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.secret_key_entity import SecretKeyEntity
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


sid = "sid_example" # str | Specify the SID of the user.

# example passing only required values which don't have defaults set
try:
	# Reset S3 secret access key
	api_response = client.user.regenerate_s3_key(sid)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->regenerate_s3_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specify the SID of the user. |

### Return type

[**SecretKeyEntity**](SecretKeyEntity.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_user_api_key**
> CreatedUserAPIKey rotate_user_api_key(user_sid, id)

Refresh an existing user API key.

Refresh an existing user API key.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.created_user_api_key import CreatedUserAPIKey
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
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
	api_response = client.user.rotate_user_api_key(user_sid, id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->rotate_user_api_key: %s\n" % e)
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

# **update_group**
> GroupParams update_group(sid, body)

Update Group

Only group settings on the Cohesity Cluster are updated. No changes are made to the referenced group principal on the Active Directory/IdP.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.group_params import GroupParams
from cohesity_sdk.cluster.model.update_group_parameters import UpdateGroupParameters
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


sid = "sid_example" # str | Specify the SID of the group.
body = UpdateGroupParameters(
        description="description_example",
        local_group_params=LocalGroupParams(
            user_sids=[
                "user_sids_example",
            ],
        ),
        restricted=True,
        roles=[
            "roles_example",
        ],
        tenant_ids=[
            "tenant_ids_example",
        ],
    ) # UpdateGroupParameters | Specifies the group information.

# example passing only required values which don't have defaults set
try:
	# Update Group
	api_response = client.user.update_group(sid, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->update_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specify the SID of the group. |
 **body** | [**UpdateGroupParameters**](UpdateGroupParameters.md)| Specifies the group information. |

### Return type

[**GroupParams**](GroupParams.md)

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

# **update_principal_sources**
> AssignedSources update_principal_sources(sid, body)

Update protection sources assigned to a user/group.

Update protection sources assigned to a user/group.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.assigned_sources import AssignedSources
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


sid = "sid_example" # str | Specify the SID of the principal.
body = AssignedSources(
        source_ids=[
            1,
        ],
        view_ids=[
            1,
        ],
    ) # AssignedSources | Specify the sources to be assigned to a principal.

# example passing only required values which don't have defaults set
try:
	# Update protection sources assigned to a user/group.
	api_response = client.user.update_principal_sources(sid, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->update_principal_sources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specify the SID of the principal. |
 **body** | [**AssignedSources**](AssignedSources.md)| Specify the sources to be assigned to a principal. |

### Return type

[**AssignedSources**](AssignedSources.md)

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

# **update_user**
> UserParams update_user(sid, body)

Update User information.

Update an existing user on the Cohesity Cluster. Only user settings on the Cohesity Cluster are updated. No changes are made to the referenced user principal on the Active Directory/IdP.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.update_user_parameters import UpdateUserParameters
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.user_params import UserParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


sid = "sid_example" # str | Specify the SID of the user.
body = UpdateUserParameters() # UpdateUserParameters | Specifies the user information.

# example passing only required values which don't have defaults set
try:
	# Update User information.
	api_response = client.user.update_user(sid, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specify the SID of the user. |
 **body** | [**UpdateUserParameters**](UpdateUserParameters.md)| Specifies the user information. |

### Return type

[**UserParams**](UserParams.md)

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

# **update_user_api_key_by_id**
> UserAPIKey update_user_api_key_by_id(id, user_sid, body)

Update a user API key.

Update a user API key.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.user_api_key import UserAPIKey
from cohesity_sdk.cluster.model.create_or_update_api_key_request import CreateOrUpdateAPIKeyRequest
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = "id_example" # str | Specify the id of the API key.
user_sid = "userSid_example" # str | Specify the SID of the API key owner.
body = CreateOrUpdateAPIKeyRequest(
        expiry_time_msecs=1,
        is_active=True,
        name="name_example",
    ) # CreateOrUpdateAPIKeyRequest | Request to update a user API key

# example passing only required values which don't have defaults set
try:
	# Update a user API key.
	api_response = client.user.update_user_api_key_by_id(id, user_sid, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UserApi->update_user_api_key_by_id: %s\n" % e)
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

