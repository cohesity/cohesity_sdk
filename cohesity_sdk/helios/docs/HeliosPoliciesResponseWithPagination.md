# HeliosPoliciesResponseWithPagination

Specifies the list of Policies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[HeliosPolicyResponse]**](HeliosPolicyResponse.md) | Specifies a list of policies. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_policies_response_with_pagination import HeliosPoliciesResponseWithPagination

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosPoliciesResponseWithPagination from a JSON string
helios_policies_response_with_pagination_instance = HeliosPoliciesResponseWithPagination.from_json(json)
# print the JSON string representation of the object
print(HeliosPoliciesResponseWithPagination.to_json())

# convert the object into a dict
helios_policies_response_with_pagination_dict = helios_policies_response_with_pagination_instance.to_dict()
# create an instance of HeliosPoliciesResponseWithPagination from a dict
helios_policies_response_with_pagination_from_dict = HeliosPoliciesResponseWithPagination.from_dict(helios_policies_response_with_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


