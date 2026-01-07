# cohesity_sdk.DataAccessorApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_access_session**](DataAccessorApi.md#create_data_access_session) | **POST** /data-access/snapshots/sessions | Create Data Access Session
[**difference_of_graph_nodes**](DataAccessorApi.md#difference_of_graph_nodes) | **POST** /data-access/snapshots/sessions/{sessionId}/graph-nodes/differences | Difference of Graph nodes
[**get_data_access_sessions**](DataAccessorApi.md#get_data_access_sessions) | **GET** /data-access/snapshots/sessions | Lists all the Data Access Sessions
[**get_graph_node_relations_differences**](DataAccessorApi.md#get_graph_node_relations_differences) | **POST** /data-access/snapshots/sessions/{sessionId}/graph-nodes/query-relations/{nodeId}/differences | Query for difference of graph node relations
[**get_graph_nodes_details**](DataAccessorApi.md#get_graph_nodes_details) | **POST** /data-access/snapshots/sessions/{sessionId}/graph-nodes | Get Graph Nodes details
[**search_graph_nodes**](DataAccessorApi.md#search_graph_nodes) | **POST** /data-access/snapshots/sessions/graph-nodes/query | Search Graph nodes
[**tear_down_data_access_session**](DataAccessorApi.md#tear_down_data_access_session) | **DELETE** /data-access/snapshots/sessions/{sessionId} | Tear down data access session for a given id


# **create_data_access_session**
> CreateDataAccessSessionResponseParams create_data_access_session(body)

Create Data Access Session

```No Privileges Required``` <br><br>Create data access session.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.create_data_access_session_request_params import CreateDataAccessSessionRequestParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.create_data_access_session_response_params import CreateDataAccessSessionResponseParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = CreateDataAccessSessionRequestParams(
        base_snapshot_info=DataAccessSnapshotInfo(
            environment="kVMware",
            restore_time_usecs=1,
            snapshot_id="snapshot_id_example",
        ),
        current_snapshot_info=DataAccessSnapshotInfo(
            environment="kVMware",
            restore_time_usecs=1,
            snapshot_id="snapshot_id_example",
        ),
        session_name="session_name_example",
        source_id=1,
    ) # CreateDataAccessSessionRequestParams | Specifies the parameters to create data access session

# example passing only required values which don't have defaults set
try:
	# Create Data Access Session
	api_response = client.data_accessor.create_data_access_session(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataAccessorApi->create_data_access_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDataAccessSessionRequestParams**](CreateDataAccessSessionRequestParams.md)| Specifies the parameters to create data access session |

### Return type

[**CreateDataAccessSessionResponseParams**](CreateDataAccessSessionResponseParams.md)

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

# **difference_of_graph_nodes**
> QueryGraphNodesDiffResult difference_of_graph_nodes(session_id, body)

Difference of Graph nodes

```Unknown Privileges``` <br><br>Query for difference of graph nodes between two snapshots of a session.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.query_graph_nodes_diff_result import QueryGraphNodesDiffResult
from cohesity_sdk.cluster.model.query_graph_nodes_diff_params import QueryGraphNodesDiffParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


session_id = "sessionId_example" # str | Specifies the id of a session.
body = QueryGraphNodesDiffParams(
        count=1,
        diff_types=[
            "Added",
        ],
        node_filter=GraphNodeFilterParams(),
        pagination_cookie="pagination_cookie_example",
        session_id="session_id_example",
    ) # QueryGraphNodesDiffParams | Specifies the parameters to determine graph nodes diff for a given session id.

# example passing only required values which don't have defaults set
try:
	# Difference of Graph nodes
	api_response = client.data_accessor.difference_of_graph_nodes(session_id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataAccessorApi->difference_of_graph_nodes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Specifies the id of a session. |
 **body** | [**QueryGraphNodesDiffParams**](QueryGraphNodesDiffParams.md)| Specifies the parameters to determine graph nodes diff for a given session id. |

### Return type

[**QueryGraphNodesDiffResult**](QueryGraphNodesDiffResult.md)

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

# **get_data_access_sessions**
> GetDataAccessSessionsResponseParams get_data_access_sessions()

Lists all the Data Access Sessions

```No Privileges Required``` <br><br>Lists the Data Access Sessions.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.get_data_access_sessions_response_params import GetDataAccessSessionsResponseParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


session_ids = [
        "sessionIds_example",
    ] # [str] | Filter Data Access Sessions for given session ids. (optional)
start_time_usecs = 1 # int | Returns the data access sessions which are started after the specific time. This value should be in Unix timestamp epoch in microseconds. (optional)
end_time_usecs = 1 # int | Returns the data access sessions which are started before the specific time. This value should be in Unix timestamp epoch in microseconds. (optional)
snapshot_environments = [
        "kVMware",
    ] # [str] | Specifies the snapshot environment types to filter data access sessions. (optional)
statuses = [
        "Pending",
    ] # [str] | Specifies the list of session states to filter data access sessions (optional)
pagination_cookie = "paginationCookie_example" # str | Specifies a cookie which can be passed in by the user in order to retrieve the next page of results. (optional)
count = 1 # int | Specifies the number of objects to be fetched for the specified pagination cookie. (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
	# Lists all the Data Access Sessions
	api_response = client.data_accessor.get_data_access_sessions(session_ids=session_ids, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, snapshot_environments=snapshot_environments, statuses=statuses, pagination_cookie=pagination_cookie, count=count)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataAccessorApi->get_data_access_sessions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_ids** | **[str]**| Filter Data Access Sessions for given session ids. | [optional]
 **start_time_usecs** | **int**| Returns the data access sessions which are started after the specific time. This value should be in Unix timestamp epoch in microseconds. | [optional]
 **end_time_usecs** | **int**| Returns the data access sessions which are started before the specific time. This value should be in Unix timestamp epoch in microseconds. | [optional]
 **snapshot_environments** | **[str]**| Specifies the snapshot environment types to filter data access sessions. | [optional]
 **statuses** | **[str]**| Specifies the list of session states to filter data access sessions | [optional]
 **pagination_cookie** | **str**| Specifies a cookie which can be passed in by the user in order to retrieve the next page of results. | [optional]
 **count** | **int**| Specifies the number of objects to be fetched for the specified pagination cookie. | [optional]

### Return type

[**GetDataAccessSessionsResponseParams**](GetDataAccessSessionsResponseParams.md)

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

# **get_graph_node_relations_differences**
> DiffGraphNodeRelation get_graph_node_relations_differences(session_id, node_id, body)

Query for difference of graph node relations

```Unknown Privileges``` <br><br>Query for difference of graph node relations between two snapshots of a session.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.get_graph_node_relations_diff_params import GetGraphNodeRelationsDiffParams
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.diff_graph_node_relation import DiffGraphNodeRelation
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


session_id = "sessionId_example" # str | Specifies the id of a session.
node_id = "nodeId_example" # str | Specifies the id of a graph node.
body = GetGraphNodeRelationsDiffParams(
        diff_relation=True,
        diff_types=[
            "Added",
        ],
        relation_filter=GraphNodeRelationFilterParams(
            aad_params=AadRelationFilterParams(
                relation_type="Group",
            ),
        ),
    ) # GetGraphNodeRelationsDiffParams | Specifies the parameters to search graph node relations for a given node id.

# example passing only required values which don't have defaults set
try:
	# Query for difference of graph node relations
	api_response = client.data_accessor.get_graph_node_relations_differences(session_id, node_id, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataAccessorApi->get_graph_node_relations_differences: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Specifies the id of a session. |
 **node_id** | **str**| Specifies the id of a graph node. |
 **body** | [**GetGraphNodeRelationsDiffParams**](GetGraphNodeRelationsDiffParams.md)| Specifies the parameters to search graph node relations for a given node id. |

### Return type

[**DiffGraphNodeRelation**](DiffGraphNodeRelation.md)

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

# **get_graph_nodes_details**
> GetGraphNodesDetailsResult get_graph_nodes_details(session_id, node_ids, body)

Get Graph Nodes details

```No Privileges Required``` <br><br>Get graph nodes details and it's relations for list of node ids.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.get_graph_node_details_request_params import GetGraphNodeDetailsRequestParams
from cohesity_sdk.cluster.model.get_graph_nodes_details_result import GetGraphNodesDetailsResult
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


session_id = "sessionId_example" # str | Specifies the id of a session.
node_ids = [
        "nodeIds_example",
    ] # [str] | Specifies the id of the graph node.
body = GetGraphNodeDetailsRequestParams(
        count=1,
        include_attributes=True,
        node_type="node_type_example",
        pagination_cookie="pagination_cookie_example",
        query_relation=True,
        relation_filter=GraphNodeRelationFilterParams(
            aad_params=AadRelationFilterParams(
                relation_type="Group",
            ),
        ),
    ) # GetGraphNodeDetailsRequestParams | Specifies the parameters to get node details in the graph for given node ids.

# example passing only required values which don't have defaults set
try:
	# Get Graph Nodes details
	api_response = client.data_accessor.get_graph_nodes_details(session_id, node_ids, body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataAccessorApi->get_graph_nodes_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Specifies the id of a session. |
 **node_ids** | **[str]**| Specifies the id of the graph node. |
 **body** | [**GetGraphNodeDetailsRequestParams**](GetGraphNodeDetailsRequestParams.md)| Specifies the parameters to get node details in the graph for given node ids. |

### Return type

[**GetGraphNodesDetailsResult**](GetGraphNodesDetailsResult.md)

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

# **search_graph_nodes**
> SearchGraphNodesResponseParams search_graph_nodes(body)

Search Graph nodes

```No Privileges Required``` <br><br>Search nodes in the graph for a given session id

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.model.search_graph_nodes_response_params import SearchGraphNodesResponseParams
from cohesity_sdk.cluster.model.search_graph_nodes_request_params import SearchGraphNodesRequestParams
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


body = SearchGraphNodesRequestParams() # SearchGraphNodesRequestParams | Specifies the parameters to query nodes in the graph for a given session id.

# example passing only required values which don't have defaults set
try:
	# Search Graph nodes
	api_response = client.data_accessor.search_graph_nodes(body)
	pprint(api_response)
except ApiException as e:
	print("Exception when calling DataAccessorApi->search_graph_nodes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchGraphNodesRequestParams**](SearchGraphNodesRequestParams.md)| Specifies the parameters to query nodes in the graph for a given session id. |

### Return type

[**SearchGraphNodesResponseParams**](SearchGraphNodesResponseParams.md)

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

# **tear_down_data_access_session**
> tear_down_data_access_session(session_id)

Tear down data access session for a given id

```No Privileges Required``` <br><br>Tear down data access session for a given id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (Bearer):
* Api Key Authentication (SessionIdHeader):
```python
from cohesity_sdk.cluster.cluster_client import ClusterClient
from cohesity_sdk.cluster.model.error import Error
from cohesity_sdk.cluster.exceptions import ApiException
from pprint import pprint


client = ClusterClient(
	cluster_vip = "0.0.0.0",
	username = "username",
	password = "password",
	domain = "LOCAL"
)


session_id = "sessionId_example" # str | Specifies the id of the data access session.

# example passing only required values which don't have defaults set
try:
	# Tear down data access session for a given id
	client.data_accessor.tear_down_data_access_session(session_id)
except ApiException as e:
	print("Exception when calling DataAccessorApi->tear_down_data_access_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Specifies the id of the data access session. |

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

