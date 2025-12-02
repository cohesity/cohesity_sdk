# CreateDataAccessSessionRequestParams

Specifies the request parameters to create a data access session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_snapshot_info** | [**DataAccessSnapshotInfo**](DataAccessSnapshotInfo.md) |  | [optional] 
**current_snapshot_info** | [**DataAccessSnapshotInfo**](DataAccessSnapshotInfo.md) |  | 
**session_name** | **str** | Specifies a user friendly name of the data access session to be created. | 
**source_id** | **int** | Specifies the entity id of the source. | 

## Example

```python
from cohesity_sdk.cluster.models.create_data_access_session_request_params import CreateDataAccessSessionRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDataAccessSessionRequestParams from a JSON string
create_data_access_session_request_params_instance = CreateDataAccessSessionRequestParams.from_json(json)
# print the JSON string representation of the object
print(CreateDataAccessSessionRequestParams.to_json())

# convert the object into a dict
create_data_access_session_request_params_dict = create_data_access_session_request_params_instance.to_dict()
# create an instance of CreateDataAccessSessionRequestParams from a dict
create_data_access_session_request_params_from_dict = CreateDataAccessSessionRequestParams.from_dict(create_data_access_session_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


