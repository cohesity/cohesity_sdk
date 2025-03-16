# UpdateDataTieringStateRequest

Specifies the parameters to perform an action on the data tiering groups for the specified Sources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the action to be performed on all the specified data tiering groups. &#39;Pause&#39;  specifies to pause. &#39;Resume&#39; specifies to resume. | 
**ids** | **List[str]** | Specifies a list of data tiering groups ids for which the state should change. | 

## Example

```python
from cohesity_sdk.helios.models.update_data_tiering_state_request import UpdateDataTieringStateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDataTieringStateRequest from a JSON string
update_data_tiering_state_request_instance = UpdateDataTieringStateRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDataTieringStateRequest.to_json())

# convert the object into a dict
update_data_tiering_state_request_dict = update_data_tiering_state_request_instance.to_dict()
# create an instance of UpdateDataTieringStateRequest from a dict
update_data_tiering_state_request_from_dict = UpdateDataTieringStateRequest.from_dict(update_data_tiering_state_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


