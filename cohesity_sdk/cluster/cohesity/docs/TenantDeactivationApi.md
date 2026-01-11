# cohesity_sdk.cluster.TenantDeactivationApi

All URIs are relative to *http://localhost/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**initiate_multi_tenant_deactivation**](TenantDeactivationApi.md#initiate_multi_tenant_deactivation) | **POST** /tenants/deactivations | 
[**initiate_tenant_deactivation**](TenantDeactivationApi.md#initiate_tenant_deactivation) | **POST** /tenants/{id}/deactivation | 


# **initiate_multi_tenant_deactivation**
> InitiateMultiTenantDeactivation initiate_multi_tenant_deactivation()



**Privileges:** ```ORGANIZATION_MODIFY``` <br><br>This API is to be used for initiating batch tenant deactivation workflow and orchestrating it

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tenant_deactivation
from cohesity_sdk.cluster.cohesity.model.initiate_multi_tenant_deactivation import InitiateMultiTenantDeactivation
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
    api_instance = tenant_deactivation.TenantDeactivationApi(api_client)
    liveness_mode = "Active" # str, none_type | Liveness mode for the tenants on this cluster. (optional)
    ownership_mode = "Primary" # str, none_type | Ownership mode for the tenants on this cluster. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.initiate_multi_tenant_deactivation(liveness_mode=liveness_mode, ownership_mode=ownership_mode)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling TenantDeactivationApi->initiate_multi_tenant_deactivation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **liveness_mode** | **str, none_type**| Liveness mode for the tenants on this cluster. | [optional]
 **ownership_mode** | **str, none_type**| Ownership mode for the tenants on this cluster. | [optional]

### Return type

[**InitiateMultiTenantDeactivation**](InitiateMultiTenantDeactivation.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_tenant_deactivation**
> InitiateTenantDeactivation initiate_tenant_deactivation(id)



```Unknown Privileges``` <br><br>This API is to be used for initiating a tenant deactivation workflow and orchestrating it. This API is not be confused with the tenants/{id}/actions API which only updates the tenant state in cluster config and mark it as active/ inactive.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import tenant_deactivation
from cohesity_sdk.cluster.cohesity.model.error import Error
from cohesity_sdk.cluster.cohesity.model.initiate_tenant_deactivation import InitiateTenantDeactivation
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
    api_instance = tenant_deactivation.TenantDeactivationApi(api_client)
    id = "C/" # str | The Tenant id.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.initiate_tenant_deactivation(id)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling TenantDeactivationApi->initiate_tenant_deactivation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Tenant id. |

### Return type

[**InitiateTenantDeactivation**](InitiateTenantDeactivation.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer), [SessionIdHeader](../README.md#SessionIdHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

