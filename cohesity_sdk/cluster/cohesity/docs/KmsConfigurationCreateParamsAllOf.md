# KmsConfigurationCreateParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of KMS. &#39;InternalKms&#39; indicates the internal cluster KMS. &#39;AwsKms&#39; indicates AWS KMS. &#39;KmipKms&#39; indicates any KMIP compliant KMS. | 
**aws_kms_params** | [**AwsKmsConfiguration**](AwsKmsConfiguration.md) |  | [optional] 
**gcp_kms_params** | [**GcpKmsConfiguration**](GcpKmsConfiguration.md) |  | [optional] 
**ibm_kms_params** | [**IbmKmsConfiguration**](IbmKmsConfiguration.md) |  | [optional] 
**ownership_context** | **str, none_type** | Specifies the ownership context of the kms config. &#39;Local&#39; indicates this is used for regular archival. &#39;FortKnox&#39; indicates this is used for FortKnox only. | [optional] 
**usage_type** | **str, none_type** | Specifies the usage type of the kms config. &#39;kArchival&#39; indicates this is used for regular archival. &#39;kRpaasArchival&#39; indicates this is used for RPaaS only. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


