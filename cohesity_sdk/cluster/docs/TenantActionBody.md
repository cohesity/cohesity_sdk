# TenantActionBody

Specifies an action on the Tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the action which will be performed on the Tenant. | 

## Example

```python
from cohesity_sdk.cluster.models.tenant_action_body import TenantActionBody

# TODO update the JSON string below
json = "{}"
# create an instance of TenantActionBody from a JSON string
tenant_action_body_instance = TenantActionBody.from_json(json)
# print the JSON string representation of the object
print(TenantActionBody.to_json())

# convert the object into a dict
tenant_action_body_dict = tenant_action_body_instance.to_dict()
# create an instance of TenantActionBody from a dict
tenant_action_body_from_dict = TenantActionBody.from_dict(tenant_action_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


