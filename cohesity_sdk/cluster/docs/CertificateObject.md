# CertificateObject

Specifies the details of a certicate which can be used for environments such as Office365.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **bytearray** | Raw certificate data. It should be a base64 encoded string. | [optional] 
**format** | **str** | Specifies the format of certificate (e.g., PEM, PFX). | [optional] 
**password** | **str** | Password for accessing the certificate. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.certificate_object import CertificateObject

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateObject from a JSON string
certificate_object_instance = CertificateObject.from_json(json)
# print the JSON string representation of the object
print(CertificateObject.to_json())

# convert the object into a dict
certificate_object_dict = certificate_object_instance.to_dict()
# create an instance of CertificateObject from a dict
certificate_object_from_dict = CertificateObject.from_dict(certificate_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


