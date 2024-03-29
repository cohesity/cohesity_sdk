# McmRigelClaimResponseParams

Specifies the response of claiming a Rigel to Helios.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **int, none_type** | Connection id for rigel instance. | [optional] 
**dataplane_endpoint** | **str, none_type** | Endpoint for associated data plane. | [optional] 
**helios_certificate** | **str, none_type** | Specifies the Helios certificate that can be used to authenticate api calls made from Helios to Rigel. | [optional] 
**region_id** | **str, none_type** | Specifies the region id of the Rigel cluster. | [optional] 
**rigel_ca_chain** | **str, none_type** | Specifies the CA chain that is used to sign the Rigel certificate. | [optional] 
**rigel_certificate** | **str, none_type** | Specifies the Rigel certificate. | [optional] 
**rigel_guid** | **int, none_type** | Unique id for rigel instance. | [optional] 
**rigel_private_key** | **str, none_type** | Specifies the Rigel private key. | [optional] 
**rigel_type** | **str, none_type** | Specifies the Rigel type that is being claimed. | [optional] 
**rigel_use_case** | **str, none_type** | Specifies the Rigel use case. | [optional] 
**tenant_ca_chain** | **[str, none_type], none_type** | Specifies the Tenant CA chain. | [optional] 
**tenant_id** | **str, none_type** | Tenant id associated with the claimed rigel. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


