# UnRegisterApplicationServersParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_environments** | **List[str]** | Specifies the types of applications such as &#39;kSQL&#39;, &#39;kExchange&#39;, &#39;kAD&#39; etc. running on the Protection Source. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.un_register_application_servers_params import UnRegisterApplicationServersParams

# TODO update the JSON string below
json = "{}"
# create an instance of UnRegisterApplicationServersParams from a JSON string
un_register_application_servers_params_instance = UnRegisterApplicationServersParams.from_json(json)
# print the JSON string representation of the object
print(UnRegisterApplicationServersParams.to_json())

# convert the object into a dict
un_register_application_servers_params_dict = un_register_application_servers_params_instance.to_dict()
# create an instance of UnRegisterApplicationServersParams from a dict
un_register_application_servers_params_from_dict = UnRegisterApplicationServersParams.from_dict(un_register_application_servers_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


