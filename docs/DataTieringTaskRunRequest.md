# DataTieringTaskRunRequest

Specifies the request to run tiering task once.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shares** | [**List[DataTieringShareInfo]**](DataTieringShareInfo.md) | Specifies the list of shares to tier. | [optional] 
**uptier_path** | **str** | Only applicable for uptiering tasks. Ignore the uptiering policy and uptier the directory pointed by the &#39;uptierPath&#39;. If path is &#39;/&#39;, then uptier everything.  This is a global property which will be applied to all shares by default. This can be overriden by specifying uptierPath for each share. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.data_tiering_task_run_request import DataTieringTaskRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataTieringTaskRunRequest from a JSON string
data_tiering_task_run_request_instance = DataTieringTaskRunRequest.from_json(json)
# print the JSON string representation of the object
print(DataTieringTaskRunRequest.to_json())

# convert the object into a dict
data_tiering_task_run_request_dict = data_tiering_task_run_request_instance.to_dict()
# create an instance of DataTieringTaskRunRequest from a dict
data_tiering_task_run_request_from_dict = DataTieringTaskRunRequest.from_dict(data_tiering_task_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


