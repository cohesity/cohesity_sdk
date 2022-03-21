# HdfsProtectionGroupParams

Specifies the parameters for HDFS Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hdfs_source_id** | **int, none_type** | The object ID of the HDFS source for this protection group. | 
**include_paths** | **[str]** | Specifies the paths to be included in the Protection Group. | [optional] 
**exclude_paths** | **[str]** | Specifies the paths to be excluded in the Protection Group. excludePaths will ovrride includePaths. | [optional] 
**concurrency** | **int, none_type** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. | [optional] 
**bandwidth_mbps** | **int, none_type** | Specifies the maximum network bandwidth that each concurrent IO Stream can use for exchanging data with the cluster. | [optional] 
**source_id** | **int, none_type** | Object ID of the Source on which this protection was run . | [optional] [readonly] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**source_name** | **str, none_type** | Specifies the name of the Source on which this protection was run. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


