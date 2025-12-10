# TenantDeactivationError

Specifies the error object during tenant deactivation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Specifies the error message. | [optional] 
**error_type** | **str** | Specifies the error type. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.tenant_deactivation_error import TenantDeactivationError

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDeactivationError from a JSON string
tenant_deactivation_error_instance = TenantDeactivationError.from_json(json)
# print the JSON string representation of the object
print(TenantDeactivationError.to_json())

# convert the object into a dict
tenant_deactivation_error_dict = tenant_deactivation_error_instance.to_dict()
# create an instance of TenantDeactivationError from a dict
tenant_deactivation_error_from_dict = TenantDeactivationError.from_dict(tenant_deactivation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


