# RestoreSpfileOrPfileInfo

Specifies information related to restoring Spfile/Pfile.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**should_restore_spfile_or_pfile** | **bool, none_type** | Specifies whether to restore spfile/pfile or skip it. | [optional] 
**file_location** | **str, none_type** | Specifies the location where spfile/file will be restored. If this is empty and shouldRestoreSpfileOrPfile is true we restore at default location: $ORACLE_HOME/dbs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


