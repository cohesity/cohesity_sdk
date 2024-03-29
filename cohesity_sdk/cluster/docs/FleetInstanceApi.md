# cohesity_sdk.FleetInstanceApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**update_fleet_env_info**](FleetInstanceApi.md#update_fleet_env_info) | **POST** /fleet-env-info | Update Fleet Env Info.


# **update_fleet_env_info**
> UpdateFleetEnvInfoRequest update_fleet_env_info(body)

Update Fleet Env Info.

Add fleet environment info to cluster.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.update_fleet_env_info_request import UpdateFleetEnvInfoRequest
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

body = UpdateFleetEnvInfoRequest(
        iam_role="iam_role_example",
        region="region_example",
        security_group_id="security_group_id_example",
        subnet_id="subnet_id_example",
        vpc_id="vpc_id_example",
    ) # UpdateFleetEnvInfoRequest | Specifies the parameters to add fleet env info.

# example passing only required values which don't have defaults set
try:
	# Update Fleet Env Info.
	api_response = client.fleet_instance.update_fleet_env_info(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling FleetInstanceApi->update_fleet_env_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateFleetEnvInfoRequest**](UpdateFleetEnvInfoRequest.md)| Specifies the parameters to add fleet env info. |

### Return type

[**UpdateFleetEnvInfoRequest**](UpdateFleetEnvInfoRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

