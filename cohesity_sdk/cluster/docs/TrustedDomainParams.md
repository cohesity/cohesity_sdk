# TrustedDomainParams

Specifies the params related to trusted domains.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool, none_type** | Specifies if trusted domain discovery is enabled. | 
**blacklisted_domains** | **[str], none_type** | Specifies a list of domains to add to blacklist. These domains will be blacklisted in trusted domain discovery. | [optional] 
**discovery_status** | **str, none_type** | Specifies the discovery status of trusted domains. | [optional] [readonly] 
**only_use_whitelisted_domains** | **bool, none_type** | Specifies whether to use &#39;whitelistedDomains&#39; only for authentication. | [optional] 
**task_identifier** | **str, none_type** | Specifies the identifier for the task running discovery. | [optional] [readonly] 
**trusted_domains** | [**[TrustedDomain], none_type**](TrustedDomain.md) | Specifies a list of trusted domains. | [optional] 
**whitelisted_domains** | **[str], none_type** | Specifies a list of domains to add to whitelist. Only these domains will be used for authentication if &#39;onlyUseWhitelistedDomains&#39; is set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


