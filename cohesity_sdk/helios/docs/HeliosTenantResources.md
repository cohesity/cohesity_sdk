# HeliosTenantResources

A list of storage domains and sources assigned to a Tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**List[HeliosTenantClusterResources]**](HeliosTenantClusterResources.md) | THe list of assigned resources grouped by cluster Id. | [optional] 
**tenant_id** | **str** | Specifies the new tenant id associated with the api key. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_tenant_resources import HeliosTenantResources

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosTenantResources from a JSON string
helios_tenant_resources_instance = HeliosTenantResources.from_json(json)
# print the JSON string representation of the object
print(HeliosTenantResources.to_json())

# convert the object into a dict
helios_tenant_resources_dict = helios_tenant_resources_instance.to_dict()
# create an instance of HeliosTenantResources from a dict
helios_tenant_resources_from_dict = HeliosTenantResources.from_dict(helios_tenant_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


