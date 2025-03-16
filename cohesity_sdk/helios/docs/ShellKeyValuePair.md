# ShellKeyValuePair

Specifies key value pairs of shell variables which defines the restore shell environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Specifies the name of the shell environment variable. | [optional] 
**value** | **str** | Specifies the value of the shell environment variable. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.shell_key_value_pair import ShellKeyValuePair

# TODO update the JSON string below
json = "{}"
# create an instance of ShellKeyValuePair from a JSON string
shell_key_value_pair_instance = ShellKeyValuePair.from_json(json)
# print the JSON string representation of the object
print(ShellKeyValuePair.to_json())

# convert the object into a dict
shell_key_value_pair_dict = shell_key_value_pair_instance.to_dict()
# create an instance of ShellKeyValuePair from a dict
shell_key_value_pair_from_dict = ShellKeyValuePair.from_dict(shell_key_value_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


