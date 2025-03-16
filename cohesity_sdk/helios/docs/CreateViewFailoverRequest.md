# CreateViewFailoverRequest

Specifies the request parameters to create a view failover task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**planned_failover_params** | [**PlannedFailoverParams**](PlannedFailoverParams.md) | Specifies parameters to create a planned failover. | [optional] 
**type** | **str** | Specifies the failover type.&lt;br&gt; &#39;Planned&#39; indicates this is a planned failover.&lt;br&gt; &#39;Unplanned&#39; indicates this is an unplanned failover, which is used when source cluster is down. | 
**unplanned_failover_params** | [**UnplannedFailoverParams**](UnplannedFailoverParams.md) | Specifies parameters to create an unplanned failover. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.create_view_failover_request import CreateViewFailoverRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateViewFailoverRequest from a JSON string
create_view_failover_request_instance = CreateViewFailoverRequest.from_json(json)
# print the JSON string representation of the object
print(CreateViewFailoverRequest.to_json())

# convert the object into a dict
create_view_failover_request_dict = create_view_failover_request_instance.to_dict()
# create an instance of CreateViewFailoverRequest from a dict
create_view_failover_request_from_dict = CreateViewFailoverRequest.from_dict(create_view_failover_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


