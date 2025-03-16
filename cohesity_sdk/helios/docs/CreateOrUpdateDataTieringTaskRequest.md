# CreateOrUpdateDataTieringTaskRequest

Specifies the request to create or update a data tiering task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_policy** | [**ProtectionGroupAlertingPolicy**](ProtectionGroupAlertingPolicy.md) |  | [optional] 
**description** | **str** | Specifies a description of the data tiering task. | [optional] 
**name** | **str** | Specifies the name of the data tiering task. | 
**schedule** | [**DataTieringSchedule**](DataTieringSchedule.md) |  | [optional] 
**source** | [**DataTieringSource**](DataTieringSource.md) |  | [optional] 
**target** | [**DataTieringTarget**](DataTieringTarget.md) |  | [optional] 
**type** | **str** | Type of data tiering task. &#39;Downtier&#39; indicates downtiering task. &#39;Uptier&#39; indicates uptiering task. | 
**downtiering_policy** | [**DowntieringPolicy**](DowntieringPolicy.md) |  | [optional] 
**uptiering_policy** | [**UptieringPolicy**](UptieringPolicy.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.create_or_update_data_tiering_task_request import CreateOrUpdateDataTieringTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateDataTieringTaskRequest from a JSON string
create_or_update_data_tiering_task_request_instance = CreateOrUpdateDataTieringTaskRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateDataTieringTaskRequest.to_json())

# convert the object into a dict
create_or_update_data_tiering_task_request_dict = create_or_update_data_tiering_task_request_instance.to_dict()
# create an instance of CreateOrUpdateDataTieringTaskRequest from a dict
create_or_update_data_tiering_task_request_from_dict = CreateOrUpdateDataTieringTaskRequest.from_dict(create_or_update_data_tiering_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


