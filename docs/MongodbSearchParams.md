# MongodbSearchParams

Specifies the parameters which are specific for searching MongoDB objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mongo_db_object_types** | **List[str]** | Specifies one or more MongoDB object types be searched. | 
**search_string** | **str** | Specifies the search string to search the MongoDB Objects | 

## Example

```python
from cohesity_sdk.cluster.models.mongodb_search_params import MongodbSearchParams

# TODO update the JSON string below
json = "{}"
# create an instance of MongodbSearchParams from a JSON string
mongodb_search_params_instance = MongodbSearchParams.from_json(json)
# print the JSON string representation of the object
print(MongodbSearchParams.to_json())

# convert the object into a dict
mongodb_search_params_dict = mongodb_search_params_instance.to_dict()
# create an instance of MongodbSearchParams from a dict
mongodb_search_params_from_dict = MongodbSearchParams.from_dict(mongodb_search_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


