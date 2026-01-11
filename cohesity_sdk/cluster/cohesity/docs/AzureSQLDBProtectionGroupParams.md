# AzureSQLDBProtectionGroupParams

Specifies the parameters which are specific to Azure related Protection Groups for Azure SQL DB workload. Objects must be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdc_data_processing_location** | **str, none_type** | Specifies the location where CDC (Change Data Capture) data processing occurs. Valid values are &#39;Server&#39; (processing on SQL DB server) or &#39;Client&#39; (processing on Cohesity cluster). | [optional] 
**exclude_object_ids** | **[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**exclude_sqldb_tag_ids** | **[[int]], none_type** | Array of arrays of SQL DB Tag Ids that specify db instances to Exclude. | [optional] 
**objects** | [**[AzureSQLDBProtectionGroupObjectParams]**](AzureSQLDBProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**sql_db_tag_ids** | **[[int]], none_type** | Array of arrays of SQL DB Tag Ids that specify db instances to Protect. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


