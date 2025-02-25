# SourceConnectionResponseParams

Specifies the response from a test connection request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str, none_type** | Specifies the environment type of the Protection Source. | 
**cassandra_connection_response_params** | [**CassandraSourceConfigParams**](CassandraSourceConfigParams.md) |  | [optional] 
**connection_id** | **int, none_type** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. | [optional] 
**hbase_connection_response_params** | [**HBaseAdditionalParams**](HBaseAdditionalParams.md) |  | [optional] 
**hdfs_connection_response_params** | [**HdfsAdditionalParams**](HdfsAdditionalParams.md) |  | [optional] 
**hive_connection_response_params** | [**HiveAdditionalParams**](HiveAdditionalParams.md) |  | [optional] 
**mssql_connection_response_params** | [**MssqlConnectionResponseParams**](MssqlConnectionResponseParams.md) |  | [optional] 
**vmware_connection_response_params** | [**VmwareAdditionalParams**](VmwareAdditionalParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


