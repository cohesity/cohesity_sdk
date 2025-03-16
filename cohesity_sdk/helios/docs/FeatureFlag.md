# FeatureFlag

Describes the feature flag struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_approved** | **bool** | Bool to approval status of feature flag. | [optional] 
**is_ui_feature** | **bool** | Bool to denote if it&#39;s a UI feature. | [optional] 
**name** | **str** | Name of the feature flag. | [optional] 
**reason** | **str** | Reason for the feature flag override status. | [optional] 
**timestamp** | **int** | Timestamp in secs when the override is done. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.feature_flag import FeatureFlag

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureFlag from a JSON string
feature_flag_instance = FeatureFlag.from_json(json)
# print the JSON string representation of the object
print(FeatureFlag.to_json())

# convert the object into a dict
feature_flag_dict = feature_flag_instance.to_dict()
# create an instance of FeatureFlag from a dict
feature_flag_from_dict = FeatureFlag.from_dict(feature_flag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


