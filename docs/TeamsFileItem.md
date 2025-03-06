# TeamsFileItem

Specifies a M365 Teams channel file item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_time_secs** | **int** | Specifies the Unix timestamp epoch in seconds at which this item is created. | [optional] 
**drive_name** | **str** | Specifies the name of the drive location for this file. | [optional] 
**file_type** | **str** | Specifies the file type. | [optional] 
**item_size** | **int** | Specifies the size in bytes for the indexed item. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.teams_file_item import TeamsFileItem

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsFileItem from a JSON string
teams_file_item_instance = TeamsFileItem.from_json(json)
# print the JSON string representation of the object
print(TeamsFileItem.to_json())

# convert the object into a dict
teams_file_item_dict = teams_file_item_instance.to_dict()
# create an instance of TeamsFileItem from a dict
teams_file_item_from_dict = TeamsFileItem.from_dict(teams_file_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


