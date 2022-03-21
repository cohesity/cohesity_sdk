# cohesity_sdk.AgentApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_upgrade_task**](AgentApi.md#create_upgrade_task) | **POST** /data-protect/agents/upgrade-tasks | Create an upgrade task
[**download_agent**](AgentApi.md#download_agent) | **POST** /data-protect/agents/download | Download agent
[**get_upgrade_tasks**](AgentApi.md#get_upgrade_tasks) | **GET** /data-protect/agents/upgrade-tasks | Get upgrade tasks
[**mcm_get_agent_image_details**](AgentApi.md#mcm_get_agent_image_details) | **GET** /mcm/data-protect/agents/images | Get agent images details.
[**perform_action_on_agent_upgrade_task**](AgentApi.md#perform_action_on_agent_upgrade_task) | **POST** /data-protect/agents/upgrade-tasks/actions | Perform action on an upgrade task.


# **create_upgrade_task**
> AgentUpgradeTaskState create_upgrade_task(body)

Create an upgrade task

Create a schedule based agent upgrade task.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.create_upgrade_task_request import CreateUpgradeTaskRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.agent_upgrade_task_state import AgentUpgradeTaskState
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = CreateUpgradeTaskRequest(
        name="name_example",
        description="description_example",
        agent_ids=[
            1,
        ],
        schedule_time_usecs=1,
        schedule_end_time_usecs=1,
        retry_task_id=1,
    ) # CreateUpgradeTaskRequest | Specifies parameters to create a schedule based agent upgrade task.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Create an upgrade task
	api_response = client.agent.create_upgrade_task(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AgentApi->create_upgrade_task: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Create an upgrade task
	api_response = client.agent.create_upgrade_task(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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
> file_type download_agent(body)

Download agent

Download agent for different hosts.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.download_agent_request_params import DownloadAgentRequestParams
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = DownloadAgentRequestParams(
        platform="kLinux",
        linux_params=LinuxAgentParams(
            package_type="kScript",
        ),
        aix_params=AixAgentParams(
            agent_type="kGo",
        ),
        sap_hana_params=SapHanaAgentParams(
            package_type="kScript",
            agent_type="kJava",
        ),
        sap_oracle_params=SapOracleAgentParams(
            package_type="kScript",
        ),
        my_sql_params=MySqlAgentParams(
            package_type="kScript",
        ),
        vmware_cdp_filter_params=VMWareCDPFilterParams(
            esxi_version="esxi_version_example",
        ),
    ) # DownloadAgentRequestParams | Specifies agent details.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Download agent
	api_response = client.agent.download_agent(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AgentApi->download_agent: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Download agent
	api_response = client.agent.download_agent(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AgentApi->download_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DownloadAgentRequestParams**](DownloadAgentRequestParams.md)| Specifies agent details. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

**file_type**

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
> AgentUpgradeTaskStates get_upgrade_tasks()

Get upgrade tasks

Get the list of agent upgrade tasks.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.agent_upgrade_task_states import AgentUpgradeTaskStates
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
ids = [
        1,
    ] # [int] | Specifies IDs of tasks to be fetched. (optional)
tenant_ids = [
        "tenantIds_example",
    ] # [str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
include_tenants = True # bool | If true, the response will include upgrade tasks which were created by all tenants which the current user has permission to see. If false, then only upgrade tasks created by the current user will be returned. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get upgrade tasks
	api_response = client.agent.get_upgrade_tasks(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, tenant_ids=tenant_ids, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AgentApi->get_upgrade_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]
 **ids** | **[int]**| Specifies IDs of tasks to be fetched. | [optional]
 **tenant_ids** | **[str]**| TenantIds contains ids of the tenants for which objects are to be returned. | [optional]
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
> McmAgentImagesResponse mcm_get_agent_image_details()

Get agent images details.

Get agent information on Helios.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.mcm_agent_images_response import McmAgentImagesResponse
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
platform = "Windows" # str | Specifies a platform for which agent information need to be fetched. (optional)
package_type = "Script" # str | Specifies a package type for which agent information need to be fetched. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get agent images details.
	api_response = client.agent.mcm_get_agent_image_details(region_id=region_id, platform=platform, package_type=package_type)
	pprint(api_response)
except ApiException as e:
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
> AgentUpgradeTaskActionObject perform_action_on_agent_upgrade_task(body)

Perform action on an upgrade task.

Perform actions on an agent upgrade task.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.agent_upgrade_task_action_object import AgentUpgradeTaskActionObject
from cohesity_sdk.helios.model.agent_upgrade_task_action_request import AgentUpgradeTaskActionRequest
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = AgentUpgradeTaskActionRequest(
        action="Retry",
        id=1,
    ) # AgentUpgradeTaskActionRequest | Specifies the parameters to perform an action on an agent upgrade task.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Perform action on an upgrade task.
	api_response = client.agent.perform_action_on_agent_upgrade_task(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AgentApi->perform_action_on_agent_upgrade_task: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Perform action on an upgrade task.
	api_response = client.agent.perform_action_on_agent_upgrade_task(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
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

