# ClusterTenantConfigUpdateWithErrorError

Error description for cluster config update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Error message for the cluster. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.cluster_tenant_config_update_with_error_error import ClusterTenantConfigUpdateWithErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterTenantConfigUpdateWithErrorError from a JSON string
cluster_tenant_config_update_with_error_error_instance = ClusterTenantConfigUpdateWithErrorError.from_json(json)
# print the JSON string representation of the object
print(ClusterTenantConfigUpdateWithErrorError.to_json())

# convert the object into a dict
cluster_tenant_config_update_with_error_error_dict = cluster_tenant_config_update_with_error_error_instance.to_dict()
# create an instance of ClusterTenantConfigUpdateWithErrorError from a dict
cluster_tenant_config_update_with_error_error_from_dict = ClusterTenantConfigUpdateWithErrorError.from_dict(cluster_tenant_config_update_with_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


