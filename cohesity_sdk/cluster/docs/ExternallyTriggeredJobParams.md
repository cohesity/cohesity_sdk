# ExternallyTriggeredJobParams

Specifies the externally triggered job paramters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_type** | **str** | Specifies the client type of the externally triggered backup job. | [optional] 
**sbt_params** | [**ExternallyTriggeredSbtParams**](ExternallyTriggeredSbtParams.md) |  | [optional] 
**tags** | **List[str]** | Specifies all the tags of the externally triggered job. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.externally_triggered_job_params import ExternallyTriggeredJobParams

# TODO update the JSON string below
json = "{}"
# create an instance of ExternallyTriggeredJobParams from a JSON string
externally_triggered_job_params_instance = ExternallyTriggeredJobParams.from_json(json)
# print the JSON string representation of the object
print(ExternallyTriggeredJobParams.to_json())

# convert the object into a dict
externally_triggered_job_params_dict = externally_triggered_job_params_instance.to_dict()
# create an instance of ExternallyTriggeredJobParams from a dict
externally_triggered_job_params_from_dict = ExternallyTriggeredJobParams.from_dict(externally_triggered_job_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


