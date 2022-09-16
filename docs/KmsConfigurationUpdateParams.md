# KmsConfigurationUpdateParams

Parameters to update key management system(KMS) on the cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the KMS. | 
**aws_kms_params** | [**AwsKmsConfigurationUpdateParams**](AwsKmsConfigurationUpdateParams.md) |  | [optional] 
**storage_domain_ids** | **[int], none_type** | Ids of storage domains used to assign the KMS for encryption. Once an external KMS (AWS KMS or KIMP KMS) is assigned to a storage domain, it cannot be changed. | [optional] 
**external_target_ids** | **[int], none_type** | Ids of external targets used to assign the KMS for encryption. Once an external KMS (AWS KMS or KIMP KMS) is assigned to an external target, it cannot be changed. | [optional] 
**kmip_kms_params** | [**KmipKmsConfiguration**](KmipKmsConfiguration.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


