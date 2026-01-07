# HbaseSourceRegistrationParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_directory** | **str** | The directory containing the hbase-site.xml. | 
**hdfs_source_registration_id** | **int** | Protection Source registration id of the HDFS on which this HBase is running. | 
**host** | **str** | IP or hostname of any host from which the HBase configuration file hbase-site.xml can be read. | 
**kerberos_principal** | **str, none_type** | The kerberos principal to be used to connect to this Hbase source. | [optional] 
**ssh_password_credentials** | [**HbaseSourceRegistrationParamsAllOfSshPasswordCredentials**](HbaseSourceRegistrationParamsAllOfSshPasswordCredentials.md) |  | [optional] 
**ssh_private_key_credentials** | [**HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials**](HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


