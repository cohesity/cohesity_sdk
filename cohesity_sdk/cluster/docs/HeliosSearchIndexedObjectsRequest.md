# HeliosSearchIndexedObjectsRequest

Specifies the request parameters to search for global indexed objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str, none_type** | Specifies the object type to be searched for. | 
**cluster_identifiers** | **[str], none_type** | List of Clusters Identifiers to filter from. The format is clusterId:clusterIncarnationId. | [optional] 
**count** | **int, none_type** | Specifies the number of indexed objects to be fetched. | [optional] 
**region_ids** | **[str], none_type** | List of Regions to filter from. | [optional] 
**source_uuids** | [**HeliosSourceUUIDs**](HeliosSourceUUIDs.md) |  | [optional] 
**cassandra_params** | [**CassandraSearchParams**](CassandraSearchParams.md) |  | [optional] 
**couchbase_params** | [**CouchbaseSearchParams**](CouchbaseSearchParams.md) |  | [optional] 
**email_params** | [**EmailHeliosSearchParams**](EmailHeliosSearchParams.md) |  | [optional] 
**exchange_params** | [**SearchExchangeObjectsRequestParams**](SearchExchangeObjectsRequestParams.md) |  | [optional] 
**file_params** | [**SearchFileRequestParamsBase**](SearchFileRequestParamsBase.md) |  | [optional] 
**hbase_params** | [**HbaseSearchParams**](HbaseSearchParams.md) |  | [optional] 
**hdfs_params** | [**HdfsSearchParams**](HdfsSearchParams.md) |  | [optional] 
**hive_params** | [**HiveSearchParams**](HiveSearchParams.md) |  | [optional] 
**mongodb_params** | [**MongodbSearchParams**](MongodbSearchParams.md) |  | [optional] 
**ms_teams_params** | [**SearchMsTeamsRequestParams**](SearchMsTeamsRequestParams.md) |  | [optional] 
**public_folder_params** | [**SearchPublicFolderRequestParams**](SearchPublicFolderRequestParams.md) |  | [optional] 
**uda_params** | [**UdaSearchParams**](UdaSearchParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


