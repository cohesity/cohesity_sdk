# FlashbladeObjectProtectionParams

Specifies the parameters which are specific to Flashblade object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | Specifies the protocol of the NAS device being backed up. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.flashblade_object_protection_params import FlashbladeObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of FlashbladeObjectProtectionParams from a JSON string
flashblade_object_protection_params_instance = FlashbladeObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(FlashbladeObjectProtectionParams.to_json())

# convert the object into a dict
flashblade_object_protection_params_dict = flashblade_object_protection_params_instance.to_dict()
# create an instance of FlashbladeObjectProtectionParams from a dict
flashblade_object_protection_params_from_dict = FlashbladeObjectProtectionParams.from_dict(flashblade_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


