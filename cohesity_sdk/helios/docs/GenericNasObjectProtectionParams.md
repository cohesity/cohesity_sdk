# GenericNasObjectProtectionParams

Specifies the parameters which are specific to Generic NAS object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | Specifies the protocol of the NAS device being backed up. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.generic_nas_object_protection_params import GenericNasObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of GenericNasObjectProtectionParams from a JSON string
generic_nas_object_protection_params_instance = GenericNasObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(GenericNasObjectProtectionParams.to_json())

# convert the object into a dict
generic_nas_object_protection_params_dict = generic_nas_object_protection_params_instance.to_dict()
# create an instance of GenericNasObjectProtectionParams from a dict
generic_nas_object_protection_params_from_dict = GenericNasObjectProtectionParams.from_dict(generic_nas_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


