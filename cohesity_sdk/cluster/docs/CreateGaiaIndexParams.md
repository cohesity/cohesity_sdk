# CreateGaiaIndexParams

Specifies the Index documents params.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[ObjectInfo], none_type**](ObjectInfo.md) | The objects and their snapshots to index. | 
**collection_id** | **str, none_type** | Opaque Id passed to emblem service on where to store the generated vector embeddings for these documents | [optional] 
**emblem_service_info** | [**EmblemServiceInfo**](EmblemServiceInfo.md) |  | [optional] 
**job_handle** | **str, none_type** | Job handle for this request. | [optional] 
**max_document_size** | **int, none_type** | Specifies the number of Bytes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


