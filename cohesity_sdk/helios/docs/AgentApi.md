# cohesity_sdk.helios.AgentApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_upgrade_task**](AgentApi.md#create_upgrade_task) | **POST** /data-protect/agents/upgrade-tasks | Create an upgrade task
[**download_agent**](AgentApi.md#download_agent) | **POST** /data-protect/agents/download | Download agent
[**get_upgrade_tasks**](AgentApi.md#get_upgrade_tasks) | **GET** /data-protect/agents/upgrade-tasks | Get upgrade tasks
[**mcm_get_agent_image_details**](AgentApi.md#mcm_get_agent_image_details) | **GET** /mcm/data-protect/agents/images | Get agent images details.
[**perform_action_on_agent_upgrade_task**](AgentApi.md#perform_action_on_agent_upgrade_task) | **POST** /data-protect/agents/upgrade-tasks/actions | Perform action on an upgrade task.


# **create_upgrade_task**
> AgentUpgradeTaskState create_upgrade_task(body, access_cluster_id=access_cluster_id, region_id=region_id)

Create an upgrade task

Create a schedule based agent upgrade task.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.agent_upgrade_task_state import AgentUpgradeTaskState
from cohesity_sdk.helios.models.create_upgrade_task_request import CreateUpgradeTaskRequest
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
    api_instance = cohesity_sdk.helios.AgentApi(api_client)
    body = cohesity_sdk.helios.CreateUpgradeTaskRequest() # CreateUpgradeTaskRequest | Specifies parameters to create a schedule based agent upgrade task.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Create an upgrade task
        api_response = api_instance.create_upgrade_task(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of AgentApi->create_upgrade_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->create_upgrade_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUpgradeTaskRequest**](CreateUpgradeTaskRequest.md)| Specifies parameters to create a schedule based agent upgrade task. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**AgentUpgradeTaskState**](AgentUpgradeTaskState.md)

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

# **download_agent**
> bytearray download_agent(body, access_cluster_id=access_cluster_id, region_id=region_id)

Download agent

Download agent for different hosts.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.download_agent_request_params import DownloadAgentRequestParams
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
    api_instance = cohesity_sdk.helios.AgentApi(api_client)
    body = cohesity_sdk.helios.DownloadAgentRequestParams() # DownloadAgentRequestParams | Specifies agent details.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Download agent
        api_response = api_instance.download_agent(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of AgentApi->download_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->download_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DownloadAgentRequestParams**](DownloadAgentRequestParams.md)| Specifies agent details. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

**bytearray**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_tasks**
> AgentUpgradeTaskStates get_upgrade_tasks(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, tenant_ids=tenant_ids, include_tenants=include_tenants)

Get upgrade tasks

Get the list of agent upgrade tasks.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.agent_upgrade_task_states import AgentUpgradeTaskStates
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
    api_instance = cohesity_sdk.helios.AgentApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    ids = [56] # List[int] | Specifies IDs of tasks to be fetched. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
    include_tenants = True # bool | If true, the response will include upgrade tasks which were created by all tenants which the current user has permission to see. If false, then only upgrade tasks created by the current user will be returned. (optional)

    try:
        # Get upgrade tasks
        api_response = api_instance.get_upgrade_tasks(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, tenant_ids=tenant_ids, include_tenants=include_tenants)
        print("The response of AgentApi->get_upgrade_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->get_upgrade_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **ids** | [**List[int]**](int.md)| Specifies IDs of tasks to be fetched. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which objects are to be returned. | [optional] 
 **include_tenants** | **bool**| If true, the response will include upgrade tasks which were created by all tenants which the current user has permission to see. If false, then only upgrade tasks created by the current user will be returned. | [optional] 

### Return type

[**AgentUpgradeTaskStates**](AgentUpgradeTaskStates.md)

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

# **mcm_get_agent_image_details**
> McmAgentImagesResponse mcm_get_agent_image_details(region_id=region_id, platform=platform, package_type=package_type)

Get agent images details.

Get agent information on Helios.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.mcm_agent_images_response import McmAgentImagesResponse
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
    api_instance = cohesity_sdk.helios.AgentApi(api_client)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    platform = 'platform_example' # str | Specifies a platform for which agent information need to be fetched. (optional)
    package_type = 'package_type_example' # str | Specifies a package type for which agent information need to be fetched. (optional)

    try:
        # Get agent images details.
        api_response = api_instance.mcm_get_agent_image_details(region_id=region_id, platform=platform, package_type=package_type)
        print("The response of AgentApi->mcm_get_agent_image_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->mcm_get_agent_image_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **platform** | **str**| Specifies a platform for which agent information need to be fetched. | [optional] 
 **package_type** | **str**| Specifies a package type for which agent information need to be fetched. | [optional] 

### Return type

[**McmAgentImagesResponse**](McmAgentImagesResponse.md)

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

# **perform_action_on_agent_upgrade_task**
> AgentUpgradeTaskActionObject perform_action_on_agent_upgrade_task(body, access_cluster_id=access_cluster_id, region_id=region_id)

Perform action on an upgrade task.

Perform actions on an agent upgrade task.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.agent_upgrade_task_action_object import AgentUpgradeTaskActionObject
from cohesity_sdk.helios.models.agent_upgrade_task_action_request import AgentUpgradeTaskActionRequest
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
    api_instance = cohesity_sdk.helios.AgentApi(api_client)
    body = cohesity_sdk.helios.AgentUpgradeTaskActionRequest() # AgentUpgradeTaskActionRequest | Specifies the parameters to perform an action on an agent upgrade task.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Perform action on an upgrade task.
        api_response = api_instance.perform_action_on_agent_upgrade_task(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of AgentApi->perform_action_on_agent_upgrade_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->perform_action_on_agent_upgrade_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AgentUpgradeTaskActionRequest**](AgentUpgradeTaskActionRequest.md)| Specifies the parameters to perform an action on an agent upgrade task. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**AgentUpgradeTaskActionObject**](AgentUpgradeTaskActionObject.md)

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

