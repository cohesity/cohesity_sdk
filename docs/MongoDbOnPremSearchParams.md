# MongoDbOnPremSearchParams

Parameters required to search Mongo DB on a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mongo_db_object_types** | **List[str]** | Specifies one or more MongoDB object types be searched. | 
**search_string** | **str** | Specifies the search string to search the MongoDB Objects | 
**source_ids** | **List[int]** | Specifies a list of source ids. Only files found in these sources will be returned. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.mongo_db_on_prem_search_params import MongoDbOnPremSearchParams

# TODO update the JSON string below
json = "{}"
# create an instance of MongoDbOnPremSearchParams from a JSON string
mongo_db_on_prem_search_params_instance = MongoDbOnPremSearchParams.from_json(json)
# print the JSON string representation of the object
print(MongoDbOnPremSearchParams.to_json())

# convert the object into a dict
mongo_db_on_prem_search_params_dict = mongo_db_on_prem_search_params_instance.to_dict()
# create an instance of MongoDbOnPremSearchParams from a dict
mongo_db_on_prem_search_params_from_dict = MongoDbOnPremSearchParams.from_dict(mongo_db_on_prem_search_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


