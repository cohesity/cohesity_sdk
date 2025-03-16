# IsilonRegistrationParams

Specifies parameters to register an Isilon Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**back_up_smb_volumes** | **bool** | Specifies whether or not to back up SMB Volumes. | [optional] 
**credentials** | [**Credentials**](Credentials.md) |  | 
**endpoint** | **str** | Specifies the IP Address Endpoint for the Isilon Source. | 
**filter_ip_config** | [**FilterIpConfig**](FilterIpConfig.md) |  | [optional] 
**smb_credentials** | [**SmbMountCredentials**](SmbMountCredentials.md) |  | [optional] 
**throttling_config** | [**NasThrottlingConfig**](NasThrottlingConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.isilon_registration_params import IsilonRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of IsilonRegistrationParams from a JSON string
isilon_registration_params_instance = IsilonRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(IsilonRegistrationParams.to_json())

# convert the object into a dict
isilon_registration_params_dict = isilon_registration_params_instance.to_dict()
# create an instance of IsilonRegistrationParams from a dict
isilon_registration_params_from_dict = IsilonRegistrationParams.from_dict(isilon_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


