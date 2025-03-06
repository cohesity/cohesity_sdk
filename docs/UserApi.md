# cohesity_sdk.cluster.UserApi

All URIs are relative to */v2*

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.create_group_params import CreateGroupParams
from cohesity_sdk.cluster.models.groups import Groups
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    body = [cohesity_sdk.cluster.CreateGroupParams()] # List[CreateGroupParams] | Specifies the new group parameters.

    try:
        # Create Groups
        api_response = api_instance.create_group(body)
        print("The response of UserApi->create_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->create_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**List[CreateGroupParams]**](CreateGroupParams.md)| Specifies the new group parameters. | 

### Return type

[**Groups**](Groups.md)

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

# **create_session**
> UserSession create_session(body)

Create a user session

Create a user session

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.create_user_session_request_params import CreateUserSessionRequestParams
from cohesity_sdk.cluster.models.user_session import UserSession
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    body = cohesity_sdk.cluster.CreateUserSessionRequestParams() # CreateUserSessionRequestParams | Specifies the parameters to create a user session

    try:
        # Create a user session
        api_response = api_instance.create_session(body)
        print("The response of UserApi->create_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->create_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserSessionRequestParams**](CreateUserSessionRequestParams.md)| Specifies the parameters to create a user session | 

### Return type

[**UserSession**](UserSession.md)

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

# **create_user_api_key**
> CreatedUserAPIKey create_user_api_key(user_sid, body)

Create a new user API key.

Create a new user API key.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.create_or_update_api_key_request import CreateOrUpdateAPIKeyRequest
from cohesity_sdk.cluster.models.created_user_api_key import CreatedUserAPIKey
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    user_sid = 'user_sid_example' # str | Specify the SID of the API key owner.
    body = cohesity_sdk.cluster.CreateOrUpdateAPIKeyRequest() # CreateOrUpdateAPIKeyRequest | Request to create a new API Key

    try:
        # Create a new user API key.
        api_response = api_instance.create_user_api_key(user_sid, body)
        print("The response of UserApi->create_user_api_key:\n")
        pprint(api_response)
    except Exception as e:
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

# **create_users**
> UsersList create_users(body)

Add one or more users to Cohesity Cluster.

Add one or more users to Cohesity Cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.create_user_parameters import CreateUserParameters
from cohesity_sdk.cluster.models.users_list import UsersList
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    body = [cohesity_sdk.cluster.CreateUserParameters()] # List[CreateUserParameters] | If an Active Directory or an IdP domain is specified, a new user is added to the Cohesity Cluster against the specified Active Directory/IdP user principal. If the LOCAL domain is specified, a new user is created directly in the default LOCAL domain on the Cohesity Cluster.

    try:
        # Add one or more users to Cohesity Cluster.
        api_response = api_instance.create_users(body)
        print("The response of UserApi->create_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->create_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**List[CreateUserParameters]**](CreateUserParameters.md)| If an Active Directory or an IdP domain is specified, a new user is added to the Cohesity Cluster against the specified Active Directory/IdP user principal. If the LOCAL domain is specified, a new user is created directly in the default LOCAL domain on the Cohesity Cluster. | 

### Return type

[**UsersList**](UsersList.md)

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

# **delete_group**
> delete_group(sid)

Delete Group

If the group on the Cohesity Cluster was added for an Active Directory/IdP group, the referenced principal group on the Active Directory/IdP domain is NOT deleted. Only the group on the Cohesity Cluster is deleted.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    sid = 'sid_example' # str | Specify the SID of the group.

    try:
        # Delete Group
        api_instance.delete_group(sid)
    except Exception as e:
        print("Exception when calling UserApi->delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specify the SID of the group. | 

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
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_groups**
> delete_groups(body)

Delete Groups

If the Cohesity group was created against an Active Directory/IdP, the referenced principal group on the Active Directory/IdP domain is NOT deleted. Only the group on the Cohesity Cluster is deleted.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.delete_groups_request import DeleteGroupsRequest
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    body = cohesity_sdk.cluster.DeleteGroupsRequest() # DeleteGroupsRequest | Specifies the delete request payload.

    try:
        # Delete Groups
        api_instance.delete_groups(body)
    except Exception as e:
        print("Exception when calling UserApi->delete_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteGroupsRequest**](DeleteGroupsRequest.md)| Specifies the delete request payload. | 

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
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_session**
> delete_session(sid=sid)

Delete user sessions

Deletes all sessions for given user sid or system wide sessions

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    sid = 'sid_example' # str | Specifies a user sid. If sid is not given system wide sessions are deleted. (optional)

    try:
        # Delete user sessions
        api_instance.delete_session(sid=sid)
    except Exception as e:
        print("Exception when calling UserApi->delete_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specifies a user sid. If sid is not given system wide sessions are deleted. | [optional] 

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
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(sid)

Delete a Cohesity (LOCAL/IdP/AD) user.

Delete a Cohesity user.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    sid = 'sid_example' # str | Specify the SID of the user.

    try:
        # Delete a Cohesity (LOCAL/IdP/AD) user.
        api_instance.delete_user(sid)
    except Exception as e:
        print("Exception when calling UserApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specify the SID of the user. | 

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
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_api_key_by_id**
> delete_user_api_key_by_id(user_sid, id)

Delete a user API key.

Delete a user API key.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    user_sid = 'user_sid_example' # str | Specify the SID of the API key owner.
    id = 'id_example' # str | Specify the id of the API key.

    try:
        # Delete a user API key.
        api_instance.delete_user_api_key_by_id(user_sid, id)
    except Exception as e:
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

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.delete_users_request import DeleteUsersRequest
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    body = cohesity_sdk.cluster.DeleteUsersRequest() # DeleteUsersRequest | If the Cohesity user was created against an Active Directory/IdP user, the referenced principal user on the Active Directory/IdP domain is NOT deleted. Only the user on the Cohesity Cluster is deleted.

    try:
        # Delete one or more Cohesity users.
        api_instance.delete_users(body)
    except Exception as e:
        print("Exception when calling UserApi->delete_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteUsersRequest**](DeleteUsersRequest.md)| If the Cohesity user was created against an Active Directory/IdP user, the referenced principal user on the Active Directory/IdP domain is NOT deleted. Only the user on the Cohesity Cluster is deleted. | 

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
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_sessions_count**
> ActiveSessionsCountParams get_active_sessions_count(sids=sids)

Get sessions count

Get the number of user sessions.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.active_sessions_count_params import ActiveSessionsCountParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    sids = ['sids_example'] # List[str] | Filter sessions based on user sids. (optional)

    try:
        # Get sessions count
        api_response = api_instance.get_active_sessions_count(sids=sids)
        print("The response of UserApi->get_active_sessions_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_active_sessions_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sids** | [**List[str]**](str.md)| Filter sessions based on user sids. | [optional] 

### Return type

[**ActiveSessionsCountParams**](ActiveSessionsCountParams.md)

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

# **get_all_api_keys**
> UserAPIKeys get_all_api_keys(ids=ids, owner_sids=owner_sids, is_active=is_active, is_expired=is_expired)

Get the list of all API keys which are created or owned by the user.

Get the list of all API keys which are created or owned by the user.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.user_api_keys import UserAPIKeys
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    ids = ['ids_example'] # List[str] | Filter by API Key Ids (optional)
    owner_sids = ['owner_sids_example'] # List[str] | Filter by list of owner (user) SIDs (optional)
    is_active = True # bool | If true, the response will only include API keys which are active. Returns all keys if the query param is not set. (optional)
    is_expired = True # bool | If true, the response will only include API keys which has been expired. Returns all keys if the query param is not set. (optional)

    try:
        # Get the list of all API keys which are created or owned by the user.
        api_response = api_instance.get_all_api_keys(ids=ids, owner_sids=owner_sids, is_active=is_active, is_expired=is_expired)
        print("The response of UserApi->get_all_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_all_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[str]**](str.md)| Filter by API Key Ids | [optional] 
 **owner_sids** | [**List[str]**](str.md)| Filter by list of owner (user) SIDs | [optional] 
 **is_active** | **bool**| If true, the response will only include API keys which are active. Returns all keys if the query param is not set. | [optional] 
 **is_expired** | **bool**| If true, the response will only include API keys which has been expired. Returns all keys if the query param is not set. | [optional] 

### Return type

[**UserAPIKeys**](UserAPIKeys.md)

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

# **get_group_by_sid**
> GroupParams get_group_by_sid(sid)

Get Group by SID

Get Group by SID.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.group_params import GroupParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    sid = 'sid_example' # str | Specify the SID of the group.

    try:
        # Get Group by SID
        api_response = api_instance.get_group_by_sid(sid)
        print("The response of UserApi->get_group_by_sid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_group_by_sid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specify the SID of the group. | 

### Return type

[**GroupParams**](GroupParams.md)

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

# **get_groups**
> Groups get_groups(names=names, roles=roles, domain=domain, sids=sids, match_partial_names=match_partial_names, tenant_ids=tenant_ids, include_tenants=include_tenants)

Get Groups.

Get groups on the Cohesity cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.groups import Groups
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    names = ['names_example'] # List[str] | Specifies a list of group names to filter. (optional)
    roles = ['roles_example'] # List[str] | Specifies a list of roles to filter. (optional)
    domain = 'domain_example' # str | Specifies the group domain to filter. (optional)
    sids = ['sids_example'] # List[str] | Specifies a list of sids to filter. (optional)
    match_partial_names = True # bool | If true, the names in group names are matched by any partial rather than exactly matched. Default is false. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which groups are to be returned. (optional)
    include_tenants = True # bool | IncludeTenants specifies if groups of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)

    try:
        # Get Groups.
        api_response = api_instance.get_groups(names=names, roles=roles, domain=domain, sids=sids, match_partial_names=match_partial_names, tenant_ids=tenant_ids, include_tenants=include_tenants)
        print("The response of UserApi->get_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**List[str]**](str.md)| Specifies a list of group names to filter. | [optional] 
 **roles** | [**List[str]**](str.md)| Specifies a list of roles to filter. | [optional] 
 **domain** | **str**| Specifies the group domain to filter. | [optional] 
 **sids** | [**List[str]**](str.md)| Specifies a list of sids to filter. | [optional] 
 **match_partial_names** | **bool**| If true, the names in group names are matched by any partial rather than exactly matched. Default is false. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which groups are to be returned. | [optional] 
 **include_tenants** | **bool**| IncludeTenants specifies if groups of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional] 

### Return type

[**Groups**](Groups.md)

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

# **get_principal_sources**
> AssignedSources get_principal_sources(sid)

Fetch sources & views assigned to a user/group.

Fetches all the sources assigned to a principal.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.assigned_sources import AssignedSources
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    sid = 'sid_example' # str | Specify the SID of the principal.

    try:
        # Fetch sources & views assigned to a user/group.
        api_response = api_instance.get_principal_sources(sid)
        print("The response of UserApi->get_principal_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_principal_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specify the SID of the principal. | 

### Return type

[**AssignedSources**](AssignedSources.md)

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

# **get_security_principals**
> SecurityPrincipals get_security_principals(sids)

Get Security Principals.

Get Security Principals

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.security_principals import SecurityPrincipals
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    sids = ['sids_example'] # List[str] | Specifies a list of SIDs.

    try:
        # Get Security Principals.
        api_response = api_instance.get_security_principals(sids)
        print("The response of UserApi->get_security_principals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_security_principals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sids** | [**List[str]**](str.md)| Specifies a list of SIDs. | 

### Return type

[**SecurityPrincipals**](SecurityPrincipals.md)

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

# **get_user_api_key_by_id**
> UserAPIKey get_user_api_key_by_id(id, user_sid)

Get the API key by id.

Get the API key by id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.user_api_key import UserAPIKey
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    id = 'id_example' # str | Specify the id of the API key.
    user_sid = 'user_sid_example' # str | Specify the SID of the API key owner.

    try:
        # Get the API key by id.
        api_response = api_instance.get_user_api_key_by_id(id, user_sid)
        print("The response of UserApi->get_user_api_key_by_id:\n")
        pprint(api_response)
    except Exception as e:
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

# **get_user_api_keys**
> UserAPIKeys get_user_api_keys(user_sid, ids=ids, is_active=is_active, is_expired=is_expired)

Get the list of API keys owned by the user.

Returns the list of API keys owned by the user. For security reasons there is no way to retrieve the key itself after it's created.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.user_api_keys import UserAPIKeys
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    user_sid = 'user_sid_example' # str | Specify the SID of the API key owner.
    ids = ['ids_example'] # List[str] | Filter by API Key Ids (optional)
    is_active = True # bool | If true, the response will only include API keys which are active. Returns all keys if the query param is not set. (optional)
    is_expired = True # bool | If true, the response will only include API keys which has been expired. Returns all keys if the query param is not set. (optional)

    try:
        # Get the list of API keys owned by the user.
        api_response = api_instance.get_user_api_keys(user_sid, ids=ids, is_active=is_active, is_expired=is_expired)
        print("The response of UserApi->get_user_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_sid** | **str**| Specify the SID of the API key owner. | 
 **ids** | [**List[str]**](str.md)| Filter by API Key Ids | [optional] 
 **is_active** | **bool**| If true, the response will only include API keys which are active. Returns all keys if the query param is not set. | [optional] 
 **is_expired** | **bool**| If true, the response will only include API keys which has been expired. Returns all keys if the query param is not set. | [optional] 

### Return type

[**UserAPIKeys**](UserAPIKeys.md)

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

# **get_user_by_sid**
> UserParams get_user_by_sid(sid)

Get User by SID.

Get User by SID.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.user_params import UserParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    sid = 'sid_example' # str | Specify the SID of the user.

    try:
        # Get User by SID.
        api_response = api_instance.get_user_by_sid(sid)
        print("The response of UserApi->get_user_by_sid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_by_sid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specify the SID of the user. | 

### Return type

[**UserParams**](UserParams.md)

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

# **get_users**
> UsersList get_users(domain=domain, sids=sids, usernames=usernames, match_partial_names=match_partial_names, email_addresses=email_addresses, roles=roles, tenant_ids=tenant_ids, include_tenants=include_tenants)

Get Users.

Get Users.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.users_list import UsersList
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    domain = 'domain_example' # str | Specifies the user domain to filter. (optional)
    sids = ['sids_example'] # List[str] | Specifies a list of sids to filter. (optional)
    usernames = ['usernames_example'] # List[str] | Specifies a list of usernames to filter. (optional)
    match_partial_names = True # bool | If true, the names in usernames are matched by any partial rather than exactly matched. (optional)
    email_addresses = ['email_addresses_example'] # List[str] | Specifies a list of email addresses to filter. (optional)
    roles = ['roles_example'] # List[str] | Specifies a list of roles to filter. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which users are to be returned. (optional)
    include_tenants = True # bool | IncludeTenants specifies if users of all the tenants under the hierarchy of the logged in user's organization should be returned. (optional)

    try:
        # Get Users.
        api_response = api_instance.get_users(domain=domain, sids=sids, usernames=usernames, match_partial_names=match_partial_names, email_addresses=email_addresses, roles=roles, tenant_ids=tenant_ids, include_tenants=include_tenants)
        print("The response of UserApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Specifies the user domain to filter. | [optional] 
 **sids** | [**List[str]**](str.md)| Specifies a list of sids to filter. | [optional] 
 **usernames** | [**List[str]**](str.md)| Specifies a list of usernames to filter. | [optional] 
 **match_partial_names** | **bool**| If true, the names in usernames are matched by any partial rather than exactly matched. | [optional] 
 **email_addresses** | [**List[str]**](str.md)| Specifies a list of email addresses to filter. | [optional] 
 **roles** | [**List[str]**](str.md)| Specifies a list of roles to filter. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which users are to be returned. | [optional] 
 **include_tenants** | **bool**| IncludeTenants specifies if users of all the tenants under the hierarchy of the logged in user&#39;s organization should be returned. | [optional] 

### Return type

[**UsersList**](UsersList.md)

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

# **regenerate_s3_key**
> SecretKeyEntity regenerate_s3_key(sid)

Reset S3 secret access key

Reset the S3 secret access key for the specified user on the Cohesity Cluster. Admin users who have the Manage Users privilege can generate keys for other users. When generating a new key, anyone using the old key will lose access until they retrieve and use the newly generated key. The user must have the following privilege to access this endpoint, 'Manage S3 Keys'.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.secret_key_entity import SecretKeyEntity
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    sid = 'sid_example' # str | Specify the SID of the user.

    try:
        # Reset S3 secret access key
        api_response = api_instance.regenerate_s3_key(sid)
        print("The response of UserApi->regenerate_s3_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->regenerate_s3_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specify the SID of the user. | 

### Return type

[**SecretKeyEntity**](SecretKeyEntity.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.created_user_api_key import CreatedUserAPIKey
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    user_sid = 'user_sid_example' # str | Specify the SID of the API key owner.
    id = 'id_example' # str | Specify the id of the API key.

    try:
        # Refresh an existing user API key.
        api_response = api_instance.rotate_user_api_key(user_sid, id)
        print("The response of UserApi->rotate_user_api_key:\n")
        pprint(api_response)
    except Exception as e:
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

# **update_group**
> GroupParams update_group(sid, body)

Update Group

Only group settings on the Cohesity Cluster are updated. No changes are made to the referenced group principal on the Active Directory/IdP.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.group_params import GroupParams
from cohesity_sdk.cluster.models.update_group_parameters import UpdateGroupParameters
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    sid = 'sid_example' # str | Specify the SID of the group.
    body = cohesity_sdk.cluster.UpdateGroupParameters() # UpdateGroupParameters | Specifies the group information.

    try:
        # Update Group
        api_response = api_instance.update_group(sid, body)
        print("The response of UserApi->update_group:\n")
        pprint(api_response)
    except Exception as e:
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

# **update_principal_sources**
> AssignedSources update_principal_sources(sid, body)

Update protection sources assigned to a user/group.

Update protection sources assigned to a user/group.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.assigned_sources import AssignedSources
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    sid = 'sid_example' # str | Specify the SID of the principal.
    body = cohesity_sdk.cluster.AssignedSources() # AssignedSources | Specify the sources to be assigned to a principal.

    try:
        # Update protection sources assigned to a user/group.
        api_response = api_instance.update_principal_sources(sid, body)
        print("The response of UserApi->update_principal_sources:\n")
        pprint(api_response)
    except Exception as e:
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

# **update_user**
> UserParams update_user(sid, body)

Update User information.

Update an existing user on the Cohesity Cluster. Only user settings on the Cohesity Cluster are updated. No changes are made to the referenced user principal on the Active Directory/IdP.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.update_user_parameters import UpdateUserParameters
from cohesity_sdk.cluster.models.user_params import UserParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    sid = 'sid_example' # str | Specify the SID of the user.
    body = cohesity_sdk.cluster.UpdateUserParameters() # UpdateUserParameters | Specifies the user information.

    try:
        # Update User information.
        api_response = api_instance.update_user(sid, body)
        print("The response of UserApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
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

# **update_user_api_key_by_id**
> UserAPIKey update_user_api_key_by_id(id, user_sid, body)

Update a user API key.

Update a user API key.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.create_or_update_api_key_request import CreateOrUpdateAPIKeyRequest
from cohesity_sdk.cluster.models.user_api_key import UserAPIKey
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.UserApi(api_client)
    id = 'id_example' # str | Specify the id of the API key.
    user_sid = 'user_sid_example' # str | Specify the SID of the API key owner.
    body = cohesity_sdk.cluster.CreateOrUpdateAPIKeyRequest() # CreateOrUpdateAPIKeyRequest | Request to update a user API key

    try:
        # Update a user API key.
        api_response = api_instance.update_user_api_key_by_id(id, user_sid, body)
        print("The response of UserApi->update_user_api_key_by_id:\n")
        pprint(api_response)
    except Exception as e:
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

