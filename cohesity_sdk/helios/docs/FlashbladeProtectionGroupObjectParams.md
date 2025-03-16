# FlashbladeProtectionGroupObjectParams

Specifies an object protected by a Flashblade Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.flashblade_protection_group_object_params import FlashbladeProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of FlashbladeProtectionGroupObjectParams from a JSON string
flashblade_protection_group_object_params_instance = FlashbladeProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(FlashbladeProtectionGroupObjectParams.to_json())

# convert the object into a dict
flashblade_protection_group_object_params_dict = flashblade_protection_group_object_params_instance.to_dict()
# create an instance of FlashbladeProtectionGroupObjectParams from a dict
flashblade_protection_group_object_params_from_dict = FlashbladeProtectionGroupObjectParams.from_dict(flashblade_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


