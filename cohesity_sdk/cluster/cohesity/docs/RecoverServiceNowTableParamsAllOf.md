# RecoverServiceNowTableParamsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the table to be restored. | 
**common_recovery_options** | [**CommonRecoveryOptions**](CommonRecoveryOptions.md) |  | [optional] 
**filter_query** | **str, none_type** | Specifies a Query to filter the records. This filtered list of records will be used for recovery. | [optional] 
**parent_object_ids** | **[str], none_type** | Specifies a list of parent object IDs to include in recovery. Specified parent objects will also be recovered as part of this recovery. | [optional] 
**records** | **[str], none_type** | Specifies a list of records IDs to be recovered for the  specified table. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


