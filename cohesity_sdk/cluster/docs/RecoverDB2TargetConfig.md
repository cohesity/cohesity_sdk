# RecoverDB2TargetConfig

Specifies the target object parameters to recover DB2.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_db2_target_config import RecoverDB2TargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverDB2TargetConfig from a JSON string
recover_db2_target_config_instance = RecoverDB2TargetConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverDB2TargetConfig.to_json())

# convert the object into a dict
recover_db2_target_config_dict = recover_db2_target_config_instance.to_dict()
# create an instance of RecoverDB2TargetConfig from a dict
recover_db2_target_config_from_dict = RecoverDB2TargetConfig.from_dict(recover_db2_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


