# cohesity_sdk.cluster.LSUApi

All URIs are relative to */v2*

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.create_lsu_params import CreateLSUParams
from cohesity_sdk.cluster.models.lsu import LSU
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.LSUApi(api_client)
    body = cohesity_sdk.cluster.CreateLSUParams() # CreateLSUParams | Specifies the request to create an LSU.

    try:
        # Create LSU.
        api_response = api_instance.create_lsu(body)
        print("The response of LSUApi->create_lsu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LSUApi->create_lsu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLSUParams**](CreateLSUParams.md)| Specifies the request to create an LSU. | 

### Return type

[**LSU**](LSU.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.common_lsu_pair_fields import CommonLSUPairFields
from cohesity_sdk.cluster.models.lsu import LSU
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.LSUApi(api_client)
    body = cohesity_sdk.cluster.CommonLSUPairFields() # CommonLSUPairFields | Specifies the request to pair LSU.

    try:
        # Delete LSU pairing.
        api_response = api_instance.delete_lsu_pairing(body)
        print("The response of LSUApi->delete_lsu_pairing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LSUApi->delete_lsu_pairing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **CommonLSUPairFields**| Specifies the request to pair LSU. | 

### Return type

[**LSU**](LSU.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
> List[LSU] get_lsu(id=id, name=name, include_tenants=include_tenants)

GET LSU.

**Privileges:** ```STORAGE_DOMAIN_VIEW``` <br><br>GET LSU.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.lsu import LSU
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.LSUApi(api_client)
    id = 56 # int | Retrieve a single result by LSU id. (optional)
    name = 'name_example' # str | Retrieve a single result by LSU name. It will be ignored if 'id' is also defined in the param. (optional)
    include_tenants = True # bool | Whether to include LSU that belong to Tenants. This param is only effective when the User has privilege to view LSU details of a tenant. (optional)

    try:
        # GET LSU.
        api_response = api_instance.get_lsu(id=id, name=name, include_tenants=include_tenants)
        print("The response of LSUApi->get_lsu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LSUApi->get_lsu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retrieve a single result by LSU id. | [optional] 
 **name** | **str**| Retrieve a single result by LSU name. It will be ignored if &#39;id&#39; is also defined in the param. | [optional] 
 **include_tenants** | **bool**| Whether to include LSU that belong to Tenants. This param is only effective when the User has privilege to view LSU details of a tenant. | [optional] 

### Return type

[**List[LSU]**](LSU.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.lsu import LSU
from cohesity_sdk.cluster.models.pair_lsu_params import PairLSUParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.LSUApi(api_client)
    body = cohesity_sdk.cluster.PairLSUParams() # PairLSUParams | Specifies the request to pair LSU.

    try:
        # Pair local and remote LSU.
        api_response = api_instance.pair_remote_lsu(body)
        print("The response of LSUApi->pair_remote_lsu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LSUApi->pair_remote_lsu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PairLSUParams**](PairLSUParams.md)| Specifies the request to pair LSU. | 

### Return type

[**LSU**](LSU.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.lsu import LSU
from cohesity_sdk.cluster.models.update_lsu_params import UpdateLSUParams
from cohesity_sdk.cluster.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cohesity_sdk.cluster.Configuration(
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

# Configure API key authorization: SessionIdHeader
configuration.api_key['SessionIdHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SessionIdHeader'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.LSUApi(api_client)
    id = 56 # int | Specifies the LSU id to update.
    body = cohesity_sdk.cluster.UpdateLSUParams() # UpdateLSUParams | Specifies the request to update an LSU.

    try:
        # Update LSU.
        api_response = api_instance.update_lsu(id, body)
        print("The response of LSUApi->update_lsu:\n")
        pprint(api_response)
    except Exception as e:
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

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

