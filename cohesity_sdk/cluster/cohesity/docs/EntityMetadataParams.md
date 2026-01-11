# EntityMetadataParams

Specifies the parameters to associate metadata with entities in the entity hierarchy.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **int** | Specifies the entity id of the entity whose metadata is being updated. | 
**aws_params** | [**AwsEntityMetadata**](AwsEntityMetadata.md) |  | [optional] 
**azure_params** | [**AzureEntityMetadata**](AzureEntityMetadata.md) |  | [optional] 
**experimental_adapter_params** | [**ExperimentalAdapterEntityMetadata**](ExperimentalAdapterEntityMetadata.md) |  | [optional] 
**gcp_params** | [**GCPEntityMetadata**](GCPEntityMetadata.md) |  | [optional] 
**maintenance_mode_config** | [**MaintenanceModeConfig**](MaintenanceModeConfig.md) |  | [optional] 
**user_tag_attributes** | [**[TagAttributeParams]**](TagAttributeParams.md) | Specifies the tag attributes associated with the entity created by the user | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


