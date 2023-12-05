# RecoverSfdcObjectParams

Specifies the parameters to recover Salesforce objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_deleted_objects** | **bool, none_type** | Specifies whether to include deleted Objects in the recovery. | 
**child_object_ids** | **[str]** | Specifies a list of child object IDs to include in the recovery. Specified object IDs will also be recovered as part of this recovery. | [optional] 
**filter_query** | **str, none_type** | Specifies a Query to filter the records. This filtered list of records will be used for recovery. | [optional] 
**object_name** | **str, none_type** | Specifies the name of the object to be restored. | [optional] 
**parent_object_ids** | **[str], none_type** | Specifies a list of parent object IDs to include in recovery. Specified parent objects will also be recovered as part of this recovery. | [optional] 
**records** | **[str], none_type** | Specifies a list of records IDs to be recovered for the specified Object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


