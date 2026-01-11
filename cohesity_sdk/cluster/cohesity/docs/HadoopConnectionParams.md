# HadoopConnectionParams

Specifies the parameters to connect to a seed node and fetch information from its config file.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_directory** | **str** | The directory containing the application specific config file. . | 
**host** | **str** | IP or hostname of any host from which the  configuration file can be read. | 
**hdfs_connection_type** | **str, none_type** | HDFS Connection Type. | [optional] 
**ssh_password_credentials** | [**HadoopConnectionParamsSshPasswordCredentials**](HadoopConnectionParamsSshPasswordCredentials.md) |  | [optional] 
**ssh_private_key_credentials** | [**HadoopConnectionParamsSshPrivateKeyCredentials**](HadoopConnectionParamsSshPrivateKeyCredentials.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


