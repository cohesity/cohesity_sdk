# GenerateSignCsrRequest

Specifies the parameters required to sign a certificate.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csr_pem** | **str** | Certificate signing request (csr) in pem format | 
**expiry** | **str** | Duration(e.g. 100h) of the certificate | [optional] 
**san_list** | **[str], none_type** | Specifies an alternative subject name component to be included in the certificate. It is used to identify the ways the Cluster will be accessed. It is given as a comma separated list of FQDNs. The default value is the Cluster&#39;s VIP hostname. | [optional] 
**tenant_id** | **str, none_type** | Specifies the tenant id | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


