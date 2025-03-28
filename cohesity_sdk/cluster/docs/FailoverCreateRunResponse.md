# FailoverCreateRunResponse

Specifies the response upon creating a special run during failover workflow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failover_id** | **str** | Specifies the unique failover Id which will be generated by orchestrator. This Id will be used to uniquely identify current failover operation. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.failover_create_run_response import FailoverCreateRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FailoverCreateRunResponse from a JSON string
failover_create_run_response_instance = FailoverCreateRunResponse.from_json(json)
# print the JSON string representation of the object
print(FailoverCreateRunResponse.to_json())

# convert the object into a dict
failover_create_run_response_dict = failover_create_run_response_instance.to_dict()
# create an instance of FailoverCreateRunResponse from a dict
failover_create_run_response_from_dict = FailoverCreateRunResponse.from_dict(failover_create_run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


