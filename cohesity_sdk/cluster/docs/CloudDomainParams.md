# CloudDomainParams

Specifies the params to attach a cloud domain to cluster config

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_id** | **int** | Specifies the external target id | 

## Example

```python
from cohesity_sdk.cluster.models.cloud_domain_params import CloudDomainParams

# TODO update the JSON string below
json = "{}"
# create an instance of CloudDomainParams from a JSON string
cloud_domain_params_instance = CloudDomainParams.from_json(json)
# print the JSON string representation of the object
print(CloudDomainParams.to_json())

# convert the object into a dict
cloud_domain_params_dict = cloud_domain_params_instance.to_dict()
# create an instance of CloudDomainParams from a dict
cloud_domain_params_from_dict = CloudDomainParams.from_dict(cloud_domain_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


