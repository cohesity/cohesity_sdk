# FirestoreProtectionGroupObjectParams

Specifies the object parameters to create GCP Firestore Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the database. | 
**name** | **str** | Specifies the name of the database. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.firestore_protection_group_object_params import FirestoreProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of FirestoreProtectionGroupObjectParams from a JSON string
firestore_protection_group_object_params_instance = FirestoreProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(FirestoreProtectionGroupObjectParams.to_json())

# convert the object into a dict
firestore_protection_group_object_params_dict = firestore_protection_group_object_params_instance.to_dict()
# create an instance of FirestoreProtectionGroupObjectParams from a dict
firestore_protection_group_object_params_from_dict = FirestoreProtectionGroupObjectParams.from_dict(firestore_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


