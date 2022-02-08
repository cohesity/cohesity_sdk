# BifrostConnector

Specify a Bifrost connector.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies the id of the connector. | [optional] 
**name** | **str, none_type** | Specifies the name of the connector. | [optional] 
**connection_id** | **int, none_type** | Specifies the Id of the connection which this connector belongs to. | [optional] 
**connection_status** | [**ConnectorConnectionInfo**](ConnectorConnectionInfo.md) |  | [optional] 
**cohesity_side_ip** | **str, none_type** | Specifies the cohesity side ip of the connector | [optional] [readonly] 
**tenant_source_side_ip** | **str, none_type** | Specifies the tenant source side ip of the connector | [optional] [readonly] 
**hyx_version** | **str, none_type** | Specifies the connector&#39;s software Version | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


