# PlannedFailoverParams

Specifies parameters of a planned failover.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prepare_planned_failver_params** | [**PreparePlannedFailverParams**](PreparePlannedFailverParams.md) | Specifies parameters of preparation of a planned failover. | [optional] 
**type** | **str** | Spcifies the planned failover type.&lt;br&gt; &#39;Prepare&#39; indicates this is a preparation for failover.&lt;br&gt; &#39;Finalize&#39; indicates this is finalization of failover. After this is done, the view can be used as source view. | 

## Example

```python
from cohesity_sdk.helios.models.planned_failover_params import PlannedFailoverParams

# TODO update the JSON string below
json = "{}"
# create an instance of PlannedFailoverParams from a JSON string
planned_failover_params_instance = PlannedFailoverParams.from_json(json)
# print the JSON string representation of the object
print(PlannedFailoverParams.to_json())

# convert the object into a dict
planned_failover_params_dict = planned_failover_params_instance.to_dict()
# create an instance of PlannedFailoverParams from a dict
planned_failover_params_from_dict = PlannedFailoverParams.from_dict(planned_failover_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


