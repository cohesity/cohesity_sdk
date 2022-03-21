# HdfsSourceRegistrationUpdateParams

Specifies parameters to update the registeration of an HDFS source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str, none_type** | IP or hostname of any host from which the HDFS configuration files core-site.xml and hdfs-site.xml can be read. | [optional] 
**configuration_directory** | **str, none_type** | The directory containing the core-site.xml and hdfs-site.xml configuration files. | [optional] 
**ssh_password_credentials** | [**HbaseSourceRegistrationParamsAllOfSshPasswordCredentials**](HbaseSourceRegistrationParamsAllOfSshPasswordCredentials.md) |  | [optional] 
**ssh_private_key_credentials** | [**HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials**](HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials.md) |  | [optional] 
**kerberos_principal** | **str, none_type** | The kerberos principal to be used to connect to this HDFS source. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


