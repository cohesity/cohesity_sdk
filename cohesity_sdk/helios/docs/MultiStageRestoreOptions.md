# MultiStageRestoreOptions

Specifies the parameters related to multi stage Sql restore.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_auto_sync** | **bool** | Set this to true if you want to enable auto sync for multi stage restore. | [optional] 
**enable_multi_stage_restore** | **bool** | Set this to true if you are creating a multi-stage Sql restore task needed for features such as Hot-Standby. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.multi_stage_restore_options import MultiStageRestoreOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MultiStageRestoreOptions from a JSON string
multi_stage_restore_options_instance = MultiStageRestoreOptions.from_json(json)
# print the JSON string representation of the object
print(MultiStageRestoreOptions.to_json())

# convert the object into a dict
multi_stage_restore_options_dict = multi_stage_restore_options_instance.to_dict()
# create an instance of MultiStageRestoreOptions from a dict
multi_stage_restore_options_from_dict = MultiStageRestoreOptions.from_dict(multi_stage_restore_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


