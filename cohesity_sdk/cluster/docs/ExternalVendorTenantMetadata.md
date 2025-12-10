# ExternalVendorTenantMetadata

Specifies the additional metadata for the tenant that is specifically set by the external vendors who are responsible for managing tenants. This field will only applicable if tenant creation is happening for a specially provisioned clusters for external vendors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ibm_tenant_metadata_params** | [**IbmTenantMetadataParams**](IbmTenantMetadataParams.md) |  | [optional] 
**type** | **str** | Specifies the type of the external vendor. The type specific parameters must be specified the provided type. | 

## Example

```python
from cohesity_sdk.cluster.models.external_vendor_tenant_metadata import ExternalVendorTenantMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalVendorTenantMetadata from a JSON string
external_vendor_tenant_metadata_instance = ExternalVendorTenantMetadata.from_json(json)
# print the JSON string representation of the object
print(ExternalVendorTenantMetadata.to_json())

# convert the object into a dict
external_vendor_tenant_metadata_dict = external_vendor_tenant_metadata_instance.to_dict()
# create an instance of ExternalVendorTenantMetadata from a dict
external_vendor_tenant_metadata_from_dict = ExternalVendorTenantMetadata.from_dict(external_vendor_tenant_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


