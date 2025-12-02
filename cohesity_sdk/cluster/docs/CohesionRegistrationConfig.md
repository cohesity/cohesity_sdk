# CohesionRegistrationConfig

Specifies the Cohesion Registration Config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**helios_connection_info** | [**CohesionHeliosConnectionInfo**](CohesionHeliosConnectionInfo.md) |  | [optional] 
**helios_reg_info** | [**CohesionHeliosRegistrationInfo**](CohesionHeliosRegistrationInfo.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cohesion_registration_config import CohesionRegistrationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CohesionRegistrationConfig from a JSON string
cohesion_registration_config_instance = CohesionRegistrationConfig.from_json(json)
# print the JSON string representation of the object
print(CohesionRegistrationConfig.to_json())

# convert the object into a dict
cohesion_registration_config_dict = cohesion_registration_config_instance.to_dict()
# create an instance of CohesionRegistrationConfig from a dict
cohesion_registration_config_from_dict = CohesionRegistrationConfig.from_dict(cohesion_registration_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


