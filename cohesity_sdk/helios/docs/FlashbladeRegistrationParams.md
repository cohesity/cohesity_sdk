# FlashbladeRegistrationParams

Specifies parameters to register an Flashblade Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_token** | **str** | Specifies the API Token of the Flashblade Source | 
**back_up_smb_volumes** | **bool** | Specifies whether or not to back up SMB Volumes. | [optional] 
**endpoint** | **str** | Specifies the Hostname or IP Address Endpoint for the Flashblade Source. | 
**smb_credentials** | [**SmbMountCredentials**](SmbMountCredentials.md) |  | [optional] 
**throttling_config** | [**NasThrottlingConfig**](NasThrottlingConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.flashblade_registration_params import FlashbladeRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of FlashbladeRegistrationParams from a JSON string
flashblade_registration_params_instance = FlashbladeRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(FlashbladeRegistrationParams.to_json())

# convert the object into a dict
flashblade_registration_params_dict = flashblade_registration_params_instance.to_dict()
# create an instance of FlashbladeRegistrationParams from a dict
flashblade_registration_params_from_dict = FlashbladeRegistrationParams.from_dict(flashblade_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


