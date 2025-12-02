# ExperimentalAdapterParams

Specifies the recovery options specific to Experimental Adapter environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_experimental_adapter_params** | [**RecoverExperimentalAdapterParams**](RecoverExperimentalAdapterParams.md) |  | 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.cluster.models.experimental_adapter_params import ExperimentalAdapterParams

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentalAdapterParams from a JSON string
experimental_adapter_params_instance = ExperimentalAdapterParams.from_json(json)
# print the JSON string representation of the object
print(ExperimentalAdapterParams.to_json())

# convert the object into a dict
experimental_adapter_params_dict = experimental_adapter_params_instance.to_dict()
# create an instance of ExperimentalAdapterParams from a dict
experimental_adapter_params_from_dict = ExperimentalAdapterParams.from_dict(experimental_adapter_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


