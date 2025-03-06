# cohesity_sdk.cluster.AntivirusServiceApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_antivirus_group**](AntivirusServiceApi.md#create_antivirus_group) | **POST** /antivirus-service/groups | Create an Antivirus Service group.
[**delete_antivirus_group**](AntivirusServiceApi.md#delete_antivirus_group) | **DELETE** /antivirus-service/groups/{id} | Delete an Antivirus Service group
[**delete_infected_files**](AntivirusServiceApi.md#delete_infected_files) | **DELETE** /antivirus-service/infected-files | Delete infected files.
[**get_antivirus_service_groups**](AntivirusServiceApi.md#get_antivirus_service_groups) | **GET** /antivirus-service/groups | Get Antivirus Service groups.
[**get_icap_uri_connection_status**](AntivirusServiceApi.md#get_icap_uri_connection_status) | **GET** /antivirus-service/icap-uri-connection-status | Get ICAP Uri connection status.
[**get_infected_files**](AntivirusServiceApi.md#get_infected_files) | **GET** /antivirus-service/infected-files | Get infected files.
[**update_antivirus_group**](AntivirusServiceApi.md#update_antivirus_group) | **PUT** /antivirus-service/groups/{id} | Update an Antivirus Service group with given parameters or if state is specified, enable or disable given group.
[**update_infected_files**](AntivirusServiceApi.md#update_infected_files) | **PUT** /antivirus-service/infected-files | Update infected files state.


# **create_antivirus_group**
> AntivirusServiceGroup create_antivirus_group(body)

Create an Antivirus Service group.

Create Antivirus Service group.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.antivirus_service_group import AntivirusServiceGroup
from cohesity_sdk.cluster.models.create_antivirus_service_group_params import CreateAntivirusServiceGroupParams
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.AntivirusServiceApi(api_client)
    body = cohesity_sdk.cluster.CreateAntivirusServiceGroupParams() # CreateAntivirusServiceGroupParams | Specifies the parameters to create antivirus service group.

    try:
        # Create an Antivirus Service group.
        api_response = api_instance.create_antivirus_group(body)
        print("The response of AntivirusServiceApi->create_antivirus_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntivirusServiceApi->create_antivirus_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAntivirusServiceGroupParams**](CreateAntivirusServiceGroupParams.md)| Specifies the parameters to create antivirus service group. | 

### Return type

[**AntivirusServiceGroup**](AntivirusServiceGroup.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_antivirus_group**
> delete_antivirus_group(id)

Delete an Antivirus Service group

Deletes an Antivirus service group based on given id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.AntivirusServiceApi(api_client)
    id = 56 # int | Specifies a unique id of the Antivirus Group to delete.

    try:
        # Delete an Antivirus Service group
        api_instance.delete_antivirus_group(id)
    except Exception as e:
        print("Exception when calling AntivirusServiceApi->delete_antivirus_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the Antivirus Group to delete. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_infected_files**
> DeleteInfectedFiles delete_infected_files(body)

Delete infected files.

Delete infected files.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.delete_infected_files import DeleteInfectedFiles
from cohesity_sdk.cluster.models.delete_infected_files_parameters import DeleteInfectedFilesParameters
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.AntivirusServiceApi(api_client)
    body = cohesity_sdk.cluster.DeleteInfectedFilesParameters() # DeleteInfectedFilesParameters | Specifies the parameters of infected files to be deleted.

    try:
        # Delete infected files.
        api_response = api_instance.delete_infected_files(body)
        print("The response of AntivirusServiceApi->delete_infected_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntivirusServiceApi->delete_infected_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteInfectedFilesParameters**](DeleteInfectedFilesParameters.md)| Specifies the parameters of infected files to be deleted. | 

### Return type

[**DeleteInfectedFiles**](DeleteInfectedFiles.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_antivirus_service_groups**
> AntivirusServiceGroups get_antivirus_service_groups()

Get Antivirus Service groups.

Get Antivirus Service groups.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.antivirus_service_groups import AntivirusServiceGroups
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.AntivirusServiceApi(api_client)

    try:
        # Get Antivirus Service groups.
        api_response = api_instance.get_antivirus_service_groups()
        print("The response of AntivirusServiceApi->get_antivirus_service_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntivirusServiceApi->get_antivirus_service_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AntivirusServiceGroups**](AntivirusServiceGroups.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_icap_uri_connection_status**
> IcapUriConnectionStatusList get_icap_uri_connection_status(uris=uris)

Get ICAP Uri connection status.

Get ICAP Uri connection status.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.icap_uri_connection_status_list import IcapUriConnectionStatusList
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.AntivirusServiceApi(api_client)
    uris = ['uris_example'] # List[str] | Specifies a list of URIs to check connection status. (optional)

    try:
        # Get ICAP Uri connection status.
        api_response = api_instance.get_icap_uri_connection_status(uris=uris)
        print("The response of AntivirusServiceApi->get_icap_uri_connection_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntivirusServiceApi->get_icap_uri_connection_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**List[str]**](str.md)| Specifies a list of URIs to check connection status. | [optional] 

### Return type

[**IcapUriConnectionStatusList**](IcapUriConnectionStatusList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_infected_files**
> InfectedFiles get_infected_files(view_ids=view_ids, path=path, states=states, max_count=max_count, cookie=cookie)

Get infected files.

Get infected files.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.infected_files import InfectedFiles
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.AntivirusServiceApi(api_client)
    view_ids = [56] # List[int] | Specifies a list of view ids. Only infected files from these views will be returned. (optional)
    path = 'path_example' # str | Specifies the file path. (optional)
    states = ['states_example'] # List[str] | Specifies the file states. (optional)
    max_count = 56 # int | Specifies the max number of files to be returned. (optional)
    cookie = 'cookie_example' # str | Specifies the pagination cookie. (optional)

    try:
        # Get infected files.
        api_response = api_instance.get_infected_files(view_ids=view_ids, path=path, states=states, max_count=max_count, cookie=cookie)
        print("The response of AntivirusServiceApi->get_infected_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntivirusServiceApi->get_infected_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_ids** | [**List[int]**](int.md)| Specifies a list of view ids. Only infected files from these views will be returned. | [optional] 
 **path** | **str**| Specifies the file path. | [optional] 
 **states** | [**List[str]**](str.md)| Specifies the file states. | [optional] 
 **max_count** | **int**| Specifies the max number of files to be returned. | [optional] 
 **cookie** | **str**| Specifies the pagination cookie. | [optional] 

### Return type

[**InfectedFiles**](InfectedFiles.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_antivirus_group**
> AntivirusServiceGroup update_antivirus_group(id, body)

Update an Antivirus Service group with given parameters or if state is specified, enable or disable given group.

Update an Antivirus Service group.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.antivirus_service_group import AntivirusServiceGroup
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.AntivirusServiceApi(api_client)
    id = 56 # int | Specifies a unique id of the Antivirus Group to update.
    body = cohesity_sdk.cluster.AntivirusServiceGroup() # AntivirusServiceGroup | Specifies the parameters to update antivirus service group.

    try:
        # Update an Antivirus Service group with given parameters or if state is specified, enable or disable given group.
        api_response = api_instance.update_antivirus_group(id, body)
        print("The response of AntivirusServiceApi->update_antivirus_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntivirusServiceApi->update_antivirus_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the Antivirus Group to update. | 
 **body** | [**AntivirusServiceGroup**](AntivirusServiceGroup.md)| Specifies the parameters to update antivirus service group. | 

### Return type

[**AntivirusServiceGroup**](AntivirusServiceGroup.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_infected_files**
> UpdateInfectedFilesList update_infected_files(body)

Update infected files state.

Update infected files state.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.update_infected_files_list import UpdateInfectedFilesList
from cohesity_sdk.cluster.models.update_infected_files_parameters import UpdateInfectedFilesParameters
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

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with cohesity_sdk.cluster.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cohesity_sdk.cluster.AntivirusServiceApi(api_client)
    body = cohesity_sdk.cluster.UpdateInfectedFilesParameters() # UpdateInfectedFilesParameters | Specifies the parameters of infected files to be updated.

    try:
        # Update infected files state.
        api_response = api_instance.update_infected_files(body)
        print("The response of AntivirusServiceApi->update_infected_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntivirusServiceApi->update_infected_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateInfectedFilesParameters**](UpdateInfectedFilesParameters.md)| Specifies the parameters of infected files to be updated. | 

### Return type

[**UpdateInfectedFilesList**](UpdateInfectedFilesList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

