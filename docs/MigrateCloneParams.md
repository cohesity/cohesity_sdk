# MigrateCloneParams

Specifies the DB migration parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delay_secs** | **int** | Specifies when the migration of the oracle instance should be started after successful recovery. | [optional] 
**target_path_vec** | **List[str]** | Specifies the target paths to be used for DB migration. | [optional] 

## Example

```python
from cohesity_sdk.models.migrate_clone_params import MigrateCloneParams

# TODO update the JSON string below
json = "{}"
# create an instance of MigrateCloneParams from a JSON string
migrate_clone_params_instance = MigrateCloneParams.from_json(json)
# print the JSON string representation of the object
print(MigrateCloneParams.to_json())

# convert the object into a dict
migrate_clone_params_dict = migrate_clone_params_instance.to_dict()
# create an instance of MigrateCloneParams from a dict
migrate_clone_params_from_dict = MigrateCloneParams.from_dict(migrate_clone_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


