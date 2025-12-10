# KubernetesRecoveryMigrationParams

Specifies an individual migration rule for mapping a region/zone to another for cross region recovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_value** | **str** | Specifies the current value for the mapping that needs to be mutated. | 
**new_value** | **str** | Specifies the new value for the mapping with which the fields need to be updated with. | 

## Example

```python
from cohesity_sdk.cluster.models.kubernetes_recovery_migration_params import KubernetesRecoveryMigrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesRecoveryMigrationParams from a JSON string
kubernetes_recovery_migration_params_instance = KubernetesRecoveryMigrationParams.from_json(json)
# print the JSON string representation of the object
print(KubernetesRecoveryMigrationParams.to_json())

# convert the object into a dict
kubernetes_recovery_migration_params_dict = kubernetes_recovery_migration_params_instance.to_dict()
# create an instance of KubernetesRecoveryMigrationParams from a dict
kubernetes_recovery_migration_params_from_dict = KubernetesRecoveryMigrationParams.from_dict(kubernetes_recovery_migration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


