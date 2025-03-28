# AwsAgentProtectionGroupObjectParams

Specifies the object parameters to create agent based AWS Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the virtual machine. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.aws_agent_protection_group_object_params import AwsAgentProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsAgentProtectionGroupObjectParams from a JSON string
aws_agent_protection_group_object_params_instance = AwsAgentProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(AwsAgentProtectionGroupObjectParams.to_json())

# convert the object into a dict
aws_agent_protection_group_object_params_dict = aws_agent_protection_group_object_params_instance.to_dict()
# create an instance of AwsAgentProtectionGroupObjectParams from a dict
aws_agent_protection_group_object_params_from_dict = AwsAgentProtectionGroupObjectParams.from_dict(aws_agent_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


