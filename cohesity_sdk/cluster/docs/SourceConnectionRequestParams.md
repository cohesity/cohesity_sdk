# SourceConnectionRequestParams

Specifies the parameters to test connectivity with a source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str, none_type** | Specifies the environment type of the Protection Source. | 
**connection_id** | **int, none_type** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. | [optional] 
**cassandra_connection_params** | [**CassandraConnectionParams**](CassandraConnectionParams.md) |  | [optional] 
**hbase_connection_params** | [**HadoopConnectionParams**](HadoopConnectionParams.md) |  | [optional] 
**hdfs_connection_params** | [**HadoopConnectionParams**](HadoopConnectionParams.md) |  | [optional] 
**hive_connection_params** | [**HadoopConnectionParams**](HadoopConnectionParams.md) |  | [optional] 
**mssql_connection_params** | [**MsSQLCommonConnectionParams**](MsSQLCommonConnectionParams.md) |  | [optional] 
**oracle_connection_params** | [**OracleConnectionParams**](OracleConnectionParams.md) |  | [optional] 
**vmware_connection_params** | [**VmwareConnectionParams**](VmwareConnectionParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


