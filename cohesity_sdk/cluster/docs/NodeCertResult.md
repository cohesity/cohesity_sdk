# NodeCertResult

Successful certificate import response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_cert_sha256** | **str** | SHA of the CA cert that was using to sign the CSR | 
**signed_cert_sha256** | **str** | SHA of the accepted complete signed cert | 

## Example

```python
from cohesity_sdk.cluster.models.node_cert_result import NodeCertResult

# TODO update the JSON string below
json = "{}"
# create an instance of NodeCertResult from a JSON string
node_cert_result_instance = NodeCertResult.from_json(json)
# print the JSON string representation of the object
print(NodeCertResult.to_json())

# convert the object into a dict
node_cert_result_dict = node_cert_result_instance.to_dict()
# create an instance of NodeCertResult from a dict
node_cert_result_from_dict = NodeCertResult.from_dict(node_cert_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


