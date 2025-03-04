# MongodbParams

Specifies the recovery options specific to MongoDB environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_mongodb_params** | [**RecoverMongodbParams**](RecoverMongodbParams.md) |  | 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.models.mongodb_params import MongodbParams

# TODO update the JSON string below
json = "{}"
# create an instance of MongodbParams from a JSON string
mongodb_params_instance = MongodbParams.from_json(json)
# print the JSON string representation of the object
print(MongodbParams.to_json())

# convert the object into a dict
mongodb_params_dict = mongodb_params_instance.to_dict()
# create an instance of MongodbParams from a dict
mongodb_params_from_dict = MongodbParams.from_dict(mongodb_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


