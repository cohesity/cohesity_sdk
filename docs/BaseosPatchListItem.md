# BaseosPatchListItem

Available Baseos patch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the baseos patch | [optional] 
**status** | **str** | Baseos patch application status | [optional] 

## Example

```python
from cohesity_sdk.models.baseos_patch_list_item import BaseosPatchListItem

# TODO update the JSON string below
json = "{}"
# create an instance of BaseosPatchListItem from a JSON string
baseos_patch_list_item_instance = BaseosPatchListItem.from_json(json)
# print the JSON string representation of the object
print(BaseosPatchListItem.to_json())

# convert the object into a dict
baseos_patch_list_item_dict = baseos_patch_list_item_instance.to_dict()
# create an instance of BaseosPatchListItem from a dict
baseos_patch_list_item_from_dict = BaseosPatchListItem.from_dict(baseos_patch_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


