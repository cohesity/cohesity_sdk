# HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials

SSH  userID + privateKey required for reading configuration file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passphrase** | **str** | Passphrase for the private key. | [optional] 
**private_key** | **str** | The private key. | 
**user_id** | **str** | userId for PrivateKey credentials. | 

## Example

```python
from cohesity_sdk.cluster.models.hbase_source_registration_params_all_of_ssh_private_key_credentials import HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials from a JSON string
hbase_source_registration_params_all_of_ssh_private_key_credentials_instance = HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials.from_json(json)
# print the JSON string representation of the object
print(HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials.to_json())

# convert the object into a dict
hbase_source_registration_params_all_of_ssh_private_key_credentials_dict = hbase_source_registration_params_all_of_ssh_private_key_credentials_instance.to_dict()
# create an instance of HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials from a dict
hbase_source_registration_params_all_of_ssh_private_key_credentials_from_dict = HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials.from_dict(hbase_source_registration_params_all_of_ssh_private_key_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


