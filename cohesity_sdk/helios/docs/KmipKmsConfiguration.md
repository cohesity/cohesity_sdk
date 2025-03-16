# KmipKmsConfiguration

KMIP compliant KMS configuration parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_server_address** | **List[str]** | Additional KMS server IP address or FQDNs for fail over. | [optional] 
**ca_certificate** | **str** | CA certificate. | 
**certificate_expiry_date** | **int** | Specifies expiry date of client certificate in msecs. | [optional] [readonly] 
**client_certificate** | **str** | Client certificate. | 
**client_key** | **str** | Client key. | 
**port** | **int** | Port on which the KMS server is listening. | [optional] [default to 5696]
**protocol_version** | **str** | KMIP protocol version used to communicate with the KMS. | 
**server** | **str** | KMS server IP address or FQDN. | 

## Example

```python
from cohesity_sdk.helios.models.kmip_kms_configuration import KmipKmsConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of KmipKmsConfiguration from a JSON string
kmip_kms_configuration_instance = KmipKmsConfiguration.from_json(json)
# print the JSON string representation of the object
print(KmipKmsConfiguration.to_json())

# convert the object into a dict
kmip_kms_configuration_dict = kmip_kms_configuration_instance.to_dict()
# create an instance of KmipKmsConfiguration from a dict
kmip_kms_configuration_from_dict = KmipKmsConfiguration.from_dict(kmip_kms_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


