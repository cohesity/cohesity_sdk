# cohesity_sdk.AgentApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**download_agent**](AgentApi.md#download_agent) | **POST** /data-protect/agents/download | Download agent


# **download_agent**
> file_type download_agent(body)

Download agent

Download agent for different hosts.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk.cluster.cohesity_client_v2 import CohesityClientV2
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.download_agent_request_params import DownloadAgentRequestParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


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
    ) # DownloadAgentRequestParams | Specifies agent details.

# example passing only required values which don't have defaults set
try:
	# Download agent
	api_response = client.agent.download_agent(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling AgentApi->download_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DownloadAgentRequestParams**](DownloadAgentRequestParams.md)| Specifies agent details. |

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

