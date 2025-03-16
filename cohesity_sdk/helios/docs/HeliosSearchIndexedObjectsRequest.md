# HeliosSearchIndexedObjectsRequest

Specifies the request parameters to search for global indexed objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_identifiers** | **List[str]** | List of Clusters Identifiers to filter from. The format is clusterId:clusterIncarnationId. | [optional] 
**count** | **int** | Specifies the number of indexed objects to be fetched. | [optional] 
**object_type** | **str** | Specifies the object type to be searched for. | 
**region_ids** | **List[str]** | List of Regions to filter from. | [optional] 
**source_uuids** | **List[str]** | Specifies a list of source UUIDs. Only matches found in these sources will be returned. | [optional] 
**cassandra_params** | [**CassandraSearchParams**](CassandraSearchParams.md) |  | [optional] 
**couchbase_params** | [**CouchbaseSearchParams**](CouchbaseSearchParams.md) |  | [optional] 
**email_params** | [**EmailHeliosSearchParams**](EmailHeliosSearchParams.md) |  | [optional] 
**exchange_params** | [**SearchExchangeObjectsRequestParams**](SearchExchangeObjectsRequestParams.md) |  | [optional] 
**file_params** | [**SearchFileRequestParamsBase**](SearchFileRequestParamsBase.md) |  | [optional] 
**hbase_params** | [**HbaseSearchParams**](HbaseSearchParams.md) |  | [optional] 
**hdfs_params** | [**HdfsSearchParams**](HdfsSearchParams.md) |  | [optional] 
**hive_params** | [**HiveSearchParams**](HiveSearchParams.md) |  | [optional] 
**mongodb_params** | [**MongodbSearchParams**](MongodbSearchParams.md) |  | [optional] 
**ms_groups_params** | [**SearchMsGroupsRequestParams**](SearchMsGroupsRequestParams.md) |  | [optional] 
**ms_teams_params** | [**SearchMsTeamsRequestParams**](SearchMsTeamsRequestParams.md) |  | [optional] 
**public_folder_params** | [**SearchPublicFolderRequestParams**](SearchPublicFolderRequestParams.md) |  | [optional] 
**sfdc_params** | [**SearchSfdcRecordsRequestParams**](SearchSfdcRecordsRequestParams.md) |  | [optional] 
**uda_params** | [**UdaSearchParams**](UdaSearchParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_search_indexed_objects_request import HeliosSearchIndexedObjectsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosSearchIndexedObjectsRequest from a JSON string
helios_search_indexed_objects_request_instance = HeliosSearchIndexedObjectsRequest.from_json(json)
# print the JSON string representation of the object
print(HeliosSearchIndexedObjectsRequest.to_json())

# convert the object into a dict
helios_search_indexed_objects_request_dict = helios_search_indexed_objects_request_instance.to_dict()
# create an instance of HeliosSearchIndexedObjectsRequest from a dict
helios_search_indexed_objects_request_from_dict = HeliosSearchIndexedObjectsRequest.from_dict(helios_search_indexed_objects_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


