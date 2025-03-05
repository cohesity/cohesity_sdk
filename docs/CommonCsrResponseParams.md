# CommonCsrResponseParams

Specifies the common response params for a CSR.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | Specifies the locality attribute, which is part of the distinguished name definition. It is used to identify the city where the company is located or the Cluster is installed. | 
**common_name** | **str** | Specifies the common name attribute, which is part of the distinguished name definition. Common name is used to specify a context for the certificate, for example, the name of the Cluster to which the certificate is to be assigned. Default value is the name of the Cluster. | [optional] 
**country_code** | **str** | Specifies the country attribute, which is part of the distinguished name definition. It is used to identify the country where the state is located. It is specified as two letter code defined by the ISO standard. | 
**dns_names** | **List[str]** | Specifies an alternative subject name component to be included in the certificate. It is used to identify the ways the Cluster will be accessed. It is given as a comma separated list of FQDNs. The default value is the Cluster&#39;s VIP hostname. | [optional] 
**email_address** | **str** | Specifies an alternative subject name component to be included in the certificate. Format is a standard e-mail address, for example joe@company.com. | [optional] 
**host_ips** | **List[str]** | Specifies an alternative subject name component to be included in the certificate. It is used to identify the ways the Cluster will be accessed. It is given as a comma separated list of IP addresses. The default value is the Cluster&#39;s VIP addresses. | [optional] 
**key_size_bits** | **int** | Specifies the size of the keys in bits. The default is 2048 bits for the RSA keys and 256 bits for ECDSA. | [optional] 
**key_type** | **str** | Specifies the algorithm to be used to generate the key pair. RSA is the default value. | [optional] [default to 'rsa']
**organization** | **str** | Specifies the organization attribute, which is part of the distinguished name definition. It is used to specify the name of the company. | 
**organization_unit** | **str** | Specifies the organization unit attribute, which is part of the distinguished name definition. It is used to identify the specific department or business unit in the company that is owning the Cluster. | 
**service_name** | **str** | Specifies the Cohesity service name for which the CSR is generated. Default service name is iris. | [optional] [default to 'iris']
**state** | **str** | Specifies the state attribute, which is part of the distinguished name definition. It is used to identify the state where the city is located. | 
**csr** | **str** | Specifies the CSR generated for the service. | [optional] 
**id** | **str** | Specifies the id of the CSR. | [optional] 
**public_key** | **str** | Specifies the public key generated for this CSR. | [optional] 

## Example

```python
from cohesity_sdk.models.common_csr_response_params import CommonCsrResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonCsrResponseParams from a JSON string
common_csr_response_params_instance = CommonCsrResponseParams.from_json(json)
# print the JSON string representation of the object
print(CommonCsrResponseParams.to_json())

# convert the object into a dict
common_csr_response_params_dict = common_csr_response_params_instance.to_dict()
# create an instance of CommonCsrResponseParams from a dict
common_csr_response_params_from_dict = CommonCsrResponseParams.from_dict(common_csr_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


