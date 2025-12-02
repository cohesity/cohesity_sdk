# ChangeServicesStatesParams

Describes the parameters for changing services states of cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the action to take on the specified service | [optional] 
**services** | **List[Optional[str]]** | Specifies the list of services to take the specified action on. If none are specified, all Cluster services will be affected. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.change_services_states_params import ChangeServicesStatesParams

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeServicesStatesParams from a JSON string
change_services_states_params_instance = ChangeServicesStatesParams.from_json(json)
# print the JSON string representation of the object
print(ChangeServicesStatesParams.to_json())

# convert the object into a dict
change_services_states_params_dict = change_services_states_params_instance.to_dict()
# create an instance of ChangeServicesStatesParams from a dict
change_services_states_params_from_dict = ChangeServicesStatesParams.from_dict(change_services_states_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


