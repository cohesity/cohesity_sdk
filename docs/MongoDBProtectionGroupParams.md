# MongoDBProtectionGroupParams

Specifies the parameters for MongoDB Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_scale_concurrency** | **bool** | Specifies the flag to automatically scale number of concurrent IO Streams that will be created to exchange data with the cluster. | [optional] 
**bandwidth_mbps** | **int** | Specifies the maximum network bandwidth that each concurrent IO Stream can use for exchanging data with the cluster. | [optional] 
**concurrency** | **int** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. | [optional] 
**custom_source_name** | **str** | The user specified name for the Source on which this protection was run. | [optional] [readonly] 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**List[NoSqlProtectionGroupObjectParams]**](NoSqlProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**source_id** | **int** | Object ID of the Source on which this protection was run . | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the Source on which this protection was run. | [optional] [readonly] 
**cdp_info** | [**MongoDBCdpJobInfo**](MongoDBCdpJobInfo.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.mongo_db_protection_group_params import MongoDBProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of MongoDBProtectionGroupParams from a JSON string
mongo_db_protection_group_params_instance = MongoDBProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(MongoDBProtectionGroupParams.to_json())

# convert the object into a dict
mongo_db_protection_group_params_dict = mongo_db_protection_group_params_instance.to_dict()
# create an instance of MongoDBProtectionGroupParams from a dict
mongo_db_protection_group_params_from_dict = MongoDBProtectionGroupParams.from_dict(mongo_db_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


