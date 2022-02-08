# cohesity_sdk.NodeGroupsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_node_group**](NodeGroupsApi.md#create_node_group) | **POST** /nodeGroups | Create a Node Group.
[**delete_node_group**](NodeGroupsApi.md#delete_node_group) | **DELETE** /nodeGroups/{groupName} | Delete a Node Group.
[**get_node_group_by_name**](NodeGroupsApi.md#get_node_group_by_name) | **GET** /nodeGroups/{groupName} | List Node Groups for a given Group Name.
[**get_node_groups**](NodeGroupsApi.md#get_node_groups) | **GET** /nodeGroups | List Node Groups based on provided filtering parameters.
[**update_node_group**](NodeGroupsApi.md#update_node_group) | **PUT** /nodeGroups/{groupName} | Update a Node Group.


# **create_node_group**
> NodeGroupResponse create_node_group(body)

Create a Node Group.

Create the Node Group and returns the newly created node group object.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.node_group_request import NodeGroupRequest
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.node_group_response import NodeGroupResponse
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = NodeGroupRequest() # NodeGroupRequest | Request to create a Node Group.

# example passing only required values which don't have defaults set
try:
	# Create a Node Group.
	api_response = client.node_groups.create_node_group(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NodeGroupsApi->create_node_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeGroupRequest**](NodeGroupRequest.md)| Request to create a Node Group. |

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
> delete_node_group(group_name)

Delete a Node Group.

Deletes a Node Group based on given node group name.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


group_name = "groupName_example" # str | Specifies a unique name of the Node Group to delete.

# example passing only required values which don't have defaults set
try:
	# Delete a Node Group.
	client.node_groups.delete_node_group(group_name)
except ApiException as e:
	print("Exception when calling NodeGroupsApi->delete_node_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Specifies a unique name of the Node Group to delete. |

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
> NodeGroupResponse get_node_group_by_name(group_name)

List Node Groups for a given Group Name.

Returns Node Group for given Group Name.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.node_group_response import NodeGroupResponse
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


group_name = "groupName_example" # str | Specifies a unique id of Node Group to return.

# example passing only required values which don't have defaults set
try:
	# List Node Groups for a given Group Name.
	api_response = client.node_groups.get_node_group_by_name(group_name)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NodeGroupsApi->get_node_group_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Specifies a unique id of Node Group to return. |

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
> NodeGroupResponse get_node_groups()

List Node Groups based on provided filtering parameters.

List node groups.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.node_group_response import NodeGroupResponse
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


group_names = [
        "groupNames_example",
    ] # [str] | Filter node groups by a list of node group names. (optional)
group_type = 1 # int | Filter node groups by a node group type. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# List Node Groups based on provided filtering parameters.
	api_response = client.node_groups.get_node_groups(group_names=group_names, group_type=group_type)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NodeGroupsApi->get_node_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_names** | **[str]**| Filter node groups by a list of node group names. | [optional]
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
> NodeGroupResponse update_node_group(group_name, body)

Update a Node Group.

Specifies the request to update the existing Node Group. On successful update, returns the updated node group object.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from cohesity_sdk import CohesityClientV2
from cohesity_sdk.cohesity_client_v2.model.node_group_request import NodeGroupRequest
from cohesity_sdk.cohesity_client_v2.model.error import Error
from cohesity_sdk.cohesity_client_v2.model.node_group_response import NodeGroupResponse
from cohesity_sdk.cohesity_client_v2.exceptions import ApiException
from pprint import pprint


client = CohesityClientV2(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


group_name = "groupName_example" # str | Specifies a unique name of the Node Group to update.
body = NodeGroupRequest() # NodeGroupRequest | Request to update a Node Group.

# example passing only required values which don't have defaults set
try:
	# Update a Node Group.
	api_response = client.node_groups.update_node_group(group_name, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling NodeGroupsApi->update_node_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Specifies a unique name of the Node Group to update. |
 **body** | [**NodeGroupRequest**](NodeGroupRequest.md)| Request to update a Node Group. |

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

