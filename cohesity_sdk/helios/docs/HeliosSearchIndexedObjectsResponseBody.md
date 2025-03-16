# HeliosSearchIndexedObjectsResponseBody

Specifies the search indexed objects response body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_errors** | [**List[HeliosSearchIndexedObjectsClusterError]**](HeliosSearchIndexedObjectsClusterError.md) | A List of errors that occured on a subset of clusters. | [optional] 
**count** | **int** | Specifies the total number of indexed objects that match the filter and search criteria. Use this value to determine how many additional requests are required to get the full result. | [optional] 
**object_type** | **str** | Specifies the object type. | [optional] 
**cassandra_objects** | [**List[HeliosCassandraObjectsInner]**](HeliosCassandraObjectsInner.md) | Specifies the indexed Cassandra objects. | [optional] 
**couchbase_objects** | [**List[HeliosCouchbaseObjectsInner]**](HeliosCouchbaseObjectsInner.md) | Specifies the indexed Couchbase objects. | [optional] 
**emails** | [**List[HeliosEmailsInner]**](HeliosEmailsInner.md) | Specifies the indexed emails and email folders. | [optional] 
**exchange_objects** | [**List[HeliosExchangeObjectsInner]**](HeliosExchangeObjectsInner.md) | Specifies the indexed HDFS objects. | [optional] 
**files** | [**List[HeliosFilesInner]**](HeliosFilesInner.md) | Specifies the indexed files and file folders. | [optional] 
**hbase_objects** | [**List[HeliosHbaseObjectsInner]**](HeliosHbaseObjectsInner.md) | Specifies the indexed Hbase objects. | [optional] 
**hdfs_objects** | [**List[HeliosHdfsObjectsInner]**](HeliosHdfsObjectsInner.md) | Specifies the indexed HDFS objects. | [optional] 
**hive_objects** | [**List[HeliosHiveObjectsInner]**](HeliosHiveObjectsInner.md) | Specifies the indexed Hive objects. | [optional] 
**mongo_objects** | [**List[HeliosMongoObjectsInner]**](HeliosMongoObjectsInner.md) | Specifies the indexed Mongo objects. | [optional] 
**public_folder_items** | [**List[HeliosPublicFolderItemsInner]**](HeliosPublicFolderItemsInner.md) | Specifies the indexed Public folder items. | [optional] 
**sfdc_records** | [**SfdcRecords**](SfdcRecords.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_search_indexed_objects_response_body import HeliosSearchIndexedObjectsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosSearchIndexedObjectsResponseBody from a JSON string
helios_search_indexed_objects_response_body_instance = HeliosSearchIndexedObjectsResponseBody.from_json(json)
# print the JSON string representation of the object
print(HeliosSearchIndexedObjectsResponseBody.to_json())

# convert the object into a dict
helios_search_indexed_objects_response_body_dict = helios_search_indexed_objects_response_body_instance.to_dict()
# create an instance of HeliosSearchIndexedObjectsResponseBody from a dict
helios_search_indexed_objects_response_body_from_dict = HeliosSearchIndexedObjectsResponseBody.from_dict(helios_search_indexed_objects_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


