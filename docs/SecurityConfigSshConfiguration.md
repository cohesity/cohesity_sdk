# SecurityConfigSshConfiguration

Specifies security config for ssh configuration of cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssh_timeout_in_mins** | **int** | Specifies the number of minutes of remaining idle before session timeout. | [optional] 

## Example

```python
from cohesity_sdk.models.security_config_ssh_configuration import SecurityConfigSshConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityConfigSshConfiguration from a JSON string
security_config_ssh_configuration_instance = SecurityConfigSshConfiguration.from_json(json)
# print the JSON string representation of the object
print(SecurityConfigSshConfiguration.to_json())

# convert the object into a dict
security_config_ssh_configuration_dict = security_config_ssh_configuration_instance.to_dict()
# create an instance of SecurityConfigSshConfiguration from a dict
security_config_ssh_configuration_from_dict = SecurityConfigSshConfiguration.from_dict(security_config_ssh_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


