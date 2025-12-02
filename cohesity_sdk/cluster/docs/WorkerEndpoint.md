# WorkerEndpoint

Definition of worker endpoint to which client should connect to access data and metadata of the object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | Specifies the end point of the worker which is combination of both endpoint and port number. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.worker_endpoint import WorkerEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of WorkerEndpoint from a JSON string
worker_endpoint_instance = WorkerEndpoint.from_json(json)
# print the JSON string representation of the object
print(WorkerEndpoint.to_json())

# convert the object into a dict
worker_endpoint_dict = worker_endpoint_instance.to_dict()
# create an instance of WorkerEndpoint from a dict
worker_endpoint_from_dict = WorkerEndpoint.from_dict(worker_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


