# HiveSourceRegistrationParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_directory** | **str** | The directory containing the hive-site.xml. | 
**hdfs_source_registration_id** | **int** | Protection Source registration id of the HDFS on which this Hive is running. | 
**host** | **str** | IP or hostname of any host from which the Hive configuration file hive-site.xml can be read. | 
**kerberos_principal** | **str, none_type** | The kerberos principal to be used to connect to this Hive source. | [optional] 
**ssh_password_credentials** | [**HiveSourceRegistrationParamsAllOfSshPasswordCredentials**](HiveSourceRegistrationParamsAllOfSshPasswordCredentials.md) |  | [optional] 
**ssh_private_key_credentials** | [**HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials**](HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


