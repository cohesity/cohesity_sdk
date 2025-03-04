# GenericNasRegistrationParams

Specifies parameters to register GenericNas MountPoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies the Description for Generic NAS Source. | [optional] 
**mode** | **str** | Specifies the mode of the source. &#39;kNfs3&#39; indicates NFS3 mode. &#39;kNfs4_1&#39; indicates NFS4.1 mode. &#39;kCifs1&#39; indicates SMB mode. | 
**mount_point** | **str** | Specifies the MountPoint for Generic NAS Source. | 
**skip_validation** | **bool** | Specifies if validation has to be skipped while registering the mount point. | [optional] 
**smb_mount_credentials** | [**Credentials**](Credentials.md) |  | [optional] 
**throttling_config** | [**NasThrottlingConfig**](NasThrottlingConfig.md) |  | [optional] 
**uid** | [**UniversalId**](UniversalId.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.generic_nas_registration_params import GenericNasRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of GenericNasRegistrationParams from a JSON string
generic_nas_registration_params_instance = GenericNasRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(GenericNasRegistrationParams.to_json())

# convert the object into a dict
generic_nas_registration_params_dict = generic_nas_registration_params_instance.to_dict()
# create an instance of GenericNasRegistrationParams from a dict
generic_nas_registration_params_from_dict = GenericNasRegistrationParams.from_dict(generic_nas_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


