# HadoopConnectionParams

Specifies the parameters to connect to a seed node and fetch information from its config file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_directory** | **str** | The directory containing the application specific config file. . | 
**host** | **str** | IP or hostname of any host from which the  configuration file can be read. | 
**ssh_password_credentials** | [**HadoopConnectionParamsSshPasswordCredentials**](HadoopConnectionParamsSshPasswordCredentials.md) |  | [optional] 
**ssh_private_key_credentials** | [**HadoopConnectionParamsSshPrivateKeyCredentials**](HadoopConnectionParamsSshPrivateKeyCredentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.hadoop_connection_params import HadoopConnectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of HadoopConnectionParams from a JSON string
hadoop_connection_params_instance = HadoopConnectionParams.from_json(json)
# print the JSON string representation of the object
print(HadoopConnectionParams.to_json())

# convert the object into a dict
hadoop_connection_params_dict = hadoop_connection_params_instance.to_dict()
# create an instance of HadoopConnectionParams from a dict
hadoop_connection_params_from_dict = HadoopConnectionParams.from_dict(hadoop_connection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


