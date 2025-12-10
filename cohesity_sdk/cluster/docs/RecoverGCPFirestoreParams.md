# RecoverGCPFirestoreParams

Specifies the parameters to recover GCP Firestore.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcp_target_params** | [**GCPTargetParamsForRecoverGCPFirestore**](GCPTargetParamsForRecoverGCPFirestore.md) |  | 
**snapshots** | [**List[RecoverGCPFirestoreSnapshotParams]**](RecoverGCPFirestoreSnapshotParams.md) | Specifies the details of the gcp firestore objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_gcp_firestore_params import RecoverGCPFirestoreParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGCPFirestoreParams from a JSON string
recover_gcp_firestore_params_instance = RecoverGCPFirestoreParams.from_json(json)
# print the JSON string representation of the object
print(RecoverGCPFirestoreParams.to_json())

# convert the object into a dict
recover_gcp_firestore_params_dict = recover_gcp_firestore_params_instance.to_dict()
# create an instance of RecoverGCPFirestoreParams from a dict
recover_gcp_firestore_params_from_dict = RecoverGCPFirestoreParams.from_dict(recover_gcp_firestore_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


