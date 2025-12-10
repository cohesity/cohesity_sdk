# FirestoreProtectionGroupParams

Specifies the parameters which are specific to GCP Firestore related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_create_cloud_storage_bucket** | **bool** | This flag controls whether Firestore backup auto-create bucket or use the provided bucket name. | 
**cloud_storage_bucket_name** | **str** | The Google Cloud Storage bucket name for Firestore backup. | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**List[FirestoreProtectionGroupObjectParams]**](FirestoreProtectionGroupObjectParams.md) | Specifies the Firestore databases to be included in the Protection Group. | [optional] 
**pitr_enabled** | **bool** | The firestore DB level PITR option needs to enabled for consistent data. | 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.firestore_protection_group_params import FirestoreProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of FirestoreProtectionGroupParams from a JSON string
firestore_protection_group_params_instance = FirestoreProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(FirestoreProtectionGroupParams.to_json())

# convert the object into a dict
firestore_protection_group_params_dict = firestore_protection_group_params_instance.to_dict()
# create an instance of FirestoreProtectionGroupParams from a dict
firestore_protection_group_params_from_dict = FirestoreProtectionGroupParams.from_dict(firestore_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


