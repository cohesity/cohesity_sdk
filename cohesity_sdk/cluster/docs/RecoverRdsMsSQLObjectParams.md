# RecoverRdsMsSQLObjectParams

Specifies details of MS SQL recovery object to be recovered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_name** | **str, none_type** | Specifies the new name to which the MS SQL cluster should be renamed to after the recovery. | [optional] 
**original_name** | **str, none_type** | Specifies the original name of the MS SQL cluster to be restored, as it exists in the source. | [optional] 
**overwrite** | **bool, none_type** | Specifies whether to overwrite an existing MS SQL cluster with the same name at the destination. If true, any existing cluster will be replaced; if false or unset, the restore may fail if a conflict occurs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


