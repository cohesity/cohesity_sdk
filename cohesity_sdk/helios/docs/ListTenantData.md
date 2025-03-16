# ListTenantData

List of tenants and the clusters to which they belong.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenants** | [**List[HeliosTenant]**](HeliosTenant.md) | List of tenants and the clusters to which they belong. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.list_tenant_data import ListTenantData

# TODO update the JSON string below
json = "{}"
# create an instance of ListTenantData from a JSON string
list_tenant_data_instance = ListTenantData.from_json(json)
# print the JSON string representation of the object
print(ListTenantData.to_json())

# convert the object into a dict
list_tenant_data_dict = list_tenant_data_instance.to_dict()
# create an instance of ListTenantData from a dict
list_tenant_data_from_dict = ListTenantData.from_dict(list_tenant_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


