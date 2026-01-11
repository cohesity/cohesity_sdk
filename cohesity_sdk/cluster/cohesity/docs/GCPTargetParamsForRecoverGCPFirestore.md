# GCPTargetParamsForRecoverGCPFirestore

Specifies the recovery target params for GCP Firestore target config.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_storage_bucket_name** | **str** | The Google Cloud Storage bucket name for Firestore recovery. | 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 
**new_source_config** | [**RecoverGCPFirestoreNewSourceConfig**](RecoverGCPFirestoreNewSourceConfig.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


