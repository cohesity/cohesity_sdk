# FirestoreProtectionGroupParams

Specifies the parameters which are specific to GCP Firestore related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_create_cloud_storage_bucket** | **bool** | This flag controls whether Firestore backup auto-create bucket or use the provided bucket name. | 
**pitr_enabled** | **bool** | The firestore DB level PITR option needs to enabled for consistent data. | 
**cloud_storage_bucket_name** | **str, none_type** | The Google Cloud Storage bucket name for Firestore backup. | [optional] 
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**[FirestoreProtectionGroupObjectParams]**](FirestoreProtectionGroupObjectParams.md) | Specifies the Firestore databases to be included in the Protection Group. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


