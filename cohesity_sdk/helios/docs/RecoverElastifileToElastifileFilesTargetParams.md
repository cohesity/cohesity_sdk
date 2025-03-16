# RecoverElastifileToElastifileFilesTargetParams

Specifies the params of the Elastifile recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverOtherNasToElastifileFilesTargetParams**](RecoverOtherNasToElastifileFilesTargetParams.md) | Specifies the new destination Source configuration parameters where the files will be recovered. This is mandatory if recoverToNewSource is set to true. | [optional] 
**original_source_config** | [**OriginalElastifileFilesTargetParams**](OriginalElastifileFilesTargetParams.md) | Specifies the Source configuration if files are being recovered to original Source. If not specified, all the configuration parameters will be retained. | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or the original Elastifile target. | 

## Example

```python
from cohesity_sdk.helios.models.recover_elastifile_to_elastifile_files_target_params import RecoverElastifileToElastifileFilesTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverElastifileToElastifileFilesTargetParams from a JSON string
recover_elastifile_to_elastifile_files_target_params_instance = RecoverElastifileToElastifileFilesTargetParams.from_json(json)
# print the JSON string representation of the object
print(RecoverElastifileToElastifileFilesTargetParams.to_json())

# convert the object into a dict
recover_elastifile_to_elastifile_files_target_params_dict = recover_elastifile_to_elastifile_files_target_params_instance.to_dict()
# create an instance of RecoverElastifileToElastifileFilesTargetParams from a dict
recover_elastifile_to_elastifile_files_target_params_from_dict = RecoverElastifileToElastifileFilesTargetParams.from_dict(recover_elastifile_to_elastifile_files_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


