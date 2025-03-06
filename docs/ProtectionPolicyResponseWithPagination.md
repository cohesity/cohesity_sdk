# ProtectionPolicyResponseWithPagination

Specifies the details about the Protection Policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[ProtectionPolicyResponse]**](ProtectionPolicyResponse.md) | Specifies a list of protection policies. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.protection_policy_response_with_pagination import ProtectionPolicyResponseWithPagination

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionPolicyResponseWithPagination from a JSON string
protection_policy_response_with_pagination_instance = ProtectionPolicyResponseWithPagination.from_json(json)
# print the JSON string representation of the object
print(ProtectionPolicyResponseWithPagination.to_json())

# convert the object into a dict
protection_policy_response_with_pagination_dict = protection_policy_response_with_pagination_instance.to_dict()
# create an instance of ProtectionPolicyResponseWithPagination from a dict
protection_policy_response_with_pagination_from_dict = ProtectionPolicyResponseWithPagination.from_dict(protection_policy_response_with_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


