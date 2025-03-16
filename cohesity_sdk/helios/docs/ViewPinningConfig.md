# ViewPinningConfig

Specifies the pinning config of a view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Specifies if view pinning is enabled. If set to true, view will be pinned to SSD and view data will be stored there. | 
**last_updated_timestamp_secs** | **int** | Specifies the timestamp when view pinning config is last updated. | [optional] [readonly] 
**pinned_time_secs** | **int** | Specifies the time to pin files after last access. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.view_pinning_config import ViewPinningConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ViewPinningConfig from a JSON string
view_pinning_config_instance = ViewPinningConfig.from_json(json)
# print the JSON string representation of the object
print(ViewPinningConfig.to_json())

# convert the object into a dict
view_pinning_config_dict = view_pinning_config_instance.to_dict()
# create an instance of ViewPinningConfig from a dict
view_pinning_config_from_dict = ViewPinningConfig.from_dict(view_pinning_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


