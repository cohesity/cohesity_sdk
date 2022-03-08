# cohesity_sdk.UsersApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_session**](UsersApi.md#create_session) | **POST** /users/sessions | Create a user session
[**create_user_api_key**](UsersApi.md#create_user_api_key) | **POST** /users/{userSid}/api-keys | Create a new user API key.
[**delete_session**](UsersApi.md#delete_session) | **DELETE** /users/sessions | Delete user sessions
[**delete_user_api_key_by_id**](UsersApi.md#delete_user_api_key_by_id) | **DELETE** /users/{userSid}/api-keys/{id} | Delete a user API key.
[**get_all_api_keys**](UsersApi.md#get_all_api_keys) | **GET** /api-keys | Get the list of all API keys which are created or owned by the user.
[**get_principal_sources**](UsersApi.md#get_principal_sources) | **GET** /security-principals/{sid}/sources | Fetch sources &amp; views assigned to a user/group.
[**get_security_principals**](UsersApi.md#get_security_principals) | **GET** /security-principals | Get Security Principals.
[**get_user_api_key_by_id**](UsersApi.md#get_user_api_key_by_id) | **GET** /users/{userSid}/api-keys/{id} | Get the API key by id.
[**get_user_api_keys**](UsersApi.md#get_user_api_keys) | **GET** /users/{userSid}/api-keys | Get the list of API keys owned by the user.
[**get_users**](UsersApi.md#get_users) | **GET** /users | Get Users.
[**rotate_user_api_key**](UsersApi.md#rotate_user_api_key) | **POST** /users/{userSid}/api-keys/{id}/rotate | Refresh an existing user API key.
[**update_principal_sources**](UsersApi.md#update_principal_sources) | **PUT** /security-principals/{sid}/sources | Update protection sources assigned to a user/group.
[**update_user_api_key_by_id**](UsersApi.md#update_user_api_key_by_id) | **PUT** /users/{userSid}/api-keys/{id} | Update a user API key.


# **create_session**
> UserSession create_session(body)

Create a user session

Create a user session

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.user_session import UserSession
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.create_user_session_request_params import CreateUserSessionRequestParams
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = CreateUserSessionRequestParams(
        username="username_example",
        password="password_example",
        domain="domain_example",
        certificate="certificate_example",
        private_key="private_key_example",
        otp_code="otp_code_example",
        otp_type="email",
    ) # CreateUserSessionRequestParams | Specifies the parameters to create a user session
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a user session
	api_response = client.users.create_session(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->create_session: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a user session
	api_response = client.users.create_session(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->create_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserSessionRequestParams**](CreateUserSessionRequestParams.md)| Specifies the parameters to create a user session |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.created_user_api_key import CreatedUserAPIKey
from cohesity_sdk.helios.model.create_or_update_api_key_request import CreateOrUpdateAPIKeyRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


user_sid = "userSid_example" # str | Specify the SID of the API key owner.
body = CreateOrUpdateAPIKeyRequest(
        name="name_example",
        is_active=True,
        expiry_time_msecs=1,
    ) # CreateOrUpdateAPIKeyRequest | Request to create a new API Key
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create a new user API key.
	api_response = client.users.create_user_api_key(user_sid, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->create_user_api_key: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create a new user API key.
	api_response = client.users.create_user_api_key(user_sid, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->create_user_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_sid** | **str**| Specify the SID of the API key owner. |
 **body** | [**CreateOrUpdateAPIKeyRequest**](CreateOrUpdateAPIKeyRequest.md)| Request to create a new API Key |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
sid = "sid_example" # str | Specifies a user sid. If sid is not given system wide sessions are deleted. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete user sessions
	client.users.delete_session(access_cluster_id=access_cluster_id, region_id=region_id, sid=sid)
except ApiException as e:
	print("Exception when calling UsersApi->delete_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


user_sid = "userSid_example" # str | Specify the SID of the API key owner.
id = "id_example" # str | Specify the id of the API key.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Delete a user API key.
	client.users.delete_user_api_key_by_id(user_sid, id)
except ApiException as e:
	print("Exception when calling UsersApi->delete_user_api_key_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Delete a user API key.
	client.users.delete_user_api_key_by_id(user_sid, id, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling UsersApi->delete_user_api_key_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_sid** | **str**| Specify the SID of the API key owner. |
 **id** | **str**| Specify the id of the API key. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.user_api_keys import UserAPIKeys
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
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
	api_response = client.users.get_all_api_keys(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, owner_sids=owner_sids, is_active=is_active, is_expired=is_expired)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->get_all_api_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
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

# **get_principal_sources**
> AssignedSources get_principal_sources(sid)

Fetch sources & views assigned to a user/group.

Fetches all the sources assigned to a principal.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.assigned_sources import AssignedSources
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


sid = "sid_example" # str | Specify the SID of the principal.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Fetch sources & views assigned to a user/group.
	api_response = client.users.get_principal_sources(sid)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->get_principal_sources: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Fetch sources & views assigned to a user/group.
	api_response = client.users.get_principal_sources(sid, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->get_principal_sources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specify the SID of the principal. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.security_principals import SecurityPrincipals
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


sids = [
        "S-0-072888001528021798096225500850762068629-39333975650685139102691291732729478601482026-0912727550417577019298162864882916633228770521-191166478378563875565986836152-8784425528468720999697682-579364428489671318576363915338224935163074506805717279357060662066496241-415434479790599868759540626151494012626181911847617323796802209082-677715773090491175877238622700367804481067589385995284318716971548-9437255518186242126631124808712-209361142227111098265387333954577961103760673817300538998580525021695595165-175112804308695820986859-22048655",
    ] # [str] | Specifies a list of SIDs.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get Security Principals.
	api_response = client.users.get_security_principals(sids)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->get_security_principals: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get Security Principals.
	api_response = client.users.get_security_principals(sids, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->get_security_principals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sids** | **[str]**| Specifies a list of SIDs. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.user_api_key import UserAPIKey
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specify the id of the API key.
user_sid = "userSid_example" # str | Specify the SID of the API key owner.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Get the API key by id.
	api_response = client.users.get_user_api_key_by_id(id, user_sid)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->get_user_api_key_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get the API key by id.
	api_response = client.users.get_user_api_key_by_id(id, user_sid, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->get_user_api_key_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify the id of the API key. |
 **user_sid** | **str**| Specify the SID of the API key owner. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.user_api_keys import UserAPIKeys
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


user_sid = "userSid_example" # str | Specify the SID of the API key owner.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
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
	api_response = client.users.get_user_api_keys(user_sid, access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, is_active=is_active, is_expired=is_expired)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->get_user_api_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_sid** | **str**| Specify the SID of the API key owner. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
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

# **get_users**
> UsersList get_users()

Get Users.

Get Users.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.users_list import UsersList
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
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
	api_response = client.users.get_users(access_cluster_id=access_cluster_id, region_id=region_id, domain=domain, usernames=usernames, match_partial_names=match_partial_names, email_addresses=email_addresses, roles=roles, tenant_ids=tenant_ids, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->get_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.created_user_api_key import CreatedUserAPIKey
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


user_sid = "userSid_example" # str | Specify the SID of the API key owner.
id = "id_example" # str | Specify the id of the API key.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Refresh an existing user API key.
	api_response = client.users.rotate_user_api_key(user_sid, id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->rotate_user_api_key: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Refresh an existing user API key.
	api_response = client.users.rotate_user_api_key(user_sid, id, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->rotate_user_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_sid** | **str**| Specify the SID of the API key owner. |
 **id** | **str**| Specify the id of the API key. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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

# **update_principal_sources**
> AssignedSources update_principal_sources(sid, body)

Update protection sources assigned to a user/group.

Update protection sources assigned to a user/group.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.assigned_sources import AssignedSources
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


sid = "sid_example" # str | Specify the SID of the principal.
body = AssignedSources(
        source_ids=[
            1,
        ],
        view_ids=[
            1,
        ],
    ) # AssignedSources | Specify the sources to be assigned to a principal.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update protection sources assigned to a user/group.
	api_response = client.users.update_principal_sources(sid, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->update_principal_sources: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update protection sources assigned to a user/group.
	api_response = client.users.update_principal_sources(sid, body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->update_principal_sources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| Specify the SID of the principal. |
 **body** | [**AssignedSources**](AssignedSources.md)| Specify the sources to be assigned to a principal. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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

# **update_user_api_key_by_id**
> UserAPIKey update_user_api_key_by_id(id, user_sid, body)

Update a user API key.

Update a user API key.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.create_or_update_api_key_request import CreateOrUpdateAPIKeyRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.user_api_key import UserAPIKey
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = "id_example" # str | Specify the id of the API key.
user_sid = "userSid_example" # str | Specify the SID of the API key owner.
body = CreateOrUpdateAPIKeyRequest(
        name="name_example",
        is_active=True,
        expiry_time_msecs=1,
    ) # CreateOrUpdateAPIKeyRequest | Request to update a user API key
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update a user API key.
	api_response = client.users.update_user_api_key_by_id(id, user_sid, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling UsersApi->update_user_api_key_by_id: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update a user API key.
	api_response = client.users.update_user_api_key_by_id(id, user_sid, body, access_cluster_id=access_cluster_id, region_id=region_id)
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
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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

