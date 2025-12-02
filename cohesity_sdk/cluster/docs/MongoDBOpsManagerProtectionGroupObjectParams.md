# MongoDBOpsManagerProtectionGroupObjectParams

Specifies the object identifier to create MongoDB Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | [optional] 
**name** | **str** | Specifies the fully qualified name of the object. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.mongo_db_ops_manager_protection_group_object_params import MongoDBOpsManagerProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of MongoDBOpsManagerProtectionGroupObjectParams from a JSON string
mongo_db_ops_manager_protection_group_object_params_instance = MongoDBOpsManagerProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(MongoDBOpsManagerProtectionGroupObjectParams.to_json())

# convert the object into a dict
mongo_db_ops_manager_protection_group_object_params_dict = mongo_db_ops_manager_protection_group_object_params_instance.to_dict()
# create an instance of MongoDBOpsManagerProtectionGroupObjectParams from a dict
mongo_db_ops_manager_protection_group_object_params_from_dict = MongoDBOpsManagerProtectionGroupObjectParams.from_dict(mongo_db_ops_manager_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


