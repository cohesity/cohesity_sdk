# MongodbOpsManagerParams

Specifies the recovery options specific to MongoDB environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**MongodbNewOpsManagerConfig**](MongodbNewOpsManagerConfig.md) |  | [optional] 
**objects** | [**List[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. | 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 
**staging_directory** | **str** | Specifies the staging directory path for PIT recovery. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.mongodb_ops_manager_params import MongodbOpsManagerParams

# TODO update the JSON string below
json = "{}"
# create an instance of MongodbOpsManagerParams from a JSON string
mongodb_ops_manager_params_instance = MongodbOpsManagerParams.from_json(json)
# print the JSON string representation of the object
print(MongodbOpsManagerParams.to_json())

# convert the object into a dict
mongodb_ops_manager_params_dict = mongodb_ops_manager_params_instance.to_dict()
# create an instance of MongodbOpsManagerParams from a dict
mongodb_ops_manager_params_from_dict = MongodbOpsManagerParams.from_dict(mongodb_ops_manager_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


