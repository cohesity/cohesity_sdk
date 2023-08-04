# RecoverHdfsParams

Specifies the parameters to recover HDFS objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**[RecoverHdfsSnapshotParams], none_type**](RecoverHdfsSnapshotParams.md) | Specifies the local snapshot ids of the Objects to be recovered. | 
**recover_to** | **int, none_type** | Specifies the &#39;Source Registration ID&#39; of the source where the objects are to be recovered. If this is not specified, the recovery job will recover to the original location. | [optional] 
**overwrite** | **bool, none_type** | Set to true to overwrite an existing object at the destination. If set to false, and the same object exists at the destination, then recovery will fail for that object. | [optional] 
**concurrency** | **int, none_type** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. | [optional] 
**bandwidth_mbps** | **int, none_type** | Specifies the maximum network bandwidth that each concurrent IO Stream can use for exchanging data with the cluster. | [optional] 
**warnings** | **[str], none_type** | This field will hold the warnings in cases where the job status is SucceededWithWarnings. | [optional] [readonly] 
**target_directory** | **str, none_type** | Specifies the target directory where files and folders are to be recovered. If not set, this will be taken as &#39;/&#39; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


