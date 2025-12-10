# ExperimentalAdapaterProtectionGroupObjectParams

Specifies the Experimental Adapter object details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | [optional] 
**name** | **str** | Specifies the fully qualified name of the object. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.experimental_adapater_protection_group_object_params import ExperimentalAdapaterProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentalAdapaterProtectionGroupObjectParams from a JSON string
experimental_adapater_protection_group_object_params_instance = ExperimentalAdapaterProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(ExperimentalAdapaterProtectionGroupObjectParams.to_json())

# convert the object into a dict
experimental_adapater_protection_group_object_params_dict = experimental_adapater_protection_group_object_params_instance.to_dict()
# create an instance of ExperimentalAdapaterProtectionGroupObjectParams from a dict
experimental_adapater_protection_group_object_params_from_dict = ExperimentalAdapaterProtectionGroupObjectParams.from_dict(experimental_adapater_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


