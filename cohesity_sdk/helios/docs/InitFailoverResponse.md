# InitFailoverResponse

Specifies the response after succesfully initiating the failover request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replica_to_source_objects** | [**List[SourceReplicaObject]**](SourceReplicaObject.md) | Specifies the list of corrosponding source objects mapped with replica objects provided at the time of initiating failover request. | [optional] 
**source_cluster_info** | [**FailoverSourceCluster**](FailoverSourceCluster.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.init_failover_response import InitFailoverResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InitFailoverResponse from a JSON string
init_failover_response_instance = InitFailoverResponse.from_json(json)
# print the JSON string representation of the object
print(InitFailoverResponse.to_json())

# convert the object into a dict
init_failover_response_dict = init_failover_response_instance.to_dict()
# create an instance of InitFailoverResponse from a dict
init_failover_response_from_dict = InitFailoverResponse.from_dict(init_failover_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


