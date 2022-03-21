# KmsConfiguration

 Key management system(KMS) configurations.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Name of the KMS. | [optional] 
**type** | **str, none_type** | Type of KMS. &#39;InternalKms&#39; indicates the internal cluster KMS. &#39;AwsKms&#39; indicates AWS KMS. &#39;KmipKms&#39; indicates any KMIP compliant KMS. | [optional] 
**usage_type** | **str, none_type** | Specifies the usage type of the kms config. &#39;kArchival&#39; indicates this is used for regular archival. &#39;kRpaasArchival&#39; indicates this is used for RPaaS only. | [optional] 
**aws_kms_params** | [**AwsKmsConfigurationResponse**](AwsKmsConfigurationResponse.md) |  | [optional] 
**kmip_kms_params** | [**KmipKmsConfigurationResponse**](KmipKmsConfigurationResponse.md) |  | [optional] 
**storage_domain_ids** | **[int], none_type** | Ids of storage domains used to assign the KMS for encryption. Once an external KMS (AWS KMS or KIMP KMS) is assigned to a storage domain, it cannot be changed. | [optional] 
**external_target_ids** | **[int], none_type** | Ids of external targets used to assign the KMS for encryption. Once an external KMS (AWS KMS or KIMP KMS) is assigned to an external target, it cannot be changed. | [optional] 
**ownership_context** | **str, none_type** | Describes the consumption of the KMS key whether it is used for local or FortKnox. | [optional] 
**id** | **int, none_type** | Id of KMS. | [optional] [readonly] 
**state** | **str, none_type** | Specifies the state of KMS. &#39;Active&#39; indicates that KMS is reachable from cluster. &#39;InActive&#39; indicates that KMS is not reachable from cluster. &#39;MarkedForRemoval&#39; indicates that KMS is marked for removal and the removal process is in progress. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


