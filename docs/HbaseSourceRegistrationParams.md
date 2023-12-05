# HbaseSourceRegistrationParams

Specifies parameters to register an HBase source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_directory** | **str** | The directory containing the hbase-site.xml. | 
**hdfs_source_registration_id** | **int** | Protection Source registration id of the HDFS on which this HBase is running. | 
**host** | **str** | IP or hostname of any host from which the HBase configuration file hbase-site.xml can be read. | 
**auth_type** | **str, none_type** | Authentication type. | [optional] [readonly] 
**data_root_directory** | **str, none_type** | The &#39;Data root directory&#39; for this HBase. | [optional] [readonly] 
**zookeeper_quorum** | **[str], none_type** | The &#39;Zookeeper Quorum&#39; for this HBase. | [optional] [readonly] 
**kerberos_principal** | **str, none_type** | The kerberos principal to be used to connect to this Hbase source. | [optional] 
**ssh_password_credentials** | [**HbaseSourceRegistrationParamsAllOfSshPasswordCredentials**](HbaseSourceRegistrationParamsAllOfSshPasswordCredentials.md) |  | [optional] 
**ssh_private_key_credentials** | [**HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials**](HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


