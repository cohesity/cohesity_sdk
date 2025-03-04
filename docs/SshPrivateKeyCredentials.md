# SshPrivateKeyCredentials

SSH  userID + privateKey that will be used for reading configuration file and for scp backup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passphrase** | **str** | Passphrase for the private key. | [optional] 
**private_key** | **str** | The private key. | 
**user_id** | **str** | userId for PrivateKey credentials. | 

## Example

```python
from cohesity_sdk.models.ssh_private_key_credentials import SshPrivateKeyCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of SshPrivateKeyCredentials from a JSON string
ssh_private_key_credentials_instance = SshPrivateKeyCredentials.from_json(json)
# print the JSON string representation of the object
print(SshPrivateKeyCredentials.to_json())

# convert the object into a dict
ssh_private_key_credentials_dict = ssh_private_key_credentials_instance.to_dict()
# create an instance of SshPrivateKeyCredentials from a dict
ssh_private_key_credentials_from_dict = SshPrivateKeyCredentials.from_dict(ssh_private_key_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


