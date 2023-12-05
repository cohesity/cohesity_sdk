# CassandraSourceRegistrationUpdateParams

Specifies parameters to update cassandra source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cassandra_credentials** | [**CassandraSourceRegistrationUpdateParamsCassandraCredentials**](CassandraSourceRegistrationUpdateParamsCassandraCredentials.md) |  | [optional] 
**commit_log_backup_location** | **str, none_type** | Commit Logs backup location on cassandra nodes | [optional] 
**config_directory** | **str** | Directory path containing Cassandra configuration YAML file. | [optional] 
**data_center_names** | **[str]** | Data centers for this cluster. | [optional] 
**dse_configuration_directory** | **str, none_type** | Directory from where DSE specific configuration can be read. This should be set only when you are using the DSE distribution of Cassandra. | [optional] 
**dse_solr_info** | [**DSESolrInfo**](DSESolrInfo.md) |  | [optional] 
**is_dse_authenticator** | **bool** | Set to true if this cluster has DSE Authenticator. | [optional] 
**is_dse_tiered_storage** | **bool** | Set to true if this cluster has DSE tiered storage. | [optional] 
**jmx_credentials** | [**CassandraSourceRegistrationUpdateParamsJmxCredentials**](CassandraSourceRegistrationUpdateParamsJmxCredentials.md) |  | [optional] 
**kerberos_principal** | **str, none_type** | Principal for the kerberos connection. (This is required only if your Cassandra has Kerberos authentication. Please refer to the user guide.) | [optional] 
**seed_node** | **str** | Any one seed node of the Cassandra cluster. | [optional] 
**ssh_password_credentials** | [**CassandraConnectionParamsSshPasswordCredentials**](CassandraConnectionParamsSshPasswordCredentials.md) |  | [optional] 
**ssh_private_key_credentials** | [**CassandraConnectionParamsSshPrivateKeyCredentials**](CassandraConnectionParamsSshPrivateKeyCredentials.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


