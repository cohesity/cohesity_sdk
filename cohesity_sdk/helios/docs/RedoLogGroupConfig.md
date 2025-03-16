# RedoLogGroupConfig

Specifies Redo log group configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_members** | **List[str]** | Specifies list of members of this redo log group. | [optional] 
**member_prefix** | **str** | Specifies Log member name prefix. | [optional] 
**num_groups** | **int** | Specifies no. of redo log groups. | [optional] 
**size_m_bytes** | **int** | Specifies Size of the member in MB. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.redo_log_group_config import RedoLogGroupConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RedoLogGroupConfig from a JSON string
redo_log_group_config_instance = RedoLogGroupConfig.from_json(json)
# print the JSON string representation of the object
print(RedoLogGroupConfig.to_json())

# convert the object into a dict
redo_log_group_config_dict = redo_log_group_config_instance.to_dict()
# create an instance of RedoLogGroupConfig from a dict
redo_log_group_config_from_dict = RedoLogGroupConfig.from_dict(redo_log_group_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


