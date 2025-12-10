# DB2ProtectionGroupParams

Specifies parameters related to the DB2 Protection job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_job_arguments** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the map of custom arguments to be supplied to the various backup scripts. | [optional] 
**concurrency** | **int** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. If not specified, the default value is taken as 1. | [optional] [default to 8]
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**mounts** | **int** | Specifies the maximum number of view mounts per host. If not specified, the default value is taken as 1. | [optional] [default to 1]
**objects** | [**List[UdaProtectionGroupObjectParams]**](UdaProtectionGroupObjectParams.md) | Specifies a list of fully qualified names of the objects to be protected. | 
**source_id** | **int** | Specifies the source Id of the objects to be protected. | 

## Example

```python
from cohesity_sdk.cluster.models.db2_protection_group_params import DB2ProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of DB2ProtectionGroupParams from a JSON string
db2_protection_group_params_instance = DB2ProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(DB2ProtectionGroupParams.to_json())

# convert the object into a dict
db2_protection_group_params_dict = db2_protection_group_params_instance.to_dict()
# create an instance of DB2ProtectionGroupParams from a dict
db2_protection_group_params_from_dict = DB2ProtectionGroupParams.from_dict(db2_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


