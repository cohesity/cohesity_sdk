# SearchIndexedObjectsRequest

Specifies the request parameters to search for indexed objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Specifies the number of indexed objects to be fetched for the specified pagination cookie. | [optional] 
**include_tenants** | **bool** | If true, the response will include objects which belongs to all tenants which the current user has permission to see. Default value is false. | [optional] [default to False]
**might_have_snapshot_tag_ids** | **List[str]** | Specifies list of snapshot tags, one or more of which might be present in the document. These are OR&#39;ed together and the resulting criteria AND&#39;ed with the rest of the query. | [optional] 
**might_have_tag_ids** | **List[str]** | Specifies list of tags, one or more of which might be present in the document. These are OR&#39;ed together and the resulting criteria AND&#39;ed with the rest of the query. | [optional] 
**must_have_snapshot_tag_ids** | **List[str]** | Specifies snapshot tags which must be all present in the document. | [optional] 
**must_have_tag_ids** | **List[str]** | Specifies tags which must be all present in the document. | [optional] 
**object_type** | **str** | Specifies the object type to be searched for. | 
**pagination_cookie** | **str** | Specifies the pagination cookie with which subsequent parts of the response can be fetched. | [optional] 
**protection_group_ids** | **List[str]** | Specifies a list of Protection Group ids to filter the indexed objects. If specified, the objects indexed by specified Protection Group ids will be returned. | [optional] 
**snapshot_tags** | **List[str]** | \&quot;This field is deprecated. Please use mightHaveSnapshotTagIds.\&quot; | [optional] 
**storage_domain_ids** | **List[int]** | Specifies the Storage Domain ids to filter indexed objects for which Protection Groups are writing data to Cohesity Views on the specified Storage Domains. | [optional] 
**tags** | **List[str]** | \&quot;This field is deprecated. Please use mightHaveTagIds.\&quot; | [optional] 
**tenant_id** | **str** | TenantId contains id of the tenant for which objects are to be returned. | [optional] 
**use_cached_data** | **bool** | Specifies whether we can serve the GET request from the read replica cache. There is a lag of 15 seconds between the read replica and primary data source. | [optional] 
**cassandra_params** | [**CassandraOnPremSearchParams**](CassandraOnPremSearchParams.md) |  | [optional] 
**couchbase_params** | [**CouchBaseOnPremSearchParams**](CouchBaseOnPremSearchParams.md) |  | [optional] 
**email_params** | [**SearchEmailRequestParams**](SearchEmailRequestParams.md) |  | [optional] 
**exchange_params** | [**SearchExchangeObjectsRequestParams**](SearchExchangeObjectsRequestParams.md) |  | [optional] 
**file_params** | [**SearchFileRequestParams**](SearchFileRequestParams.md) |  | [optional] 
**hbase_params** | [**HbaseOnPremSearchParams**](HbaseOnPremSearchParams.md) |  | [optional] 
**hdfs_params** | [**HDFSOnPremSearchParams**](HDFSOnPremSearchParams.md) |  | [optional] 
**hive_params** | [**HiveOnPremSearchParams**](HiveOnPremSearchParams.md) |  | [optional] 
**mongodb_params** | [**MongoDbOnPremSearchParams**](MongoDbOnPremSearchParams.md) |  | [optional] 
**ms_groups_params** | [**SearchMsGroupsRequestParams**](SearchMsGroupsRequestParams.md) |  | [optional] 
**ms_teams_params** | [**SearchMsTeamsRequestParams**](SearchMsTeamsRequestParams.md) |  | [optional] 
**one_drive_params** | [**SearchDocumentLibraryRequestParams**](SearchDocumentLibraryRequestParams.md) |  | [optional] 
**public_folder_params** | [**SearchPublicFolderRequestParams**](SearchPublicFolderRequestParams.md) |  | [optional] 
**sfdc_params** | [**SearchSfdcRecordsRequestParams**](SearchSfdcRecordsRequestParams.md) |  | [optional] 
**sharepoint_params** | [**SearchDocumentLibraryRequestParams**](SearchDocumentLibraryRequestParams.md) |  | [optional] 
**uda_params** | [**UdaOnPremSearchParams**](UdaOnPremSearchParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.search_indexed_objects_request import SearchIndexedObjectsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchIndexedObjectsRequest from a JSON string
search_indexed_objects_request_instance = SearchIndexedObjectsRequest.from_json(json)
# print the JSON string representation of the object
print(SearchIndexedObjectsRequest.to_json())

# convert the object into a dict
search_indexed_objects_request_dict = search_indexed_objects_request_instance.to_dict()
# create an instance of SearchIndexedObjectsRequest from a dict
search_indexed_objects_request_from_dict = SearchIndexedObjectsRequest.from_dict(search_indexed_objects_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


