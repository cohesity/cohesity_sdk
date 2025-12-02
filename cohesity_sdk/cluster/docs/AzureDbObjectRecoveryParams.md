# AzureDbObjectRecoveryParams

Specifies common parameters for Azure database object recovery.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_database_name** | **str** | Specifies the original name of the object to be restored, as it exists in the source. | 
**overwrite** | **bool** | Specifies whether to overwrite an existing object with the same name at the destination. If true, any existing object will be replaced; if false or unset, the restore may fail if a conflict occurs. | 
**new_database_name** | **str, none_type** | Specifies the new name to which the object should be renamed to after the recovery. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


