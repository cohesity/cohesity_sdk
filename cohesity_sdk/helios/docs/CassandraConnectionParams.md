# CassandraConnectionParams

Specifies the parameters to connect to a Cassandra seed node and fetch information from its cassandra config file.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seed_node** | **str** | Any one seed node of the Cassandra cluster. | 
**config_directory** | **str** | Directory path containing Cassandra configuration YAML file. | 
**is_dse_tiered_storage** | **bool** | Set to true if this cluster has DSE tiered storage. | 
**is_dse_authenticator** | **bool** | Set to true if this cluster has DSE Authenticator. | 
**dse_configuration_directory** | **str, none_type** | Directory from where DSE specific configuration can be read. This should be set only when you are using the DSE distribution of Cassandra. | [optional] 
**ssh_password_credentials** | [**CassandraConnectionParamsSshPasswordCredentials**](CassandraConnectionParamsSshPasswordCredentials.md) |  | [optional] 
**ssh_private_key_credentials** | [**CassandraConnectionParamsSshPrivateKeyCredentials**](CassandraConnectionParamsSshPrivateKeyCredentials.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


