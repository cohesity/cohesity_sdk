# cohesity_sdk.cluster.KeyManagementSystemApi

All URIs are relative to *http://localhost/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_kms_configuration**](KeyManagementSystemApi.md#add_kms_configuration) | **POST** /kms | Add KMS
[**delete_kms_config**](KeyManagementSystemApi.md#delete_kms_config) | **DELETE** /kms/{id} | Delete KMS
[**get_kms_configurations**](KeyManagementSystemApi.md#get_kms_configurations) | **GET** /kms | Get KMS
[**update_kms_configuration**](KeyManagementSystemApi.md#update_kms_configuration) | **PUT** /kms/{id} | Update KMS


# **add_kms_configuration**
> KmsConfiguration add_kms_configuration(body)

Add KMS

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Add a key management system(KMS) to the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import key_management_system
from cohesity_sdk.cluster.cohesity.model.kms_configuration import KmsConfiguration
from cohesity_sdk.cluster.cohesity.model.kms_configuration_create_params import KmsConfigurationCreateParams
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_management_system.KeyManagementSystemApi(api_client)
    body = KmsConfigurationCreateParams() # KmsConfigurationCreateParams | Parameters to add KMS on the cluster.

    # example passing only required values which don't have defaults set
    try:
        # Add KMS
        api_response = api_instance.add_kms_configuration(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling KeyManagementSystemApi->add_kms_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KmsConfigurationCreateParams**](KmsConfigurationCreateParams.md)| Parameters to add KMS on the cluster. |

### Return type

[**KmsConfiguration**](KmsConfiguration.md)

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

# **delete_kms_config**
> delete_kms_config(id)

Delete KMS

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Delete KMS configued on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import key_management_system
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_management_system.KeyManagementSystemApi(api_client)
    id = 1 # int | ID of the KMS configured on the cluster.

    # example passing only required values which don't have defaults set
    try:
        # Delete KMS
        api_instance.delete_kms_config(id)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling KeyManagementSystemApi->delete_kms_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the KMS configured on the cluster. |

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

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

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get key management systems(KMS) configured on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import key_management_system
from cohesity_sdk.cluster.cohesity.model.kms_configurations import KmsConfigurations
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_management_system.KeyManagementSystemApi(api_client)
    ids = [
        1,
    ] # [int] | Ids of KMS configured on the cluster. (optional)
    include_rpaas_kms = True # bool, none_type | If true, returns KMS that are configured by FortKnox. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get KMS
        api_response = api_instance.get_kms_configurations(ids=ids, include_rpaas_kms=include_rpaas_kms)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
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

# **update_kms_configuration**
> KmsConfiguration update_kms_configuration(id, body)

Update KMS

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update KMS on the cluster.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import key_management_system
from cohesity_sdk.cluster.cohesity.model.kms_configuration_update_params import KmsConfigurationUpdateParams
from cohesity_sdk.cluster.cohesity.model.kms_configuration import KmsConfiguration
from cohesity_sdk.cluster.cohesity.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
    host = "http://localhost/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = key_management_system.KeyManagementSystemApi(api_client)
    id = 1 # int | ID of the KMS configured on the cluster.
    body = KmsConfigurationUpdateParams() # KmsConfigurationUpdateParams | Parameters to update KMS on the cluster.

    # example passing only required values which don't have defaults set
    try:
        # Update KMS
        api_response = api_instance.update_kms_configuration(id, body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
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

