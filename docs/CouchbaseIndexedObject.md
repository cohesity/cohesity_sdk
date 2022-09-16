# CouchbaseIndexedObject

Specifies a Couchbase indexed object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the object. | [optional] 
**path** | **str, none_type** | Specifies the path of the object. | [optional] 
**protection_group_id** | **str, none_type** | \&quot;Specifies the protection group id which contains this object.\&quot; | [optional] 
**protection_group_name** | **str, none_type** | \&quot;Specifies the protection group name which contains this object.\&quot; | [optional] 
**storage_domain_id** | **int, none_type** | \&quot;Specifies the Storage Domain id where the backup data of Object is present.\&quot; | [optional] 
**source_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the Source Object information. | [optional] 
**tags** | [**[TagInfo], none_type**](TagInfo.md) | Specifies tag applied to the object. | [optional] 
**snapshot_tags** | [**[SnapshotTagInfo], none_type**](SnapshotTagInfo.md) | Specifies snapshot tags applied to the object. | [optional] 
**type** | **str, none_type** | Specifies the Couchbase Object Type. For Couchbase this is alywas set to Bucket. | [optional]  if omitted the server will use the default value of "CouchbaseBuckets"
**id** | **str, none_type** | Specifies the id of the indexed object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


