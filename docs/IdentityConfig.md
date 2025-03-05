# IdentityConfig

Identity Provider Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Specifies domain of idp configuration | 
**id** | **int** | Specifies the ID of the IDP. | [optional] [readonly] 
**identity_provider_type** | **str** | Specifies the type of identity provider. | 
**is_enabled** | **bool** | Specifies a flag to enable or disable this idp service. When it is set to true, idp service is enabled. When it is set to false, idp service is disabled. By defaut idp is enabled i.e the value is true. | [optional] [default to True]
**last_modified_timestamp_usecs** | **int** | Specifies the last time this configuration was modified in microseconds since the epoch. This is may be specified for PUT operations to prevent stale requests from being written. If it is specified during a PUT operation then the request will be rejected if the specified time does not match the actual last modified time. | [optional] 
**o_auth2_params** | [**OAuth2Provider**](OAuth2Provider.md) |  | [optional] 
**open_id_connect_params** | [**OpenIdProvider**](OpenIdProvider.md) |  | [optional] 
**tenant_id** | **str** | Specifies the tenant id if the idp is configured for a tenant. If this is not set, this idp configuration is used for the cluster level users and for all users of tenants not having an idp configuration. | [optional] 

## Example

```python
from cohesity_sdk.models.identity_config import IdentityConfig

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityConfig from a JSON string
identity_config_instance = IdentityConfig.from_json(json)
# print the JSON string representation of the object
print(IdentityConfig.to_json())

# convert the object into a dict
identity_config_dict = identity_config_instance.to_dict()
# create an instance of IdentityConfig from a dict
identity_config_from_dict = IdentityConfig.from_dict(identity_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


