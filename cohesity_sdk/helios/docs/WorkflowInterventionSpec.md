# WorkflowInterventionSpec

Specifies the intervention for each workflow type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intervention** | **str** | Specifies the intervention type for ongoing tasks. | 
**workflow_type** | **str** | Specifies the workflow type for which an intervention would be needed when maintenance mode begins | 

## Example

```python
from cohesity_sdk.helios.models.workflow_intervention_spec import WorkflowInterventionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowInterventionSpec from a JSON string
workflow_intervention_spec_instance = WorkflowInterventionSpec.from_json(json)
# print the JSON string representation of the object
print(WorkflowInterventionSpec.to_json())

# convert the object into a dict
workflow_intervention_spec_dict = workflow_intervention_spec_instance.to_dict()
# create an instance of WorkflowInterventionSpec from a dict
workflow_intervention_spec_from_dict = WorkflowInterventionSpec.from_dict(workflow_intervention_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


