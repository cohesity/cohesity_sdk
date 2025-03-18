# AwsAgentProtectionGroupParams

Specifies the parameters which are specific to AWS related Protection Groups using cohesity protection-service installed on EC2 instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_consistent_snapshot** | **bool** | Specifies whether or not to quiesce apps and the file system in order to take app consistent snapshots. If not specified or false then snapshots will not be app consistent. | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**objects** | [**List[AwsAgentProtectionGroupObjectParams]**](AwsAgentProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.aws_agent_protection_group_params import AwsAgentProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsAgentProtectionGroupParams from a JSON string
aws_agent_protection_group_params_instance = AwsAgentProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(AwsAgentProtectionGroupParams.to_json())

# convert the object into a dict
aws_agent_protection_group_params_dict = aws_agent_protection_group_params_instance.to_dict()
# create an instance of AwsAgentProtectionGroupParams from a dict
aws_agent_protection_group_params_from_dict = AwsAgentProtectionGroupParams.from_dict(aws_agent_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


