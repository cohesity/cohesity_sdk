# ConfigItem

Specifies config item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key of the config item | [optional] 
**value** | **str** | Value of the config item | [optional] 

## Example

```python
from cohesity_sdk.helios.models.config_item import ConfigItem

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigItem from a JSON string
config_item_instance = ConfigItem.from_json(json)
# print the JSON string representation of the object
print(ConfigItem.to_json())

# convert the object into a dict
config_item_dict = config_item_instance.to_dict()
# create an instance of ConfigItem from a dict
config_item_from_dict = ConfigItem.from_dict(config_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


