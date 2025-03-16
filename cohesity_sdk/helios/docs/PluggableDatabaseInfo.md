# PluggableDatabaseInfo

Specifies the information about Pluggable databases.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_id** | **str** | Specifies the database Id of the Pluggable DB. | [optional] 
**database_name** | **str** | Specifies the name of the Pluggable DB. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.pluggable_database_info import PluggableDatabaseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PluggableDatabaseInfo from a JSON string
pluggable_database_info_instance = PluggableDatabaseInfo.from_json(json)
# print the JSON string representation of the object
print(PluggableDatabaseInfo.to_json())

# convert the object into a dict
pluggable_database_info_dict = pluggable_database_info_instance.to_dict()
# create an instance of PluggableDatabaseInfo from a dict
pluggable_database_info_from_dict = PluggableDatabaseInfo.from_dict(pluggable_database_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


