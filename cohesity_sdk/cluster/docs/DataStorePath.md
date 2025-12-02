# DataStorePath

Specifies the datastore path of restore config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elastic** | **str** | Specifies the elastic datastore path. | [optional] 
**mongo** | **str** | Specifies the mongo datastore path. | [optional] 
**postgres** | **str** | Specifies the postgres datastore path. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.data_store_path import DataStorePath

# TODO update the JSON string below
json = "{}"
# create an instance of DataStorePath from a JSON string
data_store_path_instance = DataStorePath.from_json(json)
# print the JSON string representation of the object
print(DataStorePath.to_json())

# convert the object into a dict
data_store_path_dict = data_store_path_instance.to_dict()
# create an instance of DataStorePath from a dict
data_store_path_from_dict = DataStorePath.from_dict(data_store_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


