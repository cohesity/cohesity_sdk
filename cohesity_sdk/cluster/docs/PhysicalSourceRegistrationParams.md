# PhysicalSourceRegistrationParams

Specifies parameters to register physical server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | **List[str]** | Specifies the list of applications to be registered with Physical Source. | [optional] 
**endpoint** | **str** | Specifies the endpoint IPaddress, URL or hostname of the physical host. | 
**force_register** | **bool** | The agent running on a physical host will fail the registration if it is already registered as part of another cluster. By setting this option to true, agent can be forced to register with the current cluster. | [optional] 
**host_type** | **str** | Specifies the type of host. | [optional] 
**physical_type** | **str** | Specifies the type of physical server. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.physical_source_registration_params import PhysicalSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalSourceRegistrationParams from a JSON string
physical_source_registration_params_instance = PhysicalSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(PhysicalSourceRegistrationParams.to_json())

# convert the object into a dict
physical_source_registration_params_dict = physical_source_registration_params_instance.to_dict()
# create an instance of PhysicalSourceRegistrationParams from a dict
physical_source_registration_params_from_dict = PhysicalSourceRegistrationParams.from_dict(physical_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


