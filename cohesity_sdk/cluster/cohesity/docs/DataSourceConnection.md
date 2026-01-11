# DataSourceConnection

Specifies all the properties of the data-source connection. A connection is specified by an ID that's guaranteed to be unique. A connection is associated with exactly one tenant. A connection can be thought of as a subset of its tenant's connectors and can contain 0 or more connectors within it. A connector can only be associated with one connection at max at a given time.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | Specifies the unique ID of the connection. | 
**connection_name** | **str** | Specifies the name of the connection. For a given tenant, different connections can&#39;t have the same name. However, two (or more) different tenants can each have a connection with the same name. | 
**cluster_vips** | **[str], none_type** | Specifies the list of cluster virtual IPs associated with the connection. | [optional] 
**connection_type** | **str, none_type** | Specifies the type of the connection. | [optional] 
**connectivity_status** | [**ConnectionConnectivityStatus**](ConnectionConnectivityStatus.md) |  | [optional] 
**connector_ids** | **[str]** | Specifies the IDs of the connectors in this connection. | [optional] [readonly] 
**patching_connector_id** | **str, none_type** | Specifies the connector ID that is currently in patch. | [optional] [readonly] 
**registration_token** | **str, none_type** | Specifies a token that can be used to register a connector against this connection | [optional] [readonly] 
**tenant_id** | **str** | Specifies the tenant ID of the connection. | [optional] [readonly] 
**upgrading_connector_id** | **str, none_type** | Specifies the connector ID that is currently in upgrade. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


