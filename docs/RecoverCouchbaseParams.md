# RecoverCouchbaseParams

Specifies the parameters to recover Couchbase objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_documents_params** | [**FilterDocumentsParams**](FilterDocumentsParams.md) |  | 
**snapshots** | [**[RecoverCouchbaseSnapshotParams], none_type**](RecoverCouchbaseSnapshotParams.md) | Specifies the local snapshot ids of the Objects to be recovered. | 
**bandwidth_mbps** | **int, none_type** | Specifies the maximum network bandwidth that each concurrent IO Stream can use for exchanging data with the cluster. | [optional] 
**concurrency** | **int, none_type** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. | [optional] 
**overwrite** | **bool, none_type** | Set to true to overwrite an existing object at the destination. If set to false, and the same object exists at the destination, then recovery will fail for that object. | [optional] 
**recover_to** | **int, none_type** | Specifies the &#39;Source Registration ID&#39; of the source where the objects are to be recovered. If this is not specified, the recovery job will recover to the original location. | [optional] 
**warnings** | **[str], none_type** | This field will hold the warnings in cases where the job status is SucceededWithWarnings. | [optional] [readonly] 
**append_documents** | **bool, none_type** | If set to true, docuements from the bucket being recovered will be appended into the bucket at the destination. | [optional] 
**ddl_only_recovery** | **bool, none_type** | Set to true to recover only the bucket configurations. No documents will be recovered. | [optional] 
**overwrite_users** | **bool, none_type** | If set to true existing users will be replaced with users from the bucket being recovered. | [optional] 
**suffix** | **str, none_type** | A suffix that is to be applied to all recovered objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


