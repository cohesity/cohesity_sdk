# HeliosSearchIndexedObjectsResponseBody

Specifies the search indexed objects response body.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_errors** | [**[HeliosSearchIndexedObjectsClusterError]**](HeliosSearchIndexedObjectsClusterError.md) | A List of errors that occured on a subset of clusters. | [optional] 
**count** | **int, none_type** | Specifies the total number of indexed objects that match the filter and search criteria. Use this value to determine how many additional requests are required to get the full result. | [optional] 
**object_type** | **str, none_type** | Specifies the object type. | [optional] 
**cassandra_objects** | [**HeliosCassandraObjects**](HeliosCassandraObjects.md) |  | [optional] 
**couchbase_objects** | [**HeliosCouchbaseObjects**](HeliosCouchbaseObjects.md) |  | [optional] 
**emails** | [**HeliosEmails**](HeliosEmails.md) |  | [optional] 
**exchange_objects** | [**HeliosExchangeObjects**](HeliosExchangeObjects.md) |  | [optional] 
**files** | [**HeliosFiles**](HeliosFiles.md) |  | [optional] 
**hbase_objects** | [**HeliosHbaseObjects**](HeliosHbaseObjects.md) |  | [optional] 
**hdfs_objects** | [**HeliosHdfsObjects**](HeliosHdfsObjects.md) |  | [optional] 
**hive_objects** | [**HeliosHiveObjects**](HeliosHiveObjects.md) |  | [optional] 
**mongo_objects** | [**HeliosMongoObjects**](HeliosMongoObjects.md) |  | [optional] 
**public_folder_items** | [**HeliosPublicFolderItems**](HeliosPublicFolderItems.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


