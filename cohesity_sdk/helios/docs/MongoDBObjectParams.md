# MongoDBObjectParams

Specifies the parameters for MongoDB object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdp_info** | [**CdpSourceObjectInfo**](CdpSourceObjectInfo.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mongo_db_object_params import MongoDBObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of MongoDBObjectParams from a JSON string
mongo_db_object_params_instance = MongoDBObjectParams.from_json(json)
# print the JSON string representation of the object
print(MongoDBObjectParams.to_json())

# convert the object into a dict
mongo_db_object_params_dict = mongo_db_object_params_instance.to_dict()
# create an instance of MongoDBObjectParams from a dict
mongo_db_object_params_from_dict = MongoDBObjectParams.from_dict(mongo_db_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


