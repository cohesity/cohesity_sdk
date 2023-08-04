# SearchIndexedObjectsResponseBody

Specifies the search indexed objects response body.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_type** | **str** | Specifies the object type. | [optional] 
**count** | **int, none_type** | Specifies the total number of indexed objects that match the filter and search criteria. Use this value to determine how many additional requests are required to get the full result. | [optional] 
**pagination_cookie** | **str, none_type** | Specifies cookie for resuming search if pagination is being used. | [optional] 
**emails** | [**Emails**](Emails.md) |  | [optional] 
**files** | [**Files**](Files.md) |  | [optional] 
**cassandra_objects** | [**CassandraIndexedObjects**](CassandraIndexedObjects.md) |  | [optional] 
**couchbase_objects** | [**CouchbaseIndexedObjects**](CouchbaseIndexedObjects.md) |  | [optional] 
**hbase_objects** | [**HbaseIndexedObjects**](HbaseIndexedObjects.md) |  | [optional] 
**hive_objects** | [**HiveIndexedObjects**](HiveIndexedObjects.md) |  | [optional] 
**mongo_objects** | [**MongoIndexedObjects**](MongoIndexedObjects.md) |  | [optional] 
**hdfs_objects** | [**HDFSIndexedObjects**](HDFSIndexedObjects.md) |  | [optional] 
**exchange_objects** | [**ExchangeIndexedObjects**](ExchangeIndexedObjects.md) |  | [optional] 
**public_folder_items** | [**PublicFolderItems**](PublicFolderItems.md) |  | [optional] 
**sharepoint_items** | [**SharepointItems**](SharepointItems.md) |  | [optional] 
**one_drive_items** | [**OneDriveItems**](OneDriveItems.md) |  | [optional] 
**uda_objects** | [**UdaIndexedObjects**](UdaIndexedObjects.md) |  | [optional] 
**teams_items** | [**TeamsItems**](TeamsItems.md) |  | [optional] 
**sfdc_records** | [**SfdcRecords**](SfdcRecords.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


