# ArchivalTargetTierInfo

Specifies the tier info for archival.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_platform** | **str, none_type** | Specifies the cloud platform to enable tiering. | 
**aws_tiering** | [**AWSTiers**](AWSTiers.md) |  | [optional] 
**azure_tiering** | [**AzureTiers**](AzureTiers.md) |  | [optional] 
**google_tiering** | [**GoogleTiers**](GoogleTiers.md) |  | [optional] 
**oracle_tiering** | [**OracleTiers**](OracleTiers.md) |  | [optional] 
**current_tier_type** | **str, none_type** | Specifies the type of the current tier where the snapshot resides. This will be specified if the run is a CAD run. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


