# CreateCsrRequest

Specifies the request to create a CSR.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str, none_type** | Specifies the locality attribute, which is part of the distinguished name definition. It is used to identify the city where the company is located or the Cluster is installed. | 
**country_code** | **str, none_type** | Specifies the country attribute, which is part of the distinguished name definition. It is used to identify the country where the state is located. It is specified as two letter code defined by the ISO standard. | 
**organization** | **str, none_type** | Specifies the organization attribute, which is part of the distinguished name definition. It is used to specify the name of the company. | 
**organization_unit** | **str, none_type** | Specifies the organization unit attribute, which is part of the distinguished name definition. It is used to identify the specific department or business unit in the company that is owning the Cluster. | 
**state** | **str, none_type** | Specifies the state attribute, which is part of the distinguished name definition. It is used to identify the state where the city is located. | 
**common_name** | **str, none_type** | Specifies the common name attribute, which is part of the distinguished name definition. Common name is used to specify a context for the certificate, for example, the name of the Cluster to which the certificate is to be assigned. Default value is the name of the Cluster. | [optional] 
**dns_names** | **[str], none_type** | Specifies an alternative subject name component to be included in the certificate. It is used to identify the ways the Cluster will be accessed. It is given as a comma separated list of FQDNs. The default value is the Cluster&#39;s VIP hostname. | [optional] 
**email_address** | **str, none_type** | Specifies an alternative subject name component to be included in the certificate. Format is a standard e-mail address, for example joe@company.com. | [optional] 
**host_ips** | **[str], none_type** | Specifies an alternative subject name component to be included in the certificate. It is used to identify the ways the Cluster will be accessed. It is given as a comma separated list of IP addresses. The default value is the Cluster&#39;s VIP addresses. | [optional] 
**key_size_bits** | **int, none_type** | Specifies the size of the keys in bits. The default is 2048 bits for the RSA keys and 256 bits for ECDSA. | [optional] 
**key_type** | **str, none_type** | Specifies the algorithm to be used to generate the key pair. RSA is the default value. | [optional]  if omitted the server will use the default value of "rsa"
**service_name** | **str, none_type** | Specifies the Cohesity service name for which the CSR is generated. Default service name is iris. | [optional]  if omitted the server will use the default value of "iris"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


