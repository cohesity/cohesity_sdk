# CommonSourceRegistrationRequestParams

Specifies the parameters which are common between all Protection Source registrations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_configs** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the advanced configuration for a protection source. | [optional] 
**async_registration** | **bool** | Indicates whether the source should be registered asynchronously. Currently supported only for VMware sources. | [optional] 
**connection_id** | **int** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. | [optional] 
**connections** | [**List[ConnectionConfig]**](ConnectionConfig.md) | Specfies the list of connections for the source. | [optional] 
**connector_group_id** | **int** | Specifies the connector group id of connector groups. | [optional] 
**data_source_connection_id** | **str** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. Also, this is the &#39;string&#39; of connectionId. This property was added to accommodate for ID values that exceed 2^53 - 1, which is the max value for which JS maintains precision. | [optional] 
**encryption_key** | **str** | Specifies the key that user has encrypted the credential with. | [optional] 
**environment** | **str** | Specifies the environment type of the Protection Source. | 
**is_internal_encrypted** | **bool** | Specifies if credentials are encrypted by internal key. | [optional] 
**name** | **str** | A user specified name for this source. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_source_registration_request_params import CommonSourceRegistrationRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonSourceRegistrationRequestParams from a JSON string
common_source_registration_request_params_instance = CommonSourceRegistrationRequestParams.from_json(json)
# print the JSON string representation of the object
print(CommonSourceRegistrationRequestParams.to_json())

# convert the object into a dict
common_source_registration_request_params_dict = common_source_registration_request_params_instance.to_dict()
# create an instance of CommonSourceRegistrationRequestParams from a dict
common_source_registration_request_params_from_dict = CommonSourceRegistrationRequestParams.from_dict(common_source_registration_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


