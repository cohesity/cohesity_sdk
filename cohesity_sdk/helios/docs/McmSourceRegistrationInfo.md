# McmSourceRegistrationInfo

Specifies the registration details and errors occured during registration of a protection source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **int** | Specifies the id of the connection from where this source is reachable. | [optional] 
**connections** | [**List[ConnectionConfig]**](ConnectionConfig.md) | Specifies the list of connections associated with this source. | [optional] 
**connector_group_id** | **int** | Specifies the connector group id of connector groups. | [optional] 
**last_refresh_time_usecs** | **int** | Specifies the registration time of the Source in Unix time epoch in microseconds. | [optional] 
**refresh_error** | **str** | Specifies the error detail occured during the refersh of a protection source. | [optional] 
**registration_error** | **str** | Specifies the error detail occured during the protection source registration. | [optional] 
**registration_time_usecs** | **int** | Specifies the registration time of the Source in Unix time epoch in microseconds. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_source_registration_info import McmSourceRegistrationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of McmSourceRegistrationInfo from a JSON string
mcm_source_registration_info_instance = McmSourceRegistrationInfo.from_json(json)
# print the JSON string representation of the object
print(McmSourceRegistrationInfo.to_json())

# convert the object into a dict
mcm_source_registration_info_dict = mcm_source_registration_info_instance.to_dict()
# create an instance of McmSourceRegistrationInfo from a dict
mcm_source_registration_info_from_dict = McmSourceRegistrationInfo.from_dict(mcm_source_registration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


