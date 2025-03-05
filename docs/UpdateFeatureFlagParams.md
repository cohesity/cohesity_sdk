# UpdateFeatureFlagParams

Describes update feature flag request params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clear** | **bool** | Clear any override status for the feature flag. | [optional] 
**is_approved** | **bool** | New override status for the feature flag. | [optional] 
**is_ui_feature** | **bool** | Bool to specify if it&#39;s UI feature flag. | [optional] 
**name** | **str** | Name of the feature flag that is to be updated. | [optional] 
**reason** | **str** | Reason for updating the feature flag override status. | [optional] 
**timestamp** | **int** | Specifies the timestamp of override operation. | [optional] 

## Example

```python
from cohesity_sdk.models.update_feature_flag_params import UpdateFeatureFlagParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFeatureFlagParams from a JSON string
update_feature_flag_params_instance = UpdateFeatureFlagParams.from_json(json)
# print the JSON string representation of the object
print(UpdateFeatureFlagParams.to_json())

# convert the object into a dict
update_feature_flag_params_dict = update_feature_flag_params_instance.to_dict()
# create an instance of UpdateFeatureFlagParams from a dict
update_feature_flag_params_from_dict = UpdateFeatureFlagParams.from_dict(update_feature_flag_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


