# IbmTenantMeteringConfig

Specifies the metering configuration that will be used for cohesity cluster to send the billing details to IBM billing service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_ids** | **List[str]** | Specifies the list of part identifiers used for metrics identification. | [optional] 
**submission_interval_in_secs** | **int** | Specifies the frequency in seconds at which the metrics will be pushed to IBM billing service from cluster. | [optional] 
**url** | **str** | Specifies the base metering URL that will be used by cluster to send the billing information. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ibm_tenant_metering_config import IbmTenantMeteringConfig

# TODO update the JSON string below
json = "{}"
# create an instance of IbmTenantMeteringConfig from a JSON string
ibm_tenant_metering_config_instance = IbmTenantMeteringConfig.from_json(json)
# print the JSON string representation of the object
print(IbmTenantMeteringConfig.to_json())

# convert the object into a dict
ibm_tenant_metering_config_dict = ibm_tenant_metering_config_instance.to_dict()
# create an instance of IbmTenantMeteringConfig from a dict
ibm_tenant_metering_config_from_dict = IbmTenantMeteringConfig.from_dict(ibm_tenant_metering_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


