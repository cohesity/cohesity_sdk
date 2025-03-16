# CreateClientcsrResponseBody

Specifies the response to creating the CSRs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csr_client** | **str** | Specifies the CSR generated for the client. | [optional] 
**csr_server** | **str** | Specifies the CSR generated for the server. | [optional] 
**file_csr_client** | **str** | Specifies the path to CSR generated for the client | [optional] 
**file_csr_server** | **str** | Specifies the path to CSR generated for the server | [optional] 
**public_key_client** | **str** | Specifies the public key generated for this CSR for the client. | [optional] 
**public_key_server** | **str** | Specifies the public key generated for this CSR for the server. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.create_clientcsr_response_body import CreateClientcsrResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClientcsrResponseBody from a JSON string
create_clientcsr_response_body_instance = CreateClientcsrResponseBody.from_json(json)
# print the JSON string representation of the object
print(CreateClientcsrResponseBody.to_json())

# convert the object into a dict
create_clientcsr_response_body_dict = create_clientcsr_response_body_instance.to_dict()
# create an instance of CreateClientcsrResponseBody from a dict
create_clientcsr_response_body_from_dict = CreateClientcsrResponseBody.from_dict(create_clientcsr_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


