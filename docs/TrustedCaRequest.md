# TrustedCaRequest

Specifies the basic info about CA Root Certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | Specifies the certificate to be imported. Certificate should be in PEM format. | 
**description** | **str** | Description of the certificate. | [optional] 
**name** | **str** | Descriptive name of the certificate. | 

## Example

```python
from cohesity_sdk.models.trusted_ca_request import TrustedCaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedCaRequest from a JSON string
trusted_ca_request_instance = TrustedCaRequest.from_json(json)
# print the JSON string representation of the object
print(TrustedCaRequest.to_json())

# convert the object into a dict
trusted_ca_request_dict = trusted_ca_request_instance.to_dict()
# create an instance of TrustedCaRequest from a dict
trusted_ca_request_from_dict = TrustedCaRequest.from_dict(trusted_ca_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


