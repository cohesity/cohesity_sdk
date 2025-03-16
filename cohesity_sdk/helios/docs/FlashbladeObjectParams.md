# FlashbladeObjectParams

Specifies the common parameters for Flashblade objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported_nas_mount_protocols** | **List[str]** | Specifies a list of NAS mount protocols supported by this object. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.flashblade_object_params import FlashbladeObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of FlashbladeObjectParams from a JSON string
flashblade_object_params_instance = FlashbladeObjectParams.from_json(json)
# print the JSON string representation of the object
print(FlashbladeObjectParams.to_json())

# convert the object into a dict
flashblade_object_params_dict = flashblade_object_params_instance.to_dict()
# create an instance of FlashbladeObjectParams from a dict
flashblade_object_params_from_dict = FlashbladeObjectParams.from_dict(flashblade_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


