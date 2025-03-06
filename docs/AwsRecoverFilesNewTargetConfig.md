# AwsRecoverFilesNewTargetConfig

Specifies the configuration for recovering files and folders to a new target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_path** | **str** | Specifies the path location to recover files to. | 
**target_vm** | [**RecoverTarget**](RecoverTarget.md) |  | 
**target_vm_credentials** | [**Credentials**](Credentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_recover_files_new_target_config import AwsRecoverFilesNewTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AwsRecoverFilesNewTargetConfig from a JSON string
aws_recover_files_new_target_config_instance = AwsRecoverFilesNewTargetConfig.from_json(json)
# print the JSON string representation of the object
print(AwsRecoverFilesNewTargetConfig.to_json())

# convert the object into a dict
aws_recover_files_new_target_config_dict = aws_recover_files_new_target_config_instance.to_dict()
# create an instance of AwsRecoverFilesNewTargetConfig from a dict
aws_recover_files_new_target_config_from_dict = AwsRecoverFilesNewTargetConfig.from_dict(aws_recover_files_new_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


