# KmipKmsConfigurationResponse

KMIP compliant KMS configuration response params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_server_address** | **List[str]** | Additional KMS server IP address or FQDNs for fail over. | [optional] 
**certificate_expiry_date** | **int** | Specifies expiry date of client certificate in msecs. | [optional] [readonly] 
**port** | **int** | Port on which the KMS server is listening. | [optional] [default to 5696]
**protocol_version** | **str** | KMIP protocol version used to communicate with the KMS. | [optional] 
**server** | **str** | KMS server IP address or FQDN. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.kmip_kms_configuration_response import KmipKmsConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KmipKmsConfigurationResponse from a JSON string
kmip_kms_configuration_response_instance = KmipKmsConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(KmipKmsConfigurationResponse.to_json())

# convert the object into a dict
kmip_kms_configuration_response_dict = kmip_kms_configuration_response_instance.to_dict()
# create an instance of KmipKmsConfigurationResponse from a dict
kmip_kms_configuration_response_from_dict = KmipKmsConfigurationResponse.from_dict(kmip_kms_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


