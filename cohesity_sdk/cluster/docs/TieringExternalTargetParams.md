# TieringExternalTargetParams

Specifies the parameters which are specific to Tiering purpose type External Targets.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption_level** | **str, none_type** | Specifies the type of encryption for the Setting. | 
**storage_type** | **str, none_type** | Specifies the Storage type of the External Target. | 
**aws_params** | [**TieringAwsExternalTargetParams**](TieringAwsExternalTargetParams.md) |  | [optional] 
**azure_params** | [**TieringAzureExternalTargetParams**](TieringAzureExternalTargetParams.md) |  | [optional] 
**gcp_params** | [**TieringGcpExternalTargetParams**](TieringGcpExternalTargetParams.md) |  | [optional] 
**oracle_params** | [**TieringOracleExternalTargetParams**](TieringOracleExternalTargetParams.md) |  | [optional] 
**s3_comp_params** | [**TieringS3CompExternalTargetParams**](TieringS3CompExternalTargetParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


