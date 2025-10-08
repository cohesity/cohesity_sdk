# MssqlConnectionResponseParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aag_groups** | [**[AAGGroup], none_type**](AAGGroup.md) | Specifies the list of AAG (Always on Avalibility) groups. | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**fci_clusters** | [**[FCICluster], none_type**](FCICluster.md) | Specifies the list of FCI (Failover Cluster Instaces) Clusters. This will contain the list of all failover pools under a windows cluster. FCI clusters which are part of AAG, will be returned seperatly under aagServers field. | [optional] 
**servers** | [**[SQLServer], none_type**](SQLServer.md) | Specifies the list of SQL servers. If SQL server is a part of avalibility group then it will be returned in aagServers field. This will include the list of all standalone SQL servers and servers belonging to any FCI enviournment. | [optional] 
**skip_connection_discovery** | **bool, none_type** | Specifies whether to skip the discovery phase of all SQL servers, AAG groups etc during registration process. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


