# CommonApplicationServersRegistrationParams

Specifies the application servers registration config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_environments** | **List[str]** | Specifies the list of application environments such as kOracle, kSQL, kExchange, kAD etc. running on the Protection Source. | 
**register_applications** | **bool** | If set to true registers application servers otherwise will update application servers registration. By default it is set to false. | [optional] 
**use_persistent_agent** | **bool** | Set to true if a persistent agent is running on the host. If this is specified, then credentials would not be used to log into the host environment. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_application_servers_registration_params import CommonApplicationServersRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonApplicationServersRegistrationParams from a JSON string
common_application_servers_registration_params_instance = CommonApplicationServersRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(CommonApplicationServersRegistrationParams.to_json())

# convert the object into a dict
common_application_servers_registration_params_dict = common_application_servers_registration_params_instance.to_dict()
# create an instance of CommonApplicationServersRegistrationParams from a dict
common_application_servers_registration_params_from_dict = CommonApplicationServersRegistrationParams.from_dict(common_application_servers_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


