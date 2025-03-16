# CommonSourceRegistrationReponseParams

Specifies the parameters which are common between all Protection Source registrations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_status** | **str** | Specifies the status of the authentication during the registration of a Protection Source. &#39;Pending&#39; indicates the authentication is in progress. &#39;Scheduled&#39; indicates the authentication is scheduled. &#39;Finished&#39; indicates the authentication is completed. &#39;RefreshInProgress&#39; indicates the refresh is in progress. | [optional] [readonly] 
**last_refreshed_time_msecs** | **int** | Specifies the time when the source was last refreshed in milliseconds. | [optional] [readonly] 
**registration_time_msecs** | **int** | Specifies the time when the source was registered in milliseconds | [optional] [readonly] 
**advanced_configs** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the advanced configuration for a protection source. | [optional] 
**connection_id** | **int** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. This field will be depricated in future. Use connections field. | [optional] 
**connections** | [**List[ConnectionConfig]**](ConnectionConfig.md) | Specfies the list of connections for the source. | [optional] 
**connector_group_id** | **int** | Specifies the connector group id of connector groups. | [optional] 
**environment** | **str** | Specifies the environment type of the Protection Source. | [optional] 
**id** | **int** | Source Registration ID. This can be used to retrieve, edit or delete the source registration. | [optional] [readonly] 
**name** | **str** | The user specified name for this source. | [optional] 
**source_id** | **int** | ID of top level source object discovered after the registration. | [optional] [readonly] 
**source_info** | [**Object**](Object.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.common_source_registration_reponse_params import CommonSourceRegistrationReponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonSourceRegistrationReponseParams from a JSON string
common_source_registration_reponse_params_instance = CommonSourceRegistrationReponseParams.from_json(json)
# print the JSON string representation of the object
print(CommonSourceRegistrationReponseParams.to_json())

# convert the object into a dict
common_source_registration_reponse_params_dict = common_source_registration_reponse_params_instance.to_dict()
# create an instance of CommonSourceRegistrationReponseParams from a dict
common_source_registration_reponse_params_from_dict = CommonSourceRegistrationReponseParams.from_dict(common_source_registration_reponse_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


