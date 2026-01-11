# cohesity_sdk.cluster.AntivirusServiceApi

All URIs are relative to *http://localhost/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_antivirus_group**](AntivirusServiceApi.md#create_antivirus_group) | **POST** /antivirus-service/groups | Create an Antivirus Service group.
[**delete_antivirus_group**](AntivirusServiceApi.md#delete_antivirus_group) | **DELETE** /antivirus-service/groups/{id} | Delete an Antivirus Service group
[**delete_infected_files**](AntivirusServiceApi.md#delete_infected_files) | **DELETE** /antivirus-service/infected-files | Delete infected files.
[**delete_infected_objects**](AntivirusServiceApi.md#delete_infected_objects) | **DELETE** /antivirus-service/infected-objects | Delete infected objects permanently.
[**get_antivirus_service_groups**](AntivirusServiceApi.md#get_antivirus_service_groups) | **GET** /antivirus-service/groups | Get Antivirus Service groups.
[**get_icap_uri_connection_status**](AntivirusServiceApi.md#get_icap_uri_connection_status) | **GET** /antivirus-service/icap-uri-connection-status | Get ICAP Uri connection status.
[**get_infected_files**](AntivirusServiceApi.md#get_infected_files) | **GET** /antivirus-service/infected-files | Get infected entities.
[**update_antivirus_group**](AntivirusServiceApi.md#update_antivirus_group) | **PUT** /antivirus-service/groups/{id} | Update an Antivirus Service group with given parameters or if state is specified, enable or disable given group.
[**update_infected_files**](AntivirusServiceApi.md#update_infected_files) | **PUT** /antivirus-service/infected-files | Update infected entities state.


# **create_antivirus_group**
> AntivirusServiceGroup create_antivirus_group(body)

Create an Antivirus Service group.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Create Antivirus Service group.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import antivirus_service
from cohesity_sdk.cluster.cohesity.model.antivirus_service_group import AntivirusServiceGroup
from cohesity_sdk.cluster.cohesity.model.create_antivirus_service_group_params import CreateAntivirusServiceGroupParams
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
    api_instance = antivirus_service.AntivirusServiceApi(api_client)
    body = CreateAntivirusServiceGroupParams(
        antivirus_services=[
            AntivirusService(
                description="description_example",
                icap_uri="icap_uri_example",
            ),
        ],
        description="description_example",
        enabled=True,
        name="name_example",
        state="Enable",
    ) # CreateAntivirusServiceGroupParams | Specifies the parameters to create antivirus service group.

    # example passing only required values which don't have defaults set
    try:
        # Create an Antivirus Service group.
        api_response = api_instance.create_antivirus_group(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling AntivirusServiceApi->create_antivirus_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAntivirusServiceGroupParams**](CreateAntivirusServiceGroupParams.md)| Specifies the parameters to create antivirus service group. |

### Return type

[**AntivirusServiceGroup**](AntivirusServiceGroup.md)

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

# **delete_antivirus_group**
> delete_antivirus_group(id)

Delete an Antivirus Service group

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Deletes an Antivirus service group based on given id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import antivirus_service
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
    api_instance = antivirus_service.AntivirusServiceApi(api_client)
    id = 1 # int | Specifies a unique id of the Antivirus Group to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete an Antivirus Service group
        api_instance.delete_antivirus_group(id)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling AntivirusServiceApi->delete_antivirus_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the Antivirus Group to delete. |

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

# **delete_infected_files**
> DeleteInfectedFiles delete_infected_files(body)

Delete infected files.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Delete infected files.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import antivirus_service
from cohesity_sdk.cluster.cohesity.model.delete_infected_files import DeleteInfectedFiles
from cohesity_sdk.cluster.cohesity.model.delete_infected_files_parameters import DeleteInfectedFilesParameters
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
    api_instance = antivirus_service.AntivirusServiceApi(api_client)
    body = DeleteInfectedFilesParameters(
        infected_files=[
            InfectedFile(
                antivirus_service_group_name="antivirus_service_group_name_example",
                antivirus_service_icap_uri="antivirus_service_icap_uri_example",
                detected_time_usecs=1,
                entity_id=1,
                entity_type="kObject",
                last_modified_time_usecs=1,
                path="path_example",
                root_inode_id=1,
                scanned_time_usecs=1,
                state="Quarantined",
                threat_descriptions=[
                    "threat_descriptions_example",
                ],
                view_id=1,
                view_name="view_name_example",
            ),
        ],
    ) # DeleteInfectedFilesParameters | Specifies the parameters of infected files to be deleted.

    # example passing only required values which don't have defaults set
    try:
        # Delete infected files.
        api_response = api_instance.delete_infected_files(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling AntivirusServiceApi->delete_infected_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteInfectedFilesParameters**](DeleteInfectedFilesParameters.md)| Specifies the parameters of infected files to be deleted. |

### Return type

[**DeleteInfectedFiles**](DeleteInfectedFiles.md)

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

# **delete_infected_objects**
> DeleteInfectedObjects delete_infected_objects(body)

Delete infected objects permanently.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Delete infected objects permanently.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import antivirus_service
from cohesity_sdk.cluster.cohesity.model.delete_infected_objects import DeleteInfectedObjects
from cohesity_sdk.cluster.cohesity.model.delete_infected_objects_parameters import DeleteInfectedObjectsParameters
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
    api_instance = antivirus_service.AntivirusServiceApi(api_client)
    body = DeleteInfectedObjectsParameters(
        infected_objects=[
            InfectedObject(
                bucket_name="bucket_name_example",
                object_name="object_name_example",
                version_id="version_id_example",
            ),
        ],
    ) # DeleteInfectedObjectsParameters | Specifies the parameters of infected objects to be deleted.

    # example passing only required values which don't have defaults set
    try:
        # Delete infected objects permanently.
        api_response = api_instance.delete_infected_objects(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling AntivirusServiceApi->delete_infected_objects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteInfectedObjectsParameters**](DeleteInfectedObjectsParameters.md)| Specifies the parameters of infected objects to be deleted. |

### Return type

[**DeleteInfectedObjects**](DeleteInfectedObjects.md)

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

# **get_antivirus_service_groups**
> AntivirusServiceGroups get_antivirus_service_groups()

Get Antivirus Service groups.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get Antivirus Service groups.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import antivirus_service
from cohesity_sdk.cluster.cohesity.model.antivirus_service_groups import AntivirusServiceGroups
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
    api_instance = antivirus_service.AntivirusServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Antivirus Service groups.
        api_response = api_instance.get_antivirus_service_groups()
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling AntivirusServiceApi->get_antivirus_service_groups: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AntivirusServiceGroups**](AntivirusServiceGroups.md)

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

# **get_icap_uri_connection_status**
> IcapUriConnectionStatusList get_icap_uri_connection_status()

Get ICAP Uri connection status.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get ICAP Uri connection status.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import antivirus_service
from cohesity_sdk.cluster.cohesity.model.icap_uri_connection_status_list import IcapUriConnectionStatusList
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
    api_instance = antivirus_service.AntivirusServiceApi(api_client)
    uris = [
        "uris_example",
    ] # [str] | Specifies a list of URIs to check connection status. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get ICAP Uri connection status.
        api_response = api_instance.get_icap_uri_connection_status(uris=uris)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling AntivirusServiceApi->get_icap_uri_connection_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | **[str]**| Specifies a list of URIs to check connection status. | [optional]

### Return type

[**IcapUriConnectionStatusList**](IcapUriConnectionStatusList.md)

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

# **get_infected_files**
> InfectedFiles get_infected_files()

Get infected entities.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Get infected entities.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import antivirus_service
from cohesity_sdk.cluster.cohesity.model.infected_files import InfectedFiles
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
    api_instance = antivirus_service.AntivirusServiceApi(api_client)
    view_ids = [
        1,
    ] # [int] | Specifies a list of view ids. Only infected entities from these views will be returned. (optional)
    path = "path_example" # str | Specifies the file path. (optional)
    states = [
        "Quarantined",
    ] # [str] | Specifies the file states. (optional)
    max_count = 1 # int | Specifies the max number of files to be returned. (optional)
    cookie = "cookie_example" # str | Specifies the pagination cookie. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get infected entities.
        api_response = api_instance.get_infected_files(view_ids=view_ids, path=path, states=states, max_count=max_count, cookie=cookie)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling AntivirusServiceApi->get_infected_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_ids** | **[int]**| Specifies a list of view ids. Only infected entities from these views will be returned. | [optional]
 **path** | **str**| Specifies the file path. | [optional]
 **states** | **[str]**| Specifies the file states. | [optional]
 **max_count** | **int**| Specifies the max number of files to be returned. | [optional]
 **cookie** | **str**| Specifies the pagination cookie. | [optional]

### Return type

[**InfectedFiles**](InfectedFiles.md)

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

# **update_antivirus_group**
> AntivirusServiceGroup update_antivirus_group(id, body)

Update an Antivirus Service group with given parameters or if state is specified, enable or disable given group.

**Privileges:** ```CLUSTER_VIEW``` <br><br>Update an Antivirus Service group.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import antivirus_service
from cohesity_sdk.cluster.cohesity.model.antivirus_service_group import AntivirusServiceGroup
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
    api_instance = antivirus_service.AntivirusServiceApi(api_client)
    id = 1 # int | Specifies a unique id of the Antivirus Group to update.
    body = AntivirusServiceGroup() # AntivirusServiceGroup | Specifies the parameters to update antivirus service group.

    # example passing only required values which don't have defaults set
    try:
        # Update an Antivirus Service group with given parameters or if state is specified, enable or disable given group.
        api_response = api_instance.update_antivirus_group(id, body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
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

# **update_infected_files**
> UpdateInfectedFilesList update_infected_files(body)

Update infected entities state.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Update infected entities state.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import antivirus_service
from cohesity_sdk.cluster.cohesity.model.update_infected_files_list import UpdateInfectedFilesList
from cohesity_sdk.cluster.cohesity.model.update_infected_files_parameters import UpdateInfectedFilesParameters
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
    api_instance = antivirus_service.AntivirusServiceApi(api_client)
    body = UpdateInfectedFilesParameters(
        infected_files=[
            InfectedFile(
                antivirus_service_group_name="antivirus_service_group_name_example",
                antivirus_service_icap_uri="antivirus_service_icap_uri_example",
                detected_time_usecs=1,
                entity_id=1,
                entity_type="kObject",
                last_modified_time_usecs=1,
                path="path_example",
                root_inode_id=1,
                scanned_time_usecs=1,
                state="Quarantined",
                threat_descriptions=[
                    "threat_descriptions_example",
                ],
                view_id=1,
                view_name="view_name_example",
            ),
        ],
        state="Quarantined",
    ) # UpdateInfectedFilesParameters | Specifies the parameters of infected entities to be updated.

    # example passing only required values which don't have defaults set
    try:
        # Update infected entities state.
        api_response = api_instance.update_infected_files(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling AntivirusServiceApi->update_infected_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateInfectedFilesParameters**](UpdateInfectedFilesParameters.md)| Specifies the parameters of infected entities to be updated. |

### Return type

[**UpdateInfectedFilesList**](UpdateInfectedFilesList.md)

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

