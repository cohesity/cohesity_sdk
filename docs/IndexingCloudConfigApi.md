# cohesity_sdk.IndexingCloudConfigApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_indexing_cloud_config**](IndexingCloudConfigApi.md#create_indexing_cloud_config) | **POST** /indexing-cloud-config | Create a new indexing config for a Tenant on Helios.


# **create_indexing_cloud_config**
> IndexingCloudConfig create_indexing_cloud_config(body)

Create a new indexing config for a Tenant on Helios.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.indexing_cloud_config import IndexingCloudConfig
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)

body = IndexingCloudConfig(
        es_config=ESConfigForIndexing(
            es_domain="es_domain_example",
            es_iam_role_arn="es_iam_role_arn_example",
        ),
        region="region_example",
        s3_config=S3ConfigForIndexing(
            s3_bucket_name="s3_bucket_name_example",
            s3_iam_role_arn="s3_iam_role_arn_example",
            s3_prefix="s3_prefix_example",
        ),
        tenant_id="tenant_id_example",
    ) # IndexingCloudConfig | 

# example passing only required values which don't have defaults set
try:
	# Create a new indexing config for a Tenant on Helios.
	api_response = client.indexing_cloud_config.create_indexing_cloud_config(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling IndexingCloudConfigApi->create_indexing_cloud_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IndexingCloudConfig**](IndexingCloudConfig.md)|  |

### Return type

[**IndexingCloudConfig**](IndexingCloudConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

