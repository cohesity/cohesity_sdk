# HdfsSourceRegistrationParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_directory** | **str** | The directory containing the core-site.xml and hdfs-site.xml configuration files. | 
**hadoop_distribution** | **str** | The hadoop distribution for this cluster. This can be either &#39;CDH&#39; or &#39;HDP&#39; | 
**hadoop_version** | **str** | The hadoop version for this cluster. | 
**host** | **str** | IP or hostname of any host from which the HDFS configuration files core-site.xml and hdfs-site.xml can be read. | 
**kerberos_principal** | **str, none_type** | The kerberos principal to be used to connect to this HDFS source. | [optional] 
**ssh_password_credentials** | [**HbaseSourceRegistrationParamsAllOfSshPasswordCredentials**](HbaseSourceRegistrationParamsAllOfSshPasswordCredentials.md) |  | [optional] 
**ssh_private_key_credentials** | [**HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials**](HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


