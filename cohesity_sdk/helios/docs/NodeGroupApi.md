# cohesity_sdk.helios.NodeGroupApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_node_group**](NodeGroupApi.md#create_node_group) | **POST** /node-groups | Create a Node Group.
[**delete_node_group**](NodeGroupApi.md#delete_node_group) | **DELETE** /node-groups/{groupName} | Delete a Node Group.
[**get_node_group_by_name**](NodeGroupApi.md#get_node_group_by_name) | **GET** /node-groups/{groupName} | List Node Groups for a given Group Name.
[**get_node_groups**](NodeGroupApi.md#get_node_groups) | **GET** /node-groups | List Node Groups based on provided filtering parameters.
[**update_node_group**](NodeGroupApi.md#update_node_group) | **PUT** /node-groups/{groupName} | Update a Node Group.


# **create_node_group**
> NodeGroupResponse create_node_group(body, access_cluster_id=access_cluster_id, region_id=region_id)

Create a Node Group.

Create the Node Group and returns the newly created node group object.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.node_group_request import NodeGroupRequest
from cohesity_sdk.helios.models.node_group_response import NodeGroupResponse
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
    api_instance = cohesity_sdk.helios.NodeGroupApi(api_client)
    body = cohesity_sdk.helios.NodeGroupRequest() # NodeGroupRequest | Request to create a Node Group.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Create a Node Group.
        api_response = api_instance.create_node_group(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of NodeGroupApi->create_node_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeGroupApi->create_node_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeGroupRequest**](NodeGroupRequest.md)| Request to create a Node Group. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**NodeGroupResponse**](NodeGroupResponse.md)

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

# **delete_node_group**
> delete_node_group(group_name, access_cluster_id=access_cluster_id, region_id=region_id)

Delete a Node Group.

Deletes a Node Group based on given node group name.

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
    api_instance = cohesity_sdk.helios.NodeGroupApi(api_client)
    group_name = 'group_name_example' # str | Specifies a unique name of the Node Group to delete.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Delete a Node Group.
        api_instance.delete_node_group(group_name, access_cluster_id=access_cluster_id, region_id=region_id)
    except Exception as e:
        print("Exception when calling NodeGroupApi->delete_node_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Specifies a unique name of the Node Group to delete. | 
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

# **get_node_group_by_name**
> NodeGroupResponse get_node_group_by_name(group_name, access_cluster_id=access_cluster_id, region_id=region_id)

List Node Groups for a given Group Name.

Returns Node Group for given Group Name.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.node_group_response import NodeGroupResponse
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
    api_instance = cohesity_sdk.helios.NodeGroupApi(api_client)
    group_name = 'group_name_example' # str | Specifies a unique id of Node Group to return.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # List Node Groups for a given Group Name.
        api_response = api_instance.get_node_group_by_name(group_name, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of NodeGroupApi->get_node_group_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeGroupApi->get_node_group_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Specifies a unique id of Node Group to return. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**NodeGroupResponse**](NodeGroupResponse.md)

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

# **get_node_groups**
> NodeGroupResponse get_node_groups(access_cluster_id=access_cluster_id, region_id=region_id, group_names=group_names, group_type=group_type)

List Node Groups based on provided filtering parameters.

List node groups.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.node_group_response import NodeGroupResponse
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
    api_instance = cohesity_sdk.helios.NodeGroupApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    group_names = ['group_names_example'] # List[str] | Filter node groups by a list of node group names. (optional)
    group_type = 56 # int | Filter node groups by a node group type. (optional)

    try:
        # List Node Groups based on provided filtering parameters.
        api_response = api_instance.get_node_groups(access_cluster_id=access_cluster_id, region_id=region_id, group_names=group_names, group_type=group_type)
        print("The response of NodeGroupApi->get_node_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeGroupApi->get_node_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **group_names** | [**List[str]**](str.md)| Filter node groups by a list of node group names. | [optional] 
 **group_type** | **int**| Filter node groups by a node group type. | [optional] 

### Return type

[**NodeGroupResponse**](NodeGroupResponse.md)

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

# **update_node_group**
> NodeGroupResponse update_node_group(group_name, body, access_cluster_id=access_cluster_id, region_id=region_id)

Update a Node Group.

Specifies the request to update the existing Node Group. On successful update, returns the updated node group object.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.node_group_request import NodeGroupRequest
from cohesity_sdk.helios.models.node_group_response import NodeGroupResponse
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
    api_instance = cohesity_sdk.helios.NodeGroupApi(api_client)
    group_name = 'group_name_example' # str | Specifies a unique name of the Node Group to update.
    body = cohesity_sdk.helios.NodeGroupRequest() # NodeGroupRequest | Request to update a Node Group.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Update a Node Group.
        api_response = api_instance.update_node_group(group_name, body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of NodeGroupApi->update_node_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodeGroupApi->update_node_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Specifies a unique name of the Node Group to update. | 
 **body** | [**NodeGroupRequest**](NodeGroupRequest.md)| Request to update a Node Group. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**NodeGroupResponse**](NodeGroupResponse.md)

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

