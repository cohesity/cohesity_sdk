# ExperimentalAdapterObjectProtectionParams

Specifies the  that are specific to Experimental Adapter Object Protection parameter section.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ExperimentalAdapterObjectProtectionObjectParams]**](ExperimentalAdapterObjectProtectionObjectParams.md) | Specifies the objects to be included in the Object Protection. | 
**workflow_params** | **str** | Specifies the object protection workflow parameters. This is a stringified JSON representation of the parameters. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.experimental_adapter_object_protection_params import ExperimentalAdapterObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentalAdapterObjectProtectionParams from a JSON string
experimental_adapter_object_protection_params_instance = ExperimentalAdapterObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(ExperimentalAdapterObjectProtectionParams.to_json())

# convert the object into a dict
experimental_adapter_object_protection_params_dict = experimental_adapter_object_protection_params_instance.to_dict()
# create an instance of ExperimentalAdapterObjectProtectionParams from a dict
experimental_adapter_object_protection_params_from_dict = ExperimentalAdapterObjectProtectionParams.from_dict(experimental_adapter_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


