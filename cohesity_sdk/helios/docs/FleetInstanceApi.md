# cohesity_sdk.FleetInstanceApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**update_fleet_env_info**](FleetInstanceApi.md#update_fleet_env_info) | **POST** /fleet-env-info | Update Fleet Env Info.


# **update_fleet_env_info**
> UpdateFleetEnvInfoRequest update_fleet_env_info(body)

Update Fleet Env Info.

Add fleet environment info to cluster.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import HeliosClient
from cohesity_sdk.helios.model.error import Error
from cohesity_sdk.helios.model.update_fleet_env_info_request import UpdateFleetEnvInfoRequest
from cohesity_sdk.helios.exceptions import ApiException
from pprint import pprint


api_key = "xxxxxx-xxxxx-xxxx-xxxxxx"

client = HeliosClient(api_key=api_key)


body = UpdateFleetEnvInfoRequest(
        iam_role="iam_role_example",
        region="region_example",
        vpc_id="vpc_id_example",
        subnet_id="subnet_id_example",
        security_group_id="security_group_id_example",
    ) # UpdateFleetEnvInfoRequest | Specifies the parameters to add fleet env info.
access_cluster_id = 1 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
region_id = "regionId_example" # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

# example passing only required values which don't have defaults set
try:
	# Update Fleet Env Info.
	api_response = client.fleet_instance.update_fleet_env_info(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling FleetInstanceApi->update_fleet_env_info: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Update Fleet Env Info.
	api_response = client.fleet_instance.update_fleet_env_info(body, access_cluster_id=access_cluster_id, region_id=region_id)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling FleetInstanceApi->update_fleet_env_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateFleetEnvInfoRequest**](UpdateFleetEnvInfoRequest.md)| Specifies the parameters to add fleet env info. |
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional]
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional]

### Return type

[**UpdateFleetEnvInfoRequest**](UpdateFleetEnvInfoRequest.md)

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

