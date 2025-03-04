# MssqlConnectionResponseParams

Specifies the response parameters after connecting to a SQL node/cluster using given IP or hostname FQDN.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_identifier** | **str** | Specifies the unique identifier to locate the SQL node or cluster. The host identifier can be IP address or FQDN. | 
**aag_groups** | [**List[AAGGroup]**](AAGGroup.md) | Specifies the list of AAG (Always on Avalibility) groups. | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**fci_clusters** | [**List[FCICluster]**](FCICluster.md) | Specifies the list of FCI (Failover Cluster Instaces) Clusters. This will contain the list of all failover pools under a windows cluster. FCI clusters which are part of AAG, will be returned seperatly under aagServers field. | [optional] 
**servers** | [**List[SQLServer]**](SQLServer.md) | Specifies the list of SQL servers. If SQL server is a part of avalibility group then it will be returned in aagServers field. This will include the list of all standalone SQL servers and servers belonging to any FCI enviournment. | [optional] 
**skip_connection_discovery** | **bool** | Specifies whether to skip the discovery phase of all SQL servers, AAG groups etc during registration process. | [optional] 

## Example

```python
from cohesity_sdk.models.mssql_connection_response_params import MssqlConnectionResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of MssqlConnectionResponseParams from a JSON string
mssql_connection_response_params_instance = MssqlConnectionResponseParams.from_json(json)
# print the JSON string representation of the object
print(MssqlConnectionResponseParams.to_json())

# convert the object into a dict
mssql_connection_response_params_dict = mssql_connection_response_params_instance.to_dict()
# create an instance of MssqlConnectionResponseParams from a dict
mssql_connection_response_params_from_dict = MssqlConnectionResponseParams.from_dict(mssql_connection_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


