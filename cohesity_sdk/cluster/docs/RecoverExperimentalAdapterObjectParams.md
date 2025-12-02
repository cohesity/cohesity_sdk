# RecoverExperimentalAdapterObjectParams

Specifies details of objects to be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **int** | Specifies the ID of the object. | [optional] 
**overwrite** | **bool** | Set to true to overwrite an existing object at the destination. If set to false, and the same object exists at the destination, then recovery will fail for that object. | [optional] 
**rename_to** | **str** | Specifies the new name to which the object should be renamed to after the recovery. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_experimental_adapter_object_params import RecoverExperimentalAdapterObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverExperimentalAdapterObjectParams from a JSON string
recover_experimental_adapter_object_params_instance = RecoverExperimentalAdapterObjectParams.from_json(json)
# print the JSON string representation of the object
print(RecoverExperimentalAdapterObjectParams.to_json())

# convert the object into a dict
recover_experimental_adapter_object_params_dict = recover_experimental_adapter_object_params_instance.to_dict()
# create an instance of RecoverExperimentalAdapterObjectParams from a dict
recover_experimental_adapter_object_params_from_dict = RecoverExperimentalAdapterObjectParams.from_dict(recover_experimental_adapter_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


