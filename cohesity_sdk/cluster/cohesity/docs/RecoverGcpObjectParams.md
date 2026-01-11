# RecoverGcpObjectParams

Specifies details of recovery object to be recovered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_database_name** | **str** | Specifies the original name of the object to be restored, as it exists in the source. | 
**overwrite** | **bool** | Specifies whether to overwrite an existing object with the same name at the destination. If true, any existing object will be replaced. If false or unset, the restore may fail if a conflict occurs. | 
**new_database_name** | **str, none_type** | Specifies the new name to which the object should be renamed to after the recovery. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


