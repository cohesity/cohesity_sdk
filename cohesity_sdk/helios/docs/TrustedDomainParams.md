# TrustedDomainParams

Specifies the params related to trusted domains.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blacklisted_domains** | **List[str]** | Specifies a list of domains to add to blacklist. These domains will be blacklisted in trusted domain discovery. | [optional] 
**discovery_status** | **str** | Specifies the discovery status of trusted domains. | [optional] [readonly] 
**enabled** | **bool** | Specifies if trusted domain discovery is enabled. | 
**only_use_whitelisted_domains** | **bool** | Specifies whether to use &#39;whitelistedDomains&#39; only for authentication. | [optional] 
**task_identifier** | **str** | Specifies the identifier for the task running discovery. | [optional] [readonly] 
**trusted_domains** | [**List[TrustedDomain]**](TrustedDomain.md) | Specifies a list of trusted domains. | [optional] 
**whitelisted_domains** | **List[str]** | Specifies a list of domains to add to whitelist. Only these domains will be used for authentication if &#39;onlyUseWhitelistedDomains&#39; is set. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.trusted_domain_params import TrustedDomainParams

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedDomainParams from a JSON string
trusted_domain_params_instance = TrustedDomainParams.from_json(json)
# print the JSON string representation of the object
print(TrustedDomainParams.to_json())

# convert the object into a dict
trusted_domain_params_dict = trusted_domain_params_instance.to_dict()
# create an instance of TrustedDomainParams from a dict
trusted_domain_params_from_dict = TrustedDomainParams.from_dict(trusted_domain_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


