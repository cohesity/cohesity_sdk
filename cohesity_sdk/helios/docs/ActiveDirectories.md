# ActiveDirectories

Response of Active Directories.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_directories** | [**List[ActiveDirectory]**](ActiveDirectory.md) | A list of Active Directories. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.active_directories import ActiveDirectories

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDirectories from a JSON string
active_directories_instance = ActiveDirectories.from_json(json)
# print the JSON string representation of the object
print(ActiveDirectories.to_json())

# convert the object into a dict
active_directories_dict = active_directories_instance.to_dict()
# create an instance of ActiveDirectories from a dict
active_directories_from_dict = ActiveDirectories.from_dict(active_directories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


