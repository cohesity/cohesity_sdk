# SourceConnectionResponseParams

Specifies the response from a test connection request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cassandra_connection_response_params** | [**CassandraSourceConfigParams**](CassandraSourceConfigParams.md) |  | [optional] 
**connection_id** | **int** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. | [optional] 
**environment** | **str** | Specifies the environment type of the Protection Source. | 
**hbase_connection_response_params** | [**HBaseAdditionalParams**](HBaseAdditionalParams.md) |  | [optional] 
**hdfs_connection_response_params** | [**HdfsAdditionalParams**](HdfsAdditionalParams.md) |  | [optional] 
**hive_connection_response_params** | [**HiveAdditionalParams**](HiveAdditionalParams.md) |  | [optional] 
**mssql_connection_response_params** | [**MssqlConnectionResponseParams**](MssqlConnectionResponseParams.md) |  | [optional] 
**vmware_connection_response_params** | [**VmwareAdditionalParams**](VmwareAdditionalParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.source_connection_response_params import SourceConnectionResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of SourceConnectionResponseParams from a JSON string
source_connection_response_params_instance = SourceConnectionResponseParams.from_json(json)
# print the JSON string representation of the object
print(SourceConnectionResponseParams.to_json())

# convert the object into a dict
source_connection_response_params_dict = source_connection_response_params_instance.to_dict()
# create an instance of SourceConnectionResponseParams from a dict
source_connection_response_params_from_dict = SourceConnectionResponseParams.from_dict(source_connection_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


