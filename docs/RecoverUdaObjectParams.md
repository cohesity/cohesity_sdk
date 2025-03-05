# RecoverUdaObjectParams

Specifies details of objects to be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **int** | Specifies the ID of the object. | [optional] 
**object_name** | **str** | Specifies the fully qualified name of the object to be restored. | [optional] 
**overwrite** | **bool** | Set to true to overwrite an existing object at the destination. If set to false, and the same object exists at the destination, then recovery will fail for that object. | [optional] 
**rename_to** | **str** | Specifies the new name to which the object should be renamed to after the recovery. | [optional] 

## Example

```python
from cohesity_sdk.models.recover_uda_object_params import RecoverUdaObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverUdaObjectParams from a JSON string
recover_uda_object_params_instance = RecoverUdaObjectParams.from_json(json)
# print the JSON string representation of the object
print(RecoverUdaObjectParams.to_json())

# convert the object into a dict
recover_uda_object_params_dict = recover_uda_object_params_instance.to_dict()
# create an instance of RecoverUdaObjectParams from a dict
recover_uda_object_params_from_dict = RecoverUdaObjectParams.from_dict(recover_uda_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


