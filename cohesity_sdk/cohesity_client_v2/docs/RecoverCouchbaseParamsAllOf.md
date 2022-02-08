# RecoverCouchbaseParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**[RecoverCouchbaseSnapshotParams], none_type**](RecoverCouchbaseSnapshotParams.md) | Specifies the local snapshot ids of the Objects to be recovered. | 
**filter_documents_params** | [**FilterDocumentsParams**](FilterDocumentsParams.md) |  | 
**suffix** | **str, none_type** | A suffix that is to be applied to all recovered objects. | [optional] 
**append_documents** | **bool, none_type** | If set to true, docuements from the bucket being recovered will be appended into the bucket at the destination. | [optional] 
**ddl_only_recovery** | **bool, none_type** | Set to true to recover only the bucket configurations. No documents will be recovered. | [optional] 
**overwrite_users** | **bool, none_type** | If set to true existing users will be replaced with users from the bucket being recovered. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


