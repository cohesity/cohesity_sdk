# CertificateRequestParams

Specifies the parameters of a CSR.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str, none_type** | Specifies the locality attribute, which is part of the distinguished name definition. It is used to identify the city where the company is located or the Cluster is installed. | 
**common_name** | **str, none_type** | Specifies the common name attribute, which is part of the distinguished name definition. Common name is used to specify a context for the certificate, for example, the name of the Cluster to which the certificate is to be assigned. Default value is the name of the Cluster. | 
**country_code** | **str, none_type** | Specifies the country attribute, which is part of the distinguished name definition. It is used to identify the country where the state is located. It is specified as two letter code defined by the ISO standard. | 
**organization** | **str, none_type** | Specifies the organization attribute, which is part of the distinguished name definition. It is used to specify the name of the company. | 
**organization_unit** | **str, none_type** | Specifies the organization unit attribute, which is part of the distinguished name definition. It is used to identify the specific department or business unit in the company that is owning the Cluster. | 
**state** | **str, none_type** | Specifies the state attribute, which is part of the distinguished name definition. It is used to identify the state where the city is located. | 
**duration** | **str, none_type** | Specifies duration of the certificate expiry in(hours). | [optional] 
**email_address** | **str, none_type** | Specifies an alternative subject name component to be included in the certificate. Format is a standard e-mail address, for example joe@company.com. | [optional] 
**key_type** | **str, none_type** | Specifies the algorithm to be used to generate the key pair. RSA is the default value. | [optional]  if omitted the server will use the default value of "RSA_4096"
**san_list** | **[str], none_type** | Specifies an alternative subject name component to be included in the certificate. It is used to identify the ways the Cluster will be accessed. It is given as a comma separated list of FQDNs. The default value is the Cluster&#39;s VIP hostname. | [optional] 
**tenant_id** | **str, none_type** | Specifies the tenant id | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


