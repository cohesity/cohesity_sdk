# UpdateBifrostConnectionRequest

Specify the params to update a Hybrid Extender connection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies the id of the connection. | 
**name** | **str, none_type** | Specifies the name of the connection. | 
**certificate_version** | **int, none_type** | Specifies the version of the connection&#39;s certificate. The version is used to revoke/renew connection&#39;s certificates. | [optional] 
**connectors** | **[str]** | Specifies the ids of the connectors in this connection | [optional] 
**network_connection_info** | [**NetworkConnectionInfo**](NetworkConnectionInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


