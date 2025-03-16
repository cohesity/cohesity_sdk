# SourceConnectionRequestParams

Specifies the parameters to test connectivity with a source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **int** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. | [optional] 
**environment** | **str** | Specifies the environment type of the Protection Source. | 
**cassandra_connection_params** | [**CassandraConnectionParams**](CassandraConnectionParams.md) |  | [optional] 
**hbase_connection_params** | [**HadoopConnectionParams**](HadoopConnectionParams.md) |  | [optional] 
**hdfs_connection_params** | [**HadoopConnectionParams**](HadoopConnectionParams.md) |  | [optional] 
**hive_connection_params** | [**HadoopConnectionParams**](HadoopConnectionParams.md) |  | [optional] 
**mssql_connection_params** | [**MssqlConnectionParams**](MssqlConnectionParams.md) |  | [optional] 
**oracle_connection_params** | [**OracleConnectionParams**](OracleConnectionParams.md) |  | [optional] 
**vmware_connection_params** | [**VmwareConnectionParams**](VmwareConnectionParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.source_connection_request_params import SourceConnectionRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of SourceConnectionRequestParams from a JSON string
source_connection_request_params_instance = SourceConnectionRequestParams.from_json(json)
# print the JSON string representation of the object
print(SourceConnectionRequestParams.to_json())

# convert the object into a dict
source_connection_request_params_dict = source_connection_request_params_instance.to_dict()
# create an instance of SourceConnectionRequestParams from a dict
source_connection_request_params_from_dict = SourceConnectionRequestParams.from_dict(source_connection_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


