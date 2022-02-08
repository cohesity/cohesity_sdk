# RecoverCassandraParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**[RecoverCassandraSnapshotParams], none_type**](RecoverCassandraSnapshotParams.md) | Specifies the local snapshot ids and other details of the Objects to be recovered. | 
**suffix** | **str, none_type** | A suffix that is to be applied to all recovered objects. | [optional] 
**selected_data_centers** | **[str]** | Selected Data centers for this cluster. | [optional] 
**staging_directory_list** | **[str]** | Specifies the directory on the primary to copy the files which are to be uploaded using destination sstableloader. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


