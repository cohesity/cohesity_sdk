# cohesity_sdk.helios.AntivirusServiceApi

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
> AntivirusServiceGroup create_antivirus_group(body, access_cluster_id=access_cluster_id, region_id=region_id)

Create an Antivirus Service group.

Create Antivirus Service group.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.antivirus_service_group import AntivirusServiceGroup
from cohesity_sdk.helios.models.create_antivirus_service_group_params import CreateAntivirusServiceGroupParams
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
    api_instance = cohesity_sdk.helios.AntivirusServiceApi(api_client)
    body = cohesity_sdk.helios.CreateAntivirusServiceGroupParams() # CreateAntivirusServiceGroupParams | Specifies the parameters to create antivirus service group.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Create an Antivirus Service group.
        api_response = api_instance.create_antivirus_group(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of AntivirusServiceApi->create_antivirus_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntivirusServiceApi->create_antivirus_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAntivirusServiceGroupParams**](CreateAntivirusServiceGroupParams.md)| Specifies the parameters to create antivirus service group. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**AntivirusServiceGroup**](AntivirusServiceGroup.md)

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

# **delete_antivirus_group**
> delete_antivirus_group(id, access_cluster_id=access_cluster_id, region_id=region_id)

Delete an Antivirus Service group

Deletes an Antivirus service group based on given id.

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
    api_instance = cohesity_sdk.helios.AntivirusServiceApi(api_client)
    id = 56 # int | Specifies a unique id of the Antivirus Group to delete.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Delete an Antivirus Service group
        api_instance.delete_antivirus_group(id, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
        print("Exception when calling AntivirusServiceApi->delete_antivirus_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the Antivirus Group to delete. | 
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

# **delete_infected_files**
> DeleteInfectedFiles delete_infected_files(body, access_cluster_id=access_cluster_id, region_id=region_id)

Delete infected files.

Delete infected files.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.delete_infected_files import DeleteInfectedFiles
from cohesity_sdk.helios.models.delete_infected_files_parameters import DeleteInfectedFilesParameters
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
    api_instance = cohesity_sdk.helios.AntivirusServiceApi(api_client)
    body = cohesity_sdk.helios.DeleteInfectedFilesParameters() # DeleteInfectedFilesParameters | Specifies the parameters of infected files to be deleted.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Delete infected files.
        api_response = api_instance.delete_infected_files(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of AntivirusServiceApi->delete_infected_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntivirusServiceApi->delete_infected_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteInfectedFilesParameters**](DeleteInfectedFilesParameters.md)| Specifies the parameters of infected files to be deleted. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**DeleteInfectedFiles**](DeleteInfectedFiles.md)

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

# **get_antivirus_service_groups**
> AntivirusServiceGroups get_antivirus_service_groups(access_cluster_id=access_cluster_id, region_id=region_id)

Get Antivirus Service groups.

Get Antivirus Service groups.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.antivirus_service_groups import AntivirusServiceGroups
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
    api_instance = cohesity_sdk.helios.AntivirusServiceApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Get Antivirus Service groups.
        api_response = api_instance.get_antivirus_service_groups(access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of AntivirusServiceApi->get_antivirus_service_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntivirusServiceApi->get_antivirus_service_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**AntivirusServiceGroups**](AntivirusServiceGroups.md)

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

# **get_icap_uri_connection_status**
> IcapUriConnectionStatusList get_icap_uri_connection_status(access_cluster_id=access_cluster_id, region_id=region_id, uris=uris)

Get ICAP Uri connection status.

Get ICAP Uri connection status.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.icap_uri_connection_status_list import IcapUriConnectionStatusList
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
    api_instance = cohesity_sdk.helios.AntivirusServiceApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    uris = ['uris_example'] # List[str] | Specifies a list of URIs to check connection status. (optional)

    try:
        # Get ICAP Uri connection status.
        api_response = api_instance.get_icap_uri_connection_status(access_cluster_id=access_cluster_id, region_id=region_id, uris=uris)
        print("The response of AntivirusServiceApi->get_icap_uri_connection_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntivirusServiceApi->get_icap_uri_connection_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **uris** | [**List[str]**](str.md)| Specifies a list of URIs to check connection status. | [optional] 

### Return type

[**IcapUriConnectionStatusList**](IcapUriConnectionStatusList.md)

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

# **get_infected_files**
> InfectedFiles get_infected_files(access_cluster_id=access_cluster_id, region_id=region_id, view_ids=view_ids, path=path, states=states, max_count=max_count, cookie=cookie)

Get infected files.

Get infected files.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.infected_files import InfectedFiles
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
    api_instance = cohesity_sdk.helios.AntivirusServiceApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    view_ids = [56] # List[int] | Specifies a list of view ids. Only infected files from these views will be returned. (optional)
    path = 'path_example' # str | Specifies the file path. (optional)
    states = ['states_example'] # List[str] | Specifies the file states. (optional)
    max_count = 56 # int | Specifies the max number of files to be returned. (optional)
    cookie = 'cookie_example' # str | Specifies the pagination cookie. (optional)

    try:
        # Get infected files.
        api_response = api_instance.get_infected_files(access_cluster_id=access_cluster_id, region_id=region_id, view_ids=view_ids, path=path, states=states, max_count=max_count, cookie=cookie)
        print("The response of AntivirusServiceApi->get_infected_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntivirusServiceApi->get_infected_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **view_ids** | [**List[int]**](int.md)| Specifies a list of view ids. Only infected files from these views will be returned. | [optional] 
 **path** | **str**| Specifies the file path. | [optional] 
 **states** | [**List[str]**](str.md)| Specifies the file states. | [optional] 
 **max_count** | **int**| Specifies the max number of files to be returned. | [optional] 
 **cookie** | **str**| Specifies the pagination cookie. | [optional] 

### Return type

[**InfectedFiles**](InfectedFiles.md)

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

# **update_antivirus_group**
> AntivirusServiceGroup update_antivirus_group(id, body, access_cluster_id=access_cluster_id, region_id=region_id)

Update an Antivirus Service group with given parameters or if state is specified, enable or disable given group.

Update an Antivirus Service group.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.antivirus_service_group import AntivirusServiceGroup
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
    api_instance = cohesity_sdk.helios.AntivirusServiceApi(api_client)
    id = 56 # int | Specifies a unique id of the Antivirus Group to update.
    body = cohesity_sdk.helios.AntivirusServiceGroup() # AntivirusServiceGroup | Specifies the parameters to update antivirus service group.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update an Antivirus Service group with given parameters or if state is specified, enable or disable given group.
        api_response = api_instance.update_antivirus_group(id, body, access_cluster_id=access_cluster_id, region_id=region_id)
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
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**AntivirusServiceGroup**](AntivirusServiceGroup.md)

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

# **update_infected_files**
> UpdateInfectedFilesList update_infected_files(body, access_cluster_id=access_cluster_id, region_id=region_id)

Update infected files state.

Update infected files state.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.update_infected_files_list import UpdateInfectedFilesList
from cohesity_sdk.helios.models.update_infected_files_parameters import UpdateInfectedFilesParameters
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
    api_instance = cohesity_sdk.helios.AntivirusServiceApi(api_client)
    body = cohesity_sdk.helios.UpdateInfectedFilesParameters() # UpdateInfectedFilesParameters | Specifies the parameters of infected files to be updated.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update infected files state.
        api_response = api_instance.update_infected_files(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of AntivirusServiceApi->update_infected_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntivirusServiceApi->update_infected_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateInfectedFilesParameters**](UpdateInfectedFilesParameters.md)| Specifies the parameters of infected files to be updated. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**UpdateInfectedFilesList**](UpdateInfectedFilesList.md)

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

