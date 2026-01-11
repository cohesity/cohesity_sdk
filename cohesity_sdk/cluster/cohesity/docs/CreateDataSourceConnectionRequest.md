# CreateDataSourceConnectionRequest

Specifies parameters, like connection name, for the request to create a data-source connection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_vips** | **[str], none_type** | List of cluster virtual IPs associated with the connection. | [optional] 
**connection_name** | **str** | Specifies the name of the connection being created. For a given tenant, different connections can&#39;t have the same name. However, two (or more) different tenants can each have a connection with the same name. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


