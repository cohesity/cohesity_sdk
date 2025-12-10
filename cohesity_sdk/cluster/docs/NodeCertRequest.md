# NodeCertRequest

Import signed cert and CA cert request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_cert** | **str** | CA cert used to sign the CSR | 
**signed_cert** | **str** | Complete signed certificate | 

## Example

```python
from cohesity_sdk.cluster.models.node_cert_request import NodeCertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NodeCertRequest from a JSON string
node_cert_request_instance = NodeCertRequest.from_json(json)
# print the JSON string representation of the object
print(NodeCertRequest.to_json())

# convert the object into a dict
node_cert_request_dict = node_cert_request_instance.to_dict()
# create an instance of NodeCertRequest from a dict
node_cert_request_from_dict = NodeCertRequest.from_dict(node_cert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


