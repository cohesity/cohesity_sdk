# cohesity_sdk.cluster.ExternalTargetApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_external_target**](ExternalTargetApi.md#create_external_target) | **POST** /data-protect/external-targets | Create a External Target.
[**delete_external_target**](ExternalTargetApi.md#delete_external_target) | **DELETE** /data-protect/external-targets/{id} | Delete a External Target.
[**get_external_target_by_id**](ExternalTargetApi.md#get_external_target_by_id) | **GET** /data-protect/external-targets/{id} | List details about single External Target.
[**get_external_target_encryption_key_info**](ExternalTargetApi.md#get_external_target_encryption_key_info) | **GET** /data-protect/external-targets/{id}/encryption-key | Get the encryption key info for an external target
[**get_external_target_media_info**](ExternalTargetApi.md#get_external_target_media_info) | **GET** /data-protect/external-targets/media-info | List archive media information
[**get_external_target_settings**](ExternalTargetApi.md#get_external_target_settings) | **GET** /data-protect/external-targets/settings | Get the list of External Target Settings.
[**get_external_targets**](ExternalTargetApi.md#get_external_targets) | **GET** /data-protect/external-targets | Get the list of External Targets.
[**update_external_target**](ExternalTargetApi.md#update_external_target) | **PUT** /data-protect/external-targets/{id} | Update a External Target.
[**update_external_target_settings**](ExternalTargetApi.md#update_external_target_settings) | **PUT** /data-protect/external-targets/settings | Update External Target Settings


# **create_external_target**
> ExternalTarget create_external_target(body)

Create a External Target.

Create a External Target.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.external_target import ExternalTarget
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ExternalTargetApi(api_client)
    body = cohesity_sdk.cluster.ExternalTarget() # ExternalTarget | Specifies the parameters to create a External Target.

    try:
        # Create a External Target.
        api_response = api_instance.create_external_target(body)
        print("The response of ExternalTargetApi->create_external_target:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalTargetApi->create_external_target: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalTarget**](ExternalTarget.md)| Specifies the parameters to create a External Target. | 

### Return type

[**ExternalTarget**](ExternalTarget.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_external_target**
> delete_external_target(id, force_delete=force_delete)

Delete a External Target.

Returns Success if the External Target is deleted.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ExternalTargetApi(api_client)
    id = 56 # int | Specifies a unique id of the External Target.
    force_delete = True # bool | Specifies whether to force delete the External target. (optional)

    try:
        # Delete a External Target.
        api_instance.delete_external_target(id, force_delete=force_delete)
    except Exception as e:
        print("Exception when calling ExternalTargetApi->delete_external_target: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the External Target. | 
 **force_delete** | **bool**| Specifies whether to force delete the External target. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_target_by_id**
> ExternalTarget get_external_target_by_id(id)

List details about single External Target.

Returns the External Target corresponding to the specified Group id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.external_target import ExternalTarget
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ExternalTargetApi(api_client)
    id = 56 # int | Specifies a unique id of the External Target.

    try:
        # List details about single External Target.
        api_response = api_instance.get_external_target_by_id(id)
        print("The response of ExternalTargetApi->get_external_target_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalTargetApi->get_external_target_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the External Target. | 

### Return type

[**ExternalTarget**](ExternalTarget.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_target_encryption_key_info**
> bytearray get_external_target_encryption_key_info(id)

Get the encryption key info for an external target

Get the encryption key info for an external target

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ExternalTargetApi(api_client)
    id = 56 # int | Specifies the id of the External Target.

    try:
        # Get the encryption key info for an external target
        api_response = api_instance.get_external_target_encryption_key_info(id)
        print("The response of ExternalTargetApi->get_external_target_encryption_key_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalTargetApi->get_external_target_encryption_key_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the External Target. | 

### Return type

**bytearray**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_target_media_info**
> ArchivalMediaInfo get_external_target_media_info(cluster_id, cluster_incarnation_id, archival_job_id, restore_task_id=restore_task_id, entity_ids=entity_ids)

List archive media information

Returns the media information about the specified archive service uid (such as a QStar tape archive service).

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.archival_media_info import ArchivalMediaInfo
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ExternalTargetApi(api_client)
    cluster_id = 56 # int | Specifies the id of the Cohesity cluster which archived to a QStart media target.
    cluster_incarnation_id = 56 # int | Specifies the incarnation Id of the Cohesity cluster which archived to a QStart media target.
    archival_job_id = 56 # int | Specifies the id of the Job that archived to a QStar media Vault.
    restore_task_id = 56 # int | Specifies the id of the restore task to optionally filter by. (optional)
    entity_ids = [56] # List[int] | Specifies an array of entityIds to optionally filter by. An entityId is a unique id for a VM assigned by the Cohesity Cluster. (optional)

    try:
        # List archive media information
        api_response = api_instance.get_external_target_media_info(cluster_id, cluster_incarnation_id, archival_job_id, restore_task_id=restore_task_id, entity_ids=entity_ids)
        print("The response of ExternalTargetApi->get_external_target_media_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalTargetApi->get_external_target_media_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| Specifies the id of the Cohesity cluster which archived to a QStart media target. | 
 **cluster_incarnation_id** | **int**| Specifies the incarnation Id of the Cohesity cluster which archived to a QStart media target. | 
 **archival_job_id** | **int**| Specifies the id of the Job that archived to a QStar media Vault. | 
 **restore_task_id** | **int**| Specifies the id of the restore task to optionally filter by. | [optional] 
 **entity_ids** | [**List[int]**](int.md)| Specifies an array of entityIds to optionally filter by. An entityId is a unique id for a VM assigned by the Cohesity Cluster. | [optional] 

### Return type

[**ArchivalMediaInfo**](ArchivalMediaInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_target_settings**
> ExternalTarget get_external_target_settings()

Get the list of External Target Settings.

Get the list of External Target Settings

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.external_target import ExternalTarget
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ExternalTargetApi(api_client)

    try:
        # Get the list of External Target Settings.
        api_response = api_instance.get_external_target_settings()
        print("The response of ExternalTargetApi->get_external_target_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalTargetApi->get_external_target_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ExternalTarget**](ExternalTarget.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_targets**
> ExternalTargets get_external_targets(ids=ids, global_ids=global_ids, names=names, purpose_types=purpose_types, storage_types=storage_types, storage_classes=storage_classes, ownership_contexts=ownership_contexts)

Get the list of External Targets.

Get the list of External Targets.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.external_targets import ExternalTargets
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ExternalTargetApi(api_client)
    ids = [56] # List[int] | Filter by a list of External Target ids. (optional)
    global_ids = ['global_ids_example'] # List[str] | Filter by a list of External Target global ids. (optional)
    names = ['names_example'] # List[str] | Filter by a list of External Target names. (optional)
    purpose_types = ['purpose_types_example'] # List[str] | Filter by a list of External Target purpose types. (optional)
    storage_types = ['storage_types_example'] # List[str] | Filter by a list of External Target storage types. Nas option in archival_target_storage_type will soon be deprecated. Please use NAS instead. (optional)
    storage_classes = ['storage_classes_example'] # List[str] | Filter by a list of External Target storage classes. (optional)
    ownership_contexts = ['ownership_contexts_example'] # List[str] | Specifies whether how this external target is being consumed either Local or FortKnox. (optional)

    try:
        # Get the list of External Targets.
        api_response = api_instance.get_external_targets(ids=ids, global_ids=global_ids, names=names, purpose_types=purpose_types, storage_types=storage_types, storage_classes=storage_classes, ownership_contexts=ownership_contexts)
        print("The response of ExternalTargetApi->get_external_targets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalTargetApi->get_external_targets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| Filter by a list of External Target ids. | [optional] 
 **global_ids** | [**List[str]**](str.md)| Filter by a list of External Target global ids. | [optional] 
 **names** | [**List[str]**](str.md)| Filter by a list of External Target names. | [optional] 
 **purpose_types** | [**List[str]**](str.md)| Filter by a list of External Target purpose types. | [optional] 
 **storage_types** | [**List[str]**](str.md)| Filter by a list of External Target storage types. Nas option in archival_target_storage_type will soon be deprecated. Please use NAS instead. | [optional] 
 **storage_classes** | [**List[str]**](str.md)| Filter by a list of External Target storage classes. | [optional] 
 **ownership_contexts** | [**List[str]**](str.md)| Specifies whether how this external target is being consumed either Local or FortKnox. | [optional] 

### Return type

[**ExternalTargets**](ExternalTargets.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_target**
> ExternalTarget update_external_target(id, body)

Update a External Target.

Update the specified External Target.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.external_target import ExternalTarget
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ExternalTargetApi(api_client)
    id = 56 # int | Specifies the id of the External Target.
    body = cohesity_sdk.cluster.ExternalTarget() # ExternalTarget | Specifies the parameters to update a External Target.

    try:
        # Update a External Target.
        api_response = api_instance.update_external_target(id, body)
        print("The response of ExternalTargetApi->update_external_target:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalTargetApi->update_external_target: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the External Target. | 
 **body** | [**ExternalTarget**](ExternalTarget.md)| Specifies the parameters to update a External Target. | 

### Return type

[**ExternalTarget**](ExternalTarget.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_target_settings**
> GlobalBandwidthSettings update_external_target_settings(body)

Update External Target Settings

Update External Target Settings

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.global_bandwidth_settings import GlobalBandwidthSettings
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.ExternalTargetApi(api_client)
    body = cohesity_sdk.cluster.GlobalBandwidthSettings() # GlobalBandwidthSettings | Specifies the parameters to update a External Target Settings.

    try:
        # Update External Target Settings
        api_response = api_instance.update_external_target_settings(body)
        print("The response of ExternalTargetApi->update_external_target_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalTargetApi->update_external_target_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GlobalBandwidthSettings**](GlobalBandwidthSettings.md)| Specifies the parameters to update a External Target Settings. | 

### Return type

[**GlobalBandwidthSettings**](GlobalBandwidthSettings.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

