# DataSourceConnection

Specifies all the properties of the data-source connection. A connection is specified by an ID that's guaranteed to be unique. A connection is associated with exactly one tenant. A connection can be thought of as a subset of its tenant's connectors and can contain 0 or more connectors within it. A connector can only be associated with one connection at max at a given time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_vips** | **List[str]** | Specifies the list of cluster virtual IPs associated with the connection. | [optional] 
**connection_id** | **str** | Specifies the unique ID of the connection. | 
**connection_name** | **str** | Specifies the name of the connection. For a given tenant, different connections can&#39;t have the same name. However, two (or more) different tenants can each have a connection with the same name. | 
**connection_type** | **str** | Specifies the type of the connection. | [optional] 
**connectivity_status** | [**ConnectionConnectivityStatus**](ConnectionConnectivityStatus.md) |  | [optional] 
**connector_ids** | **List[str]** | Specifies the IDs of the connectors in this connection. | [optional] [readonly] 
**patching_connector_id** | **str** | Specifies the connector ID that is currently in patch. | [optional] [readonly] 
**registration_token** | **str** | Specifies a token that can be used to register a connector against this connection | [optional] [readonly] 
**tenant_id** | **str** | Specifies the tenant ID of the connection. | [optional] [readonly] 
**upgrading_connector_id** | **str** | Specifies the connector ID that is currently in upgrade. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.data_source_connection import DataSourceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceConnection from a JSON string
data_source_connection_instance = DataSourceConnection.from_json(json)
# print the JSON string representation of the object
print(DataSourceConnection.to_json())

# convert the object into a dict
data_source_connection_dict = data_source_connection_instance.to_dict()
# create an instance of DataSourceConnection from a dict
data_source_connection_from_dict = DataSourceConnection.from_dict(data_source_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


