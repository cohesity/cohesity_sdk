# AzureSQLMIProtectionGroupParams

Specifies the parameters which are specific to Azure related Protection Groups for Azure SQL MI workload. Objects must be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdc_data_processing_location** | **str, none_type** | Specifies the location where CDC (Change Data Capture) data processing occurs. Valid values are &#39;Server&#39; (processing on SQL MI server) or &#39;Client&#39; (processing on Cohesity cluster). | [optional] 
**exclude_object_ids** | **[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**exclude_sqlmi_tag_ids** | **[[int]], none_type** | Array of arrays of SQL MI Tag Ids that specify db instances to Exclude. | [optional] 
**objects** | [**[AzureSQLMIProtectionGroupObjectParams]**](AzureSQLMIProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**sql_mi_tag_ids** | **[[int]], none_type** | Array of arrays of SQL MI Tag Ids that specify db instances to Protect. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


