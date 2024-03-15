# ImportCertRequest

Specifies the paramaters required to import external ca signed certificate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_chain_pem** | **[str]** | Full ca certificate chain in pem format. | 
**cert_pem** | **str** | Certificate (pem) to be imported | 
**private_key** | **str** | Private key | 
**service_type** | **str, none_type** | Specifies the service that this certificate/key material is used. | [optional]  if omitted the server will use the default value of "kAll"
**tenant_id** | **str, none_type** | Specifies the tenant id | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


