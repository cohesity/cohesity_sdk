# MongodbNewOpsManagerConfig

Specifies the new destination Source configuration where the Mongodb cluster will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | Specifies the Cluster id. | 
**org_id** | **str** | Specifies the Organization id. | 
**project_id** | **str** | Specifies the Project id. | 
**source_id** | **int** | Specifies the id of the parent source to recover. | 
**source_name** | **str** | Specifies the name of the target source. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.mongodb_new_ops_manager_config import MongodbNewOpsManagerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MongodbNewOpsManagerConfig from a JSON string
mongodb_new_ops_manager_config_instance = MongodbNewOpsManagerConfig.from_json(json)
# print the JSON string representation of the object
print(MongodbNewOpsManagerConfig.to_json())

# convert the object into a dict
mongodb_new_ops_manager_config_dict = mongodb_new_ops_manager_config_instance.to_dict()
# create an instance of MongodbNewOpsManagerConfig from a dict
mongodb_new_ops_manager_config_from_dict = MongodbNewOpsManagerConfig.from_dict(mongodb_new_ops_manager_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


