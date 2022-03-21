# cohesity_sdk.RunbooksApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**perform_runbook_action**](RunbooksApi.md#perform_runbook_action) | **POST** /runbook/actions | Perform actions based on the passed args


# **perform_runbook_action**
> perform_runbook_action(body)

Perform actions based on the passed args

Perform actions like power-off vms, power-off vApp, cloud resource cleanup etc. based on the args that are passed.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.execute_runbook_action_request import ExecuteRunbookActionRequest
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = ExecuteRunbookActionRequest(
        action="PowerOffVM",
        power_off_vm_params=PowerOffVmParams(
            vm_ids=[
                3.14,
            ],
        ),
    ) # ExecuteRunbookActionRequest | Specifies the parameters to perform action.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Perform actions based on the passed args
	client.runbooks.perform_runbook_action(body)
except ApiException as e:
	print("Exception when calling RunbooksApi->perform_runbook_action: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Perform actions based on the passed args
	client.runbooks.perform_runbook_action(body, access_cluster_id=access_cluster_id, region_id=region_id)
except ApiException as e:
	print("Exception when calling RunbooksApi->perform_runbook_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExecuteRunbookActionRequest**](ExecuteRunbookActionRequest.md)| Specifies the parameters to perform action. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

