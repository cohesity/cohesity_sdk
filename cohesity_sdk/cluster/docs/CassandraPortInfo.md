# CassandraPortInfo

Contains info about specific cassandra ports.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jmx_port** | **int, none_type** | Cassandra management port. | [optional] 
**native_transport_port** | **int, none_type** | Port for the CQL native transport. | [optional] 
**rpc_port** | **int, none_type** | Remote Procedure Call (RPC) port for general mechanism for client-server applications. | [optional] 
**ssl_storage_port** | **int, none_type** | SSL port for encrypted communication. Internally used by the Cassandra bulk loader. | [optional] 
**storage_port** | **int, none_type** | TCP port for data. Internally used by Cassandra bulk loader. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


