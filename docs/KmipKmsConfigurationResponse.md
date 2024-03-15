# KmipKmsConfigurationResponse

KMIP compliant KMS configuration response params.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_server_address** | **[str]** | Additional KMS server IP address or FQDNs for fail over. | [optional] 
**certificate_expiry_date** | **int, none_type** | Specifies expiry date of client certificate in msecs. | [optional] [readonly] 
**port** | **int, none_type** | Port on which the KMS server is listening. | [optional]  if omitted the server will use the default value of 5696
**protocol_version** | **str, none_type** | KMIP protocol version used to communicate with the KMS. | [optional] 
**server** | **str, none_type** | KMS server IP address or FQDN. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


