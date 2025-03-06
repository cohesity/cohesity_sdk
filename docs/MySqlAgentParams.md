# MySqlAgentParams

MySQL agent parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_type** | **str** | Specifies the type of installer. | 

## Example

```python
from cohesity_sdk.cluster.models.my_sql_agent_params import MySqlAgentParams

# TODO update the JSON string below
json = "{}"
# create an instance of MySqlAgentParams from a JSON string
my_sql_agent_params_instance = MySqlAgentParams.from_json(json)
# print the JSON string representation of the object
print(MySqlAgentParams.to_json())

# convert the object into a dict
my_sql_agent_params_dict = my_sql_agent_params_instance.to_dict()
# create an instance of MySqlAgentParams from a dict
my_sql_agent_params_from_dict = MySqlAgentParams.from_dict(my_sql_agent_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


