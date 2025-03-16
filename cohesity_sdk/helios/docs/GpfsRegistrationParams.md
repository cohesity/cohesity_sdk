# GpfsRegistrationParams

Specifies parameters to register an GPFS Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**Credentials**](Credentials.md) |  | 
**endpoint** | **str** | Specifies the Hostname or IP Address Endpoint for the GPFS Source. | 
**filter_ip_config** | [**FilterIpConfig**](FilterIpConfig.md) |  | [optional] 
**throttling_config** | [**NasThrottlingConfig**](NasThrottlingConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.gpfs_registration_params import GpfsRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of GpfsRegistrationParams from a JSON string
gpfs_registration_params_instance = GpfsRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(GpfsRegistrationParams.to_json())

# convert the object into a dict
gpfs_registration_params_dict = gpfs_registration_params_instance.to_dict()
# create an instance of GpfsRegistrationParams from a dict
gpfs_registration_params_from_dict = GpfsRegistrationParams.from_dict(gpfs_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


