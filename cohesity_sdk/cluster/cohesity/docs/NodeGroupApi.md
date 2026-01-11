# cohesity_sdk.cluster.NodeGroupApi

All URIs are relative to *http://localhost/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_node_group**](NodeGroupApi.md#create_node_group) | **POST** /node-groups | Create a Node Group.
[**delete_node_group**](NodeGroupApi.md#delete_node_group) | **DELETE** /node-groups/{groupName} | Delete a Node Group.
[**get_node_groups**](NodeGroupApi.md#get_node_groups) | **GET** /node-groups | List Node Groups based on provided filtering parameters.
[**update_node_group**](NodeGroupApi.md#update_node_group) | **PUT** /node-groups/{groupName} | Update a Node Group.


# **create_node_group**
> NodeGroupResponse create_node_group(body)

Create a Node Group.

**Privileges:** ```CLUSTER_MODIFY``` <br><br>Create the Node Group and returns the newly created node group object.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import node_group
from cohesity_sdk.cluster.cohesity.model.node_group_response import NodeGroupResponse
from cohesity_sdk.cluster.cohesity.model.node_group_request import NodeGroupRequest
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
    api_instance = node_group.NodeGroupApi(api_client)
    body = NodeGroupRequest() # NodeGroupRequest | Request to create a Node Group.

    # example passing only required values which don't have defaults set
    try:
        # Create a Node Group.
        api_response = api_instance.create_node_group(body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling NodeGroupApi->create_node_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeGroupRequest**](NodeGroupRequest.md)| Request to create a Node Group. |

### Return type

[**NodeGroupResponse**](NodeGroupResponse.md)

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

# **delete_node_group**
> delete_node_group(group_name)

Delete a Node Group.

```Unknown Privileges``` <br><br>Deletes a Node Group based on given node group name.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import node_group
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
    api_instance = node_group.NodeGroupApi(api_client)
    group_name = "groupName_example" # str | Specifies a unique name of the Node Group to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Node Group.
        api_instance.delete_node_group(group_name)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling NodeGroupApi->delete_node_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Specifies a unique name of the Node Group to delete. |

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

# **get_node_groups**
> NodeGroupResponse get_node_groups()

List Node Groups based on provided filtering parameters.

**Privileges:** ```CLUSTER_VIEW``` <br><br>List node groups.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import node_group
from cohesity_sdk.cluster.cohesity.model.node_group_response import NodeGroupResponse
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
    api_instance = node_group.NodeGroupApi(api_client)
    group_names = [
        "groupNames_example",
    ] # [str] | Filter node groups by a list of node group names. (optional)
    group_type = 1 # int | Filter node groups by a node group type. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Node Groups based on provided filtering parameters.
        api_response = api_instance.get_node_groups(group_names=group_names, group_type=group_type)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling NodeGroupApi->get_node_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_names** | **[str]**| Filter node groups by a list of node group names. | [optional]
 **group_type** | **int**| Filter node groups by a node group type. | [optional]

### Return type

[**NodeGroupResponse**](NodeGroupResponse.md)

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

# **update_node_group**
> NodeGroupResponse update_node_group(group_name, body)

Update a Node Group.

```Unknown Privileges``` <br><br>Specifies the request to update the existing Node Group. On successful update, returns the updated node group object.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
import time
import cohesity_sdk.cluster
from cohesity_sdk.cluster.api import node_group
from cohesity_sdk.cluster.cohesity.model.node_group_response import NodeGroupResponse
from cohesity_sdk.cluster.cohesity.model.node_group_request import NodeGroupRequest
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
    api_instance = node_group.NodeGroupApi(api_client)
    group_name = "groupName_example" # str | Specifies a unique name of the Node Group to update.
    body = NodeGroupRequest() # NodeGroupRequest | Request to update a Node Group.

    # example passing only required values which don't have defaults set
    try:
        # Update a Node Group.
        api_response = api_instance.update_node_group(group_name, body)
        pprint(api_response)
    except cohesity_sdk.cluster.ApiException as e:
        print("Exception when calling NodeGroupApi->update_node_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Specifies a unique name of the Node Group to update. |
 **body** | [**NodeGroupRequest**](NodeGroupRequest.md)| Request to update a Node Group. |

### Return type

[**NodeGroupResponse**](NodeGroupResponse.md)

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

