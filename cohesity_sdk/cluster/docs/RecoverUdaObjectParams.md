# RecoverUdaObjectParams

Specifies details of objects to be recovered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **int, none_type** | Specifies the ID of the object. | [optional] 
**object_name** | **str, none_type** | Specifies the fully qualified name of the object to be restored. | [optional] 
**overwrite** | **bool, none_type** | Set to true to overwrite an existing object at the destination. If set to false, and the same object exists at the destination, then recovery will fail for that object. | [optional] 
**rename_to** | **str, none_type** | Specifies the new name to which the object should be renamed to after the recovery. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


