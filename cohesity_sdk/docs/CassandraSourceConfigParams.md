# CassandraSourceConfigParams

Specifies the parameters fetched by reading cassandra configuration on the seed node.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seeds** | **[str]** | Seed nodes of this cluster. | [optional] 
**is_jmx_auth_enable** | **bool, none_type** | Is JMX Authentication enabled in this cluster ? | [optional] 
**cassandra_port_info** | [**CassandraPortInfo**](CassandraPortInfo.md) |  | [optional] 
**cassandra_security_info** | [**CassandraSecurityInfo**](CassandraSecurityInfo.md) |  | [optional] 
**data_center_names** | **[str]** | Data centers for this cluster. | [optional] 
**commit_log_backup_location** | **str, none_type** | Commit Logs backup location on cassandra nodes | [optional] 
**endpoint_snitch** | **str, none_type** | Endpoint snitch used for this cluster. | [optional] 
**cassandra_partitioner** | **str, none_type** | Cassandra partitioner required in compaction. | [optional] 
**kerberos_sasl_protocol** | **str, none_type** | Populated if cassandraAuthType is Kerberos. | [optional] 
**cassandra_version** | **str, none_type** | Cassandra Version. | [optional] 
**dse_version** | **str, none_type** | DSE Version | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


