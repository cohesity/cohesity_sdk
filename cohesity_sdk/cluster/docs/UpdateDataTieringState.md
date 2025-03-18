# UpdateDataTieringState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_ids** | **List[str]** | Specifies a list of data tiering groups ids for which updation of state failed. | [optional] 
**successful_ids** | **List[str]** | Specifies a list of data tiering groups ids for which updation of state was successful. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.update_data_tiering_state import UpdateDataTieringState

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDataTieringState from a JSON string
update_data_tiering_state_instance = UpdateDataTieringState.from_json(json)
# print the JSON string representation of the object
print(UpdateDataTieringState.to_json())

# convert the object into a dict
update_data_tiering_state_dict = update_data_tiering_state_instance.to_dict()
# create an instance of UpdateDataTieringState from a dict
update_data_tiering_state_from_dict = UpdateDataTieringState.from_dict(update_data_tiering_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


