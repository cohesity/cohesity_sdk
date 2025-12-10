# CommonDataAccessSessionInformation

Common Data Access Session Information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_time_usecs** | **int** | Specifies the time at which the session was created. | [optional] [readonly] 
**last_modification_time_usecs** | **int** | Specifies the time at which the session was last modified. | [optional] [readonly] 
**name** | **str** | The name of the data access session. | [optional] 
**session_id** | **str** | Specifies the id of the data access session. | [optional] 
**status** | **str** | Specifies the status of the Data Access Session. Machine status such as Admitted/WaitingForArchiveDownload/ WaitingForResource/SetupInProgress/Ready/Finished | [optional] 
**worker_endpoints** | [**List[WorkerEndpoint]**](WorkerEndpoint.md) | Specifies the list of metadata worker endpoints. In case of more than one metadata point client can contact any metadata worker. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_data_access_session_information import CommonDataAccessSessionInformation

# TODO update the JSON string below
json = "{}"
# create an instance of CommonDataAccessSessionInformation from a JSON string
common_data_access_session_information_instance = CommonDataAccessSessionInformation.from_json(json)
# print the JSON string representation of the object
print(CommonDataAccessSessionInformation.to_json())

# convert the object into a dict
common_data_access_session_information_dict = common_data_access_session_information_instance.to_dict()
# create an instance of CommonDataAccessSessionInformation from a dict
common_data_access_session_information_from_dict = CommonDataAccessSessionInformation.from_dict(common_data_access_session_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


