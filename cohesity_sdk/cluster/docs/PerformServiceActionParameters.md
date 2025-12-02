# PerformServiceActionParameters

Specifies perform service action parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Specifies the action. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.perform_service_action_parameters import PerformServiceActionParameters

# TODO update the JSON string below
json = "{}"
# create an instance of PerformServiceActionParameters from a JSON string
perform_service_action_parameters_instance = PerformServiceActionParameters.from_json(json)
# print the JSON string representation of the object
print(PerformServiceActionParameters.to_json())

# convert the object into a dict
perform_service_action_parameters_dict = perform_service_action_parameters_instance.to_dict()
# create an instance of PerformServiceActionParameters from a dict
perform_service_action_parameters_from_dict = PerformServiceActionParameters.from_dict(perform_service_action_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


