# MongoDBOpsManagerProtectionGroupParams

Specifies parameters related to the Mongodb Physical Protection job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**convert_to_full_on_failure** | **bool** | Specifies the flag to convert incremental backup to full backup on node failure. | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**List[MongoDBOpsManagerProtectionGroupObjectParams]**](MongoDBOpsManagerProtectionGroupObjectParams.md) | Specifies the list of objects to be protected. | [optional] 
**preferred_backup_nodes** | **str** | Specifies the comma separated list of hostnames to take backup from; in the order of preference. If provided, these nodes will be preferred as a backup source. The hostnames MUST match the hostnames reported by OpsManager in cluster status result. | [optional] 
**preferred_node** | **str** | Specifies the preferred node for backup. | [optional] 
**source_id** | **int** | Object ID of the Source on which this protection was run . | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.mongo_db_ops_manager_protection_group_params import MongoDBOpsManagerProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of MongoDBOpsManagerProtectionGroupParams from a JSON string
mongo_db_ops_manager_protection_group_params_instance = MongoDBOpsManagerProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(MongoDBOpsManagerProtectionGroupParams.to_json())

# convert the object into a dict
mongo_db_ops_manager_protection_group_params_dict = mongo_db_ops_manager_protection_group_params_instance.to_dict()
# create an instance of MongoDBOpsManagerProtectionGroupParams from a dict
mongo_db_ops_manager_protection_group_params_from_dict = MongoDBOpsManagerProtectionGroupParams.from_dict(mongo_db_ops_manager_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


