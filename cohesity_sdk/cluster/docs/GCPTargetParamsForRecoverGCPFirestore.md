# GCPTargetParamsForRecoverGCPFirestore

Specifies the recovery target params for GCP Firestore target config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_storage_bucket_name** | **str** | The Google Cloud Storage bucket name for Firestore recovery. | 
**new_source_config** | [**RecoverGCPFirestoreNewSourceConfig**](RecoverGCPFirestoreNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 

## Example

```python
from cohesity_sdk.cluster.models.gcp_target_params_for_recover_gcp_firestore import GCPTargetParamsForRecoverGCPFirestore

# TODO update the JSON string below
json = "{}"
# create an instance of GCPTargetParamsForRecoverGCPFirestore from a JSON string
gcp_target_params_for_recover_gcp_firestore_instance = GCPTargetParamsForRecoverGCPFirestore.from_json(json)
# print the JSON string representation of the object
print(GCPTargetParamsForRecoverGCPFirestore.to_json())

# convert the object into a dict
gcp_target_params_for_recover_gcp_firestore_dict = gcp_target_params_for_recover_gcp_firestore_instance.to_dict()
# create an instance of GCPTargetParamsForRecoverGCPFirestore from a dict
gcp_target_params_for_recover_gcp_firestore_from_dict = GCPTargetParamsForRecoverGCPFirestore.from_dict(gcp_target_params_for_recover_gcp_firestore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


