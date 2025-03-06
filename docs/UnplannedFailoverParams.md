# UnplannedFailoverParams

Specifies parameters of an unplanned failover.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reverse_replication** | **bool** | Specifies whether a reverse replication needs to be set for the view on target cluster after failover. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.unplanned_failover_params import UnplannedFailoverParams

# TODO update the JSON string below
json = "{}"
# create an instance of UnplannedFailoverParams from a JSON string
unplanned_failover_params_instance = UnplannedFailoverParams.from_json(json)
# print the JSON string representation of the object
print(UnplannedFailoverParams.to_json())

# convert the object into a dict
unplanned_failover_params_dict = unplanned_failover_params_instance.to_dict()
# create an instance of UnplannedFailoverParams from a dict
unplanned_failover_params_from_dict = UnplannedFailoverParams.from_dict(unplanned_failover_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


