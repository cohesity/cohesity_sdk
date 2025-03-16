# HdfsProtectionGroupParams

Specifies the parameters for HDFS Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth_mbps** | **int** | Specifies the maximum network bandwidth that each concurrent IO Stream can use for exchanging data with the cluster. | [optional] 
**concurrency** | **int** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. | [optional] 
**exclude_paths** | **List[str]** | Specifies the paths to be excluded in the Protection Group. excludePaths will ovrride includePaths. | [optional] 
**hdfs_source_id** | **int** | The object ID of the HDFS source for this protection group. | 
**include_paths** | **List[str]** | Specifies the paths to be included in the Protection Group. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**source_id** | **int** | Object ID of the Source on which this protection was run . | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the Source on which this protection was run. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.hdfs_protection_group_params import HdfsProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of HdfsProtectionGroupParams from a JSON string
hdfs_protection_group_params_instance = HdfsProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(HdfsProtectionGroupParams.to_json())

# convert the object into a dict
hdfs_protection_group_params_dict = hdfs_protection_group_params_instance.to_dict()
# create an instance of HdfsProtectionGroupParams from a dict
hdfs_protection_group_params_from_dict = HdfsProtectionGroupParams.from_dict(hdfs_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


