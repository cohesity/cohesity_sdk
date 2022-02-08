# HdfsSourceRegistrationParams

Specifies parameters to register an HDFS source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | IP or hostname of any host from which the HDFS configuration files core-site.xml and hdfs-site.xml can be read. | 
**configuration_directory** | **str** | The directory containing the core-site.xml and hdfs-site.xml configuration files. | 
**hadoop_distribution** | **str** | The hadoop distribution for this cluster. This can be either &#39;CDH&#39; or &#39;HDP&#39; | 
**hadoop_version** | **str** | The hadoop version for this cluster. | 
**namenode_address** | **str** | The HDFS Namenode IP or hostname. | [optional] [readonly] 
**webhdfs_port** | **int** | The HDFS WebHDFS port. | [optional] [readonly] 
**auth_type** | **str, none_type** | Authentication type. | [optional] [readonly] 
**ssh_password_credentials** | [**HbaseSourceRegistrationParamsAllOfSshPasswordCredentials**](HbaseSourceRegistrationParamsAllOfSshPasswordCredentials.md) |  | [optional] 
**ssh_private_key_credentials** | [**HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials**](HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials.md) |  | [optional] 
**kerberos_principal** | **str, none_type** | The kerberos principal to be used to connect to this HDFS source. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


