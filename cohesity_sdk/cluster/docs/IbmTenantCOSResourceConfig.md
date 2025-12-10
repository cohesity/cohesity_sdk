# IbmTenantCOSResourceConfig

Specifies the details of COS resource configuration required for posting metrics and trackinb billing information for IBM tenants.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_url** | **str** | Specifies the resource COS resource configuration endpoint that will be used for fetching bucket usage for a given tenant. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ibm_tenant_cos_resource_config import IbmTenantCOSResourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of IbmTenantCOSResourceConfig from a JSON string
ibm_tenant_cos_resource_config_instance = IbmTenantCOSResourceConfig.from_json(json)
# print the JSON string representation of the object
print(IbmTenantCOSResourceConfig.to_json())

# convert the object into a dict
ibm_tenant_cos_resource_config_dict = ibm_tenant_cos_resource_config_instance.to_dict()
# create an instance of IbmTenantCOSResourceConfig from a dict
ibm_tenant_cos_resource_config_from_dict = IbmTenantCOSResourceConfig.from_dict(ibm_tenant_cos_resource_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


