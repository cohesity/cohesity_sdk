# InitFailoverRequest

Specifies the failover request parameters to initiate a failover.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_group_environment** | **str** | If this field is specified then protection groups will be looked up only for this specific environment | [optional] 
**replication_cluster** | [**FailoverReplicaCluster**](FailoverReplicaCluster.md) |  | [optional] 
**source_cluster** | [**FailoverSourceCluster**](FailoverSourceCluster.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.init_failover_request import InitFailoverRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InitFailoverRequest from a JSON string
init_failover_request_instance = InitFailoverRequest.from_json(json)
# print the JSON string representation of the object
print(InitFailoverRequest.to_json())

# convert the object into a dict
init_failover_request_dict = init_failover_request_instance.to_dict()
# create an instance of InitFailoverRequest from a dict
init_failover_request_from_dict = InitFailoverRequest.from_dict(init_failover_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


