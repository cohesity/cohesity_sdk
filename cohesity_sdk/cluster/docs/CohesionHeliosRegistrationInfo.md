# CohesionHeliosRegistrationInfo

Specifies the Cohesion Helios registration information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Specifies possible error message during registration. | [optional] 
**status** | **str** | Specifies the registration status. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cohesion_helios_registration_info import CohesionHeliosRegistrationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CohesionHeliosRegistrationInfo from a JSON string
cohesion_helios_registration_info_instance = CohesionHeliosRegistrationInfo.from_json(json)
# print the JSON string representation of the object
print(CohesionHeliosRegistrationInfo.to_json())

# convert the object into a dict
cohesion_helios_registration_info_dict = cohesion_helios_registration_info_instance.to_dict()
# create an instance of CohesionHeliosRegistrationInfo from a dict
cohesion_helios_registration_info_from_dict = CohesionHeliosRegistrationInfo.from_dict(cohesion_helios_registration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


