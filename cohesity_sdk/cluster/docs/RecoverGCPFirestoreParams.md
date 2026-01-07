# RecoverGCPFirestoreParams

Specifies the parameters to recover GCP Firestore.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcp_target_params** | [**GCPTargetParamsForRecoverGCPFirestore**](GCPTargetParamsForRecoverGCPFirestore.md) |  | 
**snapshots** | [**[RecoverGCPFirestoreSnapshotParams]**](RecoverGCPFirestoreSnapshotParams.md) | Specifies the details of the gcp firestore objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kGCP"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


