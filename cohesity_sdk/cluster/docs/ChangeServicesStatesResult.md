# ChangeServicesStatesResult

Specifies the result returned after a successful request to change the state of services running on the Cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Specifies a description of the result of the operation | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.change_services_states_result import ChangeServicesStatesResult

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeServicesStatesResult from a JSON string
change_services_states_result_instance = ChangeServicesStatesResult.from_json(json)
# print the JSON string representation of the object
print(ChangeServicesStatesResult.to_json())

# convert the object into a dict
change_services_states_result_dict = change_services_states_result_instance.to_dict()
# create an instance of ChangeServicesStatesResult from a dict
change_services_states_result_from_dict = ChangeServicesStatesResult.from_dict(change_services_states_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


