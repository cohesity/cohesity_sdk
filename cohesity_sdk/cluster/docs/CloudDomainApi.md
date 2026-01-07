# cohesity_sdk.CloudDomainApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_cloud_domain**](CloudDomainApi.md#attach_cloud_domain) | **POST** /data-protect/attach-cloud-domain | 


# **attach_cloud_domain**
> AttachCloudDomainResponse attach_cloud_domain(body)



**Privileges:** ```CLUSTER_EXTERNAL_TARGET_MODIFY``` <br><br>Attaches the cloud domain present in the vault to cluster config in read-only mode without validating if contents can be decrypted.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.attach_cloud_domain_response import AttachCloudDomainResponse
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.cloud_domain_params import CloudDomainParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CloudDomainParams(
        vault_id=1,
    ) # CloudDomainParams | Specified the vault id

# example passing only required values which don't have defaults set
try:
	api_response = client.cloud_domain.attach_cloud_domain(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling CloudDomainApi->attach_cloud_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudDomainParams**](CloudDomainParams.md)| Specified the vault id |

### Return type

[**AttachCloudDomainResponse**](AttachCloudDomainResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

