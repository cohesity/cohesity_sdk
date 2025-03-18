# PrePostScriptParams

Specifies the params for pre and post scripts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_script** | [**CommonPrePostScriptParams**](CommonPrePostScriptParams.md) |  | [optional] 
**pre_script** | [**CommonPreBackupScriptParams**](CommonPreBackupScriptParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.pre_post_script_params import PrePostScriptParams

# TODO update the JSON string below
json = "{}"
# create an instance of PrePostScriptParams from a JSON string
pre_post_script_params_instance = PrePostScriptParams.from_json(json)
# print the JSON string representation of the object
print(PrePostScriptParams.to_json())

# convert the object into a dict
pre_post_script_params_dict = pre_post_script_params_instance.to_dict()
# create an instance of PrePostScriptParams from a dict
pre_post_script_params_from_dict = PrePostScriptParams.from_dict(pre_post_script_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


