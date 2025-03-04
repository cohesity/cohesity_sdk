# HadoopConnectionParamsSshPasswordCredentials

SSH username + password required for reading configuration file and for scp backup.Either 'sshPasswordCredential' or 'sshPrivateKeyCredential' are required.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | SSH password. | 
**username** | **str** | SSH username. | 

## Example

```python
from cohesity_sdk.models.hadoop_connection_params_ssh_password_credentials import HadoopConnectionParamsSshPasswordCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of HadoopConnectionParamsSshPasswordCredentials from a JSON string
hadoop_connection_params_ssh_password_credentials_instance = HadoopConnectionParamsSshPasswordCredentials.from_json(json)
# print the JSON string representation of the object
print(HadoopConnectionParamsSshPasswordCredentials.to_json())

# convert the object into a dict
hadoop_connection_params_ssh_password_credentials_dict = hadoop_connection_params_ssh_password_credentials_instance.to_dict()
# create an instance of HadoopConnectionParamsSshPasswordCredentials from a dict
hadoop_connection_params_ssh_password_credentials_from_dict = HadoopConnectionParamsSshPasswordCredentials.from_dict(hadoop_connection_params_ssh_password_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


