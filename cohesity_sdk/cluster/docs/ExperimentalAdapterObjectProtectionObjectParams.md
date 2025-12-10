# ExperimentalAdapterObjectProtectionObjectParams

Specifies the object parameters to create an Experimental Adapter Object Protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_object_ids** | **List[int]** | Specifies the ids of the objects to be excluded in the Object Protection. This can be used to ignore specific objects under a parent object which has been included for protection. | [optional] 
**id** | **int** | Specifies the id of the object being protected. This can be a leaf level or non leaf level object. | 

## Example

```python
from cohesity_sdk.cluster.models.experimental_adapter_object_protection_object_params import ExperimentalAdapterObjectProtectionObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentalAdapterObjectProtectionObjectParams from a JSON string
experimental_adapter_object_protection_object_params_instance = ExperimentalAdapterObjectProtectionObjectParams.from_json(json)
# print the JSON string representation of the object
print(ExperimentalAdapterObjectProtectionObjectParams.to_json())

# convert the object into a dict
experimental_adapter_object_protection_object_params_dict = experimental_adapter_object_protection_object_params_instance.to_dict()
# create an instance of ExperimentalAdapterObjectProtectionObjectParams from a dict
experimental_adapter_object_protection_object_params_from_dict = ExperimentalAdapterObjectProtectionObjectParams.from_dict(experimental_adapter_object_protection_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


