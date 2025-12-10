# IbmTenantIAMMetricsConfig

Specifies the IAM configuration that will be used for accessing the billing service in IBM cloud.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iam_url** | **str** | Specifies the IAM URL needed to fetch the operator token from IBM. The operator token is needed to make service API calls to IBM billing service. | [optional] 
**billing_api_key_secret_id** | **str** | Specifies Id of the secret that contains the API key. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ibm_tenant_iam_metrics_config import IbmTenantIAMMetricsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of IbmTenantIAMMetricsConfig from a JSON string
ibm_tenant_iam_metrics_config_instance = IbmTenantIAMMetricsConfig.from_json(json)
# print the JSON string representation of the object
print(IbmTenantIAMMetricsConfig.to_json())

# convert the object into a dict
ibm_tenant_iam_metrics_config_dict = ibm_tenant_iam_metrics_config_instance.to_dict()
# create an instance of IbmTenantIAMMetricsConfig from a dict
ibm_tenant_iam_metrics_config_from_dict = IbmTenantIAMMetricsConfig.from_dict(ibm_tenant_iam_metrics_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


