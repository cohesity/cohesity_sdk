# RpaasRegionInfo

Specifies a Rpaas enabled region.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region_id** | **str, none_type** | ID that identifies a region. | [optional] 
**region_name** | **str, none_type** | Name of the region. | [optional] 
**kms_key_info** | [**KmsKeyBasicInfo**](KmsKeyBasicInfo.md) |  | [optional] 
**provision_status** | [**ProvisionStatus**](ProvisionStatus.md) |  | [optional] 
**pairing_info** | [**[RpaasPairingInfo], none_type**](RpaasPairingInfo.md) | The configured cluster for the particular region. | [optional] 
**vault_name** | **str, none_type** | Name of the vault. | [optional] 
**bucket_name** | **str, none_type** | Name of the S3 bucket. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


