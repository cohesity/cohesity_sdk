# cohesity_sdk.cluster.DataAccessorApi

All URIs are relative to */v2*

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.create_data_access_session_request_params import CreateDataAccessSessionRequestParams
from cohesity_sdk.cluster.models.create_data_access_session_response_params import CreateDataAccessSessionResponseParams
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
    api_instance = cohesity_sdk.cluster.DataAccessorApi(api_client)
    body = cohesity_sdk.cluster.CreateDataAccessSessionRequestParams() # CreateDataAccessSessionRequestParams | Specifies the parameters to create data access session

    try:
        # Create Data Access Session
        api_response = api_instance.create_data_access_session(body)
        print("The response of DataAccessorApi->create_data_access_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAccessorApi->create_data_access_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDataAccessSessionRequestParams**](CreateDataAccessSessionRequestParams.md)| Specifies the parameters to create data access session | 

### Return type

[**CreateDataAccessSessionResponseParams**](CreateDataAccessSessionResponseParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

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
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.query_graph_nodes_diff_params import QueryGraphNodesDiffParams
from cohesity_sdk.cluster.models.query_graph_nodes_diff_result import QueryGraphNodesDiffResult
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
    api_instance = cohesity_sdk.cluster.DataAccessorApi(api_client)
    session_id = 'session_id_example' # str | Specifies the id of a session.
    body = cohesity_sdk.cluster.QueryGraphNodesDiffParams() # QueryGraphNodesDiffParams | Specifies the parameters to determine graph nodes diff for a given session id.

    try:
        # Difference of Graph nodes
        api_response = api_instance.difference_of_graph_nodes(session_id, body)
        print("The response of DataAccessorApi->difference_of_graph_nodes:\n")
        pprint(api_response)
    except Exception as e:
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

# **get_data_access_sessions**
> GetDataAccessSessionsResponseParams get_data_access_sessions(session_ids=session_ids, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, snapshot_environments=snapshot_environments, statuses=statuses, pagination_cookie=pagination_cookie, count=count)

Lists all the Data Access Sessions

```No Privileges Required``` <br><br>Lists the Data Access Sessions.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.get_data_access_sessions_response_params import GetDataAccessSessionsResponseParams
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
    api_instance = cohesity_sdk.cluster.DataAccessorApi(api_client)
    session_ids = ['session_ids_example'] # List[str] | Filter Data Access Sessions for given session ids. (optional)
    start_time_usecs = 56 # int | Returns the data access sessions which are started after the specific time. This value should be in Unix timestamp epoch in microseconds. (optional)
    end_time_usecs = 56 # int | Returns the data access sessions which are started before the specific time. This value should be in Unix timestamp epoch in microseconds. (optional)
    snapshot_environments = ['snapshot_environments_example'] # List[str] | Specifies the snapshot environment types to filter data access sessions. (optional)
    statuses = ['statuses_example'] # List[str] | Specifies the list of session states to filter data access sessions (optional)
    pagination_cookie = 'pagination_cookie_example' # str | Specifies a cookie which can be passed in by the user in order to retrieve the next page of results. (optional)
    count = 56 # int | Specifies the number of objects to be fetched for the specified pagination cookie. (optional)

    try:
        # Lists all the Data Access Sessions
        api_response = api_instance.get_data_access_sessions(session_ids=session_ids, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, snapshot_environments=snapshot_environments, statuses=statuses, pagination_cookie=pagination_cookie, count=count)
        print("The response of DataAccessorApi->get_data_access_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAccessorApi->get_data_access_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_ids** | [**List[str]**](str.md)| Filter Data Access Sessions for given session ids. | [optional] 
 **start_time_usecs** | **int**| Returns the data access sessions which are started after the specific time. This value should be in Unix timestamp epoch in microseconds. | [optional] 
 **end_time_usecs** | **int**| Returns the data access sessions which are started before the specific time. This value should be in Unix timestamp epoch in microseconds. | [optional] 
 **snapshot_environments** | [**List[str]**](str.md)| Specifies the snapshot environment types to filter data access sessions. | [optional] 
 **statuses** | [**List[str]**](str.md)| Specifies the list of session states to filter data access sessions | [optional] 
 **pagination_cookie** | **str**| Specifies a cookie which can be passed in by the user in order to retrieve the next page of results. | [optional] 
 **count** | **int**| Specifies the number of objects to be fetched for the specified pagination cookie. | [optional] 

### Return type

[**GetDataAccessSessionsResponseParams**](GetDataAccessSessionsResponseParams.md)

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

# **get_graph_node_relations_differences**
> DiffGraphNodeRelation get_graph_node_relations_differences(session_id, node_id, body)

Query for difference of graph node relations

```Unknown Privileges``` <br><br>Query for difference of graph node relations between two snapshots of a session.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.diff_graph_node_relation import DiffGraphNodeRelation
from cohesity_sdk.cluster.models.get_graph_node_relations_diff_params import GetGraphNodeRelationsDiffParams
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
    api_instance = cohesity_sdk.cluster.DataAccessorApi(api_client)
    session_id = 'session_id_example' # str | Specifies the id of a session.
    node_id = 'node_id_example' # str | Specifies the id of a graph node.
    body = cohesity_sdk.cluster.GetGraphNodeRelationsDiffParams() # GetGraphNodeRelationsDiffParams | Specifies the parameters to search graph node relations for a given node id.

    try:
        # Query for difference of graph node relations
        api_response = api_instance.get_graph_node_relations_differences(session_id, node_id, body)
        print("The response of DataAccessorApi->get_graph_node_relations_differences:\n")
        pprint(api_response)
    except Exception as e:
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

# **get_graph_nodes_details**
> GetGraphNodesDetailsResult get_graph_nodes_details(session_id, node_ids, body)

Get Graph Nodes details

```No Privileges Required``` <br><br>Get graph nodes details and it's relations for list of node ids.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.get_graph_node_details_request_params import GetGraphNodeDetailsRequestParams
from cohesity_sdk.cluster.models.get_graph_nodes_details_result import GetGraphNodesDetailsResult
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
    api_instance = cohesity_sdk.cluster.DataAccessorApi(api_client)
    session_id = 'session_id_example' # str | Specifies the id of a session.
    node_ids = ['node_ids_example'] # List[str] | Specifies the id of the graph node.
    body = cohesity_sdk.cluster.GetGraphNodeDetailsRequestParams() # GetGraphNodeDetailsRequestParams | Specifies the parameters to get node details in the graph for given node ids.

    try:
        # Get Graph Nodes details
        api_response = api_instance.get_graph_nodes_details(session_id, node_ids, body)
        print("The response of DataAccessorApi->get_graph_nodes_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAccessorApi->get_graph_nodes_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Specifies the id of a session. | 
 **node_ids** | [**List[str]**](str.md)| Specifies the id of the graph node. | 
 **body** | [**GetGraphNodeDetailsRequestParams**](GetGraphNodeDetailsRequestParams.md)| Specifies the parameters to get node details in the graph for given node ids. | 

### Return type

[**GetGraphNodesDetailsResult**](GetGraphNodesDetailsResult.md)

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

# **search_graph_nodes**
> SearchGraphNodesResponseParams search_graph_nodes(body)

Search Graph nodes

```No Privileges Required``` <br><br>Search nodes in the graph for a given session id

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
* Api Key Authentication (Bearer):

```python
import cohesity_sdk.cluster
from cohesity_sdk.cluster.models.search_graph_nodes_request_params import SearchGraphNodesRequestParams
from cohesity_sdk.cluster.models.search_graph_nodes_response_params import SearchGraphNodesResponseParams
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
    api_instance = cohesity_sdk.cluster.DataAccessorApi(api_client)
    body = cohesity_sdk.cluster.SearchGraphNodesRequestParams() # SearchGraphNodesRequestParams | Specifies the parameters to query nodes in the graph for a given session id.

    try:
        # Search Graph nodes
        api_response = api_instance.search_graph_nodes(body)
        print("The response of DataAccessorApi->search_graph_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAccessorApi->search_graph_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchGraphNodesRequestParams**](SearchGraphNodesRequestParams.md)| Specifies the parameters to query nodes in the graph for a given session id. | 

### Return type

[**SearchGraphNodesResponseParams**](SearchGraphNodesResponseParams.md)

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

# **tear_down_data_access_session**
> tear_down_data_access_session(session_id)

Tear down data access session for a given id

```No Privileges Required``` <br><br>Tear down data access session for a given id.

### Example

* Api Key Authentication (APIKeyHeader):
* Api Key Authentication (SessionIdHeader):
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
    api_instance = cohesity_sdk.cluster.DataAccessorApi(api_client)
    session_id = 'session_id_example' # str | Specifies the id of the data access session.

    try:
        # Tear down data access session for a given id
        api_instance.tear_down_data_access_session(session_id)
    except Exception as e:
        print("Exception when calling DataAccessorApi->tear_down_data_access_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Specifies the id of the data access session. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [SessionIdHeader](../README.md#SessionIdHeader), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

