# KmipKmsConfiguration

KMIP compliant KMS configuration parameters.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_certificate** | **str** | CA certificate. | 
**client_key** | **str** | Client key. | 
**client_certificate** | **str** | Client certificate. | 
**protocol_version** | **str** | KMIP protocol version used to communicate with the KMS. | 
**server** | **str** | KMS server IP address or FQDN. | 
**port** | **int, none_type** | Port on which the KMS server is listening. | [optional]  if omitted the server will use the default value of 5696
**certificate_expiry_date** | **int, none_type** | Specifies expiry date of client certificate in msecs. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


