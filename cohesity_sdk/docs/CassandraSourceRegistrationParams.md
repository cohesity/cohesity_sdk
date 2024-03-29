# CassandraSourceRegistrationParams

Specifies parameters to register cassandra source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seed_node** | **str** | Any one seed node of the Cassandra cluster. | 
**config_directory** | **str** | Directory path containing Cassandra configuration YAML file. | 
**is_dse_tiered_storage** | **bool** | Set to true if this cluster has DSE tiered storage. | 
**is_dse_authenticator** | **bool** | Set to true if this cluster has DSE Authenticator. | 
**dse_configuration_directory** | **str, none_type** | Directory from where DSE specific configuration can be read. This should be set only when you are using the DSE distribution of Cassandra. | [optional] 
**ssh_password_credentials** | [**SshPasswordCredentials**](SshPasswordCredentials.md) |  | [optional] 
**ssh_private_key_credentials** | [**SshPrivateKeyCredentials**](SshPrivateKeyCredentials.md) |  | [optional] 
**jmx_credentials** | [**CassandraSourceRegistrationParamsAllOfJmxCredentials**](CassandraSourceRegistrationParamsAllOfJmxCredentials.md) |  | [optional] 
**cassandra_credentials** | [**CassandraSourceRegistrationParamsAllOfCassandraCredentials**](CassandraSourceRegistrationParamsAllOfCassandraCredentials.md) |  | [optional] 
**data_center_names** | **[str]** | Data centers for this cluster. | [optional] 
**commit_log_backup_location** | **str, none_type** | Commit Logs backup location on cassandra nodes | [optional] 
**kerberos_principal** | **str, none_type** | Principal for the kerberos connection. (This is required only if your Cassandra has Kerberos authentication. Please refer to the user guide.) | [optional] 
**dse_solr_info** | [**DSESolrInfo**](DSESolrInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


