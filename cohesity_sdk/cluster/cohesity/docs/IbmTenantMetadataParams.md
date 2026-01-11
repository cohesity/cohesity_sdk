# IbmTenantMetadataParams

Specifies the additional metadata for the tenant that is specifically set by the external vendor of type 'IBM'.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str, none_type** | Specifies the unique identifier of the IBM&#39;s account ID. | [optional] 
**crn** | **str, none_type** | Specifies the unique CRN associated with the tenant. | [optional] 
**custom_properties** | [**[ExternalVendorCustomProperties], none_type**](ExternalVendorCustomProperties.md) | Specifies the list of custom properties associated with the tenant. External vendors can choose to set any properties inside following list. Note that the fields set inside the following will not be available for direct filtering. API callers should make sure that no sensitive information such as passwords is sent in these fields. | [optional] 
**liveness_mode** | **str, none_type** | Specifies the current liveness mode of the tenant. This mode may change based on AZ failures when vendor chooses to failover or failback the tenants to other AZs. | [optional] 
**metrics_config** | [**IbmTenantMetricsConfig**](IbmTenantMetricsConfig.md) |  | [optional] 
**ownership_mode** | **str, none_type** | Specifies the current ownership mode for the tenant. The ownership of the tenant represents the active role for functioning of the tenant. | [optional] 
**plan_id** | **str, none_type** | Specifies the Plan Id associated with the tenant. This field is introduced for tracking purposes inside IBM enviournment. | [optional] 
**resource_group_id** | **str, none_type** | Specifies the Resource Group ID associated with the tenant. | [optional] 
**resource_instance_id** | **str, none_type** | Specifies the Resource Instance ID associated with the tenant. This field is introduced for tracking purposes inside IBM enviournment. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


