# DisasterRecoveryOptions

Specifies the parameters that are needed for Disaster Recovery of a database to its production configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cleanup_original_db_files** | **bool** | Specifies whether to cleanup the original database files or to do precheck to ensure no conflicting files exists. Recovery will fail if there are any conflicting files. | [optional] 
**is_disaster_recovery** | **bool** | Specifies whether the recovery is of type Disaster Recovery. | [optional] 
**rename_database_asm_directory** | **bool** | Whether to rename the database ASM directory. If false, the adapter will leave the database files and continue with clone and migration of datafiles. This might cause extra files left behind on the Oracle host from the existing database instance. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.disaster_recovery_options import DisasterRecoveryOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DisasterRecoveryOptions from a JSON string
disaster_recovery_options_instance = DisasterRecoveryOptions.from_json(json)
# print the JSON string representation of the object
print(DisasterRecoveryOptions.to_json())

# convert the object into a dict
disaster_recovery_options_dict = disaster_recovery_options_instance.to_dict()
# create an instance of DisasterRecoveryOptions from a dict
disaster_recovery_options_from_dict = DisasterRecoveryOptions.from_dict(disaster_recovery_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


