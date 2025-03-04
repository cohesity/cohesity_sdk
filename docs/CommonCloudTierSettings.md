# CommonCloudTierSettings

Specifies the common settings required for configuring cloud tiering.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_after** | **int** | Specifies the time period after which the backup will be moved from current tier to next tier. | [optional] 
**move_after_unit** | **str** | Specifies the unit for moving the data from current tier to next tier. This unit will be a base unit for the &#39;moveAfter&#39; field specified below. | [optional] 

## Example

```python
from cohesity_sdk.models.common_cloud_tier_settings import CommonCloudTierSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CommonCloudTierSettings from a JSON string
common_cloud_tier_settings_instance = CommonCloudTierSettings.from_json(json)
# print the JSON string representation of the object
print(CommonCloudTierSettings.to_json())

# convert the object into a dict
common_cloud_tier_settings_dict = common_cloud_tier_settings_instance.to_dict()
# create an instance of CommonCloudTierSettings from a dict
common_cloud_tier_settings_from_dict = CommonCloudTierSettings.from_dict(common_cloud_tier_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


