# GenerateNewStoreCertificateRequestAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid_till_usecs** | **int, none_type** | The date till which the certificate is valid, expressed as a Unix timestamp epoch in microseconds. The validity period must not exceed the maximum allowed duration of 397 days (configurable). If a value exceeding this duration is provided, the request will be rejected with a validation error. If the field is not provided, a default value will be used instead. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


