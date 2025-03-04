# SshPasswordCredentials

SSH username + password that will be used for reading configuration file and for scp backup.Either 'sshPasswordCredentials' or 'sshPrivateKeyCredentials' are required.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | SSH password. | 
**username** | **str** | SSH username. | 

## Example

```python
from cohesity_sdk.models.ssh_password_credentials import SshPasswordCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of SshPasswordCredentials from a JSON string
ssh_password_credentials_instance = SshPasswordCredentials.from_json(json)
# print the JSON string representation of the object
print(SshPasswordCredentials.to_json())

# convert the object into a dict
ssh_password_credentials_dict = ssh_password_credentials_instance.to_dict()
# create an instance of SshPasswordCredentials from a dict
ssh_password_credentials_from_dict = SshPasswordCredentials.from_dict(ssh_password_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


