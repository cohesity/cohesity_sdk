# IbmTenantMetricsConfig

Specifies the metadata for metrics configuration. The metadata defined here will be used by cluster to send the usgae metrics to IBM cloud metering service for calculating the tenant billing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cos_resource_config** | [**IbmTenantCOSResourceConfig**](IbmTenantCOSResourceConfig.md) |  | [optional] 
**iam_metrics_config** | [**IbmTenantIAMMetricsConfig**](IbmTenantIAMMetricsConfig.md) |  | [optional] 
**metering_config** | [**IbmTenantMeteringConfig**](IbmTenantMeteringConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ibm_tenant_metrics_config import IbmTenantMetricsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of IbmTenantMetricsConfig from a JSON string
ibm_tenant_metrics_config_instance = IbmTenantMetricsConfig.from_json(json)
# print the JSON string representation of the object
print(IbmTenantMetricsConfig.to_json())

# convert the object into a dict
ibm_tenant_metrics_config_dict = ibm_tenant_metrics_config_instance.to_dict()
# create an instance of IbmTenantMetricsConfig from a dict
ibm_tenant_metrics_config_from_dict = IbmTenantMetricsConfig.from_dict(ibm_tenant_metrics_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


