# OracleRecoveryValidationInfo

Specifies information related to Oracle Recovery Validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_dummy_instance** | **bool** | Specifies whether we will be creating a dummy oracle instance to run the validations. Generally if source and target location are different we create a dummy oracle instance else we use the source db. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.oracle_recovery_validation_info import OracleRecoveryValidationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OracleRecoveryValidationInfo from a JSON string
oracle_recovery_validation_info_instance = OracleRecoveryValidationInfo.from_json(json)
# print the JSON string representation of the object
print(OracleRecoveryValidationInfo.to_json())

# convert the object into a dict
oracle_recovery_validation_info_dict = oracle_recovery_validation_info_instance.to_dict()
# create an instance of OracleRecoveryValidationInfo from a dict
oracle_recovery_validation_info_from_dict = OracleRecoveryValidationInfo.from_dict(oracle_recovery_validation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


