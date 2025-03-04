# HadoopConnectionParamsSshPrivateKeyCredentials

SSH  userID + privateKey required for reading configuration file and for scp backup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passphrase** | **str** | Passphrase for the private key. | [optional] 
**private_key** | **str** | The private key. | 
**user_id** | **str** | userId for PrivateKey credentials. | 

## Example

```python
from cohesity_sdk.models.hadoop_connection_params_ssh_private_key_credentials import HadoopConnectionParamsSshPrivateKeyCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of HadoopConnectionParamsSshPrivateKeyCredentials from a JSON string
hadoop_connection_params_ssh_private_key_credentials_instance = HadoopConnectionParamsSshPrivateKeyCredentials.from_json(json)
# print the JSON string representation of the object
print(HadoopConnectionParamsSshPrivateKeyCredentials.to_json())

# convert the object into a dict
hadoop_connection_params_ssh_private_key_credentials_dict = hadoop_connection_params_ssh_private_key_credentials_instance.to_dict()
# create an instance of HadoopConnectionParamsSshPrivateKeyCredentials from a dict
hadoop_connection_params_ssh_private_key_credentials_from_dict = HadoopConnectionParamsSshPrivateKeyCredentials.from_dict(hadoop_connection_params_ssh_private_key_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


