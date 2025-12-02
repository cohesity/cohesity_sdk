# IbmTenantMetadataParams

Specifies the additional metadata for the tenant that is specifically set by the external vendor of type 'IBM'.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Specifies the unique identifier of the IBM&#39;s account ID. | [optional] 
**crn** | **str** | Specifies the unique CRN associated with the tenant. | [optional] 
**custom_properties** | [**List[ExternalVendorCustomProperties]**](ExternalVendorCustomProperties.md) | Specifies the list of custom properties associated with the tenant. External vendors can choose to set any properties inside following list. Note that the fields set inside the following will not be available for direct filtering. API callers should make sure that no sensitive information such as passwords is sent in these fields. | [optional] 
**liveness_mode** | **str** | Specifies the current liveness mode of the tenant. This mode may change based on AZ failures when vendor chooses to failover or failback the tenants to other AZs. | [optional] 
**metrics_config** | [**IbmTenantMetricsConfig**](IbmTenantMetricsConfig.md) |  | [optional] 
**ownership_mode** | **str** | Specifies the current ownership mode for the tenant. The ownership of the tenant represents the active role for functioning of the tenant. | [optional] 
**plan_id** | **str** | Specifies the Plan Id associated with the tenant. This field is introduced for tracking purposes inside IBM enviournment. | [optional] 
**resource_group_id** | **str** | Specifies the Resource Group ID associated with the tenant. | [optional] 
**resource_instance_id** | **str** | Specifies the Resource Instance ID associated with the tenant. This field is introduced for tracking purposes inside IBM enviournment. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ibm_tenant_metadata_params import IbmTenantMetadataParams

# TODO update the JSON string below
json = "{}"
# create an instance of IbmTenantMetadataParams from a JSON string
ibm_tenant_metadata_params_instance = IbmTenantMetadataParams.from_json(json)
# print the JSON string representation of the object
print(IbmTenantMetadataParams.to_json())

# convert the object into a dict
ibm_tenant_metadata_params_dict = ibm_tenant_metadata_params_instance.to_dict()
# create an instance of IbmTenantMetadataParams from a dict
ibm_tenant_metadata_params_from_dict = IbmTenantMetadataParams.from_dict(ibm_tenant_metadata_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


