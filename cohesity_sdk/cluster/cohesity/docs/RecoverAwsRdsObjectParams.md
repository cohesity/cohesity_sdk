# RecoverAwsRdsObjectParams

Specifies details of recovery object to be recovered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_name** | **str, none_type** | Specifies the new name to which the object should be renamed to after the recovery. | [optional] 
**original_name** | **str, none_type** | Specifies the original name of the object to be restored, as it exists in the source. | [optional] 
**overwrite** | **bool, none_type** | Specifies whether to overwrite an existing object with the same name at the destination. If true, any existing object will be replaced; if false or unset, the restore may fail if a conflict occurs. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


