# ImportCertBundleRequest

Specifies the parameters for importing custom certificates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **bytearray** | Raw certificate data. It should be a base64 encoded string. | [optional] 
**format** | **str** | Specifies the format of certificate (e.g., PEM, PFX). | [optional] 
**password** | **str** | Password for accessing the certificate. | [optional] 
**display_name** | **str** | Display name of the certificate. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.import_cert_bundle_request import ImportCertBundleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportCertBundleRequest from a JSON string
import_cert_bundle_request_instance = ImportCertBundleRequest.from_json(json)
# print the JSON string representation of the object
print(ImportCertBundleRequest.to_json())

# convert the object into a dict
import_cert_bundle_request_dict = import_cert_bundle_request_instance.to_dict()
# create an instance of ImportCertBundleRequest from a dict
import_cert_bundle_request_from_dict = ImportCertBundleRequest.from_dict(import_cert_bundle_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


