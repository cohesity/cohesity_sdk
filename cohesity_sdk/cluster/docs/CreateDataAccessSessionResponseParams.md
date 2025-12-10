# CreateDataAccessSessionResponseParams

Create Data Access Session Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Specifies the id of the data access session. | 

## Example

```python
from cohesity_sdk.cluster.models.create_data_access_session_response_params import CreateDataAccessSessionResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDataAccessSessionResponseParams from a JSON string
create_data_access_session_response_params_instance = CreateDataAccessSessionResponseParams.from_json(json)
# print the JSON string representation of the object
print(CreateDataAccessSessionResponseParams.to_json())

# convert the object into a dict
create_data_access_session_response_params_dict = create_data_access_session_response_params_instance.to_dict()
# create an instance of CreateDataAccessSessionResponseParams from a dict
create_data_access_session_response_params_from_dict = CreateDataAccessSessionResponseParams.from_dict(create_data_access_session_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


