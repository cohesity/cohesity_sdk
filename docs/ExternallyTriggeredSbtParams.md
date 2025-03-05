# ExternallyTriggeredSbtParams

Specifies SBT paramters for the externally triggered job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_view** | **str** | Specifies the catalog view for the SBT backup. | [optional] 

## Example

```python
from cohesity_sdk.models.externally_triggered_sbt_params import ExternallyTriggeredSbtParams

# TODO update the JSON string below
json = "{}"
# create an instance of ExternallyTriggeredSbtParams from a JSON string
externally_triggered_sbt_params_instance = ExternallyTriggeredSbtParams.from_json(json)
# print the JSON string representation of the object
print(ExternallyTriggeredSbtParams.to_json())

# convert the object into a dict
externally_triggered_sbt_params_dict = externally_triggered_sbt_params_instance.to_dict()
# create an instance of ExternallyTriggeredSbtParams from a dict
externally_triggered_sbt_params_from_dict = ExternallyTriggeredSbtParams.from_dict(externally_triggered_sbt_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


