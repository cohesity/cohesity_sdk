# HiveSourceRegistrationParamsAllOfSshPasswordCredentials

SSH username + password required for reading configuration file.Either 'sshPasswordCredentials' or 'sshPrivateKeyCredentials' are required.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | SSH password. | 
**username** | **str** | SSH username. | 

## Example

```python
from cohesity_sdk.helios.models.hive_source_registration_params_all_of_ssh_password_credentials import HiveSourceRegistrationParamsAllOfSshPasswordCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of HiveSourceRegistrationParamsAllOfSshPasswordCredentials from a JSON string
hive_source_registration_params_all_of_ssh_password_credentials_instance = HiveSourceRegistrationParamsAllOfSshPasswordCredentials.from_json(json)
# print the JSON string representation of the object
print(HiveSourceRegistrationParamsAllOfSshPasswordCredentials.to_json())

# convert the object into a dict
hive_source_registration_params_all_of_ssh_password_credentials_dict = hive_source_registration_params_all_of_ssh_password_credentials_instance.to_dict()
# create an instance of HiveSourceRegistrationParamsAllOfSshPasswordCredentials from a dict
hive_source_registration_params_all_of_ssh_password_credentials_from_dict = HiveSourceRegistrationParamsAllOfSshPasswordCredentials.from_dict(hive_source_registration_params_all_of_ssh_password_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


