# GenerateNewStoreCertificateRequest

Specifies the parameters to generate a certificate signed by Cohesity CA and store it in secret store. The certificate generated will have a default validity of 365 days. Please contact Cohesity Support to update this value. The maximum validity of the certificate generated can be 397 days.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str, none_type** | Display name of the certificate. | [optional] 
**common_name** | **str, none_type** | Common Name (CN) of the certificate. | [optional] 
**organization** | **str, none_type** | Organization (O) name of the certificate. | [optional] 
**organization_unit** | **str, none_type** | Organization unit (OU) of the certificate. | [optional] 
**valid_till_usecs** | **int, none_type** | The date till which the certificate is valid, expressed as a Unix timestamp epoch in microseconds. The validity period must not exceed the maximum allowed duration of 397 days (configurable). If a value exceeding this duration is provided, the request will be rejected with a validation error. If the field is not provided, a default value will be used instead. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


