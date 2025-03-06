# CassandraPortInfo

Contains info about specific cassandra ports.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jmx_port** | **int** | Cassandra management port. | [optional] 
**native_transport_port** | **int** | Port for the CQL native transport. | [optional] 
**rpc_port** | **int** | Remote Procedure Call (RPC) port for general mechanism for client-server applications. | [optional] 
**ssl_storage_port** | **int** | SSL port for encrypted communication. Internally used by the Cassandra bulk loader. | [optional] 
**storage_port** | **int** | TCP port for data. Internally used by Cassandra bulk loader. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cassandra_port_info import CassandraPortInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CassandraPortInfo from a JSON string
cassandra_port_info_instance = CassandraPortInfo.from_json(json)
# print the JSON string representation of the object
print(CassandraPortInfo.to_json())

# convert the object into a dict
cassandra_port_info_dict = cassandra_port_info_instance.to_dict()
# create an instance of CassandraPortInfo from a dict
cassandra_port_info_from_dict = CassandraPortInfo.from_dict(cassandra_port_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


