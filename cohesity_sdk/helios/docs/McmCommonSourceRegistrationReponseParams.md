# McmCommonSourceRegistrationReponseParams

Specifies the parameters which are common between all Protection Source registrations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the cluster id. | [optional] [readonly] 
**cluster_incarnation_id** | **int** | Specifies the cluster incarnation id. | [optional] [readonly] 
**connection_id** | **int** | Specifies the id of the connection from where this source is reachable. | [optional] 
**connections** | [**List[ConnectionConfig]**](ConnectionConfig.md) | Specifies the list of connections associated with this source. | [optional] 
**connector_group_id** | **int** | Specifies the connector group id of connector groups. | [optional] 
**environment** | **str** | Specifies the environment type of the Protection Source. | [optional] 
**id** | **str** | Source Registration ID. This can be used to retrieve, edit or delete the source registration. | [optional] [readonly] 
**name** | **str** | The user specified name for this source. | [optional] [readonly] 
**region_id** | **str** | Specifies the region id. | [optional] [readonly] 
**source_id** | **str** | ID of top level source object discovered after the registration. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.mcm_common_source_registration_reponse_params import McmCommonSourceRegistrationReponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of McmCommonSourceRegistrationReponseParams from a JSON string
mcm_common_source_registration_reponse_params_instance = McmCommonSourceRegistrationReponseParams.from_json(json)
# print the JSON string representation of the object
print(McmCommonSourceRegistrationReponseParams.to_json())

# convert the object into a dict
mcm_common_source_registration_reponse_params_dict = mcm_common_source_registration_reponse_params_instance.to_dict()
# create an instance of McmCommonSourceRegistrationReponseParams from a dict
mcm_common_source_registration_reponse_params_from_dict = McmCommonSourceRegistrationReponseParams.from_dict(mcm_common_source_registration_reponse_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


