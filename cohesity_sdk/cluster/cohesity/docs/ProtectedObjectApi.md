# cohesity_sdk.cluster.ProtectedObjectApi

All URIs are relative to *http://localhost/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**perform_action_on_protect_objects**](ProtectedObjectApi.md#perform_action_on_protect_objects) | **POST** /data-protect/protected-objects/actions | Perform Actions on Protect Objects.
[**protect_objects_of_any_type**](ProtectedObjectApi.md#protect_objects_of_any_type) | **POST** /data-protect/protected-objects | Create Object Backup.
[**update_protected_objects_of_any_type**](ProtectedObjectApi.md#update_protected_objects_of_any_type) | **PUT** /data-protect/protected-objects/{id} | Update Object Backup.


# **perform_action_on_protect_objects**
> ProtectedObjectActionResponse perform_action_on_protect_objects(body)

Perform Actions on Protect Objects.

**Privileges:** ```PROTECTION_JOB_OPERATE``` <br><br>Perform actions on Protected Objects.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import protected_object
from cohesity_sdk.cluster.cohesity.model.protectd_objects_action_request import ProtectdObjectsActionRequest
from cohesity_sdk.cluster.cohesity.model.protected_object_action_response import ProtectedObjectActionResponse
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = protected_object.ProtectedObjectApi(api_client)
    body = ProtectdObjectsActionRequest(
        action="Pause",
        object_action_key="kVMware",
        pause_params=ProtectedObjectPauseActionParams(
            objects=[
                ProtectionObjectInput(
                    id=1,
                ),
            ],
        ),
        resume_params=ProtectedObjectResumeActionParams(
            objects=[
                ProtectionObjectInput(
                    id=1,
                ),
            ],
        ),
        run_now_params=ProtectedObjectRunNowActionParams(
            objects=[
                RunNowActionObjectLevelParams(),
            ],
            run_label="run_label_example",
        ),
        snapshot_backend_types=[
            "kAWSNative",
        ],
        un_protect_params=ProtectedObjectUnProtectActionParams(
            objects=[
                UnprotectActionObjectLevelParams(),
            ],
        ),
    ) # ProtectdObjectsActionRequest | Specifies the parameters to perform an action on an already protected object.

    # example passing only required values which don't have defaults set
    try:
        # Perform Actions on Protect Objects.
        api_response = api_instance.perform_action_on_protect_objects(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling ProtectedObjectApi->perform_action_on_protect_objects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtectdObjectsActionRequest**](ProtectdObjectsActionRequest.md)| Specifies the parameters to perform an action on an already protected object. |

### Return type

[**ProtectedObjectActionResponse**](ProtectedObjectActionResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```PROTECTION_MODIFY``` <br><br>Create Protect Objects Backup.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import protected_object
from cohesity_sdk.cluster.cohesity.model.create_protected_objects_request import CreateProtectedObjectsRequest
from cohesity_sdk.cluster.cohesity.model.error import Error
from cohesity_sdk.cluster.cohesity.model.create_protected_objects_response import CreateProtectedObjectsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = protected_object.ProtectedObjectApi(api_client)
    body = CreateProtectedObjectsRequest() # CreateProtectedObjectsRequest | Specifies the parameters to protect objects.
    request_initiator_type = "UIUser" # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Object Backup.
        api_response = api_instance.protect_objects_of_any_type(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling ProtectedObjectApi->protect_objects_of_any_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Object Backup.
        api_response = api_instance.protect_objects_of_any_type(body, request_initiator_type=request_initiator_type)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling ProtectedObjectApi->protect_objects_of_any_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateProtectedObjectsRequest**](CreateProtectedObjectsRequest.md)| Specifies the parameters to protect objects. |
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional]

### Return type

[**CreateProtectedObjectsResponse**](CreateProtectedObjectsResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```PROTECTION_MODIFY``` <br><br>Update Protected object backup configuration given a object id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import protected_object
from cohesity_sdk.cluster.cohesity.model.update_protected_objects_request import UpdateProtectedObjectsRequest
from cohesity_sdk.cluster.cohesity.model.get_protected_object_response import GetProtectedObjectResponse
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = protected_object.ProtectedObjectApi(api_client)
    id = 1 # int | Specifies the id of the Protected Object.
    body = UpdateProtectedObjectsRequest() # UpdateProtectedObjectsRequest | Specifies the parameters to perform an update on protected objects.
    request_initiator_type = "UIUser" # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Object Backup.
        api_response = api_instance.update_protected_objects_of_any_type(id, body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling ProtectedObjectApi->update_protected_objects_of_any_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Object Backup.
        api_response = api_instance.update_protected_objects_of_any_type(id, body, request_initiator_type=request_initiator_type)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling ProtectedObjectApi->update_protected_objects_of_any_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the Protected Object. |
 **body** | [**UpdateProtectedObjectsRequest**](UpdateProtectedObjectsRequest.md)| Specifies the parameters to perform an update on protected objects. |
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional]

### Return type

[**GetProtectedObjectResponse**](GetProtectedObjectResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

