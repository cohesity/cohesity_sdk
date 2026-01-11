# PhysicalEnvJobParams

Protection Job parameters applicable to 'kPhysical' Environment type. Specifies job parameters applicable for all 'kPhysical' Environment type Protection Sources in a Protection Job.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cobmr_backup** | **bool, none_type** | Specifies whether to enable CoBMR backup. | [optional] 
**file_path_filters** | [**FileFilteringPolicy**](FileFilteringPolicy.md) |  | [optional] 
**incremental_snapshot_upon_restart** | **bool, none_type** | If true, performs an incremental backup after server restarts. Otherwise a full backup is done. NOTE: This is applicable only to Windows servers. If not set, default value is false. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


