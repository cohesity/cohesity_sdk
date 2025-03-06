# CommonDataTieringTaskParams

Specifies the data tiering task details.

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

## Example

```python
from cohesity_sdk.cluster.models.common_data_tiering_task_params import CommonDataTieringTaskParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonDataTieringTaskParams from a JSON string
common_data_tiering_task_params_instance = CommonDataTieringTaskParams.from_json(json)
# print the JSON string representation of the object
print(CommonDataTieringTaskParams.to_json())

# convert the object into a dict
common_data_tiering_task_params_dict = common_data_tiering_task_params_instance.to_dict()
# create an instance of CommonDataTieringTaskParams from a dict
common_data_tiering_task_params_from_dict = CommonDataTieringTaskParams.from_dict(common_data_tiering_task_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


