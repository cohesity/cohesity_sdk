# SearchIndexedObjectsResponseBody

Specifies the search indexed objects response body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Specifies the total number of indexed objects that match the filter and search criteria. Use this value to determine how many additional requests are required to get the full result. | [optional] 
**object_type** | **str** | Specifies the object type. | [optional] 
**pagination_cookie** | **str** | Specifies cookie for resuming search if pagination is being used. | [optional] 
**cassandra_objects** | [**List[CassandraIndexedObject]**](CassandraIndexedObject.md) | Specifies the indexed Cassandra objects. | [optional] 
**couchbase_objects** | [**List[CouchbaseIndexedObject]**](CouchbaseIndexedObject.md) | Specifies the indexed Couchbase objects. | [optional] 
**emails** | [**List[Email]**](Email.md) | Specifies the indexed emails and email folders. | [optional] 
**exchange_objects** | [**List[ExchangeIndexedObject]**](ExchangeIndexedObject.md) | Specifies the indexed HDFS objects. | [optional] 
**files** | [**List[File]**](File.md) | Specifies the indexed files. | [optional] 
**hbase_objects** | [**List[HbaseIndexedObject]**](HbaseIndexedObject.md) | Specifies the indexed Hbase objects. | [optional] 
**hdfs_objects** | [**List[HDFSIndexedObject]**](HDFSIndexedObject.md) | Specifies the indexed HDFS objects. | [optional] 
**hive_objects** | [**List[HiveIndexedObject]**](HiveIndexedObject.md) | Specifies the indexed Hive objects. | [optional] 
**mongo_objects** | [**List[MongoIndexedObject]**](MongoIndexedObject.md) | Specifies the indexed Mongo objects. | [optional] 
**ms_group_items** | [**List[MsGroupItem]**](MsGroupItem.md) | Specifies the indexed M365 Groups items like group mail items, files etc. | [optional] 
**one_drive_items** | [**List[DocumentLibraryItem]**](DocumentLibraryItem.md) | Specifies the indexed one drive items. | [optional] 
**public_folder_items** | [**List[PublicFolderItem]**](PublicFolderItem.md) | Specifies the indexed Public folder items. | [optional] 
**sfdc_records** | [**SfdcRecords**](SfdcRecords.md) |  | [optional] 
**sharepoint_items** | [**List[SharepointItem]**](SharepointItem.md) | Specifies the indexed Sharepoint items. | [optional] 
**teams_items** | [**List[TeamsItem]**](TeamsItem.md) | Specifies the indexed M365 Teams items like channels, files etc. | [optional] 
**uda_objects** | [**List[UdaIndexedObject]**](UdaIndexedObject.md) | Specifies the indexed Universal Data Adapter objects. | [optional] 

## Example

```python
from cohesity_sdk.models.search_indexed_objects_response_body import SearchIndexedObjectsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of SearchIndexedObjectsResponseBody from a JSON string
search_indexed_objects_response_body_instance = SearchIndexedObjectsResponseBody.from_json(json)
# print the JSON string representation of the object
print(SearchIndexedObjectsResponseBody.to_json())

# convert the object into a dict
search_indexed_objects_response_body_dict = search_indexed_objects_response_body_instance.to_dict()
# create an instance of SearchIndexedObjectsResponseBody from a dict
search_indexed_objects_response_body_from_dict = SearchIndexedObjectsResponseBody.from_dict(search_indexed_objects_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


