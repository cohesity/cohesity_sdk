# HbaseSourceRegistrationParamsAllOfSshPasswordCredentials

SSH username + password required for reading configuration file. Either 'sshPasswordCredentials' or 'sshPrivateKeyCredentials' are required.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | SSH password. | 
**username** | **str** | SSH username. | 

## Example

```python
from cohesity_sdk.models.hbase_source_registration_params_all_of_ssh_password_credentials import HbaseSourceRegistrationParamsAllOfSshPasswordCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of HbaseSourceRegistrationParamsAllOfSshPasswordCredentials from a JSON string
hbase_source_registration_params_all_of_ssh_password_credentials_instance = HbaseSourceRegistrationParamsAllOfSshPasswordCredentials.from_json(json)
# print the JSON string representation of the object
print(HbaseSourceRegistrationParamsAllOfSshPasswordCredentials.to_json())

# convert the object into a dict
hbase_source_registration_params_all_of_ssh_password_credentials_dict = hbase_source_registration_params_all_of_ssh_password_credentials_instance.to_dict()
# create an instance of HbaseSourceRegistrationParamsAllOfSshPasswordCredentials from a dict
hbase_source_registration_params_all_of_ssh_password_credentials_from_dict = HbaseSourceRegistrationParamsAllOfSshPasswordCredentials.from_dict(hbase_source_registration_params_all_of_ssh_password_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


