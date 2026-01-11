# ExternalVendorTenantMetadata

Specifies the additional metadata for the tenant that is specifically set by the external vendors who are responsible for managing tenants. This field will only applicable if tenant creation is happening for a specially provisioned clusters for external vendors.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str, none_type** | Specifies the type of the external vendor. The type specific parameters must be specified the provided type. | defaults to "IBM"
**ibm_tenant_metadata_params** | [**IbmTenantMetadataParams**](IbmTenantMetadataParams.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


