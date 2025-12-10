# RecoverGCPFirestoreNewSourceConfig

Specifies the configuration for recovering GCP Firestore database to the new target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**target_region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_gcp_firestore_new_source_config import RecoverGCPFirestoreNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGCPFirestoreNewSourceConfig from a JSON string
recover_gcp_firestore_new_source_config_instance = RecoverGCPFirestoreNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverGCPFirestoreNewSourceConfig.to_json())

# convert the object into a dict
recover_gcp_firestore_new_source_config_dict = recover_gcp_firestore_new_source_config_instance.to_dict()
# create an instance of RecoverGCPFirestoreNewSourceConfig from a dict
recover_gcp_firestore_new_source_config_from_dict = RecoverGCPFirestoreNewSourceConfig.from_dict(recover_gcp_firestore_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


