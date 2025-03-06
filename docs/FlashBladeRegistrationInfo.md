# FlashBladeRegistrationInfo

Specifies the information specific to flashblade registration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_token** | **str** | Specifies the api token of the pure flashblade. | 
**ip** | **str** | Specifies management ip of pure flashblade server. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.flash_blade_registration_info import FlashBladeRegistrationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FlashBladeRegistrationInfo from a JSON string
flash_blade_registration_info_instance = FlashBladeRegistrationInfo.from_json(json)
# print the JSON string representation of the object
print(FlashBladeRegistrationInfo.to_json())

# convert the object into a dict
flash_blade_registration_info_dict = flash_blade_registration_info_instance.to_dict()
# create an instance of FlashBladeRegistrationInfo from a dict
flash_blade_registration_info_from_dict = FlashBladeRegistrationInfo.from_dict(flash_blade_registration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


