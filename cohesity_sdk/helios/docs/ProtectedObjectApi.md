# cohesity_sdk.helios.ProtectedObjectApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**perform_action_on_protect_objects**](ProtectedObjectApi.md#perform_action_on_protect_objects) | **POST** /data-protect/protected-objects/actions | Perform Actions on Protect Objects.
[**protect_objects_of_any_type**](ProtectedObjectApi.md#protect_objects_of_any_type) | **POST** /data-protect/protected-objects | Create Object Backup.
[**update_protected_objects_of_any_type**](ProtectedObjectApi.md#update_protected_objects_of_any_type) | **PUT** /data-protect/protected-objects/{id} | Update Object Backup.


# **perform_action_on_protect_objects**
> ProtectedObjectActionResponse perform_action_on_protect_objects(body, access_cluster_id=access_cluster_id, region_id=region_id)

Perform Actions on Protect Objects.

Perform actions on Protected Objects.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.protectd_objects_action_request import ProtectdObjectsActionRequest
from cohesity_sdk.helios.models.protected_object_action_response import ProtectedObjectActionResponse
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.ProtectedObjectApi(api_client)
    body = cohesity_sdk.helios.ProtectdObjectsActionRequest() # ProtectdObjectsActionRequest | Specifies the parameters to perform an action on an already protected object.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Perform Actions on Protect Objects.
        api_response = api_instance.perform_action_on_protect_objects(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of ProtectedObjectApi->perform_action_on_protect_objects:\n")
        pprint(api_response)
    except Exception as e:
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
> CreateProtectedObjectsResponse protect_objects_of_any_type(body, access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type)

Create Object Backup.

Create Protect Objects Backup.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.create_protected_objects_request import CreateProtectedObjectsRequest
from cohesity_sdk.helios.models.create_protected_objects_response import CreateProtectedObjectsResponse
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.ProtectedObjectApi(api_client)
    body = cohesity_sdk.helios.CreateProtectedObjectsRequest() # CreateProtectedObjectsRequest | Specifies the parameters to protect objects.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    request_initiator_type = 'request_initiator_type_example' # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)

    try:
        # Create Object Backup.
        api_response = api_instance.protect_objects_of_any_type(body, access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type)
        print("The response of ProtectedObjectApi->protect_objects_of_any_type:\n")
        pprint(api_response)
    except Exception as e:
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
> GetProtectedObjectResponse update_protected_objects_of_any_type(id, body, access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type)

Update Object Backup.

Update Protected object backup configuration given a object id.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.get_protected_object_response import GetProtectedObjectResponse
from cohesity_sdk.helios.models.update_protected_objects_request import UpdateProtectedObjectsRequest
from cohesity_sdk.helios.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.helios.Configuration(
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

# Enter a context with an instance of the API client
with cohesity_sdk.helios.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.helios.ProtectedObjectApi(api_client)
    id = 56 # int | Specifies the id of the Protected Object.
    body = cohesity_sdk.helios.UpdateProtectedObjectsRequest() # UpdateProtectedObjectsRequest | Specifies the parameters to perform an update on protected objects.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    request_initiator_type = 'request_initiator_type_example' # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)

    try:
        # Update Object Backup.
        api_response = api_instance.update_protected_objects_of_any_type(id, body, access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type)
        print("The response of ProtectedObjectApi->update_protected_objects_of_any_type:\n")
        pprint(api_response)
    except Exception as e:
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

