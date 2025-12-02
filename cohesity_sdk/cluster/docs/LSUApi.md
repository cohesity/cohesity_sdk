# cohesity_sdk.LSUApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_lsu**](LSUApi.md#create_lsu) | **POST** /lsu | Create LSU.
[**delete_lsu_pairing**](LSUApi.md#delete_lsu_pairing) | **DELETE** /lsu/pair | Delete LSU pairing.
[**get_lsu**](LSUApi.md#get_lsu) | **GET** /lsu | GET LSU.
[**pair_remote_lsu**](LSUApi.md#pair_remote_lsu) | **POST** /lsu/pair | Pair local and remote LSU.
[**update_lsu**](LSUApi.md#update_lsu) | **PUT** /lsu/{id} | Update LSU.


# **create_lsu**
> LSU create_lsu(body)

Create LSU.

**Privileges:** ```STORAGE_DOMAIN_MODIFY``` <br><br>Create LSU.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.create_lsu_params import CreateLSUParams
from cohesity_sdk.cluster.model.lsu import LSU
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateLSUParams(
        cloud_domain_id=1,
        name="name_example",
        nbu_domain="nbu_domain_example",
        storage_domain_id=1,
        worm_config=WormConfig(
            max_retention_secs=1,
            min_retention_secs=1,
            mode="Compliance",
        ),
    ) # CreateLSUParams | Specifies the request to create an LSU.

# example passing only required values which don't have defaults set
try:
	# Create LSU.
	api_response = client.lsu.create_lsu(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling LSUApi->create_lsu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLSUParams**](CreateLSUParams.md)| Specifies the request to create an LSU. |

### Return type

[**LSU**](LSU.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lsu_pairing**
> LSU delete_lsu_pairing(body)

Delete LSU pairing.

**Privileges:** ```STORAGE_DOMAIN_MODIFY, CLUSTER_REMOTE_MODIFY``` <br><br>Delete LSU pairing.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.common_lsu_pair_fields import CommonLSUPairFields
from cohesity_sdk.cluster.model.lsu import LSU
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CommonLSUPairFields(
        local_lsuid=1,
        remote_cluster_id=1,
        remote_lsuid=1,
    ) # CommonLSUPairFields | Specifies the request to pair LSU.

# example passing only required values which don't have defaults set
try:
	# Delete LSU pairing.
	api_response = client.lsu.delete_lsu_pairing(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling LSUApi->delete_lsu_pairing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommonLSUPairFields**](CommonLSUPairFields.md)| Specifies the request to pair LSU. |

### Return type

[**LSU**](LSU.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lsu**
> [LSU] get_lsu()

GET LSU.

**Privileges:** ```STORAGE_DOMAIN_VIEW``` <br><br>GET LSU.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.lsu import LSU
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Retrieve a single result by LSU id. (optional)
name = "name_example" # str | Retrieve a single result by LSU name. It will be ignored if 'id' is also defined in the param. (optional)
include_tenants = True # bool | Whether to include LSU that belong to Tenants. This param is only effective when the User has privilege to view LSU details of a tenant. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# GET LSU.
	api_response = client.lsu.get_lsu(id=id, name=name, include_tenants=include_tenants)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling LSUApi->get_lsu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retrieve a single result by LSU id. | [optional]
 **name** | **str**| Retrieve a single result by LSU name. It will be ignored if &#39;id&#39; is also defined in the param. | [optional]
 **include_tenants** | **bool**| Whether to include LSU that belong to Tenants. This param is only effective when the User has privilege to view LSU details of a tenant. | [optional]

### Return type

[**[LSU]**](LSU.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pair_remote_lsu**
> LSU pair_remote_lsu(body)

Pair local and remote LSU.

**Privileges:** ```STORAGE_DOMAIN_MODIFY, CLUSTER_REMOTE_MODIFY``` <br><br>Pair local and remote LSU. The remote cluster must already be paired.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.lsu import LSU
from cohesity_sdk.cluster.model.pair_lsu_params import PairLSUParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = PairLSUParams() # PairLSUParams | Specifies the request to pair LSU.

# example passing only required values which don't have defaults set
try:
	# Pair local and remote LSU.
	api_response = client.lsu.pair_remote_lsu(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling LSUApi->pair_remote_lsu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PairLSUParams**](PairLSUParams.md)| Specifies the request to pair LSU. |

### Return type

[**LSU**](LSU.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lsu**
> LSU update_lsu(id, body)

Update LSU.

**Privileges:** ```STORAGE_DOMAIN_MODIFY``` <br><br>Update LSU.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.update_lsu_params import UpdateLSUParams
from cohesity_sdk.cluster.model.lsu import LSU
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


id = 1 # int | Specifies the LSU id to update.
body = UpdateLSUParams(
        name="name_example",
        nbu_domain="nbu_domain_example",
        worm_config=WormConfig(
            max_retention_secs=1,
            min_retention_secs=1,
            mode="Compliance",
        ),
    ) # UpdateLSUParams | Specifies the request to update an LSU.

# example passing only required values which don't have defaults set
try:
	# Update LSU.
	api_response = client.lsu.update_lsu(id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling LSUApi->update_lsu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the LSU id to update. |
 **body** | [**UpdateLSUParams**](UpdateLSUParams.md)| Specifies the request to update an LSU. |

### Return type

[**LSU**](LSU.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

