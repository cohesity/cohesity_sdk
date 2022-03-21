# cohesity_sdk.ProtectedObjectApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**perform_action_on_protect_objects**](ProtectedObjectApi.md#perform_action_on_protect_objects) | **POST** /data-protect/protected-objects/actions | Perform Actions on Protect Objects.
[**protect_objects_of_any_type**](ProtectedObjectApi.md#protect_objects_of_any_type) | **POST** /data-protect/protected-objects | Create Object Backup.
[**update_protected_objects_of_any_type**](ProtectedObjectApi.md#update_protected_objects_of_any_type) | **PUT** /data-protect/protected-objects/{id} | Update Object Backup.


# **perform_action_on_protect_objects**
> ProtectedObjectActionResponse perform_action_on_protect_objects(body)

Perform Actions on Protect Objects.

Perform actions on Protected Objects.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.protectd_objects_action_request import ProtectdObjectsActionRequest
from cohesity_sdk.helios.model.protected_object_action_response import ProtectedObjectActionResponse
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = ProtectdObjectsActionRequest(
        action="Pause",
        object_action_key="kVMware",
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
            run_label="run_label_example",
            objects=[
                RunNowActionObjectLevelParams(),
            ],
        ),
        un_protect_params=ProtectedObjectUnProtectActionParams(
            objects=[
                UnprotectActionObjectLevelParams(),
            ],
        ),
        snapshot_backend_types=[
            "kAWSNative",
        ],
    ) # ProtectdObjectsActionRequest | Specifies the parameters to perform an action on an already protected object.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Perform Actions on Protect Objects.
	api_response = client.protected_object.perform_action_on_protect_objects(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectedObjectApi->perform_action_on_protect_objects: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Perform Actions on Protect Objects.
	api_response = client.protected_object.perform_action_on_protect_objects(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectedObjectApi->perform_action_on_protect_objects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtectdObjectsActionRequest**](ProtectdObjectsActionRequest.md)| Specifies the parameters to perform an action on an already protected object. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

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
**207** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_objects_of_any_type**
> CreateProtectedObjectsResponse protect_objects_of_any_type(body)

Create Object Backup.

Create Protect Objects Backup.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.create_protected_objects_response import CreateProtectedObjectsResponse
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.create_protected_objects_request import CreateProtectedObjectsRequest
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = CreateProtectedObjectsRequest() # CreateProtectedObjectsRequest | Specifies the parameters to protect objects.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
request_initiator_type = "UIUser" # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)

# example passing only required values which don't have defaults set
try:
	# Create Object Backup.
	api_response = client.protected_object.protect_objects_of_any_type(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectedObjectApi->protect_objects_of_any_type: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create Object Backup.
	api_response = client.protected_object.protect_objects_of_any_type(body, access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectedObjectApi->protect_objects_of_any_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateProtectedObjectsRequest**](CreateProtectedObjectsRequest.md)| Specifies the parameters to protect objects. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional]

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
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.get_protected_object_response import GetProtectedObjectResponse
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.update_protected_objects_request import UpdateProtectedObjectsRequest
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


id = 1 # int | Specifies the id of the Protected Object.
body = UpdateProtectedObjectsRequest() # UpdateProtectedObjectsRequest | Specifies the parameters to perform an update on protected objects.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
request_initiator_type = "UIUser" # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)

# example passing only required values which don't have defaults set
try:
	# Update Object Backup.
	api_response = client.protected_object.update_protected_objects_of_any_type(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectedObjectApi->update_protected_objects_of_any_type: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update Object Backup.
	api_response = client.protected_object.update_protected_objects_of_any_type(id, body, access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling ProtectedObjectApi->update_protected_objects_of_any_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protected Object. |
 **body** | [**UpdateProtectedObjectsRequest**](UpdateProtectedObjectsRequest.md)| Specifies the parameters to perform an update on protected objects. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional]

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

