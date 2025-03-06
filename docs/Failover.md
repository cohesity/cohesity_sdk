# Failover

Specifies the details of a failover.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int** | Specifies the failover complete time in micro seconds. | [optional] 
**error_message** | **str** | Specifies the error details if failover status is &#39;Failed&#39;. | [optional] 
**id** | **str** | Specifies the failover id. | [optional] 
**replications** | [**List[FailoverReplication]**](FailoverReplication.md) | Specifies a list of replications in this failover. | [optional] 
**start_time_usecs** | **int** | Specifies the failover start time in micro seconds. | [optional] 
**status** | **str** | Specifies the failover status. | [optional] 
**type** | **str** | Specifies the failover type. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.failover import Failover

# TODO update the JSON string below
json = "{}"
# create an instance of Failover from a JSON string
failover_instance = Failover.from_json(json)
# print the JSON string representation of the object
print(Failover.to_json())

# convert the object into a dict
failover_dict = failover_instance.to_dict()
# create an instance of Failover from a dict
failover_from_dict = Failover.from_dict(failover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


