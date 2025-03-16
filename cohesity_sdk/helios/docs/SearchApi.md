# cohesity_sdk.helios.SearchApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**global_search_indexed_objects**](SearchApi.md#global_search_indexed_objects) | **POST** /mcm/search/indexed-objects | Search for indexed objects.
[**search_indexed_objects**](SearchApi.md#search_indexed_objects) | **POST** /data-protect/search/indexed-objects | List indexed objects.
[**search_objects**](SearchApi.md#search_objects) | **GET** /data-protect/search/objects | List Objects.
[**search_protected_objects**](SearchApi.md#search_protected_objects) | **GET** /data-protect/search/protected-objects | List Protected Objects.


# **global_search_indexed_objects**
> HeliosSearchIndexedObjectsResponseBody global_search_indexed_objects(body, region_id=region_id)

Search for indexed objects.

Search for indexed objects like files, emails etc across clusters.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.helios_search_indexed_objects_request import HeliosSearchIndexedObjectsRequest
from cohesity_sdk.helios.models.helios_search_indexed_objects_response_body import HeliosSearchIndexedObjectsResponseBody
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
    api_instance = cohesity_sdk.helios.SearchApi(api_client)
    body = cohesity_sdk.helios.HeliosSearchIndexedObjectsRequest() # HeliosSearchIndexedObjectsRequest | Specifies the parameters to search for indexed objects.
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # Search for indexed objects.
        api_response = api_instance.global_search_indexed_objects(body, region_id=region_id)
        print("The response of SearchApi->global_search_indexed_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->global_search_indexed_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HeliosSearchIndexedObjectsRequest**](HeliosSearchIndexedObjectsRequest.md)| Specifies the parameters to search for indexed objects. | 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**HeliosSearchIndexedObjectsResponseBody**](HeliosSearchIndexedObjectsResponseBody.md)

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

# **search_indexed_objects**
> SearchIndexedObjectsResponseBody search_indexed_objects(body, access_cluster_id=access_cluster_id, region_id=region_id)

List indexed objects.

List all the indexed objects like files and folders, emails, mailboxes etc., that match the specified search and filter criteria from protected objects.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.search_indexed_objects_request import SearchIndexedObjectsRequest
from cohesity_sdk.helios.models.search_indexed_objects_response_body import SearchIndexedObjectsResponseBody
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
    api_instance = cohesity_sdk.helios.SearchApi(api_client)
    body = cohesity_sdk.helios.SearchIndexedObjectsRequest() # SearchIndexedObjectsRequest | Specifies the parameters to search for indexed objects.
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)

    try:
        # List indexed objects.
        api_response = api_instance.search_indexed_objects(body, access_cluster_id=access_cluster_id, region_id=region_id)
        print("The response of SearchApi->search_indexed_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_indexed_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchIndexedObjectsRequest**](SearchIndexedObjectsRequest.md)| Specifies the parameters to search for indexed objects. | 
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 

### Return type

[**SearchIndexedObjectsResponseBody**](SearchIndexedObjectsResponseBody.md)

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

# **search_objects**
> ObjectsSearchResponseBody search_objects(access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type, search_string=search_string, environments=environments, protection_types=protection_types, tenant_ids=tenant_ids, include_tenants=include_tenants, protection_group_ids=protection_group_ids, object_ids=object_ids, os_types=os_types, o365_object_types=o365_object_types, azure_object_types=azure_object_types, source_ids=source_ids, source_uuids=source_uuids, is_protected=is_protected, is_deleted=is_deleted, last_run_status_list=last_run_status_list, region_ids=region_ids, cluster_identifiers=cluster_identifiers, storage_domain_ids=storage_domain_ids, include_deleted_objects=include_deleted_objects, pagination_cookie=pagination_cookie, count=count, must_have_tag_ids=must_have_tag_ids, might_have_tag_ids=might_have_tag_ids, must_have_snapshot_tag_ids=must_have_snapshot_tag_ids, might_have_snapshot_tag_ids=might_have_snapshot_tag_ids)

List Objects.

List objects.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.objects_search_response_body import ObjectsSearchResponseBody
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
    api_instance = cohesity_sdk.helios.SearchApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    request_initiator_type = 'request_initiator_type_example' # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)
    search_string = 'search_string_example' # str | Specifies the search string to filter the objects. This search string will be applicable for objectnames. User can specify a wildcard character '*' as a suffix to a string where all object names are matched with the prefix string. For example, if vm1 and vm2 are the names of objects, user can specify vm* to list the objects. If not specified, then all the objects will be returned which will match other filtering criteria. (optional)
    environments = ['environments_example'] # List[str] | Specifies the environment type to filter objects. (optional)
    protection_types = ['protection_types_example'] # List[str] | Specifies the protection type to filter objects. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
    include_tenants = True # bool | If true, the response will include Objects which belongs to all tenants which the current user has permission to see. (optional)
    protection_group_ids = ['protection_group_ids_example'] # List[str] | Specifies a list of Protection Group ids to filter the objects. If specified, the objects protected by specified Protection Group ids will be returned. (optional)
    object_ids = [56] # List[int] | Specifies a list of Object ids to filter. (optional)
    os_types = ['os_types_example'] # List[str] | Specifies the operating system types to filter objects on. (optional)
    o365_object_types = ['o365_object_types_example'] # List[str] | Specifies the object types to filter objects on. Only applicable if the environment is o365. (optional)
    azure_object_types = ['azure_object_types_example'] # List[str] | Specifies the object types to filter objects on. Only applicable if the environment is Azure. (optional)
    source_ids = [56] # List[int] | Specifies a list of Protection Source object ids to filter the objects. If specified, the object which are present in those Sources will be returned. (optional)
    source_uuids = ['source_uuids_example'] # List[str] | Specifies a list of Protection Source object uuids to filter the objects. If specified, the object which are present in those Sources will be returned. (optional)
    is_protected = True # bool | Specifies the protection status of objects. If set to true, only protected objects will be returned. If set to false, only unprotected objects will be returned. If not specified, all objects will be returned. (optional)
    is_deleted = True # bool | If set to true, then objects which are deleted on atleast one cluster will be returned. If not set or set to false then objects which are registered on atleast one cluster are returned. (optional)
    last_run_status_list = ['last_run_status_list_example'] # List[str] | Specifies a list of status of the object's last protection run. Only objects with last run status of these will be returned. (optional)
    region_ids = ['region_ids_example'] # List[str] | Specifies a list of region ids. Only records from clusters having these region ids will be returned. (optional)
    cluster_identifiers = ['cluster_identifiers_example'] # List[str] | Specifies the list of cluster identifiers. Format is clusterId:clusterIncarnationId. Only records from clusters having these identifiers will be returned. (optional)
    storage_domain_ids = ['storage_domain_ids_example'] # List[str] | Specifies the list of storage domain ids. Format is clusterId:clusterIncarnationId:storageDomainId. Only objects having protection in these storage domains will be returned. (optional)
    include_deleted_objects = True # bool | Specifies whether to include deleted objects in response. These objects can't be protected but can be recovered. This field is deprecated. (optional)
    pagination_cookie = 'pagination_cookie_example' # str | Specifies the pagination cookie with which subsequent parts of the response can be fetched. (optional)
    count = 56 # int | Specifies the number of objects to be fetched for the specified pagination cookie. (optional)
    must_have_tag_ids = ['must_have_tag_ids_example'] # List[str] | Specifies tags which must be all present in the document. (optional)
    might_have_tag_ids = ['might_have_tag_ids_example'] # List[str] | Specifies list of tags, one or more of which might be present in the document. These are OR'ed together and the resulting criteria AND'ed with the rest of the query. (optional)
    must_have_snapshot_tag_ids = ['must_have_snapshot_tag_ids_example'] # List[str] | Specifies snapshot tags which must be all present in the document. (optional)
    might_have_snapshot_tag_ids = ['might_have_snapshot_tag_ids_example'] # List[str] | Specifies list of snapshot tags, one or more of which might be present in the document. These are OR'ed together and the resulting criteria AND'ed with the rest of the query. (optional)

    try:
        # List Objects.
        api_response = api_instance.search_objects(access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type, search_string=search_string, environments=environments, protection_types=protection_types, tenant_ids=tenant_ids, include_tenants=include_tenants, protection_group_ids=protection_group_ids, object_ids=object_ids, os_types=os_types, o365_object_types=o365_object_types, azure_object_types=azure_object_types, source_ids=source_ids, source_uuids=source_uuids, is_protected=is_protected, is_deleted=is_deleted, last_run_status_list=last_run_status_list, region_ids=region_ids, cluster_identifiers=cluster_identifiers, storage_domain_ids=storage_domain_ids, include_deleted_objects=include_deleted_objects, pagination_cookie=pagination_cookie, count=count, must_have_tag_ids=must_have_tag_ids, might_have_tag_ids=might_have_tag_ids, must_have_snapshot_tag_ids=must_have_snapshot_tag_ids, might_have_snapshot_tag_ids=might_have_snapshot_tag_ids)
        print("The response of SearchApi->search_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional] 
 **search_string** | **str**| Specifies the search string to filter the objects. This search string will be applicable for objectnames. User can specify a wildcard character &#39;*&#39; as a suffix to a string where all object names are matched with the prefix string. For example, if vm1 and vm2 are the names of objects, user can specify vm* to list the objects. If not specified, then all the objects will be returned which will match other filtering criteria. | [optional] 
 **environments** | [**List[str]**](str.md)| Specifies the environment type to filter objects. | [optional] 
 **protection_types** | [**List[str]**](str.md)| Specifies the protection type to filter objects. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which objects are to be returned. | [optional] 
 **include_tenants** | **bool**| If true, the response will include Objects which belongs to all tenants which the current user has permission to see. | [optional] 
 **protection_group_ids** | [**List[str]**](str.md)| Specifies a list of Protection Group ids to filter the objects. If specified, the objects protected by specified Protection Group ids will be returned. | [optional] 
 **object_ids** | [**List[int]**](int.md)| Specifies a list of Object ids to filter. | [optional] 
 **os_types** | [**List[str]**](str.md)| Specifies the operating system types to filter objects on. | [optional] 
 **o365_object_types** | [**List[str]**](str.md)| Specifies the object types to filter objects on. Only applicable if the environment is o365. | [optional] 
 **azure_object_types** | [**List[str]**](str.md)| Specifies the object types to filter objects on. Only applicable if the environment is Azure. | [optional] 
 **source_ids** | [**List[int]**](int.md)| Specifies a list of Protection Source object ids to filter the objects. If specified, the object which are present in those Sources will be returned. | [optional] 
 **source_uuids** | [**List[str]**](str.md)| Specifies a list of Protection Source object uuids to filter the objects. If specified, the object which are present in those Sources will be returned. | [optional] 
 **is_protected** | **bool**| Specifies the protection status of objects. If set to true, only protected objects will be returned. If set to false, only unprotected objects will be returned. If not specified, all objects will be returned. | [optional] 
 **is_deleted** | **bool**| If set to true, then objects which are deleted on atleast one cluster will be returned. If not set or set to false then objects which are registered on atleast one cluster are returned. | [optional] 
 **last_run_status_list** | [**List[str]**](str.md)| Specifies a list of status of the object&#39;s last protection run. Only objects with last run status of these will be returned. | [optional] 
 **region_ids** | [**List[str]**](str.md)| Specifies a list of region ids. Only records from clusters having these region ids will be returned. | [optional] 
 **cluster_identifiers** | [**List[str]**](str.md)| Specifies the list of cluster identifiers. Format is clusterId:clusterIncarnationId. Only records from clusters having these identifiers will be returned. | [optional] 
 **storage_domain_ids** | [**List[str]**](str.md)| Specifies the list of storage domain ids. Format is clusterId:clusterIncarnationId:storageDomainId. Only objects having protection in these storage domains will be returned. | [optional] 
 **include_deleted_objects** | **bool**| Specifies whether to include deleted objects in response. These objects can&#39;t be protected but can be recovered. This field is deprecated. | [optional] 
 **pagination_cookie** | **str**| Specifies the pagination cookie with which subsequent parts of the response can be fetched. | [optional] 
 **count** | **int**| Specifies the number of objects to be fetched for the specified pagination cookie. | [optional] 
 **must_have_tag_ids** | [**List[str]**](str.md)| Specifies tags which must be all present in the document. | [optional] 
 **might_have_tag_ids** | [**List[str]**](str.md)| Specifies list of tags, one or more of which might be present in the document. These are OR&#39;ed together and the resulting criteria AND&#39;ed with the rest of the query. | [optional] 
 **must_have_snapshot_tag_ids** | [**List[str]**](str.md)| Specifies snapshot tags which must be all present in the document. | [optional] 
 **might_have_snapshot_tag_ids** | [**List[str]**](str.md)| Specifies list of snapshot tags, one or more of which might be present in the document. These are OR&#39;ed together and the resulting criteria AND&#39;ed with the rest of the query. | [optional] 

### Return type

[**ObjectsSearchResponseBody**](ObjectsSearchResponseBody.md)

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

# **search_protected_objects**
> ProtectedObjectsSearchResponseBody search_protected_objects(access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type, search_string=search_string, environments=environments, snapshot_actions=snapshot_actions, object_action_key=object_action_key, tenant_ids=tenant_ids, include_tenants=include_tenants, protection_group_ids=protection_group_ids, object_ids=object_ids, storage_domain_ids=storage_domain_ids, sub_result_size=sub_result_size, filter_snapshot_from_usecs=filter_snapshot_from_usecs, filter_snapshot_to_usecs=filter_snapshot_to_usecs, os_types=os_types, source_ids=source_ids, run_instance_ids=run_instance_ids, cdp_protected_only=cdp_protected_only, region_ids=region_ids, use_cached_data=use_cached_data)

List Protected Objects.

List protected objects and corresponding detail information from registered sources filtered by specified query parameters. If no search pattern or filter parameters are specified, all protected objects currently found are returned.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import cohesity_sdk.helios
from cohesity_sdk.helios.models.protected_objects_search_response_body import ProtectedObjectsSearchResponseBody
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
    api_instance = cohesity_sdk.helios.SearchApi(api_client)
    access_cluster_id = 56 # int | This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. (optional)
    region_id = 'region_id_example' # str | This field uniquely represents a region and is used for making Helios calls to a specific region. (optional)
    request_initiator_type = 'request_initiator_type_example' # str | Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. (optional)
    search_string = 'search_string_example' # str | Specifies the search string to filter the objects. This search string will be applicable for objectnames and Protection Group names. User can specify a wildcard character '*' as a suffix to a string where all object and their Protection Group names are matched with the prefix string. For example, if vm1 and vm2 are the names of objects, user can specify vm* to list the objects. If not specified, then all the objects with Protection Groups will be returned which will match other filtering criteria. (optional)
    environments = ['environments_example'] # List[str] | Specifies the environment type to filter objects. (optional)
    snapshot_actions = ['snapshot_actions_example'] # List[str] | Specifies a list of recovery actions. Only snapshots that applies to these actions will be returned. (optional)
    object_action_key = 'object_action_key_example' # str | Filter by ObjectActionKey, which uniquely represents protection of an object. An object can be protected in multiple ways but atmost once for a given combination of ObjectActionKey. When specified, latest snapshot info matching the objectActionKey is for corresponding object. (optional)
    tenant_ids = ['tenant_ids_example'] # List[str] | TenantIds contains ids of the tenants for which objects are to be returned. (optional)
    include_tenants = True # bool | If true, the response will include Objects which belongs to all tenants which the current user has permission to see. (optional)
    protection_group_ids = ['protection_group_ids_example'] # List[str] | Specifies a list of Protection Group ids to filter the objects. If specified, the objects protected by specified Protection Group ids will be returned. (optional)
    object_ids = [56] # List[int] | Specifies a list of Object ids to filter. (optional)
    storage_domain_ids = [56] # List[int] | Specifies the Storage Domain ids to filter objects for which Protection Groups are writing data to Cohesity Views on the specified Storage Domains. (optional)
    sub_result_size = 56 # int | Specifies the size of objects to be fetched for a single subresult. (optional)
    filter_snapshot_from_usecs = 56 # int | Specifies the timestamp in Unix time epoch in microseconds to filter the objects if the Object has a successful snapshot after this value. (optional)
    filter_snapshot_to_usecs = 56 # int | Specifies the timestamp in Unix time epoch in microseconds to filter the objects if the Object has a successful snapshot before this value. (optional)
    os_types = ['os_types_example'] # List[str] | Specifies the operating system types to filter objects on. (optional)
    source_ids = [56] # List[int] | Specifies a list of Protection Source object ids to filter the objects. If specified, the object which are present in those Sources will be returned. (optional)
    run_instance_ids = [56] # List[int] | Specifies a list of run instance ids. If specified only objects belonging to the provided run id will be retunrned. (optional)
    cdp_protected_only = True # bool | Specifies whether to only return the CDP protected objects. (optional)
    region_ids = ['region_ids_example'] # List[str] | Specifies a list of region ids. Only records from clusters having these region ids will be returned. (optional)
    use_cached_data = True # bool | Specifies whether we can serve the GET request to the read replica cache cache. There is a lag of 15 seconds between the read replica and primary data source. (optional)

    try:
        # List Protected Objects.
        api_response = api_instance.search_protected_objects(access_cluster_id=access_cluster_id, region_id=region_id, request_initiator_type=request_initiator_type, search_string=search_string, environments=environments, snapshot_actions=snapshot_actions, object_action_key=object_action_key, tenant_ids=tenant_ids, include_tenants=include_tenants, protection_group_ids=protection_group_ids, object_ids=object_ids, storage_domain_ids=storage_domain_ids, sub_result_size=sub_result_size, filter_snapshot_from_usecs=filter_snapshot_from_usecs, filter_snapshot_to_usecs=filter_snapshot_to_usecs, os_types=os_types, source_ids=source_ids, run_instance_ids=run_instance_ids, cdp_protected_only=cdp_protected_only, region_ids=region_ids, use_cached_data=use_cached_data)
        print("The response of SearchApi->search_protected_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_protected_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_cluster_id** | **int**| This field uniquely represents a Cohesity Cluster and is used for making on-prem calls from Helios. | [optional] 
 **region_id** | **str**| This field uniquely represents a region and is used for making Helios calls to a specific region. | [optional] 
 **request_initiator_type** | **str**| Specifies the type of request from UI, which is used for services like magneto to determine the priority of requests. | [optional] 
 **search_string** | **str**| Specifies the search string to filter the objects. This search string will be applicable for objectnames and Protection Group names. User can specify a wildcard character &#39;*&#39; as a suffix to a string where all object and their Protection Group names are matched with the prefix string. For example, if vm1 and vm2 are the names of objects, user can specify vm* to list the objects. If not specified, then all the objects with Protection Groups will be returned which will match other filtering criteria. | [optional] 
 **environments** | [**List[str]**](str.md)| Specifies the environment type to filter objects. | [optional] 
 **snapshot_actions** | [**List[str]**](str.md)| Specifies a list of recovery actions. Only snapshots that applies to these actions will be returned. | [optional] 
 **object_action_key** | **str**| Filter by ObjectActionKey, which uniquely represents protection of an object. An object can be protected in multiple ways but atmost once for a given combination of ObjectActionKey. When specified, latest snapshot info matching the objectActionKey is for corresponding object. | [optional] 
 **tenant_ids** | [**List[str]**](str.md)| TenantIds contains ids of the tenants for which objects are to be returned. | [optional] 
 **include_tenants** | **bool**| If true, the response will include Objects which belongs to all tenants which the current user has permission to see. | [optional] 
 **protection_group_ids** | [**List[str]**](str.md)| Specifies a list of Protection Group ids to filter the objects. If specified, the objects protected by specified Protection Group ids will be returned. | [optional] 
 **object_ids** | [**List[int]**](int.md)| Specifies a list of Object ids to filter. | [optional] 
 **storage_domain_ids** | [**List[int]**](int.md)| Specifies the Storage Domain ids to filter objects for which Protection Groups are writing data to Cohesity Views on the specified Storage Domains. | [optional] 
 **sub_result_size** | **int**| Specifies the size of objects to be fetched for a single subresult. | [optional] 
 **filter_snapshot_from_usecs** | **int**| Specifies the timestamp in Unix time epoch in microseconds to filter the objects if the Object has a successful snapshot after this value. | [optional] 
 **filter_snapshot_to_usecs** | **int**| Specifies the timestamp in Unix time epoch in microseconds to filter the objects if the Object has a successful snapshot before this value. | [optional] 
 **os_types** | [**List[str]**](str.md)| Specifies the operating system types to filter objects on. | [optional] 
 **source_ids** | [**List[int]**](int.md)| Specifies a list of Protection Source object ids to filter the objects. If specified, the object which are present in those Sources will be returned. | [optional] 
 **run_instance_ids** | [**List[int]**](int.md)| Specifies a list of run instance ids. If specified only objects belonging to the provided run id will be retunrned. | [optional] 
 **cdp_protected_only** | **bool**| Specifies whether to only return the CDP protected objects. | [optional] 
 **region_ids** | [**List[str]**](str.md)| Specifies a list of region ids. Only records from clusters having these region ids will be returned. | [optional] 
 **use_cached_data** | **bool**| Specifies whether we can serve the GET request to the read replica cache cache. There is a lag of 15 seconds between the read replica and primary data source. | [optional] 

### Return type

[**ProtectedObjectsSearchResponseBody**](ProtectedObjectsSearchResponseBody.md)

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

