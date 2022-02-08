# cohesity_sdk.ProtectedObjectsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**perform_action_on_protect_objects**](ProtectedObjectsApi.md#perform_action_on_protect_objects) | **POST** /data-protect/protected-objects/actions | Perform Actions on Protect Objects.
[**protect_objects_of_any_type**](ProtectedObjectsApi.md#protect_objects_of_any_type) | **POST** /data-protect/protected-objects | Create Object Backup.
[**update_protected_objects_of_any_type**](ProtectedObjectsApi.md#update_protected_objects_of_any_type) | **PUT** /data-protect/protected-objects/{id} | Update Object Backup.


# **perform_action_on_protect_objects**
> ProtectedObjectActionResponse perform_action_on_protect_objects(body)

Perform Actions on Protect Objects.

Perform actions on Protected Objects.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.protectd_objects_action_request import ProtectdObjectsActionRequest
from cohesity_sdk.cohesity_client_v2.model.protected_object_action_response import ProtectedObjectActionResponse
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = ProtectdObjectsActionRequest(
        action="Pause",
        pause_params=ProtectedObjectPauseActionParams(
            objects=[
                PauseActionObjectLevelParams(),
            ],
        ),
        resume_params=ProtectedObjectResumeActionParams(
            objects=[
                ResumeActionObjectLevelParams(),
            ],
        ),
        run_now_params=ProtectedObjectRunNowActionParams(
            objects=[
                RunNowActionObjectLevelParams(),
            ],
        ),
        un_protect_params=ProtectedObjectUnProtectActionParams(
            objects=[
                UnprotectActionObjectLevelParams(),
            ],
        ),
    ) # ProtectdObjectsActionRequest | Specifies the parameters to perform an action on an already protected object.

# example passing only required values which don't have defaults set
try:
	# Perform Actions on Protect Objects.
	api_response = client.protected_objects.perform_action_on_protect_objects(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectedObjectsApi->perform_action_on_protect_objects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtectdObjectsActionRequest**](ProtectdObjectsActionRequest.md)| Specifies the parameters to perform an action on an already protected object. |

### Return type

[**ProtectedObjectActionResponse**](ProtectedObjectActionResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_objects_of_any_type**
> CreateProtectedObjectsResponse protect_objects_of_any_type(body)

Create Object Backup.

Create Protect Objects Backup.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.create_protected_objects_request import CreateProtectedObjectsRequest
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.create_protected_objects_response import CreateProtectedObjectsResponse
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateProtectedObjectsRequest() # CreateProtectedObjectsRequest | Specifies the parameters to protect objects.

# example passing only required values which don't have defaults set
try:
	# Create Object Backup.
	api_response = client.protected_objects.protect_objects_of_any_type(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectedObjectsApi->protect_objects_of_any_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateProtectedObjectsRequest**](CreateProtectedObjectsRequest.md)| Specifies the parameters to protect objects. |

### Return type

[**CreateProtectedObjectsResponse**](CreateProtectedObjectsResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_protected_objects_of_any_type**
> GetProtectedObjectResponse update_protected_objects_of_any_type(id, body)

Update Object Backup.

Update Protected object backup configuration given a object id.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.update_protected_objects_request import UpdateProtectedObjectsRequest
from cohesity_sdk.cohesity_client_v2.model.get_protected_object_response import GetProtectedObjectResponse
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the id of the Protected Object.
body = UpdateProtectedObjectsRequest() # UpdateProtectedObjectsRequest | Specifies the parameters to perform an update on protected objects.

# example passing only required values which don't have defaults set
try:
	# Update Object Backup.
	api_response = client.protected_objects.update_protected_objects_of_any_type(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectedObjectsApi->update_protected_objects_of_any_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protected Object. |
 **body** | [**UpdateProtectedObjectsRequest**](UpdateProtectedObjectsRequest.md)| Specifies the parameters to perform an update on protected objects. |

### Return type

[**GetProtectedObjectResponse**](GetProtectedObjectResponse.md)

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

