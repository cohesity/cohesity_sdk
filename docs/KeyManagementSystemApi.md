# cohesity_sdk.KeyManagementSystemApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**add_kms_configuration**](KeyManagementSystemApi.md#add_kms_configuration) | **POST** /kms | Add KMS
[**delete_kms_config**](KeyManagementSystemApi.md#delete_kms_config) | **DELETE** /kms/{id} | Delete KMS
[**get_kms_configurations**](KeyManagementSystemApi.md#get_kms_configurations) | **GET** /kms | Get KMS
[**update_kms_configuration**](KeyManagementSystemApi.md#update_kms_configuration) | **PUT** /kms/{id} | Update KMS


# **add_kms_configuration**
> KmsConfiguration add_kms_configuration(body)

Add KMS

Add a key management system(KMS) to the cluster.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.kms_configuration import KmsConfiguration
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.kms_configuration_create_params import KmsConfigurationCreateParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint



client = ClusterClient(cluster_vip)

body = KmsConfigurationCreateParams() # KmsConfigurationCreateParams | Parameters to add KMS on the cluster.

# example passing only required values which don't have defaults set
try:
	# Add KMS
	api_response = client.key_management_system.add_kms_configuration(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling KeyManagementSystemApi->add_kms_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KmsConfigurationCreateParams**](KmsConfigurationCreateParams.md)| Parameters to add KMS on the cluster. |

### Return type

[**KmsConfiguration**](KmsConfiguration.md)

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

# **delete_kms_config**
> delete_kms_config(id)

Delete KMS

Delete KMS configued on the cluster.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint



client = ClusterClient(cluster_vip)

id = 1 # int | ID of the KMS configured on the cluster.

# example passing only required values which don't have defaults set
try:
	# Delete KMS
	client.key_management_system.delete_kms_config(id)
except ApiException as e:
	print("Exception when calling KeyManagementSystemApi->delete_kms_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the KMS configured on the cluster. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kms_configurations**
> KmsConfigurations get_kms_configurations()

Get KMS

Get key management systems(KMS) configured on the cluster.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.kms_configurations import KmsConfigurations
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint



client = ClusterClient(cluster_vip)

ids = [
        1,
    ] # [int] | Ids of KMS configured on the cluster. (optional)
include_rpaas_kms = True # bool, none_type | If true, returns KMS that are configured by FortKnox. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Get KMS
	api_response = client.key_management_system.get_kms_configurations(ids=ids, include_rpaas_kms=include_rpaas_kms)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling KeyManagementSystemApi->get_kms_configurations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[int]**| Ids of KMS configured on the cluster. | [optional]
 **include_rpaas_kms** | **bool, none_type**| If true, returns KMS that are configured by FortKnox. | [optional]

### Return type

[**KmsConfigurations**](KmsConfigurations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kms_configuration**
> KmsConfiguration update_kms_configuration(id, body)

Update KMS

Update KMS on the cluster.

### Example

```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.kms_configuration_update_params import KmsConfigurationUpdateParams
from cohesity_sdk.cluster.model.kms_configuration import KmsConfiguration
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint



client = ClusterClient(cluster_vip)

id = 1 # int | ID of the KMS configured on the cluster.
body = KmsConfigurationUpdateParams() # KmsConfigurationUpdateParams | Parameters to update KMS on the cluster.

# example passing only required values which don't have defaults set
try:
	# Update KMS
	api_response = client.key_management_system.update_kms_configuration(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling KeyManagementSystemApi->update_kms_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the KMS configured on the cluster. |
 **body** | [**KmsConfigurationUpdateParams**](KmsConfigurationUpdateParams.md)| Parameters to update KMS on the cluster. |

### Return type

[**KmsConfiguration**](KmsConfiguration.md)

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

