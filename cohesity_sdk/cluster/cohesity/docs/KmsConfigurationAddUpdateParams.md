# KmsConfigurationAddUpdateParams

Parameters to update or add key management system(KMS) on the cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the KMS. | 
**external_target_ids** | **[int], none_type** | Ids of external targets used to assign the KMS for encryption. Once an external KMS (AWS KMS or KIMP KMS) is assigned to an external target, it cannot be changed. | [optional] 
**kmip_kms_params** | [**KmipKmsConfiguration**](KmipKmsConfiguration.md) |  | [optional] 
**storage_domain_ids** | **[int], none_type** | Ids of storage domains used to assign the KMS for encryption. Once an external KMS (AWS KMS or KIMP KMS) is assigned to a storage domain, it cannot be changed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


