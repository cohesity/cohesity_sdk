# cohesity_sdk.helios.KeyManagementSystemApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_kms_configuration**](KeyManagementSystemApi.md#add_kms_configuration) | **POST** /kms | Add KMS
[**delete_kms_config**](KeyManagementSystemApi.md#delete_kms_config) | **DELETE** /kms/{id} | Delete KMS
[**get_kms_configurations**](KeyManagementSystemApi.md#get_kms_configurations) | **GET** /kms | Get KMS
[**update_kms_configuration**](KeyManagementSystemApi.md#update_kms_configuration) | **PUT** /kms/{id} | Update KMS


# **add_kms_configuration**
> KmsConfiguration add_kms_configuration(body, access_cluster_id=access_cluster_id, region_id=region_id)

Add KMS

Add a key management system(KMS) to the cluster.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.kms_configuration import KmsConfiguration
from cohesity_sdk.helios.models.kms_configuration_create_params import KmsConfigurationCreateParams
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
    api_instance = cohesity_sdk.helios.KeyManagementSystemApi(api_client)
    body = cohesity_sdk.helios.KmsConfigurationCreateParams() # KmsConfigurationCreateParams | Parameters to add KMS on the cluster.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Add KMS
        api_response = api_instance.add_kms_configuration(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of KeyManagementSystemApi->add_kms_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyManagementSystemApi->add_kms_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KmsConfigurationCreateParams**](KmsConfigurationCreateParams.md)| Parameters to add KMS on the cluster. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**KmsConfiguration**](KmsConfiguration.md)

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

# **delete_kms_config**
> delete_kms_config(id, access_cluster_id=access_cluster_id, region_id=region_id)

Delete KMS

Delete KMS configued on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
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
    api_instance = cohesity_sdk.helios.KeyManagementSystemApi(api_client)
    id = 56 # int | ID of the KMS configured on the cluster.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Delete KMS
        api_instance.delete_kms_config(id, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
        print("Exception when calling KeyManagementSystemApi->delete_kms_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the KMS configured on the cluster. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

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
> KmsConfigurations get_kms_configurations(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, include_rpaas_kms=include_rpaas_kms)

Get KMS

Get key management systems(KMS) configured on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.kms_configurations import KmsConfigurations
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
    api_instance = cohesity_sdk.helios.KeyManagementSystemApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    ids = [56] # List[int] | Ids of KMS configured on the cluster. (optional)
    include_rpaas_kms = True # bool | If true, returns KMS that are configured by FortKnox. (optional)

    try:
        # Get KMS
        api_response = api_instance.get_kms_configurations(access_cluster_id=access_cluster_id, region_id=region_id, ids=ids, include_rpaas_kms=include_rpaas_kms)
        print("The response of KeyManagementSystemApi->get_kms_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyManagementSystemApi->get_kms_configurations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **ids** | [**List[int]**](int.md)| Ids of KMS configured on the cluster. | [optional] 
 **include_rpaas_kms** | **bool**| If true, returns KMS that are configured by FortKnox. | [optional] 

### Return type

[**KmsConfigurations**](KmsConfigurations.md)

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

# **update_kms_configuration**
> KmsConfiguration update_kms_configuration(id, body, access_cluster_id=access_cluster_id, region_id=region_id)

Update KMS

Update KMS on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.kms_configuration import KmsConfiguration
from cohesity_sdk.helios.models.kms_configuration_update_params import KmsConfigurationUpdateParams
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
    api_instance = cohesity_sdk.helios.KeyManagementSystemApi(api_client)
    id = 56 # int | ID of the KMS configured on the cluster.
    body = cohesity_sdk.helios.KmsConfigurationUpdateParams() # KmsConfigurationUpdateParams | Parameters to update KMS on the cluster.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update KMS
        api_response = api_instance.update_kms_configuration(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of KeyManagementSystemApi->update_kms_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyManagementSystemApi->update_kms_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the KMS configured on the cluster. | 
 **body** | [**KmsConfigurationUpdateParams**](KmsConfigurationUpdateParams.md)| Parameters to update KMS on the cluster. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**KmsConfiguration**](KmsConfiguration.md)

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

